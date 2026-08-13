#!/usr/bin/env python3
"""Deterministic checks for evidence-based copy deliverables.

Three check families, all CI-friendly (non-zero exit on failure):

1. Banned lexicon      -- scans for marketing-slop and hype terms that the
                          copy standard bans. Extend per project.
2. Limit markers       -- HTML comments embedded in the deliverable declare
                          word/character limits; the script enforces them.
3. Citation worksheet  -- inventories every URL with its surrounding sentence
                          so a fact-check pass (human or agent) can verify each
                          claim against its source. Informational; never fails
                          the run.

Marker syntax (put the comment on its own line; the limit applies to the next
non-empty line, so put the target text on its own line after the marker):

    <!-- check: max-words=9 label="headline" -->
    <!-- check: max-chars=155 -->
    <!-- check-block: max-words=150 -->      (applies until the closing marker)
    ...block content...
    <!-- end-check-block -->

An unclosed check-block is itself a failure.

Lexicon file format (--lexicon): one term per line; blank lines and lines
starting with '#' ignored. Terms are matched case-insensitively as substrings.
A term containing regex metacharacters (.*+?[]()\\) is compiled as a regex;
if it fails to compile it is matched literally instead.

Usage:
    python3 check_copy.py DELIVERABLE.md               # run all checks
    python3 check_copy.py DELIVERABLE.md --lexicon extra-banned.txt
    python3 check_copy.py DELIVERABLE.md --urls        # citation worksheet only
    python3 check_copy.py DELIVERABLE.md --json        # machine-readable output

Exit codes: 0 = all checks pass, 1 = at least one failure, 2 = usage error.
Python 3.8+, standard library only.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Terms that almost never survive a skeptical technical reader. Grounded in
# peer-reviewed measurement of LLM-overused vocabulary (Kobak et al., Science
# Advances 2025; Liang et al., ICML 2024 -- see references/copy-craft.md) plus
# hype terms a claims-discipline standard bans outright. The script enforces
# this list mechanically; copy-craft.md adds editorial patterns (structural
# tells, bare-word judgment calls like "leverage" as a noun) that need a human
# or adversarial-review pass. Overlapping matches on a line are deduplicated,
# reporting the longest term at each position.
DEFAULT_LEXICON = [
    # hype / empty superlatives
    "revolutionary",
    "revolutionize",
    "revolutionizing",
    "cutting-edge",
    "cutting edge",
    "game-changing",
    "game changer",
    "game-changer",
    "world-class",
    "world class",
    "best-in-class",
    "best in class",
    "industry-leading",
    "industry leading",
    "state-of-the-art",
    "state of the art",
    "unparalleled",
    "unrivaled",
    "next-gen",
    "next generation platform",
    # measured LLM-overuse vocabulary
    "seamless",
    "seamlessly",
    "delve",
    "delves",
    "delving",
    "pivotal",
    "groundbreaking",
    "transformative",
    "meticulous",
    "meticulously",
    "intricate",
    "commendable",
    "showcasing",
    "showcases",
    "underscores",
    "harnessing",
    "leverages",
    "leveraging",
    "streamline",
    "streamlining",
    # slop verbs and framings
    "unleash",
    "unleashed",
    "unleashing",
    "supercharge",
    "supercharged",
    "empower",
    "empowering",
    "empowers",
    "empowered",
    "holistic",
    "synergy",
    "synergies",
    "paradigm shift",
    "turbocharge",
    "frictionless",
    "effortless",
    "effortlessly",
    "elevate your",
    "unlock the power",
    "harness the power",
    "take your .* to the next level",
    "in today's fast-paced",
    "in today's digital landscape",
    "in today's evolving threat landscape",
    "ai-powered",  # banned as a hero adjective; if the product IS an AI product,
                   # name the mechanism instead ("detects X with a fine-tuned model")
]

MARKER_RE = re.compile(r"<!--\s*check:\s*(?P<attrs>[^>]*?)\s*-->")
BLOCK_OPEN_RE = re.compile(r"<!--\s*check-block:\s*(?P<attrs>[^>]*?)\s*-->")
BLOCK_CLOSE_RE = re.compile(r"<!--\s*end-check-block\s*-->")
# Accepts balanced parentheses inside URLs (CFR/statute links like .../275.206(4)-1)
URL_RE = re.compile(r"https?://(?:\([^\s()]*\)|[^\s()\]>\"'])+")
ATTR_RE = re.compile(r"(max-words|max-chars|label)\s*=\s*(\"[^\"]*\"|\S+)")


def strip_markdown(line: str) -> str:
    """Reduce a markdown line to the words a reader would actually read."""
    text = line.strip()
    text = re.sub(r"^#{1,6}\s+", "", text)               # headings
    text = re.sub(r"^[-*>]\s+", "", text)                 # bullets / quotes
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)      # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # links -> link text
    text = re.sub(r"[*_`]{1,3}", "", text)                # emphasis / code marks
    text = re.sub(r"<[^>]+>", "", text)                   # inline html
    return text.strip()


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9$€£%][A-Za-z0-9$€£%'’\-–—/.]*", text))


def parse_attrs(raw: str) -> dict:
    attrs = {}
    for key, value in ATTR_RE.findall(raw):
        attrs[key] = value.strip('"')
    return attrs


def compile_term(term: str):
    if any(ch in term for ch in ".*+?[]()\\"):
        try:
            return re.compile(term, re.IGNORECASE)
        except re.error:
            return re.compile(re.escape(term), re.IGNORECASE)
    return re.compile(re.escape(term), re.IGNORECASE)


def check_lexicon(lines, lexicon):
    findings = []
    patterns = [(term, compile_term(term)) for term in lexicon]
    for num, line in enumerate(lines, 1):
        scannable = URL_RE.sub("", line)  # never flag terms inside URLs
        matches = []
        for term, pattern in patterns:
            for m in pattern.finditer(scannable):
                matches.append((m.start(), m.end(), term))
        # Dedupe overlaps: keep the longest match at any position
        matches.sort(key=lambda t: (t[0], -(t[1] - t[0])))
        kept, occupied_end = [], -1
        for start, end, term in matches:
            if start >= occupied_end:
                kept.append(term)
                occupied_end = end
        for term in kept:
            findings.append({
                "check": "banned-term",
                "line": num,
                "term": term,
                "text": line.strip()[:120],
            })
    return findings


def check_markers(lines):
    findings = []
    i = 0
    while i < len(lines):
        line = lines[i]
        block = BLOCK_OPEN_RE.search(line)
        marker = MARKER_RE.search(line)
        if block:
            attrs = parse_attrs(block.group("attrs"))
            content, j, closed = [], i + 1, False
            while j < len(lines):
                if BLOCK_CLOSE_RE.search(lines[j]):
                    closed = True
                    break
                content.append(strip_markdown(lines[j]))
                j += 1
            if not closed:
                findings.append({
                    "check": "unclosed-check-block", "line": i + 1,
                    "label": attrs.get("label", "block"),
                })
                i = j
                continue
            body = " ".join(t for t in content if t)
            if "max-words" in attrs:
                limit, actual = int(attrs["max-words"]), word_count(body)
                if actual > limit:
                    findings.append({
                        "check": "max-words", "line": i + 1,
                        "label": attrs.get("label", "block"),
                        "limit": limit, "actual": actual,
                    })
            i = j + 1
            continue
        if marker:
            attrs = parse_attrs(marker.group("attrs"))
            j = i + 1
            while j < len(lines) and not strip_markdown(lines[j]):
                j += 1
            target = strip_markdown(lines[j]) if j < len(lines) else ""
            if "max-words" in attrs:
                limit, actual = int(attrs["max-words"]), word_count(target)
                if actual > limit:
                    findings.append({
                        "check": "max-words", "line": j + 1,
                        "label": attrs.get("label", target[:40]),
                        "limit": limit, "actual": actual,
                    })
            if "max-chars" in attrs:
                limit, actual = int(attrs["max-chars"]), len(target)
                if actual > limit:
                    findings.append({
                        "check": "max-chars", "line": j + 1,
                        "label": attrs.get("label", target[:40]),
                        "limit": limit, "actual": actual,
                    })
        i += 1
    return findings


def citation_worksheet(lines):
    rows = []
    for num, line in enumerate(lines, 1):
        for url in URL_RE.findall(line):
            context = strip_markdown(line)
            rows.append({"line": num, "url": url.rstrip(".,;"), "context": context[:160]})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("file", help="deliverable markdown file")
    parser.add_argument("--lexicon", help="file of extra banned terms, one per line")
    parser.add_argument("--urls", action="store_true", help="print citation worksheet only")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.is_file():
        print(f"error: {path} not found", file=sys.stderr)
        return 2
    lines = path.read_text(encoding="utf-8").splitlines()

    worksheet = citation_worksheet(lines)
    if args.urls:
        print("| line | url | context |")
        print("|---|---|---|")
        for row in worksheet:
            print(f"| {row['line']} | {row['url']} | {row['context']} |")
        return 0

    lexicon = list(DEFAULT_LEXICON)
    if args.lexicon:
        lex_path = Path(args.lexicon)
        if not lex_path.is_file():
            print(f"error: {lex_path} not found", file=sys.stderr)
            return 2
        extra = lex_path.read_text(encoding="utf-8").splitlines()
        lexicon += [t.strip() for t in extra if t.strip() and not t.startswith("#")]

    findings = check_lexicon(lines, lexicon) + check_markers(lines)

    if args.json:
        print(json.dumps({"findings": findings, "citations": len(worksheet)}, indent=2))
    else:
        for f in findings:
            if f["check"] == "banned-term":
                print(f"FAIL line {f['line']}: banned term '{f['term']}' — {f['text']}")
            elif f["check"] == "unclosed-check-block":
                print(f"FAIL line {f['line']}: check-block never closed "
                      f"({f['label']}) — add <!-- end-check-block -->")
            else:
                print(f"FAIL line {f['line']}: {f['check']} {f['actual']} > {f['limit']} ({f['label']})")
        print(f"\n{len(findings)} failure(s); {len(worksheet)} cited URL(s) "
              f"(run with --urls for the citation worksheet)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
