# ArcheAge PlayerBots Navigation-Extractor

Extract local navigation assets and export recorded route graphs.

**Role:** Companion tool. **Status:** source preview. Requires your own matching game data; graph export alone does not prove a route is walkable.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch navigation-extractor`, then `cd tools/navigation-extractor`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Navigation-Extractor.git
cd ArcheAge-PlayerBots-Navigation-Extractor
```

This companion is public. The master and most variants currently require owner-granted access.

## Setup

This is a supporting library or tool, not a standalone bot server. Commands below run from this repository directory. Use external directories for build output and runtime data.

## Commands

From this repository directory:
```powershell
dotnet build extractor/AAEmu.NavigationExtractor --artifacts-path ../artifacts/navigation -p:AAEmuOutput=<built-Core-AAEmu.Game-output>
```
Run the resulting `AAEmu.NavigationExtractor.dll --help` with `dotnet` for game archive extraction options. `graph <prebuilt-roads.json> <new-output.json>` exports a deterministic graph. Choose a new output filename: existing output is refused. Game assets and generated maps remain outside the repository.

## Development

See [AGENTS.md](../../AGENTS.md) for contributor and agent rules. Tests and detailed logs are retained in a separate validation workspace. Preserve the supplied license files and attribution.
