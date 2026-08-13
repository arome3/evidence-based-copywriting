# Copy Craft

Contents: [Voice contract](#voice-contract) · [Banned lexicon](#banned-lexicon-and-structural-tells) · [Heroes and the five-second test](#heroes-and-the-five-second-test) · [Section architecture](#section-architecture) · [Stage-honesty proof playbook](#stage-honesty-proof-playbook) · [Metadata truth](#metadata-truth)

## Voice contract

Plain, calm, specific, evidence-first. Short sentences. Concrete nouns. Active voice. This is not taste — it is measured: in Nielsen Norman Group's controlled study, rewriting promotional "marketese" into objective language alone improved measured usability 27% (concise + scannable + objective combined: 124%); users "detested marketese" because filtering hype is cognitive work (https://www.nngroup.com/articles/how-users-read-on-the-web/, 1997 — dated but still NN/g's published guidance).

Working tests, applied per sentence:

- **The any-vendor test.** If the sentence could appear unchanged on any competitor's site, cut or rewrite it.
- **The read-aloud test.** If a founder couldn't say it on a sales call without wincing or restarting, rewrite it.
- **The information-density test.** Every sentence adds a verifiable fact, a real mechanism, or a decision the reader can act on. Research on "AI slop" finds the failure is low density and incoherence, not just tell-words — word substitution alone leaves the signature intact (https://arxiv.org/abs/2509.19163, preprint).
- **The skeptic test.** Would the named buyer persona believe this from this company at its actual stage?

## Banned lexicon and structural tells

The default banned list lives in `scripts/check_copy.py` (extend per project with `--lexicon`). The script enforces the unambiguous terms mechanically; bare-word judgment calls stay editorial because they have legitimate uses the script can't distinguish — "leverage" (finance), "elevate" (privilege escalation), "robust" (engineering) — catch those in the write and verify passes. The list is grounded in peer-reviewed measurement of LLM-overused vocabulary, not folklore:

- Kobak et al., *Science Advances* 2025 — 15M+ PubMed abstracts; "excess words" with effect sizes: *delves* (r=28.0), *underscores* (13.8), *showcasing* (10.7); the rare-excess list includes *seamless(ly)*, *leverages*, *pivotal*, *transformative*, *groundbreaking*, *unparalleled*, *revolutionize*, *harnessing*, *streamline*, *elevate*, *empowers* (https://arxiv.org/html/2406.07016v3).
- Liang et al., ICML 2024 — LLM-favored adjectives: *meticulous* 34.7×, *intricate* 11.2×, *commendable* 9.8× (https://arxiv.org/html/2403.07183v2).
- Why they're overused is unproven — keep the list descriptive, not etiological (Juzek & Ward, COLING 2025: https://arxiv.org/abs/2412.11385).

Structural tells to edit out (curated by Wikipedia's AI-cleanup project — practitioner curation, not research: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing):

- Negative parallelism ("not just X, but Y") and rule-of-three cadences used reflexively
- Trailing "-ing" analysis clauses ("...reflecting the market's shift", "...highlighting the need for")
- Significance inflation and unearned "in today's landscape" framing
- Vague attribution ("industry reports say", "observers note") — this skill requires a named, linked source instead
- Em-dash overuse — ration them; more than one per paragraph is a tell

Also banned: empty superlatives, unsupported category-leadership claims ("#1", "leading"), generic transformation language, fear-based messaging, and "AI-powered" as a hero adjective — name the mechanism instead.

## Heroes and the five-second test

Budgets (conventions that force clarity, not laws): headline ≤9 words, subheadline ≤25 words, enforced via the template's `check:` markers.

**Five-second test** — what a first-time visitor can say after one glance: *what it is, who it's for, what action to take*. That is all the method validly measures — first-impression clarity, not comprehension or task success; the 5-second bound is convention, first-impression judgments simply form very fast (method: https://www.lyssna.com/guides/five-second-testing/; origin & limits: https://www.smashingmagazine.com/2023/12/five-second-testing-case-study/).

Rules that follow:

- Declarative headlines. Check the mapped competitor set first — if the category leader uses a rhetorical-question hook, a question hero reads as an echo.
- The vertical/audience qualifier rides in an eyebrow line if the headline can't carry it.
- CTAs name the artifact the click produces ("Request a preview — one verified error"), never "Get started" / "Book a demo" (generic CTA overlap with competitors is a similarity-screen finding).
- Offer 2–3 hero options with genuinely different angles (mechanism-first, trigger-first, offer-first) and state which is recommended and why.
- The hero must not promise what the FAQ disclaims. If verification can't guarantee outcomes, the hero's verbs bind to what is controllable ("verify the corrections held", not "stay #1 in AI answers").

## Section architecture

1. **Hero** — with a stage-honesty line if pre-launch ("No customer logos appear here because we don't have customers yet").
2. **Problem** — written from the buyer's seat: symptoms they recognize first, evidence second. Every stat date-stamped and scope-caveated inline; the caveats do persuasion work with skeptical readers. If the evidence has a gap, say so in the copy and convert it into the offer ("no one has measured X — that's what the assessment does for you"). Rejected stats go in the annotation's *deliberately excluded* list.
3. **How it works** — the real mechanism in the customer's timeline. Only capabilities the fact base establishes. Concede what cannot be controlled ("some sources can only be petitioned, never edited") — each concession pre-empts the skeptic's first objection.
4. **What you get** — deliverables as owned artifacts ("yours to keep"). If acceptance criteria exist, quote them; the contract is the strongest proof a young company has. Mirror binding disjunctions exactly.
5. **Proof** — see stage playbook below.
6. **Offer and pricing** — publish real numbers when the owner allows: transparent pricing has been technology buyers' #1 wish of vendors four years running (TrustRadius 2026 Buying Disconnect, vendor survey: https://www.prnewswire.com/news-releases/trustradius-2026-b2b-buying-disconnect-report-reveals-ai-has-changed-how-buyers-research-but-not-what-they-trust-302825792.html). State what moves price within a band. Payment mechanics unstated by the owner = `[Open decision]`, not invention.
7. **FAQ** — the questions the skeptical buyer would actually ask, hardest first, including the one about your weakest fact ("Why trust a company with no public customers?"). Pattern: concede the premise, then convert it into a term of the deal ("You shouldn't — not on trust. Here's what you can check...").
8. **Final CTA** — restate the offer in miniature as a checkable artifact; include the null case ("if we find nothing material, we'll tell you that too").
9. **Footer** — required legal/brand lines; one page-level integrity statement at most.

## Stage-honesty proof playbook

Proof must match the company's actual stage. Buyers rank hands-on and third-party evidence (demos, trials, reviews) above vendor-controlled content (TrustRadius 2026, above) — so borrowed or invented credibility underperforms even before it becomes a legal problem.

| Stage | Proof that works | Never |
|---|---|---|
| Zero customers / pre-launch | Published methodology; contractual acceptance criteria quoted; design-partner pricing framed as priced-in stage risk; labeled commitments ("in development — a commitment, not a credential"); real founder facts only; a real worked specimen of the work | Logos, testimonials, case studies, "trusted by" counts, certifications "in progress" presented as held |
| Early customers | Named results **with written permission** and typicality honesty (16 CFR 255.2: a featured non-typical result requires disclosing generally expected performance) | Cherry-picked outlier results without the typicality disclosure |
| Established | Substantiated metrics with methodology links; third-party validation | Unsourced aggregate claims ("87% fewer incidents") |

Honesty-density rule: at most two self-referential integrity statements in the body plus one footer line. Past that, honesty reads as the product instead of the proof — and one caught slip flips the whole posture from "confident" to "performing."

## Metadata truth

What the primary sources actually say (both fetched):

- Google documents **no character limit** for title links or meta descriptions; truncation is by device width, titles may be rewritten, and snippets are primarily generated from page content (https://developers.google.com/search/docs/appearance/title-link, https://developers.google.com/search/docs/appearance/snippet). The familiar 50–60 / 155–160 character rules are folklore.
- The Open Graph spec sets **no length limits**; og:description is specced only as "a one to two sentence description" (https://ogp.me/).

Practice: front-load substance and use the template's char budgets (60/155/60/200) as *truncation-safe conventions* — state them as conventions, never as platform requirements. Metadata sells the actual offer (the deliverable and its price/duration where allowed), not a mission statement.
