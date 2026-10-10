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
