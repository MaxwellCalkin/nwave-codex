# Codex Interaction Mode

Use this file to preserve the part of nWave that feels collaborative, not just procedural.

## Principle

The planning and specification phases should involve the user in real time. Codex should not jump straight from a broad request to finished design or acceptance-test documents when important decisions are still open.

## Phases that should ask questions

These phases should normally include a clarification round before final artifacts are produced:

- `discuss`
- `design`
- `devops`
- `distill`

## When to ask

Ask when:

- the upstream command includes `Interactive Decision Points`
- multiple valid options exist and the choice affects the spec
- acceptance-test scope is unclear
- an integration, deployment, or architecture decision depends on business context
- the user asked for planning rather than direct implementation

Do not ask when:

- the answer is already explicit in prior wave artifacts
- the user explicitly said to make reasonable assumptions
- the question would not materially change the produced artifacts

## How to ask

Prefer one compact question round with the smallest set of high-value questions.

Good:

- `Before I lock the design, which matters more here: fastest implementation, easiest future extension, or lowest operational risk?`
- `For distill, what absolutely has to be proven before you would trust this integration in production?`
- `For devops, are we targeting an existing deployment platform or designing this from scratch?`

Avoid:

- long questionnaires
- generic questions that do not change the output
- repeating answers that already exist in the docs

## Phase-specific prompts

### discuss

Ask about:

- who the user is
- what success looks like
- unhappy paths and constraints
- what acceptance would mean in business terms

### design

Ask about:

- hard constraints
- important tradeoffs
- integration boundaries
- performance, reliability, or security priorities

### devops

Ask about:

- deployment target
- existing CI/CD or infrastructure
- observability expectations
- branching and release expectations

### distill

Ask about:

- must-pass acceptance scenarios
- important edge cases
- external dependencies that should be real vs mocked
- what would make the user trust the feature as done

## Required summary

After the question round, briefly summarize the answers you are using before generating the final artifacts.
