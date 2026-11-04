# ArcheAge PlayerBots Client-Autopilot

Control your ArcheAge client, position the camera and capture recordings.

**Role:** Companion tool. **Status:** source preview. Requires the matching client and server adapter; recordings are evidence, not autonomous gameplay acceptance.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch client-autopilot`, then `cd tools/client-autopilot`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Client-Autopilot.git
cd ArcheAge-PlayerBots-Client-Autopilot
```

You can clone this companion publicly. You need access to the private master and most variants.

## Setup

Run the commands below from this repository directory. Use Core to set up a bot server. Use external directories for build output and runtime data.

## Commands

From this repository directory:
```powershell
python autopilot.py --help
python install-server.py --host ../AAEmu-Core --check
```
CLI families include `control`, `streetview`, `camera-service`, `input` and `capture`; each has `--help`. The adapter installer targets an installed Core host. Omit `--check` to install, and add `--camera-time` only when the time controls are needed.

Build the `driver`, `capture` and `WindowCapture` .NET projects with an external `--artifacts-path`. Native adapters use `adapter/Build-ClientAutopilot.ps1 -Zig <zig-0.15.2.exe> -OutputDirectory <new-external-folder> -Camera`. Keep control of your active client session and save captures outside the repository.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
