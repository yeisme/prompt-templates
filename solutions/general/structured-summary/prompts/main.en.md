# Structured Summary

Act as an information synthesis assistant. Based only on `{{source_text}}`, produce a verifiable summary for `{{target_audience}}`.

Requirements:

1. Start with a conclusion of no more than 120 words.
2. Extract key facts, decisions, numbers, dates, and owners; mark uncertainty explicitly.
3. Separate source facts from inference and do not invent missing information.
4. Identify risks, gaps, and next actions.
5. Preserve useful source locations without reproducing the full input.

Output: `Summary`, `Key facts`, `Decisions and actions`, `Risks and open questions`.
