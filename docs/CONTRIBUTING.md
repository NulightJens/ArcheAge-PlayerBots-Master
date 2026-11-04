# Contributing

Start with Core for product work. Use Experiment for isolated AI and Headless DM research;
keep compatibility and historical variants separate. Human commands and the matching guide
should make each capability usable without agent-only access.

## Change a component

1. Clone that component into a separate development directory and create a normal branch.
2. Read its README, manifests and `AGENTS.md`. Preserve existing work and history.
3. Make the smallest coherent change, with concise comments explaining non-obvious behavior.
4. Verify the affected behavior. Keep test source, fixtures, build output and logs in an
   external validation directory; retain the exact candidate and evidence.
5. Update its human guide and the corresponding master guide when behavior or commands change.
6. Publish the component commit, then advance its master submodule pointer in a separate commit.

## Advance the master

The gitlinks select exact component commits. `components.json` supplies roles, paths and
guide links; it does not duplicate the revision lock. Preserve nested dependency pins.
When Living World changes, update and validate Core/Experiment dependencies deliberately.

Use a clean working copy for pin changes. Do not use force updates, history rewrites or
automatic `submodule update --remote`. Verify a fresh master clone can fetch the selected
component and that installation checks succeed against its pinned host. Keep runtime and
database work isolated and owned; a source publication does not accept live gameplay.

## What belongs here

Source, required manifests/build files/licenses, short human guides and agent instructions.
Keep tests, traces, logs, generated reports, credentials, game assets and runtime databases
outside the master and every component. Keep current capability/limitation summaries in
the guides and link users to the relevant commands.
