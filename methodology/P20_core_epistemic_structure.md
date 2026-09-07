# P20 — Core Epistemic Structure: who brought the world in, who bridged, which machines took part

tier: Dr (specified; independently unreviewed)

> readout-not-truth applies to this card itself. Founder ruling 2026-09-07 (Blackbox Log BBL-2026-09-07-216 and
> BBL-2026-09-07-217, the latter relayed from the founder's reading of Collins and Evans on experience-based and
> interactional expertise). AI drafted this card. Comparison language is same/different/cited only.

## id

`P20`

## Rule

Every draft, paper, note, or deposited record of the programme carries a mandatory block, near the top, in this exact
shape (template: `templates/core_epistemic_structure.md`):

> **Core Epistemic Structure**
> **Core Respondent / Experience-Based Expert:** [name or anonymised role] — [basis of experience]
> **Interactional Expert:** [name / role] or **None**
> **AI Model(s) Used:** [Model 1 — role]; [Model 2 — role]; …

Three roles, never merged, because each contributes a different kind of knowledge:

1. **Core Respondent / Experience-Based Expert** — the person who lives with the problem and has specific experience
   from practice (an entrepreneur, a patient, a farmer, a craftsperson, a teacher, an officer, a practitioner in that
   field). No academic credential is required: experience-based expertise is separated from certification. This person
   is the owner of the problem or the project's primary source of world contact.
2. **Interactional Expert** — someone who understands the language, concepts, standards and practice of another world
   well enough to converse, analyse and translate across groups without necessarily doing that work. If the project
   has no such person, write **None**. Never appoint someone to fill the slot: "None" is itself epistemic information
   (the role is not yet held).
3. **AI Model(s) Used** — every model that actually played a part, each with its role (literature search, rival
   hypothesis generation, formalisation, adversarial review, provenance audit, typesetting, …). Two models ⇒ two
   entries; never the summary "AI was used".

Non-collapse rule of the system (Toledo code weld/H.33.v1, registered before use per `P19`):

    Experience-Based Expertise ≠ Interactional Expertise ≠ AI Model

A model that connects and widens the candidate space does not thereby become an experience-based expert: it was not
at the site of the problem. A person with real experience does not thereby hold interactional expertise across fields.

Formal objects (founder's [New Definition / Proposal], registered in Toledo 2026-09-07 — cite these codes): E_p = weld/H.30.v1; M_p^AI = weld/H.31.v1; X_p^int = ∅ = weld/H.32.v1; the non-collapse rule = weld/H.33.v1 (tier Dr); X_p^exp = ⟨Exp, Sel, Int⟩ = weld/H.34.v1 (Toledo v1.4.0, concept DOI 10.5281/zenodo.22537318):

    E_p = ⟨ X_p^exp , X_p^int , M_p^AI ⟩ ,   M_p^AI = { M_1, …, M_k } ,   X_p^int = ∅ when no interactional expert holds the role.

`M_p^AI` is a set, since one project may use several models; `X_p^int = ∅` means the role is unheld, not a zero score.


### The experience-holder, in three components (founder emphasis, 2026-09-07)

The Core Respondent's contribution is read in three parts, each a readout of practice and none a warrant by position:

    X_p^exp = ⟨ Exp , Sel , Int ⟩

- **Exp — lived experience (world contact):** experience-based expertise separated from certification (Collins and
  Evans, *Studies of Expertise and Experience*), tacit and personal knowledge (Polanyi), lived experience in the
  phenomenological sense, situated knowledge (Haraway; standpoint epistemology).
- **Sel — selection (decisions taken):** recognition-primed, naturalistic decision making (Klein; Kahneman and Klein on
  when expert intuition is reliable: regular environments with feedback), practical wisdom (Aristotle's phronesis),
  enactment → selection → retention (Weick).
- **Int — interpretation (meaning given):** sensemaking (Weick), hermeneutic application from the practitioner's
  horizon (Gadamer), reflection-in-action (Schön).

Write the block line with the basis of each part, e.g. "lived experience: …; selections: … (recorded in the Blackbox
Note); interpretation: …". Related terms usable as support: *expert by experience* (health and social-care
involvement literature), *lay expertise* (Epstein) — with Collins and Evans's own caution that experience-based
standing is not authority. Citation details (year, page, DOI) are to be verified under rule 17 before they enter a
paper; this card names the sources only.

## Why / incident

The manuscript *The Economics of Expertise in the Age of Generative AI* (v1.0, 2026-09-07) introduced a three-part
project registration and used it on itself. Reading it, the founder ruled that the block becomes the default of every
draft: a reader must see at once who brought the real world in, who did the bridging, and which machines produced or
transformed knowledge, with none of the three blended into the others. It extends `P7` (AI-fill disclosure by route)
from "what the AI added" to "which role each participant held".

## Inputs → outputs

- **Inputs:** the project's people and models and their actual roles at the time of writing.
- **Outputs:** the block in the draft; the same facts in the deposit metadata where the record type allows a role list;
  a line in the Blackbox Note when a role changes between versions.

## Gate

A draft without the block, or with an interactional expert named only to fill the slot, or with an AI line that names
no model or no role, does not pass the publish gate (`P10`). Naming an AI model inside this block is disclosure of a
role, not authorship or credit: the no-AI-attribution rule (`P10`, gate rule 9) still forbids any AI as author,
co-author or contributor, and the founder's per-artifact permission is recorded in the Blackbox Log when a model is
named in a public artifact (BBL-2026-09-07-214/215 for the first such case).

Enforcement (2026-09-07): `kernel/glosa_kernel.py`'s `gate_release` hard-fails a `release_manifest`
missing a `core_epistemic_structure` field (schema/core_epistemic_structure.schema.json) or carrying
one that does not validate (`glosa ces check <path...>` / `scripts/check_core_epistemic_structure.py`
run the same check against a raw Markdown/LaTeX/YAML/JSON file). The pre-commit/`scripts/check_repo.sh`
gate applies this check to a tracked file under `paper/`, `cases/`, `records/`, or `templates/` ONLY
when that file matches `templates/paper/*/main.tex` (the two paper templates that already carry the
block; their `disclaimers.tex`/`refs.bib` siblings are included files, not the document itself, and
are out of scope) or its own first 5 lines declare `ces: required` — a historical file that predates
this ruling and declares neither is not retroactively failed by this gate; a project that wants the
gate on a specific file opts in by adding that marker line. `templates/knowledge/*.yaml` data-card
templates (citation cards, blackbox notes, etc.) are deliberately out of scope of both the mandatory-
block requirement and this gate: they are structured ledger rows validated by their own schema, not
a "draft, paper, or note" in P20's sense; `templates/knowledge/*.md` protocol/checklist templates are
likewise out of scope for the same reason, except `project_skeleton.md`, which documents (without
itself carrying the block) that `paper/main.md`/`paper/main_en.md` must.

## Human / AI split

Founder/human: decides who holds each role and whether the interactional slot is None. AI: fills its own line with its
model name and its actual roles, never more.

## Disclaimers

Registration is an attribution device, not a certification of truth, competence or expertise (the manuscript's own
words). An experience-based expert's statement is a readout of practice, not a warrant by position.

## NC pairs

experience-based ≠ interactional ≠ AI · registered ≠ certified · None ≠ zero.

## Not-do

- Do not merge the three lines into one "authors and tools" sentence.
- Do not write "AI was used"; name each model and its role.
- Do not invent an interactional expert.
- Do not treat the AI line as a co-author line.

## Tier

Dr — specified from the founder ruling and the manuscript's own registration section; independently unreviewed.
