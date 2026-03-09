"""CLI entrypoint for nwave-codex."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .installer import install_skill, target_skill_dir, uninstall_skill


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nwave-codex",
        description="Install the bundled nWave skill pack into Codex.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser(
        "install", help="Install the bundled nwave skill into Codex."
    )
    install_parser.add_argument(
        "--codex-home",
        type=Path,
        help="Override CODEX_HOME (defaults to CODEX_HOME or ~/.codex).",
    )
    install_parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed skill directory.",
    )

    uninstall_parser = subparsers.add_parser(
        "uninstall", help="Remove the bundled nwave skill from Codex."
    )
    uninstall_parser.add_argument(
        "--codex-home",
        type=Path,
        help="Override CODEX_HOME (defaults to CODEX_HOME or ~/.codex).",
    )

    subparsers.add_parser("version", help="Print the nwave-codex version.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "version":
        print(__version__)
        return 0

    if args.command == "install":
        try:
            installed = install_skill(args.codex_home, force=args.force)
        except FileExistsError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        except FileNotFoundError as exc:
            print(str(exc), file=sys.stderr)
            return 1

        print(f"Installed $nwave to {installed}")
        return 0

    if args.command == "uninstall":
        removed = uninstall_skill(args.codex_home)
        location = target_skill_dir(args.codex_home)
        if removed:
            print(f"Removed $nwave from {location}")
        else:
            print(f"No installed $nwave skill found at {location}")
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
