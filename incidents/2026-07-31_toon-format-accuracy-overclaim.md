tier: Dr (specified; independently unreviewed)

# toon-format accuracy overclaim — 2026-07-31

## Source
the internal survey (local, not public) §A (`information-discrete-math`/skill-library context) and §B
(`skill-library VETTING_PROTOCOL` entry): "Incident: toon-format 2026-07-31 token claim
`[finite_diagnostic]` verified, accuracy claim → `[Open]` after independent test contradicted
upstream."

## What happened [tier: finite_diagnostic (documented)]
The `toon-format` skill was vetted for internal use on 2026-07-31. It carried two distinct claims
from its upstream project: (1) a token-count reduction claim (TOON encodes uniform tabular data in
fewer tokens than JSON), and (2) an accuracy claim (a model reading TOON-encoded data back out
performs as well as, or better than, reading the same data as JSON). The vetting process initially
cited the upstream project's own numbers for both as if they were settled. Running an independent
measurement — the official encoder plus a real tokenizer, on data actually held by this workspace
— confirmed claim (1): roughly 35–36% fewer tokens on uniform table data (kept as
`finite_diagnostic`), but also found TOON performed *worse* than JSON (roughly 22–25% more tokens)
on non-uniform, deeply nested data — a boundary the upstream framing had not stated. For claim (2),
an independent blind read-back test found the opposite of what upstream's own numbers implied, and
at least one external, independent benchmark search also found a result contradicting upstream on
some data. The accuracy claim was downgraded to `Open` and removed from the shipped skill; only the
token-count claim, with its now-stated boundary condition, was kept.

## What rule it produced [tier: Dr]
The `skill-library` `VETTING_PROTOCOL.md`'s standing rule, generalized here for glosa's own
citation-integrity subsystem (§7.8): **an external source's own benchmark number about itself is
not evidence until independently reproduced** — this is the same `NC-18` (Source existence ≠ Claim
support) boundary the Integrity Firewall enforces for citations generally, applied to a skill's own
self-reported capability claims rather than to a paper's cited facts. Practically: a `citation_card`
or `assumed[]` entry that names an external tool/paper's own stated performance number must carry
`claim_match_verified: false` until an independent, decorrelated route (§4.2) has actually re-run
the measurement — the vendor's documentation is `metadata_verified`-adjacent at best, never
`claim_match_verified` on its own. It is also a direct instance of `NC-17` (mechanical validity ≠
semantic validity): the token-count math was mechanically reproducible and held; the accuracy claim
required a semantic judgment (did the model actually retrieve the right value) that a different,
independent test contradicted.

## What would have caught it earlier
Treating "the upstream project's README states X%" as `fetch_status: FETCHED,
claim_match_verified: false` from the first read, rather than upgrading it to a usable claim before
any independent re-run — exactly the `citation_card.yaml` discipline this repo's own template
enforces (§7.8): a card cannot appear in a paper's evidence list or a claim card's
`evidence_relations[]` until `status: VERIFIED`, which requires both booleans, not the vendor's word
alone.

## Non-collapse pairs this incident illustrates
- `NC-18` Source existence ≠ Claim support.
- `NC-17` Mechanical validity ≠ Semantic validity — one half of a two-part claim held mechanically,
  the other did not, and treating them as one claim would have hidden that split.
- `NC-11` `Th_coqc` ≠ `finite_diagnostic` ≠ `Dr` ≠ `Open` — the two halves of one upstream claim
  correctly landed on two different tiers rather than being averaged into one.
