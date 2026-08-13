# Enterprise Integration

Contents: [Where this standard sits](#where-this-standard-sits) · [Interop with claims review](#interop-with-claims-review) · [Claims-registry schema](#claims-registry-schema) · [Message-map traceability](#message-map-traceability) · [Regulated-industry notes](#regulated-industry-notes)

## Where this standard sits

Large organizations run layered content governance: a brand voice layer (tone, terminology, style) and a claims layer (what may be asserted, with what evidence, approved by whom). Public examples: Mailchimp's content style guide keeps "Writing Legal Content" as its own section apart from voice (https://styleguide.mailchimp.com/); Intuit runs one content-design system with per-brand voice layers and channel chapters (https://contentdesign.intuit.com/); GOV.UK maintains style rules as individually addressable, versioned entries with change notifications to all publishers (https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/).

**This skill is a claims layer.** It defers voice decisions to the host company's style guide where one exists — apply their terminology and tone rules on top; keep this skill's evidence, labeling, and verification rules underneath. Where the two conflict on a factual-claim matter, the claims layer wins. Its Iron Laws are numbered so reviews can cite them the way GOV.UK entries are cited.

## Interop with claims review

The deliverable format is designed to drop into formal review gates without rework:

- **Annotated-claims review (pharma MLR model).** MLR review expects materials to arrive with every claim annotated to an approved evidence source so reviewers verify rather than hunt (e.g., https://www.propharmagroup.com/thought-leadership/medical-legal-regulatory-mlr-submission-checklist). The per-section annotations and labeled registers in the deliverable are exactly that artifact — hand reviewers the deliverable, not a stripped copy deck.
- **Named pre-approval gate (FINRA model).** FINRA Rule 2210 requires a registered principal to approve retail communications before first use, with dated records (https://www.finra.org/rules-guidance/rulebooks/finra-rules/2210). Generalized: ship copy through a named human approver, record who and when. The deliverable's `[Open decision for the owner]` flags are the approver's queue.
- **Substantiation on demand (SEC model).** The SEC Marketing Rule bans material factual statements the firm cannot substantiate on demand (https://www.law.cornell.edu/cfr/text/17/275.206(4)-1). The citation worksheet (`check_copy.py --urls`) plus the fact base is that on-demand file — retain both with the shipped copy, not just the copy.
- **Fair balance within the asset (FDA model).** 21 CFR 202.1: misleading content in one section is not cured by truth in another (https://www.law.cornell.edu/cfr/text/21/202.1). Generalized: caveats live next to the claims they qualify — never deferred to another page, footnote cluster, or the FAQ alone.

## Claims-registry schema

Companies with claims libraries treat each approved claim as a record; review tooling auto-links copy against the library, and retiring a claim recalls the assets using it (Veeva MedTech on central claims libraries: https://www.veeva.com/medtech/resources/efficiency-compliance-collaboration-the-benefits-of-a-central-claims-library/). A directly adoptable per-claim schema (via https://ciberspring.com/articles/build-a-pre-approved-claims-library-by-2026/):

> claim text (approved wording) · source · owner · jurisdiction tags · use tags (audience/channel) · risk level · **expiry date and version** · linked variants (short/long/social)

When the client has a registry: write copy in registry-matchable form (use the canonical claim wording or its approved variants), and feed newly verified claims from the fact base into the registry with expiry dates rather than leaving them in a one-off document. When the client has no registry: the fact base plus the deliverable annotations *are* the starter registry — say so in the handoff.

## Message-map traceability

Enterprise messaging is typically structured as value proposition → 3–4 messaging pillars → proof points, maintained as a living message map all teams draw from (https://www.productmarketingalliance.com/your-guide-to-messaging/). Where a message map exists, every claim in the copy should trace upward to a pillar and downward to a proof point; orphan claims — supported by evidence but belonging to no pillar — are a strategy flag for the owner, not necessarily a cut. Where none exists, note in the handoff which de facto pillars the page asserts; that list is the seed of the message map.

## Regulated-industry notes

For clients in finance, healthcare, pharma, or other regulated verticals: this skill raises copy to the general FTC floor and produces reviewer-ready artifacts, but sector rules (FINRA filing windows, FDA 2253 submission of final-form assets, SEC performance-presentation mechanics) are outside its scope. Route final copy through the client's counsel and compliance function; present this skill's output as the input to that gate, never a substitute for it.
