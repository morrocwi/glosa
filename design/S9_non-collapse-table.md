# S9 — The Non-Collapse Table (append-only)

> **Tier: Dr.** Append-only ledger: ids are never reused or renumbered once assigned. This file
> is the canonical source `FOUNDATION_v0.4.md` Appendix A says it reproduces from
> (`design/S9_non-collapse-table.md`); at the time of this pass the file did not exist on disk
> under this path — **NC-01..NC-64 below are a Dr-tier reconstruction** from the compact index
> preserved in `FOUNDATION_v0.4.md` Appendix A (ids, pair text, family groupings, and
> `enforced_by` pointers only). The richer per-row detail (meaning EN/TH, failure prose, source
> line refs) that the original working file may have carried for NC-01..64 was **not recovered**
> — mark any such missing per-row prose `Open` until a source copy of the original file is found
> or those rows are independently re-expanded. **NC-65 onward are new this pass**, added per
> HANDOFF §6 request 43, sourced from `sources/WRITTEN_BY_AI_STILL_TRUE_v6.txt` (Zenodo DOI
> `10.5281/zenodo.22301202`, CC BY 4.0), with full detail (meaning EN/TH, failure, source line
> ref, enforced_by) as specified.
>
> **Rule (unchanged, chair ruling C6):** ids are assigned in order of first appearance in a
> design pass and never reused, even if a row is later found to duplicate another — a duplicate
> is noted and cross-referenced, not deleted (append-only; `feedback-sync-all-canonical-docs`).

---

## Families A–H (NC-01..NC-64) — reconstructed index, Dr, pending detail recovery

### Family A — Truth / Warrant
`NC-01` World≠Record≠Readout≠Meaning≠Truth≠Warrant≠Knowledge-Attribution · `NC-02` Truth≠Warrant≠
Practical Efficacy≠Ethical/Legal Legitimacy · `NC-03` Legitimacy≠Truth (horizontal & vertical) ·
`NC-04` legal≠epistemic · `NC-05` Solving≠true · `NC-06` correct output≠true theory
(Bounded-Judge Law) · `NC-07` Conformance≠Truth · `NC-08` readout≠truth (universal lens) ·
`NC-09` M_A[n]≠θ(E) · `NC-10` finite_diagnostic≠proof · `NC-11` Th_coqc≠finite_diagnostic≠Dr≠
Open≠fit_calibrated≠definition · `NC-12` Verified MATH≠true physics · `NC-13` Institutional
accept/reject≠Truth. *Enforced by: `tier`, `verdict_tier`, `verdict` enum, §1.3/§4.1, §7.3.*

### Family B — Access / Inference
`NC-14` Existence≠Attribution≠Disclosure (E-A-D) · `NC-15` represented≠actual essential
dependency set (Silent Lift) · `NC-16` doxastic warrant≠assertoric disclosure · `NC-17`
Mechanical validity≠Semantic validity · `NC-18` Source existence≠Claim support · `NC-19`
metadata_verification≠scope_verification · `NC-20` reliable route≠crediting a specific source ·
`NC-21` training-derived background≠current-case-specific access route · `NC-22` access model
K̃≠literally reading K* · `NC-23` P_A≠H_A (appearance≠epistemic horizon) · `NC-24`
forced≠borrowed≠Open · `NC-25` 0≠⊥ · `NC-26` "not checked"≠"checked, nothing found" (A2) ·
`NC-27` LOCAL_EVIDENCE_NOT_FOUND≠NO_LOCAL_EVIDENCE_EXISTS. *Enforced by: `silent_lift_check`,
citation card booleans, `zero_vs_bottom`, §3.3, §7.8.*

### Family C — Independence / Review
`NC-28` maker≠checker≠approver · `NC-29` AI generator≠AI reviewer of the same commit · `NC-30`
same-model self-approval≠review (MC-02) · `NC-31` ManyModels⇏Independence · `NC-32` DVP≠K2 ·
`NC-33` K1≠Certification · `NC-34` No independent check⇒No K2 / No independent check⇒No release
(two distinct gates) · `NC-35` Observation≠Claim≠Inference≠Hypothesis≠Decision≠
Valid-checkpoint≠Success≠Skill-plan≠Installed-skill≠Design-doc≠Working-product · `NC-36`
Reproduction≠Replication · `NC-37` Evidence≠Evidence Relation. *Enforced by: `independent_check`,
§4.2, §7.1–7.2.*

