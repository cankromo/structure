# Complete the Words Style Reference

This file defines the content standard for future agents generating `complete_words` items. It is a style reference only. Do not copy real ETS content; write fully original questions.

## Core Structure

Complete the Words should follow a structure inferred from ETS/Flex Practice-style examples:

- Text should be roughly 80-120 words.
- The first sentence should remain fully intact.
- After the first sentence, approximately 10 words should be partially hidden.
- For each hidden word:
  - The beginning of the word must remain visible.
  - The missing letters must be represented by the same number of underscores.
  - The `answers` entry must contain only the missing letters.
- Example:
  - `enviro______`
  - answer: `nmental`
- The full word must not be hidden.
- Do not only test difficult academic vocabulary; include function words and grammar-sensitive words when useful.
- The item should test grammar, spelling, morphology, vocabulary, and context together.
- The paragraph must feel natural and coherent; do not write artificial sentences just to create blanks.
- Target difficulty should be around B2-C1.

## Suitable Topics

Academic or general-knowledge topics work well, including:

- archaeology
- climate
- oceanography
- sleep
- animal behavior
- ecology
- biology
- geology
- history
- social sciences

## Blank Placement

- Blanks may be concentrated mostly in the middle of the paragraph.
- The last one or several sentences may remain fully visible when that improves natural flow.
- Prefix length should not be produced by the same mechanical algorithm for every word.
- Prefixes should look natural and close to ETS-style partial-word cues.

## Validation Requirements

For every set:

- visible prefix + answer = original word
- underscore count = answer character count
- `answers` contains only the missing letters

The selected blank words in one paragraph should measure different skills. Do not choose 10 nouns only, 10 vocabulary-only targets, or the same suffix repeatedly.

## Good Examples

GOOD content has:

- A natural academic paragraph with clear context.
- Approximately 10 blanks that test different skills.
- Answers that are solvable from context but not completely obvious.
- A mix of morphology, grammar, spelling, vocabulary, and discourse context.
- Original wording, not copied ETS text.

Example pattern:

```json
{
  "text": "Coastal wetlands influence nearby communities in ways that extend beyond wildlife protection. In many reg____, these habitats abs___ storm water, red____ erosion, and supp___ fish populations that local economies depend on.",
  "answers": ["ions", "orb", "uce", "ort"]
}
```

## Bad Examples

BAD content includes:

- Mechanically deleting half of every selected word.
- Meaningless or artificial sentences.
- Repeating the same suffix or morphology target over and over.
- Using underscore counts that do not match answer lengths.
- Using overly specialized C2 vocabulary that is not appropriate for broad TOEFL-style testing.
- Copying ETS passages or prompts.

Do not treat this file as permission to reproduce ETS wording. It is only a guide to style, length, and task logic.
