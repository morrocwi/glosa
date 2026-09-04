> tier: Dr (specified; independently unreviewed)

# P1 — Standpoint

## One-line rule

Every claim declares who speaks, from what base, and what disciplines are explicitly *not*
claimed — standpoint disclosure is never a substitute for domain-credentialed authority, and it is
never optional.

## Why

Founder ruling, request 31, 2026-09-04 (`design/FOUNDATION_v0.5.md` §1.1, chair ruling A2 —
*"เราไม่สนเรื่องใหม่ ... เน้นไปที่เราเสนออะไรก็พอ เพราะเราไม่ได้แข่งขันใคร โลกผ่านจุดนั้นไปแล้ว"*): glosa states
what it proposes, what it builds on, and what would make it wrong — from a declared position, not
from an unstated claim of authority. Request 24 (`HANDOFF_2026-09-04_founding-meeting.md` §6 —
"อย่าลืมนะ เป้าหมายคือ human–AI co-production") requires the division of labour visible per claim;
standpoint is the first place that visibility must show up, before any evidence is read.

## Inputs → outputs

- Input: the human's own account of their position relative to the claim (practitioner, founder,
  community member — role, not name).
- Output: `claim_card.standpoint` (`schema/claim_card.schema.json`): `declared_basis`,
  `disciplines_not_claimed[]`, `method_basis`. Also feeds `claim_card.produced_by` and the
  const `responsible: human`.

## Gate

A stub card (`shape: stub`, §3.2a) still requires `standpoint` populated — it is one of the few
fields a stub cannot leave null. No card, stub or full, may skip this field.

## Human / AI division of labour

Human: states `declared_basis` and `disciplines_not_claimed[]` in their own words — this is
non-delegable, since only the human can attest to their own position. AI: may prompt for
completeness (e.g. "does this also claim expertise in X you have not named?") but never fills
`declared_basis` on the human's behalf.

## Disclaimers emitted

`D-STANDPOINT` (always on, every claim card, paper front matter, README) · `D-NONEXPERT` (always
on — restores the "disciplines explicitly not claimed" disclosure, FOUNDATION §5).

## Non-collapse pairs enforced

`NC-54` Standpoint disclosure≠Domain-credentialed authority · `NC-45` PositionalAccess≠
PopulationAuthority; CommunityTrust≠Representativeness · `NC-60` Founder=ideas/direction≠
AI=assistant.

## What this card does NOT do

It does not grant legitimacy — declaring a standpoint is not itself evidence and never raises tier
or independence class. It does not substitute for `five_questions` (P3) — a fully honest
standpoint attached to an empty claim card is still an incomplete card. It never proposes an
outside credential as what would make the standpoint legitimate (`EPIS-KNOWLEDGE-VALIDATION` /
AGENTS.md rule 6).
