# ArcheAge PlayerBots Legacy

Explore the original PlayerBots overlay and its historical revisions.

**Role:** Historical reference. **Status:** source preview. Historical implementation; use Core for continued development.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch legacy`, then `cd variants/legacy`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Legacy.git
cd ArcheAge-PlayerBots-Legacy
```

You need access to this private repository before cloning it.

## Setup

Requires Git, Python 3.11+, .NET 10 SDK and your own matching client/data. Install this module on your server. From this repository directory:

```powershell
git clone https://github.com/AAEmu/AAEmu ../AAEmu-Legacy
git -C ../AAEmu-Legacy checkout 62e3eb1d87da01194802ac886cd500134facad28
python install.py --host ../AAEmu-Legacy --check
python install.py --host ../AAEmu-Legacy
```

Use a new host directory for each installation. The installer verifies the host revision and applies source changes; it does not configure a database or start a server. [Complete host setup and build instructions](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/SETUP.md).

## Commands

Use `/bothelp` in game. The `original-overlay` branch retains the original overlay revision; `main` includes the recovered loose-file revisions. Use a separate host for comparison.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
