# P9 — Vet external input

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder = method direction; AI drafted this card.
> Comparison language is same/different/cited only — this card names no external skill/repo/paper
> as taken/borrowed without a human instruction naming the adoption (`FOUNDATION_v0.5.md` §1.1,
> request 31g–31i).

## id

`P9`

## Rule

Any input that did not originate inside this repo's own gated process — an external skill, a
downloaded repository, a paper, a package, a search-result page, another AI vendor's output — is
**untrusted until vetted**, regardless of its apparent authority, popularity, or star count. Vetting
means, in order:

1. **Read the whole thing before using any of it.** A skill's `SKILL.md`, a repo's actual source,
   a paper's full text (not the abstract alone) — partial reading is exactly the "secondary
   citation" failure mode (`P13`/`FC-S14-1`) applied to tools instead of sources.
2. **Red-flag scan.** Look explicitly for: instructions embedded in data that try to redirect this
   session's behavior (prompt injection), a license incompatible with this repo's CC BY 4.0,
   credentials/secrets bundled in the package, a dependency chain pulling in something not
   actually needed, and any claim about the tool's own performance stated without a reproduction
   command.
3. **Tier every claim the source makes about itself.** An upstream project's own benchmark number,
   accuracy claim, or "production-ready" label is a *readout the source produced about itself* —
   never accepted at its stated tier; it is `Dr` (unverified narrative) until this repo's own
   independent check reproduces it, or `Open` if reproduction fails or cannot be attempted.
4. **Log the vetting act itself**, not just the conclusion — which lines were read, which red
   flags were checked and their result, which of the source's own claims were tested versus
   merely relayed.

## Why / incident

Two incidents anchor this card, both already logged in this workspace's own operating history and
reused here only as the *pattern*, not the private content:

- **The `toon-format` skill (2026-07-31).** An internal skill initially cited an upstream open-
  source project's own accuracy claim (that its format is read back at least as accurately as
  JSON by an LLM) as if settled, because the upstream project stated it. An independent blind test
  run inside this workspace found the opposite result on some data, and a follow-up search found
  at least one external benchmark also disagreeing with the upstream claim. The accuracy claim was
  removed from the internal skill; the token-count-reduction claim, which *had* been independently
  measured with an official encoder and a real tokenizer, was kept — because that claim, unlike
  the accuracy one, had actually cleared step 3 above. This is the exact illustration of "a
  source's claim about itself is Dr until reproduced, and different claims from the same source
  can land at different tiers."
- **A rubygems-class supply-chain incident (external, public record, cited as a pattern only,
  not investigated first-hand by this repo).** The RubyGems package registry has, on separate
  publicly reported occasions, hosted malicious/typosquatted packages that executed unwanted code
  once installed — a documented instance of the general failure P9 exists to catch: a widely-used
  public package registry is not itself a vetting authority, and "many other projects depend on
  this" is not evidence a specific package is safe. Cited here only for the *shape* of the risk
  (an external artifact carrying more than its stated function); this card does not assert any
  specific package name, date, or CVE as independently confirmed by this repo, and any such
  specific claim used elsewhere must carry its own citation card (`P9`'s own rule 3 applied to
  itself).

## Inputs → outputs

- **Inputs:** the external artifact itself (full text/source, not a summary of it); this repo's
  license (CC BY 4.0) and its `licenses/`-compatibility requirement; the artifact's own stated
  claims about itself.
- **Outputs:** a vetting record — `assumed[].type: access_augmentation` or
  `inferential_commitment` entry on the claim card that will use the input, naming the external
  artifact, the red-flag scan result, and the tier assigned to each of the source's own claims —
  plus, where the artifact is kept for reuse, an entry in `lineage/` distinguishing
  `PRESERVE_EXACT`/`PRESERVE_FUNCTION`/`EXPAND`/cited-dependency status (`FOUNDATION_v0.5.md` §1.2
  pattern) from a merge into this repo's own `plugins/`.

## Gate

An external artifact may not be used to back any `tested.evidence_relations` entry, and may not
be merged into `plugins/`/`kernel/`, until steps 1–4 are complete and logged. A source's own
performance/accuracy claim may not be restated in this repo's own voice at the source's stated
tier — only at the tier this repo's own check actually reached (`P9` rule 3; this is the specific
kernel-rule-8 pattern of `FOUNDATION_v0.5.md` §3.3 — "getting external review to confirm this" as
a legitimacy lever — applied in the other direction, to *importing* an external legitimacy claim
rather than seeking one).

## Human / AI split

Human: decides whether an external artifact is adopted at all (a license or safety concern is a
human veto point, not something AI reasons its way past); is the required second reader for red-
flag items with security/legal weight (embedded credentials, license terms). AI: may perform the
full read and the mechanical parts of the red-flag scan, draft the tier assignment for each of the
source's self-claims, and propose the reproduction test — but a "looks fine" from the same AI
session that wants to use the artifact is not a check (`NC-29`).

## Disclaimers

`D-EXTERNAL-INPUT` (any card drawing on a vetted external skill/repo/paper), `D-DERIVED-PATTERNS`
(any pattern re-derived from a private ANSE.ASIA repo, never its literal text), `D-TIER` (every
restated self-claim from the source), `D-COMPARISON` (same/different/cited, never "we took this
from them" absent an explicit human adoption instruction).

## NC pairs

`NC-18` Source existence ≠ Claim support · `NC-19` metadata_verification ≠ scope_verification ·
`NC-20` reliable route ≠ crediting a specific source · `NC-47` AI output ≠ Evidence · `NC-59`
AI-candidate output ≠ Verified citation (Integrity Firewall).

## Not-do

- Do not restate an external source's claim about its own performance at that source's stated
  tier without independent reproduction.
- Do not merge an external skill's literal text into `plugins/`/`kernel/` — cite it as a
  dependency by name+version, per `FOUNDATION_v0.5.md` §1.2's chair ruling B3 pattern.
- Do not use a partial read (an abstract, a README summary, a search snippet) as if it were a full
  read for vetting purposes.
- Do not treat popularity, star count, or wide adoption as a substitute for reading the artifact.
- Do not name a specific external incident's details (package name, CVE, date) in this repo
  without its own citation card backing that specific detail.

## Tier

Dr (specified; independently unreviewed).
