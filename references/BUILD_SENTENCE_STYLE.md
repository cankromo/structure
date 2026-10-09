# Build a Sentence Style Reference

This file defines the content standard for future agents generating `build_sentence` items. It is based on observed/user-provided references under `references/raw_official_samples/build_sentence/`. The raw references include user-ordered responses and may contain mistakes, OCR artifacts, repeated words, or incorrect grammar. Do not treat them as answer keys.

## Task Identity

In the current repo schema, generated items belong under:

```json
{
  "build_sentence": [
    {
      "id": "bs_###",
      "parts": ["..."]
    }
  ]
}
```

The `parts` array must be stored in the correct final order. The UI may display the blocks in a shuffled order and check whether the user reconstructs the correct sequence.

## Core Task Pattern

The task usually presents a context sentence, then asks the learner to arrange phrase blocks into a natural follow-up sentence or question.

Common output patterns include:

- indirect questions:
  - `Can you tell me whether ...?`
  - `Do you know if ...?`
- direct wh-questions:
  - `Who was the main performer?`
  - `Which city are you moving to?`
  - `Where do you plan to shop for it?`
- practical clarification questions after a short context sentence.

## Content Standard

Good Build a Sentence items should:

- Produce exactly one clear, grammatical final sentence.
- Use natural everyday or campus/workplace contexts.
- Test word order, auxiliary placement, embedded questions, prepositions, and clause structure.
- Be solvable without specialized background knowledge.
- Avoid ambiguity in the correct order.
- Keep phrase blocks meaningful, not single-letter or overly tiny fragments.
- Usually use 3-6 blocks.

## Common Grammar Targets

Useful targets include:

- indirect question word order:
  - correct: `Do you know if the schedule is available online?`
  - incorrect: `Do you know if is the schedule available online?`
- whether/if clauses:
  - `Can you tell me whether families are invited?`
- wh-question formation:
  - `Which beach are you visiting?`
- auxiliary placement:
  - `Do you know when the offer ends?`
- object/preposition placement:
  - `Where do you plan to shop for it?`
- tense and agreement:
  - `Do you know if they announced the dates?`

## Block Design Rules

When creating `parts`:

- Store the correct order in `parts`.
- Each block should be a natural phrase or word group.
- Do not include duplicate blocks unless duplication is required by the sentence.
- Do not include typo blocks in generated questions.
- Do not create multiple possible correct orders.
- Keep punctuation attached to the final block when practical.

Good example:

```json
{
  "id": "bs_###",
  "parts": [
    "do you know",
    "if the new schedule",
    "includes",
    "Sunday afternoons?"
  ]
}
```

Bad example:

```json
{
  "id": "bs_###",
  "parts": [
    "do you know if",
    "the sale",
    "the sale includes",
    "online purchases?"
  ]
}
```

The bad example repeats `the sale` and creates confusion about the intended answer.

## Source Reference Warning

The raw references in `references/raw_official_samples/build_sentence/samples.json` include user-provided answer attempts. Some are visibly incorrect:

- repeated words
- typos
- malformed phrases
- missing spaces
- OCR artifacts
- incorrect embedded question order

Use them only to infer task style and common grammar targets. Do not copy them directly into `data/questions.json`.

## Quality Checks

Before adding a generated `build_sentence` item:

- Read the final sentence aloud.
- Confirm it is grammatical.
- Confirm no block contains a typo.
- Confirm the order is unique.
- Confirm the sentence is natural in context.
- Confirm the `parts` array is already in the correct order.
- Confirm the sentence is not copied from the raw references.

## Suitable Contexts

Suitable context sentences include:

- campus events
- local services
- community activities
- travel plans
- school assignments
- technology updates
- museums, libraries, lectures, workshops
- restaurants and public events

Avoid contexts requiring specialized knowledge or obscure facts.