### Family D — Credit / Legitimacy
`NC-38` Credit≠EpistemicValue · `NC-39` Attention≠Credit · `NC-40` Friction≠Fellowship · `NC-41`
Friendship≠IndependentEvidence; Correspondence≠PeerReview; IntellectualAffinity≠Truth · `NC-42`
Production-supercritical≠Credit-supercritical · `NC-43` Latent≠Legible programme coherence ·
`NC-44` ActivationAction≠CreditEvent · `NC-45` PositionalAccess≠PopulationAuthority;
CommunityTrust≠Representativeness. *Enforced by: §7.6, §7.7.*

### Family E — Evidence / Search
`NC-46` Systematic Review≠Rapid/Scoping/Targeted evidence challenge · `NC-47` AI output≠Evidence
· `NC-48` Global/Anglophone route≠Local/Thai-language route. *Enforced by: `review_mode` enum,
§7.8.*

### Family F — Practice / Positional
`NC-49` Practice experience≠Population evidence · `NC-50` Intervention creator≠Sole evaluator ·
`NC-51` Author positional counter-readout≠External K2 · `NC-52` Thai track≠Public relations ·
`NC-53` No human available≠Research stop · `NC-54` Standpoint disclosure≠Domain-credentialed
authority. *Enforced by: `scope.generalization_claimed`, `standpoint`, §1.3.*

### Family G — AI / Authorship
`NC-55` Discovery≠Justification · `NC-56` AI exploration≠Human commitment · `NC-57` Claim scope≤
Evidence scope · `NC-58` AIContribution≠EpistemicResponsibility · `NC-59` AI-candidate output≠
Verified citation (Integrity Firewall) · `NC-60` Founder=ideas/direction≠AI=assistant · `NC-61`
questions defended without AI≠questions merely produced with AI. *Enforced by: `ai_filled`,
`produced_by`/`responsible`, §7.5, §7.8.*

### Family H — Stakeholder / Representation (chair ruling C6)
`NC-62` Stakeholder ≠ Agency — being affected by a decision is not the same as holding power over
it (skillme's stakeholder-agency map, re-derived independently, pattern only). *Enforced by:
`five_questions.assumed[]` review; the Project Advisor's stakeholder framing, §7.7.*
`NC-63` Representationality ≠ Selectivity — that a source is *representative* of a population is
a different property from that a source was *selected* by some (possibly biased) process;
conflating them silently launders a selection artifact into a population claim. *Enforced by:
`scope.generalization_claimed`, §3.2.*
`NC-64` SelfExperience ≠ GeneralEvidence — a first-person account licenses a claim about that
person's own experience, never automatically a claim about a population. *Enforced by:
`standpoint`, the preserved-experience field per genre (§6.2), §2.4.*

---

## Family I — Possession / Constitution (NC-65..NC-73, new this pass)

Source: `sources/WRITTEN_BY_AI_STILL_TRUE_v6.txt`, "Written by AI. Still True." v6 (Yaoharee
Lahtee, Aug 2026; Zenodo DOI `10.5281/zenodo.22301202`, CC BY 4.0). All nine rows tier `Dr`,
single reading, not independently cross-checked (I0/I1 only). Citation card:
`sources/citation_cards/CIT-written-by-ai-v6.yaml`.

### `NC-65` Possession ≠ Constitution

- **EN meaning:** That a subject must *possess* knowledge (be the one who knows) does not mean
  that subject *constitutes* — creates, generates, or is the source of — the evidential,
  provenance, or constraint structure that makes possession correct or incorrect. Possession is a
  condition on a knower; constitution is a condition on what can make a representation succeed or
  fail. The paper's Definition 2 names conflating them the "Possession–Constitution Collapse."
- **TH meaning (เขียนใหม่ ไม่ใช่แปล):** การที่ใครสักคนต้อง "มี" ความรู้ (เป็นผู้รู้) ไม่ได้แปลว่าคนคนนั้นเป็นผู้
  "สร้าง" โครงสร้างของหลักฐาน ที่มา หรือข้อจำกัดที่ทำให้การรู้นั้นถูกหรือผิด — การครอบครองความรู้เป็นเงื่อนไขของ
  ผู้รู้ ส่วนการก่อร่างความรู้เป็นเงื่อนไขของสิ่งที่ทำให้ข้อความนั้นสำเร็จหรือล้มเหลว
- **Failure if collapsed:** A schema or reviewer starts requiring a named human "knower" before a
  route can be typed, checked, or gated — reintroducing the exact collapse the paper diagnoses,
  and blocking glosa's own non-knower roles (mechanical checks, AI-generated drafts,
  instrument-like retrieval routes) from occupying an epistemically productive position.
