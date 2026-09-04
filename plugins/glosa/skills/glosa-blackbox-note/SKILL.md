---
name: glosa-blackbox-note
description: Record or extend a Blackbox Note — the verbatim, never-edited-in-place log of a human's raw dialogue lines plus the append-only cooking log, the required lens_used attribution block, and the hypothesis signature line. Triggers - "blackbox note", "raw line", "verbatim", "cooking log", "lens_used", "hypothesis signature", "who said this", "R0" (superseded term), "readout universe attribution".
---

# glosa-blackbox-note

> tier: Dr (specified; independently unreviewed). Readout-not-truth applies to this file.

## Load first

- `../../../../schema/blackbox_note.schema.json` — authoritative field list: `id`, `participants`,
  `language`, `privacy_scan`, `lines[]` (verbatim, never edited/translated in place — a correction
  is a new line), `cooking[]` (append-only: `lens_in`/`analysis`/`lens_out`/`revision`/
  `translation`/`review` steps).
- `../../../../methodology/P00_lens.md` — the Lens Law: the lens translation that must happen
  before any Five Question is answered from a Blackbox Note line.
- `../../../../design/FOUNDATION_v0.5.md` §2.3 — the `lens_used` block and hypothesis signature
  rule in full (founder requests 38/38b/38c/38d, binding). Do not restate its wording here; read it
  there.
- `../../../../templates/knowledge/blackbox_note.yaml` — fill-in template.

## Pending protocol card

`../../../../design/REPO_SPEC_v0.5.md` names `methodology/P15_blackbox_note.md` as the owning
protocol card for this skill's full narrative (split out from the intake/claim-card cards it was
previously implicit in). **That file does not exist yet in this checkout** — until it lands, use
`P00_lens.md`, `P02_intake.md` §"Blackbox Note line" input, and `FOUNDATION_v0.5.md` §2.3 directly.

## Hard rules (pointer only — full text in the sources above)

1. Raw lines are verbatim, never edited or translated in place — a correction is a **new** line.
2. `cooking:` is append-only.
3. Every note carries a `lens_used` block; the required display string is exactly
   `"Readout Universe — Yaoharee Lahtee"` (`FOUNDATION_v0.5.md` §2.3, §6.4). Missing or wrong ⇒
   `D-LENS-UNCITED`/`D-LENS-UNSIGNED` (`FOUNDATION_v0.5.md` §5) — hard validation errors, not
   warnings.
4. Every hypothesis statement carries a signature line naming the lens `lens_ref` points at
   (`FOUNDATION_v0.5.md` §3.3 rule 12).
5. `privacy_scan` must be `done`, not `pending`, before any line is marked `public`.

## Related

- `../../../../methodology/P11_log_and_decision.md` — how `cooking:` entries and
  `origin_blackbox_ref` feed the Disagreement Ledger and decision log.
- `../../../../methodology/P13_literature_review.md` §"hypothesis selection" — where a
  hypothesis's cooking-log selection reasoning is logged.
- `glosa-publish-gate` — R1 leak scan and the reflexive glosa-cites-glosa `D-LENS-UNCITED` check
  run again, independently, before anything public.
