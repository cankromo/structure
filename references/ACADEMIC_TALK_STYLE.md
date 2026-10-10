# Listen to an Academic Talk Style Reference

This file defines the content standard for future agents generating `academic_talks` items for TOEFL-style Listening practice and full mock tests.

## Sources Used For Pattern

This reference is based on:

- Official ETS TOEFL iBT 2026 specifications and overview materials.
- User-provided TOEFL Flex Practice-style Academic Talk transcripts and questions.

Do not copy official or user-provided scripts into public practice content. Use them only to understand format, length, difficulty, and question logic.

## Task Identity

Generated items belong under:

```json
{
  "academic_talks": [
    {
      "id": "talk_###",
      "title": "...",
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

## Core Format

Official ETS overview materials describe Listen to an Academic Talk as a short academic-related talk of about 100-250 words followed by four questions. New generated content should use:

- one short lecture, podcast-style explanation, or expert talk
- about 150-230 words as the normal target range
- exactly 4 multiple-choice questions
- 4 options per question
- no transcript shown to the user during normal listening flow

## Talk Structure

A strong talk usually includes:

1. A clear topic introduction or hook.
2. A definition, concept, or problem.
3. One concrete example, case, historical reference, or process.
4. A consequence, challenge, limitation, or benefit.
5. Sometimes a final sentence previewing what the speaker will discuss next.

Good topic areas include:

- literature and rhetoric
- physics, astronomy, biology, ecology, medicine, or psychology
- business, economics, sociology, urban planning, or history
- art, music, archaeology, communication, or technology

No outside specialist knowledge should be required.

## Question Pattern

Each talk should normally include 4 questions. A balanced set often uses:

1. Main topic / main purpose.
2. Detail, definition, or process.
3. Rhetorical purpose / why the speaker mentions an example or phrase.
4. Inference, problem/challenge, recommendation, likely next topic, or speaker attitude.

Common question stems:

- "What is the main topic of the talk?"
- "What does the speaker say about ...?"
- "Why does the speaker mention ...?"
- "What problem/challenge does the speaker mention?"
- "What will the speaker probably discuss next?"
- "What does the speaker imply about ...?"
- "Why does the speaker say, '...'?"

## Distractor Rules

Good distractors should:

- use vocabulary or ideas from the talk without being correct
- be plausible for a listener who missed a key detail
- be parallel in grammar and length when possible
- avoid being obviously silly or unrelated

Do not make the correct answer position predictable. Across a large set, distribute correct answers among A, B, C, and D.

## Audio And UI Rules

- The script should be played with the existing listening audio system.
- The transcript should not be displayed during the question flow.
- For this repo, each question may have its own one-time play button for the same talk audio.
- Preserve the one-audio-at-a-time rule.
- Academic Talk should generally use a clear lecturer voice at a slightly slower natural rate.

## Quality Rules

When generating Academic Talk content:

- Keep scripts coherent and spoken, not written like dense textbook prose.
- Use natural lecture transitions: "for example," "however," "now," "this matters because."
- Include enough information to support all four questions.
- Avoid too many numbers, names, or technical terms.
- Define technical vocabulary briefly.
- Avoid unstable current-event claims.
- Do not copy official or user-provided samples.

