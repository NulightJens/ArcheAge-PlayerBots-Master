# ArcheAge PlayerBots Route-Recorder

Record roads, junctions, landmarks and photographs as you play.

**Role:** Companion tool. **Status:** source preview. A route recording supplies navigation evidence; it does not prove bot traversal.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch route-recorder`, then `cd tools/route-recorder`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Route-Recorder.git
cd ArcheAge-PlayerBots-Route-Recorder
```

You can clone this companion publicly. You need access to the private master and most variants.

## Setup

Run the commands below from this repository directory. Use Core to set up a bot server. Use external directories for build output and runtime data.

## Commands

On Windows, from this repository directory:
```powershell
powershell -NoProfile -File scripts/route-recorder/Start-PlayerRouteRecorder.ps1
```
Use the window's **Help** and **Server setup** controls. `Ctrl+Alt+R` starts/stops a recording; `Ctrl+Alt+P` takes a photograph. Keep recordings outside the repository.

`scripts/route-recorder/Build-PlayerRouteRecorder.ps1 -OutputPath <external-path>` builds the application. `scripts/New-StandaloneRouteRecorder.ps1 -OutputDirectory <new-external-folder>` packages a committed revision.

## Contributing

[Read the contribution guide](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/CONTRIBUTING.md).
