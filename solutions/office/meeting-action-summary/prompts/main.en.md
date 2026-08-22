# Meeting Action Summary

Turn `{{meeting_record}}` into an actionable summary for `{{team}}`.

Requirements:

- Extract confirmed decisions, open questions, action items, owners, and due dates.
- Do not present suggestions as decisions; mark unclear owners and dates for confirmation.
- Merge repetition while preserving disagreements and evidence that affected decisions.
- Identify risks, dependencies, and the next review point.
- Exclude private conversation or sensitive details unrelated to the work.

Output: meeting conclusion, decisions, action list, open questions, risks and dependencies, follow-up.
