# Agent instructions

- Read `README.md` first. Keep setup instructions and command examples concise and accurate.
- Preserve files, Git history, databases, configurations and existing runtime state. Use new checkouts and versioned outputs; never delete, force-push, reset, clean or force-stop processes.
- Keep tests, fixtures, logs, traces, reports, credentials, game assets and generated build output outside code repositories. Required licenses, manifests and useful source comments stay with the code.
- Use the exact host and dependency revisions in the manifests. Do not treat a successful build or offline check as live gameplay acceptance.
- Maintain Core as the primary AAEmu 1.2 product. PvP stays in Core; Headless DM stays in Experiment. Preserve 3.0 as the compatibility track.
- Changes need focused verification against the behavior they affect. Record candidate revision, configuration, result and evidence outside the code repository. Do not fabricate quest credit, weaken native guards or equate translated code with working native integration.
- Do not start a server or touch a database until runtime ownership and an isolated registered test database are established. Preserve normal native persistence behavior. Hostile resets and data destruction are prohibited.
- Do not enable retired Codex Router or Astra Flash integrations. Use the current user's tools and instructions.
- Publish component changes before advancing the master gitlink; retain a reproducible external evidence record. Document commands that readers can run themselves.

## Master workspace

`components.json` contains component roles and guide paths. Git submodule entries are the single authority for selected revisions. `playerbots.py` refuses local changes or revision drift when fetching/installing; preserve work and use a fresh checkout rather than forcing an update.

When changing a component, work on a normal branch in its own repository. Update its README and relevant master guide together. After publishing, advance the gitlink in a dedicated master commit and record external validation. Never use `git submodule update --remote` to silently replace reviewed pins.

The roadmap records outcomes, not scheduling authority. Small city, party, duel and property proofs can proceed independently when their native prerequisites exist. Do not reopen the completed five-quest milestone or substitute travel-only testing for the quest-bearing Wardton journey.

## Write directly to the reader

When the user says "human-friendly", "human-forward" or "human-facing", write for the person using the product. Address the reader directly and explain what they can do and how to do it. This is a writing requirement, not wording to repeat in the product.

Use plain labels such as "Setup", "Commands" and "Get started". Do not label pages, repository descriptions or tools "Human Setup Guides", "Human Command Tools" or similar. Avoid third-person handoff prose about "the user" when you can say "you" or give a direct instruction. Describe the product and its use, not the process of making it readable.

Keep agent workflow and maintenance instructions in AGENTS.md or contributor documentation, separate from the main product introduction. Apply this preference to READMEs, GitHub descriptions, interfaces, guides and future revisions.
