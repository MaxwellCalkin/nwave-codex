# Command Map

Use this table to route a Codex request into the vendored nWave sources.

## Core waves

| Command | Upstream command | Specialist role | Agent file | Skill bundle |
| --- | --- | --- | --- | --- |
| `discover` | `references/upstream/commands/discover.md` | product discoverer | `references/upstream/agents/nw-product-discoverer.md` | `references/upstream/skills/product-discoverer/` |
| `discuss` | `references/upstream/commands/discuss.md` | product owner | `references/upstream/agents/nw-product-owner.md` | `references/upstream/skills/product-owner/` |
| `design` | `references/upstream/commands/design.md` | solution architect | `references/upstream/agents/nw-solution-architect.md` | `references/upstream/skills/solution-architect/` |
| `devops` | `references/upstream/commands/devops.md` | platform architect | `references/upstream/agents/nw-platform-architect.md` | `references/upstream/skills/platform-architect/` |
| `distill` | `references/upstream/commands/distill.md` | acceptance designer | `references/upstream/agents/nw-acceptance-designer.md` | `references/upstream/skills/acceptance-designer/` |
| `deliver` | `references/upstream/commands/deliver.md` | orchestrator plus crafter persona | `references/upstream/agents/nw-software-crafter.md` or `references/upstream/agents/nw-functional-software-crafter.md` | `references/upstream/skills/software-crafter/` or `references/upstream/skills/functional-software-crafter/` |

## Cross-wave commands

| Command | Upstream command | Default role |
| --- | --- | --- |
| `continue` | `references/upstream/commands/continue.md` | workflow orchestrator |
| `diagram` | `references/upstream/commands/diagram.md` | solution architect |
| `document` | `references/upstream/commands/document.md` | researcher plus documentarist |
| `execute` | `references/upstream/commands/execute.md` | selected crafter persona |
| `fast-forward` | `references/upstream/commands/fast-forward.md` | workflow orchestrator |
| `finalize` | `references/upstream/commands/finalize.md` | platform architect |
| `forge` | `references/upstream/commands/forge.md` | agent builder |
| `hotspot` | `references/upstream/commands/hotspot.md` | software crafter |
| `mikado` | `references/upstream/commands/mikado.md` | software crafter |
| `mutation-test` | `references/upstream/commands/mutation-test.md` | software crafter reviewer |
| `new` | `references/upstream/commands/new.md` | workflow orchestrator |
| `refactor` | `references/upstream/commands/refactor.md` | software crafter |
| `research` | `references/upstream/commands/research.md` | researcher |
| `review` | `references/upstream/commands/review.md` | mapped reviewer persona |
| `rigor` | `references/upstream/commands/rigor.md` | main Codex session |
| `roadmap` | `references/upstream/commands/roadmap.md` | domain-appropriate planner |
| `root-why` | `references/upstream/commands/root-why.md` | troubleshooter |

## Reviewer mapping

When the upstream workflow asks for a reviewer, load the matching reviewer agent file under `references/upstream/agents/` and the matching reviewer skill bundle under `references/upstream/skills/`.

Examples:

- `nw-software-crafter-reviewer.md`
- `nw-solution-architect-reviewer.md`
- `nw-product-owner-reviewer.md`
- `nw-researcher-reviewer.md`

## Deliver stack

`deliver` is composite. In addition to `deliver.md`, load these upstream command files as needed:

- `roadmap.md`
- `execute.md`
- `review.md`
- `refactor.md`
- `mutation-test.md`
- `finalize.md`

Then apply `references/codex/deliver-mode.md`.