- **Source line ref:** lines 247–249 (Definition 2, Possession–Constitution Collapse).
- **Enforced by:** absence of any "possession"/"knower" field in the claim card schema (§3.2,
  Pillar 2 §2.1 crosswalk, `design/S15_pillars-ontology-epistemology-methodology.md`); `NC-58`
  AIContribution≠EpistemicResponsibility (existing row, same family).

### `NC-66` m(A) ≠ ρ(A) — source metadata ≠ reliability estimate

- **EN meaning:** Metadata about a source ("senior professor," "AI-generated," "anonymous") is
  not identical to the reliability estimate an evaluator extracts from it, and neither is
  identical to the epistemic standing of the claim itself. Metadata can be *evidence for* a
  reliability estimate; it is never the estimate, and the estimate is never the claim's standing.
- **TH meaning:** ข้อมูลเมทาดาทาเกี่ยวกับแหล่งที่มา ("อาจารย์อาวุโส", "AI สร้าง", "ไม่ระบุนาม") ไม่ใช่สิ่ง
  เดียวกับค่าประเมินความน่าเชื่อถือที่ผู้ประเมินดึงออกมา และทั้งสองอย่างก็ไม่ใช่สถานะทางญาณวิทยาของข้อความ
  นั้นเอง — เมทาดาทาเป็น "หลักฐานสำหรับ" การประเมิน ไม่ใช่ตัวการประเมิน และการประเมินก็ไม่ใช่สถานะของ
  ข้อความ
