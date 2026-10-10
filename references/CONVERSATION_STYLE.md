# Listen to a Conversation Style Reference

This file defines the content standard for future agents generating `conversations` items for TOEFL-style Listening practice and full mock tests.

## Sources Used For Pattern

This reference is based on:

- Official ETS TOEFL iBT 2026 Listening materials and overview descriptions.
- User-provided TOEFL Flex Practice-style short conversation transcripts and questions.

Do not copy official or user-provided conversations into public practice content. Use them only to understand format, length, difficulty, and question logic.

## Task Identity

Generated items belong under:

```json
{
  "conversations": [
    {
      "id": "conv_###",
      "title": "...",
      "turns": [
        ["Student", "..."],
        ["Staff Member", "..."]
      ],
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

Official ETS materials describe Listen to a Conversation as measuring comprehension of conversations in modern academic situations. The observed TOEFL Flex Practice-style samples are short two-speaker exchanges followed by 2 questions.

For new practice content, use:

- one short conversation between two speakers
- about 50-120 spoken words for short practice sets
- exactly 2 questions when modeling the observed short Flex Practice pattern
- 4 answer options per question
- no transcript shown to the user during normal listening flow

Longer campus conversations may use more questions only when a full mock distribution requires it, but new practice-first items should default to 2 questions.

## Conversation Structure

A strong short conversation usually includes:

1. A problem, plan, or misunderstanding introduced by one speaker.
2. Clarification, advice, correction, or follow-up from the second speaker.
3. A practical reason, upcoming action, or consequence.

Common situations include:

- phone, computer, printer, or app problems
- home, housing, or campus service issues
- class schedule, advising, library, or campus office conversations
- planning a visit, event, trip, meeting, or repair
- misunderstanding about what happened, when it happened, or what someone plans to do

## Question Pattern

Each short conversation should normally include 2 questions:

1. Problem / main situation / misunderstanding.
2. Detail / future action / reason / speaker plan.

Common question stems:

- "What problem does the woman/man have?"
- "What aspect of ... is the man/woman mistaken about?"
- "What does the woman/man say she/he will do?"
- "What does the man/woman suggest?"
- "Why is the woman/man concerned?"
- "What will the woman/man probably do next?"

## Speaker And Audio Rules

- Store speaker names in `turns`, but do not read speaker labels aloud.
- Use different voices or tones for the two speakers when possible.
- Preserve the current UI behavior where each question can replay the same conversation once.
- Preserve the one-audio-at-a-time rule.

## Distractor Rules

Good distractors should:

- be plausible and connected to words or ideas in the conversation
- reflect common misunderstandings
- avoid being obviously silly
- be parallel in grammar and length when possible

Do not make the correct answer position predictable. Across a large set, distribute correct answers among A, B, C, and D.

## Quality Rules

When generating Conversation content:

- Keep the exchange natural and spoken.
- Avoid long monologues.
- Make the situation understandable after one listen.
- Include enough detail to support both questions.
- Avoid highly technical or specialized topics.
- Avoid unsafe, traumatic, or overly personal content.
- Do not copy official or user-provided examples.

