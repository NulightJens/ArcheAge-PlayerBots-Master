# ArcheAge PlayerBots

Add playerbot companions to your AAEmu server. Bring a saved character into the world,
invite it to your party and give it orders. **Start with Core for ArcheAge 1.2.**
Choose Experiment to explore additional bot AI and Headless DM. PvP stays in Core.

**Current maturity: source preview.** The source builds and offline checks have passed.
Full autonomous quest progression, live 50v50 and economic settlement remain in development.
[See what works and what comes next](docs/STATUS.md).

## Start here

To install PlayerBots on your server, you need Git, Python 3.11+, .NET 10 SDK
and your own matching ArcheAge client/data. To play on an existing PlayerBots server,
join with its matching client. You need GitHub access to clone the private master
and most variants.

```powershell
git clone https://github.com/NulightJens/ArcheAge-PlayerBots-Master.git
cd ArcheAge-PlayerBots-Master
python playerbots.py doctor
python playerbots.py fetch core
python playerbots.py guide core
```

Next, follow the [server setup guide](docs/SETUP.md). Once the server is configured,
`/bot` shows in-game help. [Bring in your first companion](docs/components/core.md#commands).

## Choose a component

| Component | Use it for |
|---|---|
| [Core](docs/components/core.md) | Main AAEmu 1.2 product: companions, movement, party behavior and PvP. |
| [Experiment](docs/components/experiment.md) | Broader AI research, native integration and opt-in Headless DM. |
| [3.0](docs/components/3-0.md) | Frozen compatibility snapshot for the matching 3.0 host. |
| [10x](docs/components/10x.md) | Caller-driven native-zone prototype for the matching 10.x host. |
| [Legacy](docs/components/legacy.md) | Original overlay and historical revisions. |
| [Legacy-Refined](docs/components/legacy-refined.md) | Historical refined overlay and Chronicle simulation. |
| [Living World](docs/components/living-world.md) | Shared journal, witnessed memory and private recall. |
| [Economy](docs/components/economy.md) | Exchange preflight prototype; native settlement is pending. |
| [Route Recorder](docs/components/route-recorder.md) | Record roads, landmarks and photographs while playing. |
| [Client Autopilot](docs/components/client-autopilot.md) | Client control, camera tools and capture. |
| [Navigation Extractor](docs/components/navigation-extractor.md) | Export navigation assets and route graphs. |

`python playerbots.py list` lists these choices. Replace `core` with any component ID
to fetch it, or use `python playerbots.py fetch --all`. Each component lives in its own
repository; this workspace pins its exact revision using Git submodules. **Use Git to
download the workspace. GitHub's ZIP download does not include component source.**

## Keep it current

Use `python playerbots.py status` to inspect your local revisions. For an upgrade,
clone the latest master into a new directory and install into a new host checkout.
Keep the previous installation, configuration, data and evidence. The launcher refuses
to replace edited or differently pinned checkouts.

[Setup and troubleshooting](docs/SETUP.md) · [Status and roadmap](docs/STATUS.md) ·
[Contributing](docs/CONTRIBUTING.md) · [Licenses](LICENSE.md)
