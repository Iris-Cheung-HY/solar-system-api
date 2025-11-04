"""Helper script to install a specific pylint version using pip.

Provides a function `install_pylint(version='4.0.2', upgrade=False, user=False, quiet=False)`
that invokes pip via the running Python executable. Also provides a small CLI.
"""
from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from typing import Sequence


def install_pylint(version: str = "4.0.2", *, upgrade: bool = False, user: bool = False, quiet: bool = False) -> subprocess.CompletedProcess:
    """Install the specified pylint version using pip.

    Args:
        version: The pylint version to install (default: "4.0.2").
        upgrade: If True, pass --upgrade to pip.
        user: If True, pass --user to pip.
        quiet: If True, pass --quiet to pip.

    Returns:
        The CompletedProcess returned by subprocess.run.

    Raises:
        subprocess.CalledProcessError: if pip install exits with a non-zero status.
    """
    pip_args: list[str] = [sys.executable, "-m", "pip", "install", f"pylint=={version}"]
    if upgrade:
        pip_args.append("--upgrade")
    if user:
        pip_args.append("--user")
    if quiet:
        pip_args.append("--quiet")

    # Use check=True so CalledProcessError is raised on failure;
    # capture_output=False so user sees pip output in the invoking terminal by default.
    return subprocess.run(pip_args, check=True)


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install a specific pylint version using pip.")
    parser.add_argument("--version", "-v", default="4.0.2", help="pylint version to install (default: 4.0.2)")
    parser.add_argument("--upgrade", action="store_true", help="pass --upgrade to pip")
    parser.add_argument("--user", action="store_true", help="pass --user to pip")
    parser.add_argument("--quiet", action="store_true", help="pass --quiet to pip")
    return parser.parse_args(argv)


def _main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        print("Running:", shlex.join([sys.executable, "-m", "pip", "install", f"pylint=={args.version}"]))
        install_pylint(args.version, upgrade=args.upgrade, user=args.user, quiet=args.quiet)
        print(f"Successfully installed pylint=={args.version}")
        return 0
    except subprocess.CalledProcessError as exc:
        print(f"Failed to install pylint=={args.version}: {exc}", file=sys.stderr)
        return exc.returncode if isinstance(exc.returncode, int) else 1


if __name__ == "__main__":
    raise SystemExit(_main())
