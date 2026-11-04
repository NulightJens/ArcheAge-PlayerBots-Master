# Status and next work

Reviewed 2026-11-04. This page distinguishes available source from proven gameplay.
The October 26 publication completed the eleven-repository cleanup, installers, command
entry points and external evidence records. The master adds one starting point and
consistent human guides. Repository organization is complete; the gameplay vision is ongoing.

## Current maturity

| Area | Available now | Still needs acceptance |
|---|---|---|
| Core | Integrated AAEmu 1.2 movement, party/command systems, PvP and memory hooks; builds and offline/native-boundary checks. | Exact published revision observed in a real client; full quest journey, restart behavior and larger-group gameplay. |
| Experiment | Broad shared AI translation, native lifecycle hooks and bounded Headless DM memory; offline and native-boundary checks. | Live navigation loader/endpoint fixes, native manager/policy bindings, lifecycle negative cases and gameplay integration. |
| Living World | Durable journal, private recall and replay with offline checks. | One real native observation through owner-only recall, non-owner denial, feature-off behavior and graceful restart/replay. |
| Economy | Exchange protocol and preflight checks. | Native auction adapter, real item/fund transfer, reconciliation and restart-safe settlement. |
| 3.0 | Pinned source installer and host build. | Regression evidence for any change; retain its compatibility boundary. |
| 10x | Bounded command-driven native operations. | Autonomous decisions and complete gameplay outcomes. |
| Legacy variants | Preserved historical source and installers; Chronicle offline simulator. | Not the main feature target. Two historical Chronicle imports still lack their original data. |
| Companion tools | Recording, capture/control and navigation exports. | Tool output must be connected to observed native behavior before claiming gameplay success. |

Prior Core evidence includes bridge/water traversal and mounted positioning defects.
Experiment's retained native checkpoint has a walking loader/endpoint problem despite
available navigation assets. Previous runs are useful diagnosis; they do not accept a
new source revision automatically.

The publication did not add live 50v50, full persistence, performance or Economy settlement
acceptance. The pinned AAEmu host also retains dependency warnings, including the recorded
SQLite package advisory. Updating the host/dependencies needs a separate compatibility pass.
No measured performance improvement is claimed from source cleanup alone.

## Development priorities

1. **Reproduce Core on one recorded candidate.** Confirm visible admission, ownership,
   stop/logout, saving and graceful restart with the matching host/client/data.
2. **Resolve native navigation blockers.** Observe bridge, water, cross-zone/local route
   handoff and mounted behavior. Recovery must be bounded and must not invent arrival.
3. **Complete the level-one Nuian-to-Wardton quest journey.** Start at the native race spawn;
   dynamically select and finish the required main story through Wardton and feasible
   side quests along the way. Record skipped side quests with reasons. Start autonomy once;
   no per-target operator control, injected quest credit or fixed walkthrough.
4. **Prove population and cooperation.** Three independent persistent bots, a small party
   fight with loot/recovery, then measured scale and native PvP. Field 50v50 remains a
   separate live acceptance outcome.
5. **Complete persistent world life.** Live witnessed memory/privacy, city routines,
   lawful property and inventory-funded trade, with recovery across restart.

Travel alone and the earlier five-quest milestone were already confirmed; do not repeat
them as substitutes for the full quest-bearing journey. Small city, duel, party and
property proofs may proceed independently once their native prerequisites exist.

Core remains the primary product. Bring Experiment improvements across only after their
native behavior is proven. Keep Headless DM in Experiment and PvP in Core.

## Evidence policy

Keep tests and detailed run logs outside code repositories. Each acceptance record needs
the exact component/host revision, configuration and data identity, commands, observed
result and retained evidence. Label source checks, host-boundary checks, server behavior
and client-witnessed outcomes separately. A compilation result or translated-code count
does not prove a complete native feature.
