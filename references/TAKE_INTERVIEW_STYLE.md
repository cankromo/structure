# Take an Interview Style Reference

This file defines the content standard for future agents generating `interview` items for the post-January 21, 2026 TOEFL iBT Speaking section.

## Task Identity

Generated items belong under:

```json
{
  "interview": [
    {
      "id": "int_###",
      "prompt": "..."
    }
  ]
}
```

## Core Pattern

Take an Interview is a spoken-response task. The user hears an interviewer question and gives a short, meaningful response based on personal experience, opinions, preferences, or familiar academic/campus situations.

For full mocks, Speaking should use:

- 7 Listen and Repeat items
- 4 Take an Interview items

## Prompt Style

Good interview prompts should:

- be phrased as natural interviewer questions
- ask for a personal example, preference, opinion, explanation, or comparison
- be answerable without specialized outside knowledge
- support a response with reasons and details
- sound conversational but still appropriate for academic or campus contexts
- avoid asking multiple unrelated questions in one item

Common prompt frames:

- "Describe a time when..."
- "Do you agree or disagree that..."
- "Some students prefer X, while others prefer Y. Which do you prefer, and why?"
- "What is an important quality of..."
- "Talk about a place, activity, person, or experience that..."

## Quality Rules

When generating new `interview` items:

- Do not copy official TOEFL prompts.
- Keep the wording clear after one listen.
- Make the question broad enough for most test takers to answer.
- Avoid controversial, traumatic, medical, legal, or highly personal topics.
- Avoid prompts that can be answered fully with only "yes" or "no."
- Prefer topics tied to study, campus life, work habits, technology, communication, community, learning, and everyday decisions.
- Ensure each prompt naturally invites elaboration.

## Full Mock Use

In a full mock:

- Use exactly 4 interview items.
- Keep all interview prompts independent.
- Do not require the user to see text on screen to understand the question.
- Preserve the MediaRecorder recording flow.
- Export all interview recordings with the speaking files.

## Scoring Note

Official scoring may consider intelligibility, fluency, grammar, vocabulary, coherence, and task fulfillment. The repo's local export workflow should preserve recordings and prompts for later human or ChatGPT-assisted review; it should not claim to reproduce official ETS scoring.

