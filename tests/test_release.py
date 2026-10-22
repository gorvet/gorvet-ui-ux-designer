import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("release_package", ROOT / "scripts/release_package.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.output = Path(cls.temp.name)
        cls.metadata = release.build(cls.output, "a" * 40)
        cls.archive = cls.output / f"{release.NAME}-{cls.metadata['version']}.zip"

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_round_trip_and_complete_payload(self):
        checked = release.verify(self.archive, self.metadata, "1.1.3")
        self.assertEqual(checked["version"], self.metadata["version"])
        self.assertEqual(len(checked["skills"]), len(list((ROOT / "skills").glob("*/SKILL.md"))))
        with zipfile.ZipFile(self.archive) as package:
            names = package.namelist()
            self.assertEqual(names, sorted(names))
            self.assertIn("skills/gorvet-plugin-update/SKILL.md", names)
            self.assertIn("scripts/release_package.py", names)
            self.assertFalse(any(".git" in Path(n).parts or "__pycache__" in n for n in names))
            for path in (ROOT / "skills").rglob("*"):
                if path.is_file() and "__pycache__" not in path.parts:
                    self.assertEqual(package.read(path.relative_to(ROOT).as_posix()),
                                     path.read_text(encoding="utf-8").replace("\r\n", "\n").encode())

    def test_reproducible_build(self):
        before = self.archive.read_bytes()
        second = release.build(self.output / "again", "a" * 40)
        self.assertEqual(self.metadata, second)
        self.assertEqual(before, (self.output / "again" / self.archive.name).read_bytes())
        for filename in ["latest.json", "SHA256SUMS", "RELEASE_NOTES.md"]:
            self.assertNotIn(b"\r\n", (self.output / filename).read_bytes())
            self.assertEqual((self.output / filename).read_bytes(),
                             (self.output / "again" / filename).read_bytes())

    def test_checksum_rejects_tampering(self):
        changed = dict(self.metadata, sha256="0" * 64)
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            release.verify(self.archive, changed)

    def test_rejects_wrong_origin_and_identity(self):
        for field, value in [("archive_url", "https://example.com/plugin.zip"),
                             ("name", "other-plugin"), ("repository", "other/repo")]:
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "origin"):
                release.verify(self.archive, dict(self.metadata, **{field: value}))

    def test_rejects_equal_older_and_nonstandard_versions(self):
        for installed in [self.metadata["version"], "99.0.0", "unknown"]:
            with self.subTest(installed=installed), self.assertRaises(ValueError):
                release.verify(self.archive, self.metadata, installed)
        self.assertGreater(release.version_key("1.10.0"), release.version_key("1.9.0"))

    def test_rejects_manifest_mismatch_traversal_and_symlinks(self):
        for kind in ["version", "traversal", "symlink"]:
            with self.subTest(kind=kind):
                archive = self.output / f"bad-{kind}.zip"
                with zipfile.ZipFile(archive, "w") as package:
                    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
                    if kind == "version":
                        manifest["version"] = "0.0.0"
                    package.writestr("plugin.json", json.dumps(manifest))
                    if kind == "traversal":
                        package.writestr("../outside.txt", "bad")
                    if kind == "symlink":
                        link = zipfile.ZipInfo("link")
                        link.create_system = 3
                        link.external_attr = 0o120777 << 16
                        package.writestr(link, "/outside")
                data = archive.read_bytes()
                meta = dict(self.metadata, sha256=hashlib.sha256(data).hexdigest(), size_bytes=len(data))
                with self.assertRaises(ValueError):
                    release.verify(archive, meta)

    def test_build_must_be_outside_source_and_identify_commit(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            release.build(ROOT / "dist", "a" * 40)
        with self.assertRaisesRegex(ValueError, "commit"):
            release.build(self.output, "main")


if __name__ == "__main__":
    unittest.main()
