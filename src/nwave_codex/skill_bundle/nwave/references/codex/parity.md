# Codex Parity Rules

This skill vendors the upstream Claude Code nWave prompt assets, but Codex does not expose the same runtime primitives. Apply these substitutions every time you use an upstream nWave reference.

## Environment mapping

| Upstream nWave assumption | Codex substitution |
| --- | --- |
| `/nw:command` slash command | Natural-language request or explicit `$nwave` invocation |
| `Task` subagent dispatch | Emulate the requested agent role directly in the current Codex session |
| `~/.claude/commands/nw/*.md` | `references/upstream/commands/*.md` |
| `~/.claude/agents/nw/*.md` | `references/upstream/agents/*.md` |
| `~/.claude/skills/nw/{agent}/...` | `references/upstream/skills/{agent}/...` |
| Project `CLAUDE.md` | Project `CLAUDE.md` if present, otherwise `AGENTS.md` or current repo instructions |
| Claude DES hooks | Manual delivery discipline documented in `deliver-mode.md` |

## Honesty rules

- Never pretend a slash command ran.
- Never pretend a separate reviewer or crafter subagent ran.
- Never claim DES enforced anything at runtime unless a real tool did so.
- Say "I am emulating the {agent-name} role in this Codex session" when the upstream workflow would have dispatched another agent.

## File-system rules

- Keep the upstream nWave directory structure for artifacts.
- Prefer `docs/feature/{feature-id}/{wave}/...` for wave outputs.
- Prefer `.nwave/des-config.json` for rigor settings to preserve compatibility with upstream docs.

## Workflow rules

- Use the upstream command file as the semantic contract for outputs, success criteria, and handoffs.
- Use the upstream agent file plus its skill bundle as the methodology contract.
- When upstream instructions require an unavailable mechanism, keep the intent and replace only the mechanism.

## User guidance rules

Codex must make the workflow state explicit after every nWave response.

Always tell the user:

- which wave or command just ran
- whether that phase is awaiting user review or is ready to continue
- which artifacts to review, if any
- the exact next wave or action
- a copy-pasteable next prompt

Do not assume the user knows nWave's state machine. State it directly.

If a phase produced design, requirements, roadmap, or acceptance-test artifacts, default to `ready for review` unless the user explicitly said to continue without pausing.

## Interactive question rules

Codex must preserve nWave's collaborative feel for the planning and specification phases.

For `discuss`, `design`, `devops`, and `distill`:

- ask focused clarification questions before writing final artifacts when key decisions remain open
- prefer a small, high-value question set rather than a giant survey
- use the literal templates in `references/codex/interaction-mode.md` as the default question shape
- treat upstream `Interactive Decision Points` sections as required user checkpoints unless prior artifacts already answer them
- if you proceed on assumptions, state those assumptions explicitly

Do not silently replace user involvement with guessed defaults when the phase is supposed to shape the spec with the user.

## Git commit rules

Codex must treat each completed nWave phase as a commit boundary when that phase changed files.

Always:

- inspect git status before closing the phase
- create a dedicated commit for the phase if the phase produced changes
- report the resulting commit in the user-facing closeout

Do not:

- silently leave completed phase changes uncommitted
- mix unrelated pre-existing changes into the phase commit
- claim a phase is complete if the user asked for commit-backed checkpoints and no commit was created

If pre-existing unrelated changes make a clean phase commit unsafe, stop and tell the user exactly why.

## Deliver-specific rules

For `deliver` and related commands, also read `deliver-mode.md` before making edits.
