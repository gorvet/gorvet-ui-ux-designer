# Update the installed plugin from GitHub

Official release metadata: [latest.json](https://github.com/gorvet/gorvet-ui-ux-designer/releases/latest/download/latest.json).

Official packages: [latest stable release](https://github.com/gorvet/gorvet-ui-ux-designer/releases/latest).

## ChatGPT web

Ask: **“Update my existing GORVET UI/UX Designer plugin from its official GitHub release.”**

The installed [gorvet-plugin-update skill](../skills/gorvet-plugin-update/SKILL.md) describes discovery, numeric version comparison, checksum/package inspection, supported account update and read-back verification. For older installations that do not yet include it, give ChatGPT this repository link and explicitly ask it to follow that update procedure with Plugin Creator.

The web host needs access to download files, inspect a ZIP and update the selected plugin. Plugin Creator must be available and must authorize editing that existing account plugin. Use its exact verified backend ID and current release ID; never create a duplicate. Git-managed installations use their owning synchronization flow. Local Codex installation and account installation are separate targets.

If the installed version is equal/newer, no upload is needed. An unavailable tool, denied edit, ambiguous target or incompatible configuration must be reported as pending rather than as an update. Repository instructions cannot install anything by themselves. Account-specific settings and unrelated files must be preserved; archive updates overlay existing files and do not imply deletion.

## Release contents

Each stable release publishes:

- `gorvet-ui-ux-designer-VERSION.zip`: one standalone plugin at ZIP root, including all skills, references and the verifier; no Git checkout or CI files.
- `latest.json`: schema version, plugin/repository identity, numeric version, tag, exact source commit, pinned archive URL, byte size, SHA-256 and skill count.
- `SHA256SUMS`: checksum for the ZIP.

The stable `releases/latest/download/latest.json` endpoint points to the latest published stable release, not unreleased `main`. The checksum checks consistency with official metadata; it is not a cryptographic publisher signature.

## Publishing from this repository

1. Update skills/support files, bump the stable numeric semantic version in `plugin.json`, and add its `CHANGELOG.md` entry.
2. Push to `main`. The release workflow runs when `plugin.json` changes; `workflow_dispatch` can retry the current main commit.
3. CI validates the skills, runs release tests, builds the package outside the plugin tree and verifies it. It uploads assets to a draft, then publishes it as latest only when the uploads succeed. Existing published versions are immutable; an identical rerun succeeds without replacement, while a different commit requires a version bump.
4. Check GitHub Actions and the published assets before asking an account plugin to update.

The workflow uses the repository's built-in `GITHUB_TOKEN` with `contents: write`. No account plugin credentials or fixed account IDs are stored here. Pushing a GitHub release never mutates a ChatGPT account installation automatically.

Local verification uses only Python's standard library:

```text
python scripts/validate_skills.py
python -m unittest discover -s tests -v
python scripts/release_package.py build --output /temporary/release-output --commit FULL_COMMIT_SHA
python scripts/release_package.py verify --archive /temporary/release-output/gorvet-ui-ux-designer-VERSION.zip --metadata /temporary/release-output/latest.json --installed-version INSTALLED_VERSION
```
