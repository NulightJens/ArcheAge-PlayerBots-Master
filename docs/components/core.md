# ArcheAge PlayerBots Core

Add companions, party controls and experimental PvP to your ArcheAge 1.2 server.

**Role:** Main product. **Status:** source preview. Full autonomous quest progression, live 50v50 and restart acceptance remain open.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch core`, then `cd core`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Core.git
cd ArcheAge-PlayerBots-Core
```

You need access to this private repository before cloning it.

## Setup

Requires Git, Python 3.11+, .NET 10 SDK and your own matching client/data. Install this module on your server. From this repository directory:

```powershell
git clone https://github.com/AAEmu/AAEmu ../AAEmu-Core
git -C ../AAEmu-Core checkout 62e3eb1d87da01194802ac886cd500134facad28
python install.py --host ../AAEmu-Core --check
python install.py --host ../AAEmu-Core
```

Use a new host directory for each installation. The installer verifies the host revision and applies source changes; it does not configure a database or start a server. [Complete host setup and build instructions](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/SETUP.md).

## Commands

In game, as a GM:
```text
/bot
/addbot 2
```
Replace `2` with a saved, offline character ID. Invite that bot through the normal party UI. As its party leader:
```text
/botcontrol 2 role attacker
/botcontrol 2 follow
```
Select a living target before `/botcontrol 2 attack`. Use `/botcontrol 2 passive` and `/botcontrol 2 stay` to stop aggression and hold. `/removebot 2` saves and logs out the bot; it does not delete the character.

PvP stays in Core. `/bot pvp` explains duels and the experimental field scenario. Mark the two opposing raid locations with `/botopenfield prepare mark-a` and `prepare mark-b`, then use `/botopenfield prepare`, `/botopenfield start`, `/botopenfield status` and `/botopenfield hold`. Live 50v50 is not accepted yet.

`/botmemory status` and `/botmemory recall` expose witnessed memory. Configure `BotConfig.json` in the installed Game host; keep journal files outside source repositories. For fresh characters, configure an existing dedicated account with `AAEMU_PLAYERBOTS_ACCOUNT_ID`, then use `/createbot FreshNuian Nuian Female Abolisher 1 race-spawn`. Quest autonomy is experimental; keep `StuckTeleportEnabled` disabled for unassisted journey validation.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
