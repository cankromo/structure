# TOEFL Study System

Folders:
- `/practice/` objective-only practice
- `/mock/` full mock with Reading/Listening auto-score, Writing/Speaking export
- `/admin/` JSON editor/export panel
- `/data/questions.json` shared question bank
- `/data/tests.json` test definitions

## GitHub Pages
Upload the whole folder to a repository.
Enable Settings → Pages → Deploy from branch → main / root.

Then:
- Practice: `/practice/`
- Full mock: `/mock/`
- Admin: `/admin/`

## Adding questions
1. Open `/admin/`
2. Edit Questions JSON / Tests JSON
3. Export the JSON files
4. Replace `/data/questions.json` and/or `/data/tests.json` in GitHub
5. Commit changes

## Agent-maintained data
Agents should follow `/AGENT_DATA_CONTRACT.md` when adding practice questions or full mock tests.
Before handing work back, run:

```sh
python3 tools/validate_data.py
```

The published sites will use the new data automatically.

## Full mock results
At the end of a mock, press **Export for ChatGPT**.
The generated ZIP contains:
- `result.json`
- Writing text files
- Speaking `.webm` recordings

Upload that ZIP into ChatGPT for full evaluation.
