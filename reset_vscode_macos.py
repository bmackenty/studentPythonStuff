#!/usr/bin/env python3
"""
reset_vscode_macos.py

Completely remove the normal (stable) Visual Studio Code installation and
its LOCAL per-user state from macOS.

Designed for classroom/support use when VS Code is behaving in a way that is
hard to diagnose and you want to return it to a first-run state.

What this script removes
------------------------
For the selected macOS user, it removes:

* Visual Studio Code.app (unless --keep-app is used)
* VS Code user settings and profiles
* Installed VS Code extensions
* Snippets, keybindings, workspace history/state, global storage, logs, etc.
  that are stored inside VS Code's user-data directory
* VS Code caches
* VS Code preferences (.plist files)
* VS Code HTTP/WebKit storage
* VS Code saved application state
* VS Code-specific crash/support remnants covered by the path patterns below
* A common `code` command-line symlink, but ONLY when the symlink clearly
  points into the Visual Studio Code application bundle

What this script deliberately DOES NOT remove
----------------------------------------------
* Student source code or project folders
* `.vscode` directories inside projects, because they may contain legitimate
  tasks.json, launch.json, settings.json, and extension recommendations
* Git configuration, SSH keys, Python installations, Node.js, Java, compilers,
  Homebrew packages, or other developer tools
* Remote VS Code Server installations on SSH hosts/containers
* Cloud copies of settings/extensions stored by VS Code Settings Sync
* macOS Keychain entries

Safety model
------------
The script is DRY-RUN by default. Nothing is deleted unless --execute is
provided. In interactive use it also requires typing ERASE, unless --yes is
supplied.

Examples
--------
Preview what would be removed for the current user:

    python3 reset_vscode_macos.py

Actually erase VS Code for the current user:

    python3 reset_vscode_macos.py --execute

Non-interactive execution:

    python3 reset_vscode_macos.py --execute --yes

If administrator privileges are needed to delete /Applications/Visual Studio
Code.app, run with sudo. The script detects SUDO_USER so it still cleans the
student's home folder instead of /var/root:

    sudo python3 reset_vscode_macos.py --execute

Explicitly target another local user (root/admin required):

    sudo python3 reset_vscode_macos.py --user studentname --execute

Reset user data but leave the application installed:

    python3 reset_vscode_macos.py --keep-app --execute

Also remove VS Code Insiders state/application:

    python3 reset_vscode_macos.py --include-insiders --execute

Remove the .vscode folder from ONE specific project as part of the reset:

    python3 reset_vscode_macos.py --project ~/Documents/MyProject --execute

Tested for Python 3 syntax; uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import os
import pwd
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class TargetUser:
    """Information about the macOS account whose VS Code state is removed."""

    name: str
    uid: int
    home: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Reset Visual Studio Code on macOS by removing its application "
            "and local per-user data. Dry-run is the default."
        )
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually delete files. Without this option, only show a preview.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the interactive ERASE confirmation. Intended for automation.",
    )
    parser.add_argument(
        "--user",
        metavar="USERNAME",
        help=(
            "macOS account to clean. By default, use SUDO_USER when invoked "
            "through sudo; otherwise use the current user."
        ),
    )
    parser.add_argument(
        "--keep-app",
        action="store_true",
        help="Reset VS Code's user data but do not delete Visual Studio Code.app.",
    )
    parser.add_argument(
        "--include-insiders",
        action="store_true",
        help="Also remove Visual Studio Code - Insiders and its local state.",
    )
    parser.add_argument(
        "--project",
        action="append",
        default=[],
        metavar="PATH",
        help=(
            "Also remove PATH/.vscode for this specific project. May be supplied "
            "more than once. Project .vscode folders are never removed otherwise."
        ),
    )
    return parser.parse_args()


def get_target_user(requested_username: str | None) -> TargetUser:
    """Resolve the account that should be cleaned.

    A common administrative mistake is running a cleanup script with sudo and
    then using Path.home(), which becomes /var/root. We explicitly prefer
    SUDO_USER so `sudo python3 ...` still cleans the invoking student's account.
    """

    if requested_username:
        username = requested_username
    elif os.geteuid() == 0 and os.environ.get("SUDO_USER"):
        username = os.environ["SUDO_USER"]
    else:
        username = pwd.getpwuid(os.getuid()).pw_name

    try:
        record = pwd.getpwnam(username)
    except KeyError as exc:
        raise SystemExit(f"ERROR: macOS user {username!r} does not exist.") from exc

    # A non-root user must not be allowed to target some other account.
    if os.geteuid() != 0 and record.pw_uid != os.getuid():
        raise SystemExit(
            "ERROR: --user may target another account only when this script is "
            "run as root/admin."
        )

    home = Path(record.pw_dir).expanduser()
    if not home.is_absolute() or str(home) in {"/", "/var", "/Users"}:
        raise SystemExit(f"ERROR: refusing suspicious home directory: {home}")

    return TargetUser(name=username, uid=record.pw_uid, home=home)


def expand_known_paths(home: Path, include_insiders: bool) -> set[Path]:
    """Return known VS Code state paths for a user's home directory.

    The two most important stable locations are:
      ~/Library/Application Support/Code
      ~/.vscode

    Additional macOS-specific caches/preferences are included so the cleanup is
    useful for difficult support cases rather than merely removing settings.json.
    """

    paths: set[Path] = {
        home / "Library/Application Support/Code",
        home / ".vscode",
        home / "Library/Logs/Code",
        home / "Library/Saved Application State/com.microsoft.VSCode.savedState",
    }

    # Prefix globs catch helper-process variants without recursively searching
    # the student's entire Library directory.
    glob_patterns = [
        "Library/Caches/com.microsoft.VSCode*",
        "Library/Preferences/com.microsoft.VSCode*",
        "Library/Preferences/ByHost/com.microsoft.VSCode*",
        "Library/HTTPStorages/com.microsoft.VSCode*",
        "Library/WebKit/com.microsoft.VSCode*",
        "Library/Cookies/com.microsoft.VSCode*",
        "Library/Application Support/com.microsoft.VSCode*",
        "Library/Application Support/CrashReporter/Code*",
        "Library/Logs/DiagnosticReports/Code*",
        "Library/Logs/DiagnosticReports/Visual Studio Code*",
    ]

    for pattern in glob_patterns:
        paths.update(home.glob(pattern))

    if include_insiders:
        paths.update(
            {
                home / "Library/Application Support/Code - Insiders",
                home / ".vscode-insiders",
                home
                / "Library/Saved Application State/com.microsoft.VSCodeInsiders.savedState",
            }
        )

        insider_patterns = [
            "Library/Caches/com.microsoft.VSCodeInsiders*",
            "Library/Preferences/com.microsoft.VSCodeInsiders*",
            "Library/Preferences/ByHost/com.microsoft.VSCodeInsiders*",
            "Library/HTTPStorages/com.microsoft.VSCodeInsiders*",
            "Library/WebKit/com.microsoft.VSCodeInsiders*",
            "Library/Cookies/com.microsoft.VSCodeInsiders*",
            "Library/Application Support/com.microsoft.VSCodeInsiders*",
        ]
        for pattern in insider_patterns:
            paths.update(home.glob(pattern))

    return paths


def app_paths(home: Path, include_insiders: bool) -> set[Path]:
    """Return normal system-wide and per-user application bundle locations."""

    paths = {
        Path("/Applications/Visual Studio Code.app"),
        home / "Applications/Visual Studio Code.app",
    }

    if include_insiders:
        paths.update(
            {
                Path("/Applications/Visual Studio Code - Insiders.app"),
                home / "Applications/Visual Studio Code - Insiders.app",
            }
        )

    return paths


def project_vscode_paths(project_args: Iterable[str], home: Path) -> set[Path]:
    """Resolve explicitly requested project .vscode directories.

    We never search the home directory for these because blindly removing every
    project .vscode folder can destroy useful project configuration.
    """

    result: set[Path] = set()
    for raw in project_args:
        # Expand environment variables, but interpret a leading ~ as the TARGET
        # user's home even when the script itself is running under sudo/root.
        expanded = os.path.expandvars(raw)
        if expanded == "~":
            expanded = str(home)
        elif expanded.startswith("~/"):
            expanded = str(home / expanded[2:])

        project = Path(expanded)
        if not project.is_absolute():
            project = Path.cwd() / project
        project = project.resolve(strict=False)

        # Guard against catastrophic inputs such as --project / or --project ~.
        forbidden = {Path("/"), home.resolve(strict=False)}
        if project in forbidden:
            raise SystemExit(
                f"ERROR: refusing --project {raw!r}; specify an individual project."
            )

        result.add(project / ".vscode")

    return result


def path_lexists(path: Path) -> bool:
    """Like exists(), but True for broken symbolic links as well."""

    return os.path.lexists(path)


def human_size(path: Path) -> int:
    """Best-effort byte count for a file/directory without following symlinks."""

    try:
        if path.is_symlink() or path.is_file():
            return path.lstat().st_size
        if path.is_dir():
            total = 0
            for root, dirs, files in os.walk(path, followlinks=False):
                root_path = Path(root)
                # Avoid descending through symlinked directories.
                dirs[:] = [d for d in dirs if not (root_path / d).is_symlink()]
                for filename in files:
                    item = root_path / filename
                    try:
                        total += item.lstat().st_size
                    except OSError:
                        pass
            return total
    except OSError:
        pass
    return 0


def format_bytes(value: int) -> str:
    """Render a byte count in a compact human-readable form."""

    amount = float(value)
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if amount < 1024.0 or unit == "TiB":
            return f"{amount:.1f} {unit}"
        amount /= 1024.0
    return f"{value} B"


def terminate_vscode_processes(uid: int, dry_run: bool) -> None:
    """Stop VS Code processes belonging to the target user.

    Removing Electron application data while VS Code is still running can let
    the application recreate state as it exits. We therefore terminate processes
    whose command line contains a VS Code application-bundle path.
    """

    patterns = [
        r"/Visual Studio Code\.app/",
        r"/Visual Studio Code - Insiders\.app/",
    ]

    for pattern in patterns:
        if dry_run:
            print(f"[DRY-RUN] Would terminate target-user processes matching: {pattern}")
            continue

        subprocess.run(
            ["pkill", "-TERM", "-u", str(uid), "-f", pattern],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )

    if dry_run:
        return

    time.sleep(1.0)

    for pattern in patterns:
        subprocess.run(
            ["pkill", "-KILL", "-u", str(uid), "-f", pattern],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )


def remove_path(path: Path, dry_run: bool) -> tuple[bool, str | None]:
    """Remove one path without following directory symlinks.

    Returns (removed_or_would_remove, error_message).
    """

    if not path_lexists(path):
        return False, None

    if dry_run:
        return True, None

    try:
        if path.is_symlink() or path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
        else:
            # Handles uncommon filesystem objects conservatively.
            path.unlink()
        return True, None
    except PermissionError:
        return False, "permission denied"
    except OSError as exc:
        return False, str(exc)


def code_cli_candidates(home: Path, include_insiders: bool) -> list[tuple[Path, tuple[str, ...]]]:
    """Return possible `code` CLI links and the app names they may point into."""

    stable_markers = ("Visual Studio Code.app",)
    insider_markers = ("Visual Studio Code - Insiders.app",)

    candidates: list[tuple[Path, tuple[str, ...]]] = [
        (Path("/usr/local/bin/code"), stable_markers),
        (Path("/opt/homebrew/bin/code"), stable_markers),
        (home / ".local/bin/code", stable_markers),
        (home / "bin/code", stable_markers),
    ]

    if include_insiders:
        candidates.extend(
            [
                (Path("/usr/local/bin/code-insiders"), insider_markers),
                (Path("/opt/homebrew/bin/code-insiders"), insider_markers),
                (home / ".local/bin/code-insiders", insider_markers),
                (home / "bin/code-insiders", insider_markers),
            ]
        )

    return candidates


def is_vscode_cli_symlink(path: Path, markers: tuple[str, ...]) -> bool:
    """Only approve a CLI path for deletion if it is clearly a VS Code symlink."""

    if not path.is_symlink():
        return False
    try:
        target_text = os.readlink(path)
    except OSError:
        return False
    return any(marker in target_text for marker in markers)


def main() -> int:
    args = parse_args()

    if sys.platform != "darwin":
        print("ERROR: This script is intentionally limited to macOS.", file=sys.stderr)
        return 2
    target = get_target_user(args.user)
    dry_run = not args.execute

    print("Visual Studio Code macOS reset")
    print("=" * 34)
    print(f"Target user : {target.name} (uid {target.uid})")
    print(f"Home        : {target.home}")
    print(f"Mode        : {'DRY-RUN — nothing will be deleted' if dry_run else 'EXECUTE'}")
    print(f"Application : {'keep installed' if args.keep_app else 'remove'}")
    print(f"Insiders    : {'include' if args.include_insiders else 'leave untouched'}")
    print()

    paths = expand_known_paths(target.home, args.include_insiders)
    paths.update(project_vscode_paths(args.project, target.home))

    if not args.keep_app:
        paths.update(app_paths(target.home, args.include_insiders))

    # Only include command-line launchers when they are symbolic links whose
    # target explicitly points into the corresponding VS Code application.
    for cli_path, markers in code_cli_candidates(target.home, args.include_insiders):
        if is_vscode_cli_symlink(cli_path, markers):
            paths.add(cli_path)

    existing = sorted(
        (p for p in paths if path_lexists(p)),
        key=lambda p: str(p).lower(),
    )

    if not existing:
        print("No matching local VS Code files were found.")
        return 0

    sizes = {path: human_size(path) for path in existing}
    total_size = sum(sizes.values())

    print("Matched paths:")
    for path in existing:
        print(f"  {format_bytes(sizes[path]):>10}  {path}")
    print(f"\nApproximate total: {format_bytes(total_size)}")

    if dry_run:
        print("\nDry-run complete. Re-run with --execute to perform the deletion.")
        return 0

    if not args.yes:
        print("\nWARNING: This permanently removes the paths shown above.")
        answer = input('Type exactly "ERASE" to continue: ')
        if answer != "ERASE":
            print("Cancelled. Nothing was deleted.")
            return 1

    print("\nStopping VS Code processes...")
    terminate_vscode_processes(target.uid, dry_run=False)

    print("Removing files...")
    removed = 0
    failures: list[tuple[Path, str]] = []

    # Remove deeper paths first, which also makes output deterministic.
    for path in sorted(existing, key=lambda p: (len(p.parts), str(p)), reverse=True):
        did_remove, error = remove_path(path, dry_run=False)
        if did_remove:
            removed += 1
            print(f"  removed: {path}")
        elif error:
            failures.append((path, error))
            print(f"  FAILED : {path} ({error})", file=sys.stderr)

    print()
    if failures:
        print(
            f"Finished with {len(failures)} failure(s). "
            "If /Applications/Visual Studio Code.app was permission-denied, "
            "run the same command with sudo.",
            file=sys.stderr,
        )
        return 3

    print(f"Reset complete. Removed {removed} path(s).")
    print(
        "For the cleanest diagnostic reinstall, launch VS Code once before "
        "enabling Settings Sync or reinstalling extensions."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
