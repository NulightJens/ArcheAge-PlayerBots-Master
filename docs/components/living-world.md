# ArcheAge PlayerBots Living-World

Durable journals, witnessed memory and private recall.

**Role:** Shared library. **Status:** source preview. Offline checks pass; real native observation, owner-only recall and restart/replay still need combined live acceptance.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch living-world`, then `cd libraries/living-world`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Living-World.git
cd ArcheAge-PlayerBots-Living-World
```

This repository requires GitHub access from its owner.

## Setup

This is a supporting library or tool, not a standalone bot server. Commands below run from this repository directory. Use external directories for build output and runtime data.

## Commands

From this repository directory:
```powershell
dotnet run --project cli/LivingWorld.Cli.csproj --artifacts-path ../artifacts/living-world -- --help
```
Use `inspect <closed-journal-path> <realm>` to validate/count an existing journal, or `replay <closed-journal-path> <realm>` to print retained events. Both commands are read-only. Close the journal writer before inspecting it. Core and Experiment pin their own dependency revision; update those pins deliberately when library behavior changes.

## Development

See [AGENTS.md](../../AGENTS.md) for contributor and agent rules. Tests and detailed logs are retained in a separate validation workspace. Preserve the supplied license files and attribution.
