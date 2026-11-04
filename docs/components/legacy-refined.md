# ArcheAge PlayerBots Legacy-Refined

Explore the historical refined bots and run offline Chronicle simulations.

**Role:** Historical reference. **Status:** source preview. Chronicle simulation is not native gameplay. Two historical import checks need unavailable macOS data exports.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch legacy-refined`, then `cd variants/legacy-refined`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Legacy-Refined.git
cd ArcheAge-PlayerBots-Legacy-Refined
```

You need access to this private repository before cloning it.

## Setup

Requires Git, Python 3.11+, .NET 10 SDK and your own matching client/data. Install this module on your server. From this repository directory:

```powershell
git clone https://github.com/AAEmu/AAEmu ../AAEmu-Legacy-Refined
git -C ../AAEmu-Legacy-Refined checkout 62e3eb1d87da01194802ac886cd500134facad28
python install.py --host ../AAEmu-Legacy-Refined --check
python install.py --host ../AAEmu-Legacy-Refined
```

Use a new host directory for each installation. The installer verifies the host revision and applies source changes; it does not configure a database or start a server. [Complete host setup and build instructions](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/SETUP.md).

## Commands

Use `/bothelp` in game. For Chronicle, from this repository directory:
```powershell
dotnet run --project overlay/extra/AAEmu.Bots.Chronicle.Cli --artifacts-path ../artifacts/chronicle -- --help
```
The CLI exposes `run`, `digest` and `world-from-exports`. Output defaults to `LocalAppData/ArcheAge/Chronicle`; pass `--out` for another external location.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
