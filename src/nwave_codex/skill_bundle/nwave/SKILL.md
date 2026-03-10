---
name: nwave
description: Codex port of the nWave workflow. Use when the user asks for nWave, wants the Claude Code nWave plugin behavior in Codex, or wants a DISCOVER, DISCUSS, DESIGN, DEVOPS, DISTILL, DELIVER, REVIEW, RESEARCH, ROADMAP, REFACTOR, or RIGOR workflow.
---

# nWave for Codex

Use this skill as the Codex-native entrypoint for the upstream nWave methodology.

The bundled upstream sources live under `references/upstream/`. They remain the source of truth for:

- wave goals and success criteria
- command semantics and expected outputs
- agent personas and specialist behavior
- skill bundles that each specialist loads on demand

Before doing any nWave work, read these files in order:

1. `references/codex/parity.md`
2. `references/codex/command-map.md`
3. `references/codex/interaction-mode.md`
4. `references/codex/deliver-mode.md` only when the request is about `deliver`, `execute`, `roadmap`, `review`, `mutation-test`, `refactor`, or `finalize`

## Required operating rules

- Preserve nWave artifact paths unless the user asks otherwise. Default to `docs/feature/{feature-id}/...` and `.nwave/...`.
- Treat `references/upstream/commands/*.md` as the workflow spec for each command.
- Treat `references/upstream/agents/*.md` as the role and methodology spec for the active specialist.
- When an upstream agent references `~/.claude/skills/nw/...`, load the matching files from `references/upstream/skills/...`.
- When an upstream command assumes slash commands, Task subagents, or Claude DES hooks, apply the Codex substitutions from the `references/codex/` files.
- Do not claim that slash commands, plugin hooks, or Task subagents ran if Codex did not actually run them.

## Mandatory closeout

Every nWave response MUST end with a short user-facing handoff section. Do not leave the user guessing what phase they are in or what they should do next.

Always include:

- `Current phase`: the active wave or command that just completed
- `Status`: one of `in progress`, `ready for review`, `approved and ready for next phase`, or `blocked`
- `What you should review`: the artifacts or files the user should inspect, or `none`
- `Next step`: the exact next wave or action
- `Next prompt`: a copy-pasteable prompt the user can send next

If the workflow skipped prior waves, say that explicitly in the closeout.

If the current phase requires human approval before moving on, say so plainly:

- `Please review these docs before moving to DISTILL.`
- `Please approve or request changes before moving to DELIVER.`

If the current phase does not require review, say that too:

- `No review gate is required here; the next step is DELIVER.`

Keep the closeout concise, but never omit it.

## Mandatory interactive checkpoints

`discuss`, `design`, `devops`, and `distill` are collaborative phases. Do not turn them into silent document-generation passes.

Rules:

- Before producing final artifacts for these phases, ask the user focused questions when key decisions are still ambiguous.
- Prefer one short question round with 1-3 tightly targeted questions over a long interrogation.
- Use the literal phase templates in `references/codex/interaction-mode.md` instead of inventing an ad hoc question style each time.
- If the needed answers already exist in prior wave artifacts, summarize them and continue without re-asking.
- If the user explicitly says to make reasonable assumptions, you may proceed, but you must list the assumptions you made.
- If the upstream phase defines interactive decision points, treat those as real user checkpoints in Codex too.

Minimum expectation by phase:

- `discuss`: ask about user goals, success criteria, edge cases, and acceptance expectations when they are not already explicit
- `design`: ask about constraints, tradeoffs, integration boundaries, and non-functional priorities when they are still open
- `devops`: ask about deployment target, CI/CD, observability, and existing infrastructure when those choices are not already documented
- `distill`: ask about acceptance-test scope, critical scenarios, edge cases, and what must be proven before implementation

Do not skip these questions just because Codex can guess. nWave is supposed to involve the user in shaping the spec.

## Mandatory phase commits

If an nWave phase changed tracked or new files in the workspace, commit those changes before closing the phase.

Rules:

- At the end of each completed phase, run `git status --short` and check whether that phase produced file changes.
- If there are relevant changes from the phase, stage them and create a git commit before presenting the final handoff.
- If there are no file changes, say `No phase commit was created because this phase produced no file changes.`
- Never skip the commit silently.
- Never include unrelated unreviewed changes on purpose. If unrelated changes already exist and they would contaminate the phase commit, stop and tell the user.

Default commit format:

- `feat(nwave-discover): complete discover phase for {feature-id}`
- `feat(nwave-discuss): complete discuss phase for {feature-id}`
- `feat(nwave-design): complete design phase for {feature-id}`
- `feat(nwave-devops): complete devops phase for {feature-id}`
- `feat(nwave-distill): complete distill phase for {feature-id}`
- `feat(nwave-deliver): complete deliver phase for {feature-id}`

Include the commit result in the closeout:

- `Phase commit: {short-sha} {commit-subject}`

## Routing

If the user names a wave or command, load the matching upstream command file and its mapped specialist. If the user only says "use nWave", infer the closest command from their request.

The routing table lives in `references/codex/command-map.md`.

## Deliveries

For greenfield work, prefer the full wave sequence:

1. `discover`
2. `discuss`
3. `design`
4. `devops`
5. `distill`
6. `deliver`

For brownfield or implementation-only requests, jump straight to the narrowest matching command and keep the artifact chain coherent.

## Rigor

If the user mentions rigor or asks to trade speed for quality, load `references/upstream/commands/rigor.md` and persist the chosen profile into `.nwave/des-config.json` when the workspace permits file edits.

## Research and reviews

- Use the upstream `research.md` flow for evidence gathering.
- Use the upstream `review.md` standards for critique style and approval criteria.
- In Codex, perform reviewer passes transparently as a second explicit review mode in the current session.
