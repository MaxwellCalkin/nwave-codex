from __future__ import annotations

import shutil
import unittest
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
TMP_ROOT = ROOT / ".tmp-test-work"
TMP_ROOT.mkdir(exist_ok=True)

import sys
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from nwave_codex.cli import main
from nwave_codex.installer import bundled_skill_dir, install_skill, target_skill_dir, uninstall_skill


class InstallerTests(unittest.TestCase):
    def make_temp_home(self) -> Path:
        temp_home = TMP_ROOT / f"codex-home-{uuid.uuid4().hex}"
        temp_home.mkdir(parents=True, exist_ok=False)
        return temp_home

    def tearDown(self) -> None:
        shutil.rmtree(TMP_ROOT, ignore_errors=True)
        TMP_ROOT.mkdir(exist_ok=True)

    def test_bundle_exists(self) -> None:
        bundle = bundled_skill_dir()
        self.assertTrue(bundle.exists())
        self.assertTrue((bundle / "SKILL.md").exists())
        self.assertTrue((bundle / "agents" / "openai.yaml").exists())
        self.assertTrue((bundle / "references" / "codex" / "parity.md").exists())
        self.assertTrue((bundle / "references" / "codex" / "command-map.md").exists())
        self.assertTrue((bundle / "references" / "codex" / "deliver-mode.md").exists())

    def test_install_and_uninstall(self) -> None:
        codex_home = self.make_temp_home()
        installed = install_skill(codex_home)
        self.assertEqual(installed, target_skill_dir(codex_home))
        self.assertTrue((installed / "SKILL.md").exists())

        removed = uninstall_skill(codex_home)
        self.assertTrue(removed)
        self.assertFalse(installed.exists())

    def test_install_requires_force_when_present(self) -> None:
        codex_home = self.make_temp_home()
        install_skill(codex_home)
        with self.assertRaises(FileExistsError):
            install_skill(codex_home)

    def test_cli_version(self) -> None:
        exit_code = main(["version"])
        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
