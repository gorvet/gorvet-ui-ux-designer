"""Build and verify the standalone GORVET release using Python's standard library."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "gorvet-ui-ux-designer"
REPOSITORY = "gorvet/gorvet-ui-ux-designer"
BASE_URL = f"https://github.com/{REPOSITORY}/releases/download"
VERSION_RE = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)")


def version_key(value):
    if not isinstance(value, str) or not VERSION_RE.fullmatch(value):
        raise ValueError("Expected a stable numeric semantic version")
    return tuple(map(int, value.split(".")))


def verify(archive, metadata, installed_version=None):
    """Inspect without extracting or installing the downloaded package."""
    version = metadata["version"]
    version_key(version)
    filename = f"{NAME}-{version}.zip"
    expected_url = f"{BASE_URL}/v{version}/{filename}"
    if (metadata.get("schema_version") != 1 or metadata.get("name") != NAME
            or metadata.get("repository") != REPOSITORY
            or metadata.get("archive_url") != expected_url):
        raise ValueError("Unexpected release identity, schema or download origin")
    if installed_version is not None and version_key(version) <= version_key(installed_version):
        raise ValueError("Release is not newer than the installed version")
    data = Path(archive).read_bytes()
    if len(data) != metadata["size_bytes"] or hashlib.sha256(data).hexdigest() != metadata["sha256"]:
        raise ValueError("Archive size or SHA-256 mismatch")
    with zipfile.ZipFile(archive) as package:
        names = package.namelist()
        if len(names) != len(set(names)) or "plugin.json" not in names:
            raise ValueError("Duplicate members or missing root plugin.json")
        for entry in package.infolist():
            path = PurePosixPath(entry.filename)
            if (path.is_absolute() or ".." in path.parts or "\\" in entry.filename
                    or ":" in entry.filename or stat.S_ISLNK(entry.external_attr >> 16)):
                raise ValueError("Unsafe archive member")
        manifest = json.loads(package.read("plugin.json"))
        if (manifest.get("name") != NAME or manifest.get("version") != version
                or manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"):
            raise ValueError("Package manifest does not match the release")
        skills = sorted(n for n in names if re.fullmatch(r"skills/[^/]+/SKILL.md", n))
        if not skills or len(skills) != metadata["skill_count"]:
            raise ValueError("Unexpected skill inventory")
        corrupt = package.testzip()
        if corrupt:
            raise ValueError(f"Corrupt archive member: {corrupt}")
    return {"name": NAME, "version": version, "skills": skills, "archive": str(Path(archive).resolve())}


def build(output, commit):
    output = Path(output).resolve()
    if output == ROOT or ROOT in output.parents:
        raise ValueError("Build outside the plugin directory")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Expected the exact source commit SHA")
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    version_key(version)
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"{NAME}-{version}.zip"
    paths = [ROOT / p for p in ("plugin.json", "README.md", "LICENSE", "NOTICE.md", "CHANGELOG.md")]
    for directory in ("skills", "docs", "scripts"):
        paths.extend(p for p in (ROOT / directory).rglob("*")
                     if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for path in sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix()):
            if path.is_symlink():
                raise ValueError(f"Do not package symlinks: {path}")
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            # Normalize tracked text so Windows and Linux produce identical packages.
            package.writestr(info, path.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8"))
    data = archive.read_bytes()
    metadata = {
        "schema_version": 1, "name": NAME, "repository": REPOSITORY,
        "version": version, "tag": f"v{version}", "source_commit": commit,
        "archive_url": f"{BASE_URL}/v{version}/{archive.name}",
        "sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data),
        "skill_count": len(list((ROOT / "skills").glob("*/SKILL.md"))),
    }
    verify(archive, metadata)
    (output / "latest.json").write_bytes((json.dumps(metadata, indent=2) + "\n").encode("utf-8"))
    (output / "SHA256SUMS").write_bytes(f"{metadata['sha256']}  {archive.name}\n".encode("utf-8"))
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    notes = changelog.split(f"## {version} - ", 1)[1].split("\n", 1)[1].split("\n## ", 1)[0].strip()
    (output / "RELEASE_NOTES.md").write_bytes((notes + "\n").encode("utf-8"))
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    builder = commands.add_parser("build")
    builder.add_argument("--output", required=True)
    builder.add_argument("--commit", required=True)
    checker = commands.add_parser("verify")
    checker.add_argument("--archive", required=True)
    checker.add_argument("--metadata", required=True)
    checker.add_argument("--installed-version")
    args = parser.parse_args()
    try:
        if args.command == "build":
            result = build(args.output, args.commit)
        else:
            metadata = json.loads(Path(args.metadata).read_text(encoding="utf-8"))
            result = verify(args.archive, metadata, args.installed_version)
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Release validation failed: {error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
