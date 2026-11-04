# ArcheAge PlayerBots

Server-controlled companions and autonomous characters for ArcheAge through AAEmu.
This is the master workspace: one starting point, one recommended Core, and separately
versioned variants and tools. **Start with Core for ArcheAge 1.2.** PvP is part of Core;
Headless DM remains in Experiment.

**Current maturity: source preview.** The source builds and offline checks have passed.
Full autonomous quest progression, live 50v50 and economic settlement remain in development.
[See what works and what comes next](docs/STATUS.md).

## Start here

The server owner installs PlayerBots. Players join that configured server with the
matching client. Requirements: Git, Python 3.11+, .NET 10 SDK and your own matching
ArcheAge client/data. The master and most variants require owner-granted GitHub access.

```powershell
git clone https://github.com/NulightJens/ArcheAge-PlayerBots-Master.git
cd ArcheAge-PlayerBots-Master
python playerbots.py doctor
python playerbots.py fetch core
python playerbots.py guide core
```

Next, follow the [server setup guide](docs/SETUP.md). Once the server is configured,
`/bot` shows in-game help. [Bring in your first companion](docs/components/core.md#commands).
All ordinary setup and control work through documented commands; an agent is optional.

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
[Contributing](docs/CONTRIBUTING.md) · [Agent instructions](AGENTS.md) · [Licenses](LICENSE.md)

Tests, detailed logs and generated evidence belong in a separate validation workspace.
This repository contains the launcher, concise guides and pinned component references.