- **Failure if collapsed:** A citation card's `metadata_verified: true` (existence/metadata check
  only) gets read as if it were `claim_match_verified` (does the passage actually support the
  claim) — the exact collapse the citation card template's own binding invariant (line 8) already
  forbids in its own words ("metadata_verified != claim_match_verified. Never infer one from the
  other").
- **Source line ref:** lines 270–281 (m(A) ≠ ρ(A), Principle 1 context).
- **Enforced by:** `citation_card.yaml` `metadata_verified` vs `claim_match_verified` (two
  independent booleans, `status: VERIFIED` requires both true); `NC-19`
  metadata_verification≠scope_verification (existing, adjacent row — `NC-66` names the general
  principle `NC-19` already applies to the citation-card case specifically).

### `NC-67` Credibility ≠ Legitimacy

- **EN meaning:** Credibility is the weight actually or rationally assigned to a source;
  legitimacy is the standing a social or institutional order grants to a source or claim. A claim
  can be epistemically strong (high credibility) and institutionally illegitimate; a claim can be
  institutionally legitimate and false.
- **TH meaning:** ความน่าเชื่อถือ คือ น้ำหนักที่ให้กับแหล่งข้อมูลจริงหรือควรให้อย่างมีเหตุผล ส่วนความชอบธรรม
  คือ สถานะที่ระเบียบสังคมหรือสถาบันมอบให้แหล่งข้อมูลหรือข้อความนั้น — ข้อความหนึ่งอาจแข็งแรงทาง
  ญาณวิทยาแต่ไม่ชอบธรรมทางสถาบัน หรือชอบธรรมทางสถาบันแต่เป็นเท็จก็ได้
  ("ข้อเสนออาจมีหนังสือเดินทางแต่ยังผิดอยู่ดี" — line 721, restated in our own words)
- **Failure if collapsed:** A future glosa gate treats a venue acceptance, institutional
  endorsement, or credential as if it raised the claim's actual credibility/tier — exactly the
  failure `D-NO-VERTICAL-AUTHORITY` and the Verification Paradox section (Pillar 2 §2.5) already
  forbid.
- **Source line ref:** lines 714–721.
- **Enforced by:** `D-NO-VERTICAL-AUTHORITY` (FOUNDATION §5); `k_state` K2/K3 gated on `I5`
  (independent human), never on institutional acceptance (§4.2); `NC-13` Institutional
  accept/reject≠Truth (existing, adjacent — `NC-67` is the credibility/legitimacy-specific form).

### `NC-68` Co-location ≠ Identity (of roles)

- **EN meaning:** That one human agent commonly occupies several epistemic roles at once
  (generation, endorsement, accountability, credibility) does not make those roles identical to
  each other. The bundle is historically common, not logically necessary — Principle 1's Role
  Separation and Table 1's ten roles exist precisely because co-location is mistaken for identity.
- **TH meaning:** การที่คนคนเดียวมักทำหลายบทบาททางญาณวิทยาพร้อมกัน (สร้าง, รับรอง, รับผิดชอบ,
  น่าเชื่อถือ) ไม่ได้แปลว่าบทบาทเหล่านั้นเป็นสิ่งเดียวกัน — การอยู่รวมกันบ่อยในประวัติศาสตร์ ไม่ใช่ความจำเป็น
  เชิงตรรกะ
- **Failure if collapsed:** A reviewer credits a claim card's `evidence` role because its
  `produced_by` field also carries high `credibility`/reputation — sliding from "this person is
  credible" to "this evidence relation is strong" without checking the evidence relation itself.
- **Source line ref:** lines 258–263, 276–279 (Role Separation, Principle 1).
- **Enforced by:** Table 1 crosswalk (`design/S15_pillars-ontology-epistemology-methodology.md`
  Pillar 2 §2.1) — ten distinct glosa fields/gates, none of which reads another's value by
  default.

### `NC-69` Two interfaces ≠ two routes

- **EN meaning:** A claim can appear to have two independent checks (two chat windows, two model
  names, two "buttons") while the generator, verifier, retrieval system, benchmark, or dataset
  share a hidden common source — making it one epistemic route wearing two interfaces.
  Independence is a property of the route's actual dependency structure, not of interface count.
- **TH meaning:** ข้อความหนึ่งอาจดูเหมือนผ่านการตรวจสองทางที่เป็นอิสระต่อกัน (สองหน้าต่างแชท สองชื่อโมเดล
  "สองปุ่ม") ทั้งที่ตัวสร้าง ตัวตรวจ ระบบสืบค้น เกณฑ์วัด หรือชุดข้อมูล มีที่มาร่วมกันซ่อนอยู่ — กลายเป็นเส้นทาง
  ญาณวิทยาเดียวที่สวมหน้ากากสองหน้า — ความเป็นอิสระเป็นคุณสมบัติของโครงสร้างการพึ่งพาจริงของเส้นทาง ไม่ใช่
  จำนวนอินเทอร์เฟซ
- **Failure if collapsed:** Two model calls from the same vendor, or two retrieval passes over
  the same corpus, get logged as two `tested.evidence_relations[]` entries at `independence_class:
  I2`/`I3` each, inflating the route's apparent independence by counting interfaces rather than
  checking shared operator/training/data ancestry.
- **Source line ref:** lines 826–835 (Objection 8 and its reply).
- **Enforced by:** single `independence_class: I0..I5` string ladder in every schema, never a
  count (§4.2, chair ruling C1); Route Dependence Matrix (`templates/knowledge/
  route_dependence_matrix.yaml`) records `operator` per route; `D-OPERATOR-SHARED` disclaimer;
  `NC-31` ManyModels⇏Independence (existing, closely related — `NC-69` is the general
  "interface vs. route" statement `NC-31` already applies to the specific many-models case).

### `NC-70` Address of responsibility ≠ address of truth

- **EN meaning:** A recognizable human is an administratively convenient address for trust,
  blame, credit, responsibility, and legitimacy. That convenience is real, but it is not
  epistemology — the address where responsibility is settled is not thereby the address where
  truth is settled.
- **TH meaning:** มนุษย์ที่จำได้ง่ายเป็น "ที่อยู่" ที่สะดวกทางบริหารสำหรับความไว้ใจ การตำหนิ เครดิต ความ
  รับผิดชอบ และความชอบธรรม — ความสะดวกนั้นมีจริง แต่ไม่ใช่ญาณวิทยา — ที่อยู่ซึ่งความรับผิดชอบถูกกำหนดไว้
  ไม่ใช่ที่อยู่เดียวกับที่ความจริงถูกกำหนด
- **Failure if collapsed:** `human_owner`/`responsible: human` (the accountability address) gets
  read as evidence that the claim itself is true, well-supported, or high-tier — the two fields
  answer different questions and must never be cross-read as if one raised the other.
- **Source line ref:** lines 462–466.
- **Enforced by:** `responsible: human` and `tier`/`k_state` are structurally independent kernel
  fields — no §3.3 rule conditions `tier` or `k_state` advancement on `responsible`'s value (it is
  always `human`, a constant, and therefore cannot carry information that discriminates
  claims — this is a built-in enforcement, not an added check).

