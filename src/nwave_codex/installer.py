"""Installer helpers for the bundled Codex skill."""

from __future__ import annotations

import os
import shutil
from pathlib import Path


SKILL_NAME = "nwave"


def bundled_skill_dir() -> Path:
    return Path(__file__).resolve().parent / "skill_bundle" / SKILL_NAME


def resolve_codex_home(codex_home: str | os.PathLike[str] | None = None) -> Path:
    if codex_home is not None:
        return Path(codex_home).expanduser().resolve()

    env_value = os.environ.get("CODEX_HOME")
    if env_value:
        return Path(env_value).expanduser().resolve()

    return (Path.home() / ".codex").resolve()


def target_skill_dir(codex_home: str | os.PathLike[str] | None = None) -> Path:
    return resolve_codex_home(codex_home) / "skills" / SKILL_NAME


def install_skill(
    codex_home: str | os.PathLike[str] | None = None,
    *,
    force: bool = False,
) -> Path:
    source = bundled_skill_dir()
    if not source.exists():
        raise FileNotFoundError(f"Bundled skill not found: {source}")

    target = target_skill_dir(codex_home)
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists():
        if not force:
            raise FileExistsError(
                f"Target skill already exists: {target}. Re-run with --force to replace it."
            )
        shutil.rmtree(target)

    shutil.copytree(source, target)
    return target


def uninstall_skill(codex_home: str | os.PathLike[str] | None = None) -> bool:
    target = target_skill_dir(codex_home)
    if not target.exists():
        return False

    shutil.rmtree(target)
    return True
