# ArcheAge PlayerBots Living-World

Record witnessed events and recall them through persistent, private bot memory.

**Role:** Shared library. **Status:** source preview. Offline checks pass; real native observation, owner-only recall and restart/replay still need combined live acceptance.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch living-world`, then `cd libraries/living-world`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Living-World.git
cd ArcheAge-PlayerBots-Living-World
```

You need access to this private repository before cloning it.

## Setup

Run the commands below from this repository directory. Use Core to set up a bot server. Use external directories for build output and runtime data.

## Commands

From this repository directory:
```powershell
dotnet run --project cli/LivingWorld.Cli.csproj --artifacts-path ../artifacts/living-world -- --help
```
Use `inspect <closed-journal-path> <realm>` to validate/count an existing journal, or `replay <closed-journal-path> <realm>` to print retained events. Both commands are read-only. Close the journal writer before inspecting it. Core and Experiment pin their own dependency revision; update those pins deliberately when library behavior changes.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
