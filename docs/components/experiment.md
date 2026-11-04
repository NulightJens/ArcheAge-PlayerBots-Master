# ArcheAge PlayerBots Experiment

Explore experimental bot AI and optional Headless DM memory on ArcheAge 1.2.

**Role:** Research variant. **Status:** source preview. Native walking, manager integration and end-to-end gameplay still need work. Headless DM is bounded witnessed memory, not a general autonomous dungeon master.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch experiment`, then `cd variants/experiment`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Experiment.git
cd ArcheAge-PlayerBots-Experiment
```

You need access to this private repository before cloning it.

## Setup

Requires Git, Python 3.11+, .NET 10 SDK and your own matching client/data. Install this module on your server. From this repository directory:

```powershell
git clone https://github.com/AAEmu/AAEmu ../AAEmu-Experiment
git -C ../AAEmu-Experiment checkout 62e3eb1d87da01194802ac886cd500134facad28
python install.py --host ../AAEmu-Experiment --check
python install.py --host ../AAEmu-Experiment
```

Use a new host directory for each installation. The installer verifies the host revision and applies source changes; it does not configure a database or start a server. [Complete host setup and build instructions](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/SETUP.md).

## Commands

In game:
```text
/pb
/pb list
/pb add 2
/pb 2 help
/pb 2 memory status
/pb 2 memory recall
```
Replace `2` with an eligible offline character ID. Use the per-bot help for lifecycle and behavior commands. Enable Headless DM only in its dedicated configuration: `Playerbots.HeadlessDm.Enabled`, distinct `BotId` and `HumanId`, `Realm`, `Candidate`, and an absolute `JournalPath` outside the code checkout. Its memory is tied to witnessed observations and the current owner.

Native asset helpers are in `apps/NativeAssets` and `apps/export_native_catalog.py`. The .NET helper needs `-p:AAEmuHost=<installed-experiment-host>`; the Python helper requires explicit external output and summary paths. Use their `--help` before exporting.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
