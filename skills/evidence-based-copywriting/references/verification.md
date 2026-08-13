# Adversarial Verification

Contents: [Why adversarial](#why-adversarial) · [The review panel](#the-review-panel) · [Severity and fix protocol](#severity-and-fix-protocol) · [Deterministic checks](#deterministic-checks) · [The checklist contract](#the-checklist-contract)

## Why adversarial

Self-review finds what you already believe. Every reviewer below is instructed to *refute* the draft, not to appreciate it. In live use, this panel has found real blockers in copy that had already been written carefully against verified sources — superlative upgrades, unit shifts, a present-tense claim in an honesty section, contract-term contradictions, and a seven-word collision with a competitor's live hero. Careful writing does not substitute for hostile reading.

Run the five reviews with independent fresh-context agents when available (parallel subagents are ideal); otherwise run them yourself sequentially, each as a separate pass with its single lens. Never combine lenses in one pass — a reviewer looking for everything finds less of each thing.

## The review panel

**1. Web fact-check (adversarial).**
Input: the deliverable + the citation worksheet (`check_copy.py --urls`).
Instruction: for every cited URL, fetch it and try to REFUTE the claim *as phrased in the copy* — numbers, units, populations, dates, superlatives, quote attribution, and whether the page actually contains what the annotation says it contains. A claim survives only if the fetched page supports the copy's exact framing. Flag unreachable pages: a claim resting solely on an unfetchable source is downgraded or cut.

**2. Internal fidelity.**
Input: the deliverable + the fact base + the project's source documents.
Instruction: find any claim about the product not supported by the fact base; any contradiction with the source documents; any design target or plan presented as achievement; any binding term (acceptance criteria, guarantees, price mechanics) paraphrased more strongly than the source states it; any required anchor language reproduced with drift. Check annotation pointers actually point at the right file and section.

**3. Constraints and compliance.**
Input: the deliverable + the engagement's constraint list (scope, banned terms, single-offer rules, buyer restrictions) + the legal floor in `evidence-standards.md`.
Instruction: strict violation hunt — scope creep (second offers, roadmap promises), banned vocabulary the script's lexicon missed (semantic variants), unlabeled projections, invented proof, testimonial/endorsement issues, unsubstantiated comparative claims about named competitors.

**4. Skeptical-buyer persona read.**
Input: the copy only (not annotations), read as the named buyer persona at their most burned-out.
Instruction: five-second test per hero (what/who/action — quote anything ambiguous); quote every sentence you don't believe from this company at its actual stage; quote every sentence that could appear on any vendor's site; read-aloud failures; verdict on whether the honesty posture reads as confidence or performance; would you take the CTA, and the single change most likely to flip you. A clean report with no findings is itself suspicious — send it back.

**5. Competitor-similarity screen.**
Input: the copy + the verbatim competitor phrase inventory from the research stage.
Instruction: flag any phrase within editing distance of a competitor line, shared distinctive vocabulary used in the same selling role, structural echoes (e.g., a two-sentence rhetorical-question hero when a competitor's hero has that shape), and generic CTA overlap. Check outbound links: every rendered link to a competitor domain is a finding. A citation-as-evidence (the competitor's measurement research is genuinely the best source for a fact) may be kept — justified in the annotation, with a drop-in removal alternative offered to the owner. A link that reads as endorsement or sends buyers to a competitor's offer is removed.

## Severity and fix protocol

- **Blocker** — a false, unsupported, or contradictory claim; an unverifiable "verified" label; a legal exposure; a hero that fails the five-second test. Fix before ship, no exceptions.
- **Should-fix** — accuracy drift that survives a casual read but not a hostile one (unit shifts, attribution drift, inference stated as fact). Fix unless the owner explicitly accepts the risk in writing.
- **Nit** — precision errors in the apparatus (wrong counts in annotations, stale internal pointers). Fix them anyway: in a document whose thesis is accuracy, counting errors are disproportionately expensive.

Fixing rules:

1. Fix toward the source: mirror its exact wording, unit, and dates. Never fix by deleting the citation and keeping the claim.
2. When a claim dies, record it in the section annotation's *deliberately excluded* list with the reason.
3. After any edit, re-run the deterministic checks and re-read the affected annotation — edits strand stale annotation references (a phrase the annotation quotes that no longer exists in the copy is a finding).
4. Fixes that change quoted anchors, prices, or binding terms get re-verified against their source, not assumed.

## Deterministic checks

Run (execute, don't read):

```
python3 scripts/check_copy.py DELIVERABLE.md                 # lexicon + embedded limits; non-zero exit on failure
python3 scripts/check_copy.py DELIVERABLE.md --lexicon X     # add project-specific banned terms
python3 scripts/check_copy.py DELIVERABLE.md --urls          # citation worksheet for reviewer #1
```

Deterministic checks run twice: before the panel (so reviewers read a clean draft) and after fixes (so fixes didn't reintroduce failures). If the project defines its own invariants (protected strings, frozen files, brand-term counts), run those too — new deliverables can silently break repo-level invariants that have nothing to do with the copy itself.

## The checklist contract

The deliverable ends with a self-review checklist. Its rules:

- Mark honestly. An item marked done that a reviewer can falsify does more damage than the defect it hides — it converts a quality issue into a credibility issue.
- Scope claims precisely ("zero occurrences in the copy, sections A–D") so the claim itself is verifiable.
- Never mark verification items in no-network mode; state the limitation instead.
- The checklist records what was checked and how, not aspirations. "Checked by search" beats "confirmed" — it tells the reviewer how to re-check.
