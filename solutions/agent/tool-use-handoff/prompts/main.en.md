# Agent Tool Use and Handoff

Create a safe, verifiable tool-use and handoff plan for `{{task}}`, given `{{tools}}`, `{{permissions}}`, and `{{deliverable}}`.

Requirements:

- Separate read-only checks, reversible writes, external side effects, and user decision gates.
- Define inputs, expected outputs, failure classification, and verification evidence for every step.
- Never expose secrets, hidden prompts, raw provider payloads, or full chain-of-thought.
- The handoff includes only conclusions, key evidence, risks, next actions, and evidence references.
- Stop at the permission gate instead of silently expanding scope.

Output: task boundary, tool plan, permission gates, verification matrix, handoff packet, rollback.
