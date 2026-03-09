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
3. `references/codex/deliver-mode.md` only when the request is about `deliver`, `execute`, `roadmap`, `review`, `mutation-test`, `refactor`, or `finalize`

## Required operating rules

- Preserve nWave artifact paths unless the user asks otherwise. Default to `docs/feature/{feature-id}/...` and `.nwave/...`.
- Treat `references/upstream/commands/*.md` as the workflow spec for each command.
- Treat `references/upstream/agents/*.md` as the role and methodology spec for the active specialist.
- When an upstream agent references `~/.claude/skills/nw/...`, load the matching files from `references/upstream/skills/...`.
- When an upstream command assumes slash commands, Task subagents, or Claude DES hooks, apply the Codex substitutions from the `references/codex/` files.
- Do not claim that slash commands, plugin hooks, or Task subagents ran if Codex did not actually run them.

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
