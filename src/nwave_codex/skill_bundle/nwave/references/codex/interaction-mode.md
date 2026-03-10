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

## Required interaction shape

For these phases, use a visible two-step structure:

1. `Questions for you`
2. `What I heard` or `Assumptions I'm using`

Do not skip step 1 when important decisions are still open.

## How to ask

Prefer one compact question round with the smallest set of high-value questions.

Rules:

- ask 1-3 questions
- keep each question short and decision-oriented
- avoid vague prompts like `Anything else?`
- make each question materially affect the phase output

Good:

- `Before I lock the design, which matters more here: fastest implementation, easiest future extension, or lowest operational risk?`
- `For distill, what absolutely has to be proven before you would trust this integration in production?`
- `For devops, are we targeting an existing deployment platform or designing this from scratch?`

Avoid:

- long questionnaires
- generic questions that do not change the output
- repeating answers that already exist in the docs

## Literal templates

Use these templates verbatim or with only small wording changes.

### discuss template

```text
Questions for you
1. Who is the primary user or operator for this feature?
2. What outcome would make you say this feature is successful?
3. What edge case, failure mode, or constraint must be handled from day one?
```

Then follow with:

```text
What I heard
- Primary user: ...
- Success signal: ...
- Must-handle constraint: ...
```

### design template

```text
Questions for you
1. Which matters most here: fastest delivery, easiest future extension, lowest operational risk, or strongest correctness guarantees?
2. Are there any hard constraints on libraries, deployment environment, protocols, or integration boundaries?
3. Is there one architecture or packaging choice you especially want to avoid?
```

Then follow with:

```text
What I heard
- Priority: ...
- Hard constraints: ...
- Avoid: ...
```

### devops template

```text
Questions for you
1. Are we deploying into existing infrastructure/CI, or should I design this as greenfield?
2. What deployment target should I optimize for first?
3. What do you need to observe or alert on before you would trust this in production?
```

Then follow with:

```text
What I heard
- Existing platform context: ...
- Primary deployment target: ...
- Observability bar: ...
```

### distill template

```text
Questions for you
1. What absolutely must be proven before you would trust this feature as done?
2. Which unhappy path or edge case is most important to capture in acceptance tests?
3. For external dependencies, what should be real versus mocked in acceptance testing?
```

Then follow with:

```text
What I heard
- Must-prove behavior: ...
- Key edge case: ...
- Real vs mocked boundary: ...
```

## Fallback if the user does not answer

If the user does not answer and the phase still needs to proceed:

- say `Assumptions I'm using`
- list the specific assumptions
- note that the artifacts should be reviewed against those assumptions

## Required summary

After the question round, briefly summarize the answers you are using before generating the final artifacts.