### `NC-71` RA ≠ W — the record is not the world

- **EN meaning:** The record `RA` an agent or system receives under an access operator and
  selection policy (`RA = OA(W; ΠA)`) is not identical to the worldly condition `W` it reports on.
  This holds regardless of whether the agent is human or not — "human observers do not escape this
  merely by having biographies."
- **TH meaning:** บันทึกที่ตัวแทนหรือระบบได้รับผ่านตัวดำเนินการเข้าถึงและนโยบายการเลือก ไม่ใช่สิ่งเดียวกับ
  สภาวะของโลกจริงที่บันทึกนั้นรายงานถึง — ไม่ว่าตัวแทนนั้นจะเป็นมนุษย์หรือไม่ก็ตาม "ผู้สังเกตที่เป็นมนุษย์ก็ไม่
  รอดพ้นจากเรื่องนี้เพียงเพราะมีชีวประวัติ"
- **Failure if collapsed:** A `five_questions.seen` (Q1) entry gets treated as if it *were* the
  worldly fact rather than an operator-conditioned readout of it — the exact readout-not-truth
  violation the glosa gate (CLAUDE.md rule 1) is built to prevent, now traced to this paper's own
  formalism as an independently-arrived-at same reading.
- **Source line ref:** lines 251–269 (the RA = OA(W;ΠA) formalism).
- **Enforced by:** `five_questions.seen.record_ref`/`access_model`/`retrievable_original`
  (distinguishes the record from the world by requiring the record's own provenance, never
  asserting the world directly); `NC-08` readout≠truth (existing, same family — `NC-71` is this
  paper's independently-formalized version of the same distinction, cited as *same*, not
  *adopted from*, per gate rule 6 — the lineage of readout-not-truth in glosa runs through
  Readout Universe/Genesis, `lens_used` block, not through this paper).

### `NC-72` Constraint ≠ evidence-for-us

- **EN meaning:** A pre-subjective constraint structure (Definition 1) need not already be
  "evidence-for-us," meaningful-to-us, or anyone's knowledge in order to constrain what later
  inquiry can responsibly say. A worldly difference can be real and load-bearing before any
  practice has taken it up as evidence within a vocabulary — and, symmetrically (Objection 7), an
  *unnamed, unrepresented* possible failure mode is not thereby evidence against a route either:
  ignorance is uncertainty, never a disguised defeater.
- **TH meaning:** โครงสร้างข้อจำกัดก่อนอัตวิสัย (นิยาม 1) ไม่จำเป็นต้องเป็น "หลักฐานสำหรับเรา" หรือมี
  ความหมายต่อเราอยู่แล้ว หรือเป็นความรู้ของใครก็ตาม เพื่อที่จะจำกัดสิ่งที่การสืบค้นในภายหลังจะพูดได้อย่างมี
  ความรับผิดชอบ — ความแตกต่างในโลกจริงอาจมีอยู่จริงและมีน้ำหนักได้ ก่อนที่การปฏิบัติใดจะหยิบมันมาเป็น
  หลักฐานในคำศัพท์ของตน — และในทางกลับกัน (ข้อโต้แย้งที่ 7) โหมดความล้มเหลวที่ยังไม่ถูกระบุชื่อ ก็ไม่ใช่
  หลักฐานคัดค้านเส้นทางนั้นเช่นกัน — ความไม่รู้คือความไม่แน่นอน ไม่ใช่หลักฐานที่ปลอมตัวมา
