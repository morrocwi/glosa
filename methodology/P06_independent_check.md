> tier: Dr (specified; independently unreviewed)

# P6 — Independent Check (maker≠checker≠approver; L0–L5; independence ladder I0–I5 with tier/K ceilings; DVP roles; Resolve-or-Declare; Query Stop)

## One-line rule

No independent check ⇒ no release: maker, checker, and approver must be three pairwise-distinct
identities whenever an artifact's status advances past Pending Review, and the *class* of check
(I0–I5, one string ladder in every schema) bounds the maximum tier and K-state that artifact can
ever reach — regardless of how many same-level routes were stacked.

## Why

`AGENTS.md` gate rule 3 states this plainly for the whole repo: "Maker ≠ checker ≠ approver. Never
certify what you produced. Same-model self-review has no standing." The independence ladder itself
is the AI assistant's ruling on founder request 18, 2026-09-04
(`HANDOFF_2026-09-04_founding-meeting.md` §6): "ทำระบบว่าต้องตรวจข้าม AI คนละยี่ห้อถึงจะเพิ่มความแม่นยำ
แม้ยังไม่คุยกับมนุษย์" → resolved as I0 self → I1 same model new session → I2 same vendor other model
→ I3 different vendor (K1-public-provisional minimum) → I4 mechanical/original-record → I5
independent external human (only route to K2), with `ManyModels⇏Independence` (`NC-31`) staying
binding. The reason this ladder has teeth: `design/FOUNDATION_v0.5.md` §3.3's opening paragraph
names a real, convergent finding across three independent design reviewers (S3/S4/S7) that the
schemas as first drafted let "a **solo AI session** reach `tier: Th_coqc`, `k_state: K2`, and
`status: Approved-for-Live` with **zero humans and zero mechanical artifacts involved**" —
directly contradicting `DVP ≠ K2` and MC-05. §3.3 rules 1–4, 9, and 11 are the specified fix for
exactly that bug. The bounded I2+I4 exception is chair ruling B4 (2026-09-04, §4.2), a narrow
carve-out for a single-vendor scholar that "never opens a K2 door."

## Inputs → outputs

- Input: a `claim_card` reaching an artifact-consequence level (`schema/claim_card.schema.json`
  `independent_check`), or a route packet at `reviews/routes/<claim_id>/<route_id>/PACKET.md`
  (`templates/knowledge/cross_vendor_review_packet.md`).
- Output: `claim_card.independent_check` (`status, maker_id, checker_id, approver_id,
  independence_class, mc_level, date, expires_at`), `schema/review_report.schema.json`
  (`verdict_tier`, per Bounded-Judge Law, §7.3), `templates/knowledge/route_dependence_matrix.yaml`
  (route_id, vendor, model, prompt_ancestry, operator, shared_with[], independence_level), and a
  per-project Disagreement Ledger row (`nature, outcome: RESOLVED|DECLARED, decisive_record`) — the
  Resolve-or-Declare rule: an unresolved cross-route disagreement is never averaged or silently
  dropped, it is declared open (`D-DISAGREEMENT-OPEN`).

## Gate

`independent_check.status` may be `PASSED` only when `independence_class ∉ {I0, I1}` (MC-02, §3.3
rule 1). `tier: Th_coqc` requires an I4/I5 evidence relation, never I3 alone (rule 2).
`k_state: K2`/`K3` requires I5 (rule 4) — no stacking of I0–I4 ever opens that door (`DVP≠K2`,
`NC-32`). `k_state: K1` requires ≥I3, or the bounded I2+I4 exception's full condition set (rule 9,
new this pass, closing the exact gap where §6.4's older `≥I2` wording contradicted §4.2's own
table). `status` may advance past Pending Review only when maker/checker/approver are pairwise
distinct, checked on the payload directly (rule 5). The MIMCG L0–L5 table (§7.1) maps this onto
release scope: L3 (public `main`) needs I3-or-exception **plus** a distinct human Approver
(release authority, not a verification level); L5 (any "verified/K2/certified" wording, a minted
DOI, or a journal submission) needs I5 — the founder's Approver role at L3 never substitutes for
L5's I5 requirement.

**Query Stop Rule** (`design/FOUNDATION_v0.5.md` §4.3): one recorded attempt per acceptance-
criteria version — re-asking a route until it agrees is a named SCRAM condition, never a legitimate
route to consensus.

## Human / AI division of labour

Human: is Checker or Approver whenever the artifact reaches L3+, never the same identity as Maker
(FOUNDATION §2.2, S4 row); is the only route that can ever supply I5. AI: may be Checker only at
I2/I3 — never the sole gate to K1 without an I3 route, never K2 alone. A DVP route reads only its
own packet (the vendor-neutral gate block, §4.3) and never edits the claim card.

## Disclaimers emitted

`D-INDEPENDENCE` (`tested`'s strongest entry is I0–I2) · `D-INDEPENDENCE-LEVEL` (any published
surface names a specific level) · `D-DVP-NOT-K2` (public text says "verified/peer reviewed/
certified/K2/K3" while `tested` tops out below I5) · `D-SAME-VENDOR` (the bounded I2+I4 exception
in use) · `D-OPERATOR-SHARED` (identical `operator` across all routes, ODC undocumented) ·
`D-DISAGREEMENT-OPEN` (a Disagreement Ledger `outcome: DECLARED`).

## Non-collapse pairs enforced

`NC-28` maker≠checker≠approver · `NC-29` AI generator≠AI reviewer of the same commit · `NC-30`
same-model self-approval≠review (MC-02) · `NC-31` ManyModels⇏Independence · `NC-32` DVP≠K2 ·
`NC-33` K1≠Certification · `NC-34` No independent check⇒No K2 / No independent check⇒No release
(two distinct gates) · `NC-36` Reproduction≠Replication · `NC-37` Evidence≠Evidence Relation.

## What this card does NOT do

It does not judge the semantic correctness of a claim — the independence ladder gates *who/what*
checked it and at what class, never whether the checker's own reasoning was right (that residual
judgment risk is exactly why the ladder, not a single review, is the mechanism). It does not
manufacture I5 — "who occupies I5 is the single most consequential open item" (`design/
FOUNDATION_v0.5.md` §11, item 7): without a named external human, no glosa claim can ever reach
K2, and this card does not solve that founder-only decision. It does not let a founder-as-Approver
sign-off at L3 stand in for L5's I5 requirement, ever (Class-5-never-substitutes-for-I5 rule).
