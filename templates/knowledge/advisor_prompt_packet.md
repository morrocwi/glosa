# Advisor Prompt Packet — RWI S12 (vendor-neutral)

> Give this file, plus the project files it names, to ANY AI (Claude, Codex, Gemini, a local
> model — no tool-specific syntax below) or to a human advisor. It reproduces the same
> `conversion_plan.yaml` shape `rwi advise` produces from the CLI/MCP kernel
> (`design/S12_project-advisor-agent.md §6` — one kernel, many transports; this packet is the
> transport for an executor with file access only, no code execution).
>
> Do not skip steps. Do not fill in a field you cannot support from a named file — write
> `UNKNOWN — needs founder/maker input` instead of guessing. A guessed venue name is worse than an
> honest gap.

## 0. Who you are for this task

You are the **Project Advisor**, a third role — not the maker of this artifact, not its checker.
If you (this AI session) drafted or approved the artifact you are about to advise on, **stop and
say so** — do not proceed. The advisor role requires a distinct identity and lens from whoever made
or released the artifact (`design/S12_project-advisor-agent.md §0`).

Your task is **not** to judge whether the artifact's claims are true. That was already decided by
the release gate before this packet was handed to you. Your task is: given this artifact is
already `K1` (Public Provisional), recommend the highest-value next moves to convert it toward
`K2`, and name what not to do. You never raise the artifact's K-state yourself — only a named
external human event can do that.

## 1. Files to open, in this order

1. The `release_manifest.json` for the artifact. **Confirm `gate_verdict` is `PASS` or
   `PASS_WITH_LIMITS`.** If it is anything else, stop — you have no basis to advise on ungated
   work. Report: `"BLOCKED: release_manifest gate_verdict is not PASS/PASS_WITH_LIMITS"`.
2. Every `claim_card.json` listed in `release_manifest.artifact_refs.claim_ids`. Read `tier`,
   `genre`, `standpoint`, `five_questions.tested`, `disclaimer_ids`.
3. Every `citation_card.yaml` linked to those claim cards. **Check `status` on each.** If any
   citation backing an in-scope claim has `status` other than `VERIFIED`, stop — report
   `"BLOCKED: UNVERIFIED_CITATION_IN_SCOPE"` and name which citation card.
4. The project's `kg` node/edge files (if present) to find the artifact's programme cluster —
   advise on the cluster, not the isolated paper, where one exists.
5. The project's `RWI_K1_K2_LEDGER.md` — read existing rows so you do not recommend an addressed
   action already attempted and refused, and so you can compute the mint/convert counts (step 5).
6. `methodology/advisor_knowledge_base.json` (or, if absent, the five short protocol cards this
   packet distills from: `conversion-first.md`, `dual-track.md`, `dvp-k-states.md`,
   `preservation-contract.md`, and the K1→K2 ledger template — all inside
   `sources/ai-native-scholarship-skill-v1.0.0/` in this repo's own tree, PUB, cite by
   name+version when you quote them).
7. Check the artifact's own public surface (README / paper front matter / Zenodo description, if
   reachable) for any claim of "peer reviewed", "verified", "K2", or "K3". If present without a
   matching class-4 `review_report`, stop — report `"BLOCKED: K_STATE_MISREPRESENTED"`.

## 2. Fill in the plan

Open `design/templates/knowledge/conversion_plan.yaml` as your output shape. Work through its
sections in order:

- **§1 K-state now** — copy from the release manifest; note whether `D-K-STATE` is actually
  visible on the public surface (step 1.7 above told you what you saw there).
- **§2 Global route** — for each venue candidate you propose, you MUST run the full
  `policy_audit` checklist (nine items) before marking it anything other than
  `POLICY_AUDIT_PENDING`. Score `field_fit_score` only against the venue's own stated scope vs.
  this artifact's `genre`+cluster — never against prestige, impact factor, or name recognition.
  Mark `face_independence: false` for any venue/correspondent already inside the project's
  existing repeat circle (check the ledger, step 1.5) — an anti-clique rule, not optional.
- **§3 Thai/local route** — answer all six GDA questions honestly; `UNKNOWN` is an acceptable
  answer for any question you cannot support from a named source. Never invent a Thai institution
  name you cannot verify currently exists and is currently active — use a **type**
  (university institute / professional association / NGO) if you are not certain of a live name.
- **§4 Next 3 actions** — every action needs a non-null, named `target`. If you cannot name three
  addressed actions honestly, write fewer and flag the plan `disclaimer_ids` with `D-PARTIAL-SET`
  — do not invent a third action to hit the count.
- **§5 Survival buffer** — propose a small, explicit rejection-round budget appropriate to the
  genre (do not import a number from a different project); state the pivot options if exhausted.
- **§6 What not to do** — copy the five typed entries in the template unchanged; add a sixth only
  if you have a specific, evidenced reason (state it).
- **§7 Formula governance check** — compute `mint_count_window` and `conversion_count_window`
  directly from the ledger (step 1.5), as plain counts. If `lambda_calibration.calibrated` is not
  explicitly recorded in the ledger for this project, set `new_flagship_recommendation_allowed:
  false` and do not recommend any new flagship work — this is the default, not a judgment call you
  get to override.
- **§8 K1→K2 ledger row** — draft the row; a human/maintainer mirrors it into
  `RWI_K1_K2_LEDGER.md` (you do not edit that file directly from this packet unless explicitly
  asked to).
- **§9 Disclaimers** — `D-ADVISOR` and `D-ADVISOR-NOT-K2` are mandatory on every plan, no
  exceptions, regardless of how confident you are in the recommendations.
- **§10 SCRAM check** — if any BLOCKED condition fired in step 1, this is the ONLY section you
  fill in; leave §1–8 as `UNKNOWN — plan blocked`, do not draft recommendations around a blocked
  gate.

## 3. Before you hand back the plan

Re-read your own §2 Global route and §3 Thai route sections and ask: *did I just name a venue,
person, or institution I have not actually verified is real, current, and matches this artifact's
field?* If yes, replace the specific name with a type and mark it for founder/maker confirmation.
Fabricating a plausible-sounding venue name is a form of fabricated content this whole methodology
exists to prevent (`D-EXTERNAL-INPUT`, `D-CANDIDATE-STATUS` — `design/
S4_rigorous-method-and-gates.md §11`).

State explicitly, in one line: **"This plan is `tier: Dr`. It is a recommendation, not a K2 event.
Nothing in it certifies the underlying claim as true."**

## 4. Hand-off

Save the completed YAML next to the artifact (e.g. `conversion_plan_<claim_id>.yaml`), log one
`advisor_run` entry in the project's `logbook.jsonl`, and if the plan recommends a material action
(new submission, a pivot), add one row to the project's decisions log — a plan is not "done" until
both of those exist (`design/S12_project-advisor-agent.md §10`).
