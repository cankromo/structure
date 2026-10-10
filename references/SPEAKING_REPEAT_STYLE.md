# Listen and Repeat Style Reference

This file defines the content standard for future agents generating `repeat` items. It is based on user-provided TOEFL Flex Practice-style Listen and Repeat samples stored under `references/raw_official_samples/listen_repeat/`. Do not copy official sample sentences into public practice content. Use them only to understand format, difficulty, and task logic.

## Task Identity

Generated items belong under:

```json
{
  "repeat": [
    {
      "id": "rep_###",
      "text": "..."
    }
  ]
}
```

## Core Pattern

Listen and Repeat prompts are short spoken instructions or practical statements. The user hears one sentence and repeats it aloud.

## Seven-Sentence Scenario Sets

The TOEFL-style pattern for this repo should use scenario-based sets:

- One scenario introduction appears before a group of 7 repeat sentences.
- The introduction explains the role and context, for example:
  - the learner works in a store, café, library, office, or campus service area
  - a manager, staff member, librarian, or trainer is explaining procedures
  - the learner should listen and repeat only once
- Each set contains exactly 7 `repeat` items sharing the same `scenario_id`.
- Each item should include:
  - `scenario_id`
  - `scenario_intro`
  - `sequence` from 1 to 7
  - `level` such as `Easy`, `Medium`, or `Hard`
  - `text`
- Keep existing `id` and `text` fields because the UI and validator depend on them.

Recommended progression inside each 7-sentence set:

- Sentences 1-2: Easy, about 9-11 syllables or short spoken instructions.
- Sentences 3-5: Medium, about 14-16 syllables or moderately longer instructions.
- Sentences 6-7: Hard / memory-wall items, about 19-23 syllables or longer procedural instructions.

All seven sentences should stay within one realistic scenario or topic. Do not mix unrelated contexts inside one set.

Common contexts in the observed samples include:

- printer, scanner, or kiosk instructions
- checkout and payment steps
- app or account actions
- customer support directions
- food ordering or pickup instructions
- short workplace/service procedures

## Sentence Length and Difficulty

Good prompts should:

- usually be one sentence
- be natural spoken American English
- be short to medium length, roughly 5-18 words
- occasionally include a longer procedural sentence, roughly 18-25 words
- target clear B1-B2+ pronunciation practice while still sounding TOEFL-like
- avoid obscure technical vocabulary
- avoid complex academic content

## Language Features to Mix

A strong set should include variation in:

- imperatives: "Select...", "Place...", "Review..."
- polite instructions: "Please ask...", "Be sure to..."
- modal statements: "You can...", "You may...", "You should..."
- time/order phrases: "before printing", "after payment", "when you are done"
- common service nouns: receipt, transaction, account, settings, support
- pronunciation targets: consonant clusters, unstressed function words, connected speech

## Quality Rules

When generating new `repeat` items:

- Do not copy official sample sentences.
- Keep each item self-contained.
- Make the sentence easy to understand after one listen.
- Avoid tongue-twister artificiality.
- Avoid very long multi-clause sentences unless intentionally used sparingly.
- Avoid unsafe, sensitive, or emergency content.
- Ensure the sentence is grammatically correct and naturally speakable.
- Prefer everyday procedural contexts over academic lectures.

## Good Examples

Good generated prompts have:

- clear action or information
- natural rhythm for speech synthesis
- familiar vocabulary
- realistic kiosk, service, campus, or app context

Example pattern, not to copy:

```text
Select your receipt option before leaving the checkout screen.
```

## Bad Examples

Avoid prompts that:

- copy official TOEFL wording
- are too short to assess repetition meaningfully
- are packed with rare technical terms
- require external context to understand
- include awkward phrasing that a native speaker would not say
- contain multiple unrelated instructions in one sentence

## Storage Policy

Official/user-provided samples should stay in:

```text
references/raw_official_samples/listen_repeat/
```

Generated practice items should go in `data/questions.json` only when explicitly requested, and must be original.
