# Academic Passage Style Reference

This file defines the content standard for future agents generating `academic_passage` items. It is based on user-provided TOEFL-style academic passage samples kept under `references/raw_official_samples/academic_passage/`. Do not copy official prompts or passages into new public practice content. Use these samples only to understand format, length, difficulty, and question logic.

## Task Identity

In the current repo schema, generated items belong under:

```json
{
  "academic_passage": [
    {
      "id": "rap_###",
      "title": "...",
      "topic": "...",
      "difficulty": "B2-C1",
      "text": "...",
      "questions": [
        {
          "q": "...",
          "options": ["...", "...", "...", "..."],
          "answer": 0
        }
      ]
    }
  ]
}
```

## Passage Structure

A strong academic passage should:

- Be short enough for practice but substantial enough for several questions.
- Usually contain 3-4 paragraphs.
- Introduce a topic, explain key concepts, then discuss applications, effects, challenges, or examples.
- Use university-level but accessible language.
- Target roughly B2-C1 difficulty.
- Avoid requiring specialist knowledge outside the passage.

Typical topics include:

- science and technology
- medicine
- ecology and environment
- psychology
- history
- literature
- social sciences
- communication and media

## Question Mix

Each passage should support multiple question types, such as:

- main idea
- detail
- inference
- vocabulary in context
- rhetorical purpose
- EXCEPT / NOT mentioned
- sentence insertion, if the UI/schema supports it

For this repo's current schema, use standard multiple-choice questions with four options unless the UI is explicitly extended.

## Vocabulary Questions

Vocabulary-in-context questions should:

- Ask for a word from the passage.
- Use answer choices from the same part of speech when possible.
- Depend on context, not only dictionary knowledge.
- Avoid obscure words that are too specialized.

Example wording:

```text
The word "advocate" in the passage is closest in meaning to
```

## Detail and Inference Questions

Detail questions should:

- Be directly supported by a specific part of the passage.
- Avoid simply copying a full sentence as the answer.
- Have distractors that are plausible but contradicted, unsupported, or too broad.

Inference questions should:

- Be safely implied by the passage.
- Not require outside factual knowledge.
- Avoid speculative answers.

## Rhetorical Purpose Questions

Rhetorical-purpose questions often ask why the author mentions a phrase, example, process, or group.

Good examples ask about:

- supporting a claim
- illustrating an application
- explaining a challenge
- clarifying a concept
- showing a consequence

Distractors should not be silly; they should represent plausible but incorrect reading purposes.

## EXCEPT / NOT Mentioned Questions

EXCEPT/NOT questions should:

- Include three options that are genuinely mentioned or supported.
- Include one option that is clearly not mentioned or contradicted.
- Avoid making the correct answer depend on tiny wording tricks.

## Passage Quality Rules

When generating new passages:

- Write fully original content.
- Do not copy official samples.
- Use clear paragraph progression.
- Keep terminology manageable.
- Define technical terms briefly when needed.
- Include enough detail to support 4-6 questions.
- Do not overload the passage with lists of unrelated facts.
- Avoid unstable current-event claims.

## Distractor Quality

Good distractors:

- Are grammatically parallel.
- Use concepts from the passage.
- Are plausible to a careless reader.
- Differ clearly from the correct answer.

Bad distractors:

- Are obviously absurd.
- Are unrelated to the passage.
- Depend on outside knowledge.
- Are almost equally correct.
- Use wording that gives away the answer.

## Storage Policy

Official/user-provided samples should stay in:

```text
references/raw_official_samples/academic_passage/
```

Generated practice questions should go in `data/questions.json` only when explicitly requested, and must be original.
