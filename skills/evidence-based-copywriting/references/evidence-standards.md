# Evidence Standards

Contents: [Verification protocol](#verification-protocol) · [Source hierarchy](#source-hierarchy) · [Labeling taxonomy](#labeling-taxonomy) · [The legal floor](#the-legal-floor) · [Evidence-trap catalog](#evidence-trap-catalog)

## Verification protocol

For every external claim a draft will use:

1. **Fetch the source URL yourself, during this engagement.** Confirm the claim appears on the fetched page, with the same number, unit, population, and date the copy will use. If the fetch fails, the claim is unverified regardless of how famous it is.
2. **Prefer the deepest primary page** — the publisher's own report page or PDF, the regulator's rule text, the company's own pricing page. Never cite a homepage when a deeper page exists.
3. **Date-stamp everything** — the source's publication date and your fetch date. Undated claims ("recent research shows") are banned.
4. **Run the supersession check.** Search for a newer edition from the same publisher before citing any recurring report (annual surveys especially). Publishers reverse their own findings year to year; citing last year's ranking as current is a factual error even though the citation is real.
5. **Record conflicts.** If credible sources disagree, the copy either carries the disagreement, uses the more defensible number with its scope stated, or drops the point. Never select the favorable number silently.
6. **Note the publisher's interest.** A vendor's research about the problem its product solves is usable as measurement but must be identified as vendor research. Never present an interested party's benchmark as independent.
7. **Blocked source? Use a labeled mirror.** Regulator and enterprise sites often block automated fetching. Official text mirrored by GPO (govinfo.gov), Cornell LII, or a full wire-service mirror is acceptable, labeled `verified-secondary`, with the block noted. What is never acceptable: treating search-snippet text as verified.

## Source hierarchy

Strongest to weakest — a claim's evidence grade is the grade of its best *fetched* source:

1. Regulator or standards-body text (statutes, CFR, official specifications)
2. The publisher's own primary page or PDF (report, study, dataset, pricing page)
3. Peer-reviewed research (note domain-transfer limits explicitly)
4. Full official mirrors of blocked primaries (GPO, LII, wire-service full text) — `verified-secondary`
5. Reputable trade coverage quoting the primary — `verified-secondary`
6. Vendor-published research with disclosed methodology — usable, labeled with interest
7. Uncited marketing content, search snippets, memory — **not usable**

## Labeling taxonomy

Every factual statement in the deliverable carries exactly one register, visible in section annotations:

- `[Verified fact — primary]` / `[Verified fact — secondary]` — external claim, fetched, with URL and dates
- `[Internal product claim]` — traced to the project's own document, with exact path §heading
- `[Projection — labeled]` — design target, plan, or intention; labeled in the copy itself at every occurrence
- `[Strategic recommendation]` — advice to the owner; needs no citation but must not read as fact
- `[Copywriting judgment]` — scenario, composite, or stylistic assertion; must not smuggle in a statistic
- `[Open decision for the owner]` — the copy needs a fact nobody has established; blocks or ships flagged
- `[Assumption]` — collected at the top of the deliverable

## The legal floor

Not legal advice; the point is that this skill's discipline is the same standard US regulators already enforce, which is what makes it defensible in enterprise review. All sources fetched and verified 2026-08-13.

- **Substantiation precedes dissemination.** The FTC's advertising substantiation doctrine requires a "reasonable basis" for objective claims *before* they are published; every objective claim implicitly represents that substantiation exists. Establishment claims ("tests prove", "studies show") require possession of the advertised level of proof — invoking evidence raises the bar to that evidence. (FTC Policy Statement Regarding Advertising Substantiation, 1983, appended to *Thompson Medical Co.*, 104 F.T.C. 648; ftc.gov blocks fetching — verified via mirror: https://pages.uoregon.edu/tgleason/j385/FTC_j385.html. Reasonable-basis-before-claim also codified at 16 CFR 260.2: https://www.law.cornell.edu/cfr/text/16/260.2)
- **Required proof scales with stakes** (the *Pfizer* factors): type of claim, consequences of falsity, cost of substantiation, expert norms. Security-efficacy, ROI, and performance claims need more than descriptive claims.
- **Endorsements are not a loophole.** 16 CFR Part 255 (2023 revision): endorsements must reflect the endorser's honest opinion, may not carry any claim the advertiser couldn't lawfully make directly, require bona fide current users, and a non-typical featured result requires clear disclosure of generally expected performance. (Official CFR text: https://www.govinfo.gov/content/pkg/CFR-2024-title16-vol1/xml/CFR-2024-title16-vol1-part255.xml)
- **Fake reviews and testimonials are a rule violation with civil penalties.** 16 CFR Part 465 (effective October 21, 2024) bans fake or AI-generated reviews/testimonials, purchased sentiment, undisclosed insider reviews, and fake independent review sites — civil penalties per violation, up to $53,088 at the 2025 inflation adjustment (89 FR 68034; adjustment 90 FR 5580 — re-check the current figure before citing it in copy).
- **Comparative claims create private liability.** Lanham Act §43(a) lets competitors sue over false or misleading statements about their products or yours — which is why competitor claims are quoted verbatim, dated, and sourced. (15 U.S.C. §1125(a): https://www.law.cornell.edu/uscode/text/15/1125)
- **The regulated-industry benchmark** — useful even outside those industries because enterprise reviewers were trained in them: FINRA Rule 2210 requires communications to be "fair and balanced," bans "false, exaggerated, unwarranted, promissory or misleading" statements, and requires principal pre-approval (https://www.finra.org/rules-guidance/rulebooks/finra-rules/2210). The SEC Marketing Rule bans material statements of fact the adviser cannot substantiate *upon demand* (17 CFR 275.206(4)-1: https://www.law.cornell.edu/cfr/text/17/275.206(4)-1). FDA fair-balance rules make truthful-in-one-section insufficient if another section misleads (21 CFR 202.1: https://www.law.cornell.edu/cfr/text/21/202.1).

## Evidence-trap catalog

Every trap below was caught in live adversarial review of professionally written, source-linked copy. Check drafts against each one.

| Trap | What it looks like | Fix |
|---|---|---|
| **Superlative upgrade** | Source says "one of the largest evaluations"; copy says "the largest audit" | Mirror the source's own self-description exactly |
| **Unit shift** | Source: "34% of suggested domains"; copy: "wrong a third of the time" (per-query frequency the study never measured) | Keep the source's unit; name the denominator |
| **Population swap** | A consumer-survey number presented as a B2B finding; one model family's result attributed to "AI models" | State the surveyed population and scope inline |
| **Quote drift / misattribution** | The study authors' summary phrase attributed to survey respondents | Quotes verbatim; attribute to exactly who said it |
| **Superseded stat** | Last year's "AI is the #1 source" finding cited after the same publisher reversed it this year | Supersession check on every recurring report |
| **Interested-source laundering** | A vendor's visibility benchmark cited as if independent; a visibility stat cited as an accuracy stat | Label the interest; use the stat only for what it measures |
| **Sample-size misattachment** | n from one chart attached to a different figure in the same report | Attach n only where the source attaches it |
| **Date drift** | "up from 29% a year earlier" when the source says "up from 29% in April 2025" | Use the source's own date anchors |
| **Client-side pricing mirage** | Competitor prices "verified" from a page that renders prices via JavaScript — the static fetch contains no prices | Only claim what the fetched artifact actually contains; otherwise say "not machine-verifiable" |
| **Present-tense promise** | "Our methodology is public" when it is planned but unpublished | Future tense or cut; a false present-tense sentence in an honesty section is fatal |
| **Absolutes contradicting contract terms** | FAQ says "corrections ship, or it isn't done" while the contract says "deployed *or formally submitted*" | Mirror the binding disjunction everywhere it is paraphrased |
| **Anchor mutation** | Required approved sentences reproduced with altered punctuation or em-dash spacing | Character-for-character reproduction; verify with search, not eyes |
