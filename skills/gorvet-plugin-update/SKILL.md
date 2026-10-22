---
name: gorvet-plugin-update
description: Update the existing installed GORVET UI/UX Designer plugin from its official GitHub release when the user asks to update or synchronize the plugin. This is package maintenance, separate from the UI design pipeline.
license: MIT
metadata:
  author: GORVET
---

# Update GORVET from GitHub

Use this only for an explicit plugin-update request. Do not check for updates during normal UI work. This skill supplies release discovery and integrity checks; the host's plugin-update workflow owns installation and authorization.

## Source and target

- Repository: `https://github.com/gorvet/gorvet-ui-ux-designer`.
- Latest stable release metadata: `https://github.com/gorvet/gorvet-ui-ux-designer/releases/latest/download/latest.json`.
- The target is the user's existing GORVET plugin, not a new plugin or the plugin files in a local Codex cache.

1. Use the available Plugin Creator/update-plugin capability and read its applicable instructions. Resolve the exact existing backend plugin ID through host discovery or a verified user-selected plugin. Inspect its metadata, current release ID, manifests and inventory. Do not assume a name, repository slug or locally cached ID identifies the account plugin. If multiple targets match, resolve the ambiguity before updating.
2. Fetch `latest.json` from the official release endpoint. Compare numeric semantic versions with the selected account plugin, not the version of these instructions. If installed is equal/newer, report that no update is needed; do not upload the same version and trigger an automatic patch bump. If the current version is missing/nonstandard, resolve it from the existing manifest before proceeding.
3. Download only the version-pinned official `archive_url` to a temporary local file. Verify identity, version, size, SHA-256, safe ZIP paths and root manifest with the bundled [release verifier](../../scripts/release_package.py). Example:

   ```text
   python release_package.py verify --archive /absolute/path/package.zip --metadata /absolute/path/latest.json --installed-version CURRENT_VERSION
   ```

   The checksum detects corruption/substitution relative to the official metadata; it is not a publisher signature. Do not execute scripts from a downloaded candidate before verification. Use the already-installed verifier or equivalent host-side inspection. If metadata or download is unavailable, stop with the precise limitation; do not substitute a branch ZIP, which has different wrapping and no published checksum.
4. Inspect the verified package against the current plugin. Preserve its backend identity, scope, audience, App/MCP bindings, custom files and host-owned configuration. A full upstream package must not silently overwrite unrelated account-specific changes. If configuration/presentation differs, use the host's supported overlay preparation to retain it; if identity or compatibility is unresolved, stop rather than creating another plugin. Omitted installed files remain unless their exact removal is authorized through the host's supported deletion workflow.
5. Once the update is concrete and reviewable, use the host's existing authorization rules. An explicit request to update this plugin is authorization within that scope; ask only for unresolved target/configuration choices or additional publication authorization actually required by the host. For an eligible account plugin, call its update tool with the absolute local archive path and observed current release ID. For a Git-managed plugin, use its owning synchronization process instead of archive editing. Never embed credentials or a fixed account plugin ID in this package.
6. Read back the saved release, version and changed skills. Report the existing plugin's returned link and verified version. If a release conflict occurs, refresh current source and reconcile before retrying; do not blindly replace the expected release ID. A successful download or packaging step is not a successful update, and a saved release does not prove runtime loading.

If the host lacks downloads/local files or a supported update tool, provide the official release link and explain which capability is missing. Do not claim that repository instructions alone can change an installation. For Codex-local requests, use its supported marketplace reinstall flow, preserving account installations and avoiding direct cache edits.
