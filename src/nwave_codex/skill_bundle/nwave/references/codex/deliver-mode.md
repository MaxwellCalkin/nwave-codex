# Codex Deliver Mode

`deliver` is the place where upstream nWave depends most heavily on Claude-specific machinery. In Codex, keep the workflow and artifacts, but run it as an explicit single-session discipline.

## Required inputs

Before implementation, read:

1. `references/upstream/commands/deliver.md`
2. `references/upstream/commands/roadmap.md`
3. `references/upstream/commands/execute.md`
4. `references/upstream/commands/review.md`
5. `references/upstream/commands/refactor.md`
6. `references/upstream/commands/mutation-test.md`
7. `references/upstream/commands/finalize.md`

Also load the selected crafter agent file and skill bundle.

## What changes in Codex

- No orchestrator subagents: the current session switches roles explicitly.
- No DES hooks: maintain the delivery ledger manually.
- No automatic agent boundary enforcement: keep the roadmap step, current phase, and evidence visible in files.

## Manual delivery ledger

Use the same upstream artifact names:

- `docs/feature/{feature-id}/deliver/roadmap.json`
- `docs/feature/{feature-id}/deliver/execution-log.json`
- `docs/feature/{feature-id}/deliver/.develop-progress.json`

Use the upstream templates in `references/upstream/templates/` as shape references.

## Single-session execution protocol

1. Create or validate `roadmap.json` before coding.
2. Choose the crafter persona from project conventions.
3. Work one roadmap step at a time.
4. For each step, record the active phase in `execution-log.json`.
5. Do not silently skip failing tests or missing review passes.
6. Run an explicit review pass against the modified files before finalizing.
7. Only finalize after tests and any required quality checks pass.

## Deliver closeout rules

During `deliver`, every meaningful checkpoint should tell the user exactly where execution stands.

At minimum, report:

- whether you are in roadmap creation, step execution, review, mutation testing, or finalize
- whether you are waiting on human review or continuing automatically
- the concrete artifact to inspect next
- the next prompt if another explicit user message is needed

Examples:

- `Current phase: DELIVER - roadmap ready for review`
- `Current phase: DELIVER - step execution in progress`
- `Current phase: DELIVER - implementation complete, ready for review`
- `Current phase: DELIVER - verified and ready to finalize`

## Crafter persona selection

- Prefer functional crafter when project conventions explicitly call for functional programming.
- Otherwise use the software crafter references.
- If the upstream workflow says to read project `CLAUDE.md`, check `CLAUDE.md` first and fall back to `AGENTS.md`.

## Rigor profile

If `.nwave/des-config.json` exists, honor the upstream `rigor.md` settings as policy guidance:

- `review_enabled`
- `reviewer_model`
- `tdd_phases`
- `refactor_pass`
- `mutation_enabled`

These are advisory in Codex, but you should still follow them unless the user overrides them.
