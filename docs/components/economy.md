# ArcheAge PlayerBots Economy

Checks proposed exchanges against native observations.

**Role:** Protocol prototype. **Status:** source preview. No native auction adapter or settlement implementation. An allowed result does not transfer items or money.

[Master workspace](https://github.com/NulightJens/ArcheAge-PlayerBots-Master) · [Current status and next work](https://github.com/NulightJens/ArcheAge-PlayerBots-Master/blob/main/docs/STATUS.md)

From the master root, run `python playerbots.py fetch economy`, then `cd libraries/economy`. The commands below also support a standalone clone.

## Get the source

```powershell
git clone --recurse-submodules https://github.com/NulightJens/ArcheAge-PlayerBots-Economy.git
cd ArcheAge-PlayerBots-Economy
```

This repository requires GitHub access from its owner.

## Setup

This is a supporting library or tool, not a standalone bot server. Commands below run from this repository directory. Use external directories for build output and runtime data.

## Commands

From this repository directory:
```powershell
dotnet run --project cli/Economy.Cli.csproj --artifacts-path ../artifacts/economy -- check request.json observation.json
```
Use `--help` in place of `check ...` for usage. JSON fields follow `AuctionExchangeRequest` and `AuctionExchangeObservation` in the source. The result reports `Allowed`, `Reason` and `Submitted=false`. Inputs and outputs belong outside the code repository.

## Development

See [AGENTS.md](../../AGENTS.md) for contributor and agent rules. Tests and detailed logs are retained in a separate validation workspace. Preserve the supplied license files and attribution.
