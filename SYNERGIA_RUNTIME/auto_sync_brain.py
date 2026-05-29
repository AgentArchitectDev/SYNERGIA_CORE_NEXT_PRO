import os
import subprocess
from datetime import datetime

# =============================
# BASE CONFIG
# =============================
BASE_PATH = "/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO"

REPOS = [
    "synergia-ai",
    "synergia-api",
    "synergia-cms",
    "synergia-core",
    "synergia-render",
    "synergia-state",
    "synergia-outputs",
    "synergia-templates"
]

CHECKPOINT_PATH = os.path.join(BASE_PATH, "SYNERGIA_RUNTIME", "CHECKPOINTS")

os.makedirs(CHECKPOINT_PATH, exist_ok=True)


# =============================
# UTILS
# =============================
def repo_path(repo):
    return os.path.join(BASE_PATH, repo)


def repo_exists(path):
    return os.path.exists(path) and os.path.isdir(path)


def run_git(cmd, path):
    try:
        subprocess.run(cmd, cwd=path, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"[GIT ERROR] {e}")


# =============================
# CHECKPOINT SYSTEM
# =============================
def create_checkpoint(event="AUTO EVENT"):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(CHECKPOINT_PATH, f"checkpoint_{ts}.md")

    content = f"""# SYNERGIA AUTO CHECKPOINT

Date: {datetime.now()}

Event: {event}

System: SYNERGIA CORE NEXT PRO
Mode: MAQ2
Status: ACTIVE

Repos detected:
"""

    for r in REPOS:
        path = repo_path(r)
        status = "OK" if repo_exists(path) else "MISSING"
        content += f"- {r}: {status}\n"

    with open(file_path, "w") as f:
        f.write(content)

    print(f"[CHECKPOINT CREATED] {file_path}")
    return file_path


# =============================
# GIT AUTO FIX + SYNC
# =============================
def git_sync(repo):
    path = repo_path(repo)

    if not repo_exists(path):
        print(f"[SKIP] {repo} (not found)")
        return

    print(f"[SYNC] {repo}")

    # ADD
    run_git(["git", "add", "."], path)

    # COMMIT
    run_git(["git", "commit", "-m", "auto-sync synergia brain"], path)

    # PUSH (safe mode)
    try:
        subprocess.run(["git", "push"], cwd=path, check=False)
    except Exception:
        print(f"[PUSH ERROR] {repo}")

    print(f"[SYNC OK] {repo}")


# =============================
# FIX GIT UPSTREAM (ONE TIME SAFE)
# =============================
def ensure_git_ready(repo):
    path = repo_path(repo)

    if not repo_exists(path):
        return

    # try safe upstream fix
    subprocess.run(
        ["git", "push", "--set-upstream", "origin", "main"],
        cwd=path,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


# =============================
# MAIN ENGINE
# =============================
def run_auto_sync(event="runtime_event"):

    print("\n🚀 SYNERGIA AUTO SYNC BRAIN v2")
    print("=" * 50)

    checkpoint = create_checkpoint(event)

    # fix git upstream silently
    for repo in REPOS:
        ensure_git_ready(repo)

    # sync repos
    for repo in REPOS:
        git_sync(repo)

    print("\n✅ AUTO SYNC COMPLETED")
    print(f"📦 CHECKPOINT: {checkpoint}")

    return checkpoint


# =============================
# ENTRY POINT
# =============================
if __name__ == "__main__":
    run_auto_sync("manual_trigger")
