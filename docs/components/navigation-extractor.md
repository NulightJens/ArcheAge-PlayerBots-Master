# ArcheAge PlayerBots Navigation-Extractor

Extract navigation assets from your game data and export recorded route graphs.

**Role:** Companion tool. **Status:** source preview. Requires your own matching game data; graph export alone does not prove a route is walkable.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch navigation-extractor`, then `cd tools/navigation-extractor`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Navigation-Extractor.git
cd ArcheAge-PlayerBots-Navigation-Extractor
```

You can clone this companion publicly. You need access to the private master and most variants.

## Setup

Run the commands below from this repository directory. Use Core to set up a bot server. Use external directories for build output and runtime data.

## Commands

From this repository directory:
```powershell
dotnet build extractor/AAEmu.NavigationExtractor --artifacts-path ../artifacts/navigation -p:AAEmuOutput=<built-Core-AAEmu.Game-output>
```
Run the resulting `AAEmu.NavigationExtractor.dll --help` with `dotnet` for game archive extraction options. `graph <prebuilt-roads.json> <new-output.json>` exports a deterministic graph. Choose a new output filename: existing output is refused. Game assets and generated maps remain outside the repository.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
