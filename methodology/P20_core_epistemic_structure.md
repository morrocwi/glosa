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

Non-collapse rule of the system (registered in Toledo before use, per `P19`):

    Experience-Based Expertise ≠ Interactional Expertise ≠ AI Model

A model that connects and widens the candidate space does not thereby become an experience-based expert: it was not
at the site of the problem. A person with real experience does not thereby hold interactional expertise across fields.

Formal object (founder's [New Definition / Proposal], registered in Toledo as a coded reading; cite its code once
assigned):

    E_p = ⟨ X_p^exp , X_p^int , M_p^AI ⟩ ,   M_p^AI = { M_1, …, M_k } ,   X_p^int = ∅ when no interactional expert holds the role.

`M_p^AI` is a set, since one project may use several models; `X_p^int = ∅` means the role is unheld, not a zero score.

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