- **Failure if collapsed (two directions):** (a) treating a raw observation as inadmissible
  because it has not yet been formalized into a typed field — losing real constraint structure by
  demanding premature formalization; (b) the Objection-7 direction — logging an unnamed "AI might
  have unknown failure modes" worry as a `tested.evidence_relations[]` entry with `bearing:
  CHALLENGES` and no `evidence_id`, making an unfalsifiable pedigree penalty masquerade as
  evidence.
- **Source line ref:** lines 159–166 (Definition 1); lines 904–921 (Objection 12 reply,
  constraint-not-yet-evidence); lines 795–805 (Objection 7, unknown-unknowns as uncertainty).
- **Enforced by:** `provenance_indeterminate` access type (S2, still admissible, typed honestly
  rather than discarded); new kernel-rule patch (`design/FOUNDATION_v0.5_PATCH.md` §5): an
  `evidence_relations[]` entry with `bearing: CHALLENGES` requires a non-empty `evidence_id` —
  an unnamed challenge belongs in `identification_ladder`'s `unidentified` value or `non_claims`,
  never in the evidence list.

### `NC-73` Certification ≠ Warrant

- **EN meaning:** An institution's act of certifying, accepting, or publishing a claim is not
  itself the epistemic warrant for that claim. Certification can *carry* warrant when it is the
  visible trace of real epistemic friction (criticism, replication, robustness testing) — but the
  stamp itself, held apart from that friction, produces permission, not warrant. "Authority should
  be the receipt for epistemic work, not the merchandise."
- **TH meaning:** การที่สถาบันรับรอง ยอมรับ หรือตีพิมพ์ข้อความหนึ่ง ไม่ใช่ตัวเหตุผลรับรองทางญาณวิทยาของ
  ข้อความนั้นเอง — การรับรองอาจ "พา" เหตุผลรับรองมาด้วยได้ เมื่อมันเป็นร่องรอยที่มองเห็นได้ของแรงเสียดทาน
  ทางญาณวิทยาจริง (การวิพากษ์ การทำซ้ำ การทดสอบความทนทาน) — แต่ตราประทับเพียงลำพัง แยกจากแรงเสียด
  ทานนั้น ให้แค่การอนุญาต ไม่ใช่เหตุผลรับรอง — "อำนาจควรเป็นใบเสร็จของงานทางญาณวิทยา ไม่ใช่ตัวสินค้า"
- **Failure if collapsed:** Treating a journal acceptance, institutional review pass, or public
  "peer reviewed" label as itself raising a card's `tier`/`k_state`, without the card also naming
  the friction (an actual `evidence_relations[]` route at the required `independence_class`) that
  earned it.
- **Source line ref:** lines 688–691 (Principle 5, Friction not magic); lines 735–751 (the
  Verification Paradox); line 745 ("Authority should be the receipt for epistemic work, not the
  merchandise").
- **Enforced by:** `D-NO-VERTICAL-AUTHORITY`; `k_state` K1/K2/K3 gates keyed to
  `independence_class` routes, never to a venue/institution field (§4.2, §3.3 rules 1–4, 9);
  `NC-33` K1≠Certification (existing, adjacent — `NC-73` states the general principle behind that
  specific K1 rule, cited from this new source).

---

## How this table is used

Unchanged in mechanism from the FOUNDATION_v0.4 Appendix A framing (preserved, not itself
reconstructed from memory since the mechanism, not the row detail, is what Appendix A's own text
states): every `NC-*` row names a pair that must never be silently identified, the concrete
failure that results if it is, and the glosa field/gate/disclaimer that mechanically or
procedurally enforces the separation. A reviewer checking a claim card or a document may cite an
`NC-*` id directly as the reason a specific inference is refused (e.g. "this sentence commits
`NC-66`: it reads `metadata_verified` as if it were `claim_match_verified`").
