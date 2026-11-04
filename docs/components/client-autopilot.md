# ArcheAge PlayerBots Client-Autopilot

Windows client control, camera tools and capture.

**Role:** Companion tool. **Status:** source preview. Requires the matching client and server adapter; recordings are evidence, not autonomous gameplay acceptance.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch client-autopilot`, then `cd tools/client-autopilot`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Client-Autopilot.git
cd ArcheAge-PlayerBots-Client-Autopilot
```

This companion is public. The master and most variants currently require owner-granted access.

## Setup

This is a supporting library or tool, not a standalone bot server. Commands below run from this repository directory. Use external directories for build output and runtime data.

## Commands

From this repository directory:
```powershell
python autopilot.py --help
python install-server.py --host ../AAEmu-Core --check
```
CLI families include `control`, `streetview`, `camera-service`, `input` and `capture`; each has `--help`. The adapter installer targets an installed Core host. Omit `--check` to install, and add `--camera-time` only when the time controls are needed.

Build the `driver`, `capture` and `WindowCapture` .NET projects with an external `--artifacts-path`. Native adapters use `adapter/Build-ClientAutopilot.ps1 -Zig <zig-0.15.2.exe> -OutputDirectory <new-external-folder> -Camera`. Retain the operator ownership rules and direct captures outside the repository.

## Development

See [AGENTS.md](../../AGENTS.md) for contributor and agent rules. Tests and detailed logs are retained in a separate validation workspace. Preserve the supplied license files and attribution.
