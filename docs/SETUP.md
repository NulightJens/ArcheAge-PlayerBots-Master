# Set up a PlayerBots server

Start with **Core on AAEmu 1.2 r208022**. Use Experiment, 3.0, 10x and the historical
overlays only with their own matching host. Each variant requires a separate host checkout.

## Prepare Core

From the master repository directory, with Git, Python 3.11+ and .NET 10 SDK installed:

```powershell
python playerbots.py doctor
python playerbots.py fetch core
python playerbots.py prepare-host core --destination ../AAEmu-Core
python playerbots.py install core --host ../AAEmu-Core --check
python playerbots.py install core --host ../AAEmu-Core
dotnet build ../AAEmu-Core/AAEmu.Game/AAEmu.Game.csproj --artifacts-path ../artifacts/core
```

`prepare-host` downloads the exact host revision from the component manifest.
`install --check` is read-only. `install` copies the selected module and applies its
host patch. These commands do not start a server, create an account or change a database.
Use a new destination if a host directory already exists.

## Finish the normal AAEmu setup

Follow the README in the pinned AAEmu host for Login/Game configuration, databases,
client version and required game data. Build and configure its Login service as needed;
the Game build above is the PlayerBots integration check. Keep credentials, client files,
game assets and runtime data outside this master and its component repositories.

For Core, apply the migration named in `core/playerbots.module.json` to the intended
isolated game database using your normal administration tool. Configure the installed
`BotConfig.json` with the Game service's other configuration. For fresh bot creation,
set `AAEMU_PLAYERBOTS_ACCOUNT_ID` to an existing dedicated game account before startup.
Using `/addbot` with a saved offline character does not require creating a new account.

Keep the exact source revision, host revision, data/configuration identity and external
output directory with each test run. Check runtime ownership and isolated database
configuration before starting the server. Start and shut down using the normal AAEmu
lifecycle; preserve existing characters and prior installations.

Join as a GM with the matching client, then use `/bot`. Follow the
[Core commands](components/core.md#commands) for admission, party orders and logout.
Automatic questing remains opt-in and under development.

## Other variants

The same `fetch`, `prepare-host` and `install` commands accept `experiment`, `3-0`,
`10x`, `legacy` and `legacy-refined`. Their guides show the correct commands and limits.
Never install two variants into the same host.

Core, Experiment, 3.0 and the historical overlays build through the pinned host's
`AAEmu.Game/AAEmu.Game.csproj`. The 10x host instead builds
`AAEmu.WorldServer/AAEmu.World` with `-p:PlayerBotsNativeExperiment=true`; its runtime
also requires `AAEMU_PLAYERBOT_EXPERIMENT=1`. Use an external `--artifacts-path`.

Libraries and companion tools have their own commands rather than host installers.
Run `python playerbots.py guide <component>` or use the links in the main README.

## Troubleshooting

| Message or symptom | Next step |
|---|---|
| Python opens Microsoft Store | Use an installed Python 3.11+ executable, `py -3`, or its full path. Run `--version` first. |
| Repository not found / permission denied | Authenticate Git with an account that can access the private master and selected components. |
| Missing component source | Run `fetch <component>` from a Git clone. ZIP downloads omit submodules. |
| Local changes or revision mismatch | Preserve the existing checkout. Clone the master into a new directory; do not reset or force-update it. |
| Host already exists or is dirty | Prepare a new host directory. Installers intentionally require a clean pinned host. |
| Unknown bot commands | Confirm the selected variant was installed, built and loaded by the running Game service. |
| Party order refused | Invite the bot normally and issue commands as its current party leader. |
| Navigation or quest stall | Preserve the bot state and capture the first blocker. Full progression is still in development. |
| Host dependency warnings | Consult the status page. The pinned host retains upstream warnings; upgrading dependencies needs compatibility validation. |

## Upgrade

Clone a new master revision into a new directory, fetch the chosen component and prepare
a new host. Reapply configuration deliberately and retain prior data and backups. The
master selects reviewed revisions; it does not track moving component heads automatically.
