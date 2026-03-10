# nwave-codex

`nwave-codex` brings the [nWave](https://github.com/nWave-ai/nWave) workflow to Codex.

It packages nWave's wave-based planning and delivery system as an installable Codex skill, so you can use one workflow to:

- shape a feature from idea to implementation
- write acceptance criteria and Given/When/Then scenarios
- drive implementation with roadmap-first TDD
- run review and verification passes before calling work complete

## What It Does

`$nwave` gives Codex a structured version of the nWave flow:

| Wave | Purpose |
| --- | --- |
| `discover` | Validate the problem, user, and opportunity |
| `discuss` | Turn the idea into requirements, stories, and acceptance criteria |
| `design` | Define architecture, boundaries, and tradeoffs |
| `devops` | Plan delivery infrastructure and operational readiness |
| `distill` | Produce executable acceptance tests and feature specs |
| `deliver` | Implement through roadmap-driven, TDD-oriented execution |

It also carries over nWave's supporting commands such as `review`, `research`, `roadmap`, `refactor`, `mutation-test`, `root-why`, and `rigor`.

## Why This Exists

nWave is built for Claude Code. Codex has different runtime primitives, so this repo ports the workflow in a Codex-native form:

- the upstream nWave command, agent, and skill prompts are vendored into the package
- a Codex compatibility layer maps slash-command and subagent assumptions into direct Codex usage
- the result installs as a skill named `$nwave`

## Install

From GitHub:

```powershell
pipx install git+https://github.com/MaxwellCalkin/nwave-codex.git
nwave-codex install --force
```

From a local clone:

```powershell
pipx install .
nwave-codex install --force
```

Install into a non-default Codex home if needed:

```powershell
nwave-codex install --codex-home C:\path\to\.codex --force
```

## Use

Once installed, start a fresh Codex session and invoke it naturally:

```text
Use $nwave to discuss a password reset feature.
Use $nwave to distill acceptance tests for password reset.
Use $nwave to deliver the password reset feature with TDD.
Use $nwave to review the implementation.
```

Every nWave response in Codex is intended to end with an explicit handoff:

- the current phase
- whether you should review artifacts now
- what to review
- the phase commit, if one was created
- the next step
- the exact next prompt to send

So instead of wondering "am I supposed to approve this design?", the response should tell you directly.

When a phase changes files, `nwave-codex` is also intended to commit that phase before handing off to you.

For `discuss`, `design`, `devops`, and `distill`, the agent is also intended to ask focused spec-shaping questions before it finalizes artifacts, unless those answers are already present in prior wave docs or you explicitly ask it to make reasonable assumptions.

Those phases now have literal question-round templates as part of the bundled skill, so the interaction should be more consistent from run to run.

## What Gets Installed

The installer copies one bundled skill into your Codex home:

```text
~/.codex/skills/nwave/
  SKILL.md
  agents/openai.yaml
  references/codex/
  references/upstream/
```

Inside that bundle:

- `references/upstream/` contains the vendored nWave command, agent, and skill prompt assets
- `references/codex/parity.md` documents how Claude-specific behavior maps to Codex
- `references/codex/command-map.md` routes requests to the right wave or support command
- `references/codex/deliver-mode.md` explains the Codex version of nWave's delivery discipline

## Parity Notes

This repo is faithful to the nWave workflow, but not every Claude Code runtime feature exists in Codex today.

What is preserved:

- the same wave model
- the same artifact flow
- the same specialist personas and methodology
- the same planning, acceptance-test, review, and TDD intent

What changes in Codex:

- no `/nw:*` slash commands; use `$nwave` or plain language
- no Claude `Task` subagents; Codex emulates the requested role in-session
- no Claude DES hooks; delivery discipline is explicit and file-driven rather than hook-enforced
- every phase should explicitly tell the user what to do next
- completed phases with file changes should end with a dedicated git commit
- planning and spec phases should ask focused user questions instead of silently guessing

## Project Layout

```text
src/nwave_codex/
  cli.py
  installer.py
  skill_bundle/nwave/
tests/
```

## Verification

The repo includes a small test suite for the installer:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests -v
```

## License and Attribution

This project vendors prompt assets from `nWave-ai/nWave`, which is released under the MIT license. See [LICENSE](LICENSE).
