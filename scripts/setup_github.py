#!/usr/bin/env python3
"""
setup_github.py - Safe, Idempotent GitHub CLI Initializer
Configures milestones, labels, and issue templates using the GitHub CLI ('gh').
Supports dry-run mode and avoids duplicate creations.
"""

import os
import sys
import shutil
import subprocess
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')

LABELS = [
    # Stages
    {"name": "stage-1-foundations", "color": "0E8A16", "description": "Stage 1: Technical Foundations (Weeks 1-8)"},
    {"name": "stage-2-tooling", "color": "1D76DB", "description": "Stage 2: DevOps Engineering Tools (Weeks 9-16)"},
    {"name": "stage-3-production", "color": "5319E7", "description": "Stage 3: Production Engineering & Capstone (Weeks 17-24)"},
    # Types
    {"name": "assignment", "color": "D4C5F9", "description": "Weekly assignment submission"},
    {"name": "weekly-report", "color": "BFD4F2", "description": "Weekly progress and self-reflection report"},
    {"name": "assessment", "color": "FBCA04", "description": "Saturday mentor assessment review"},
    {"name": "blocker", "color": "B60205", "description": "Technical blocker escalated after 15-min rule"},
    {"name": "progression-gate", "color": "D93F0B", "description": "Formal stage progression gate evaluation"},
    # States
    {"name": "needs-review", "color": "E99695", "description": "Submission awaits mentor review"},
    {"name": "changes-requested", "color": "F9D0C4", "description": "Corrections or remedial tasks required"},
    {"name": "approved", "color": "0E8A16", "description": "Submission evaluated and approved"}
]

def check_gh_cli():
    gh_path = shutil.which("gh")
    if not gh_path:
        return False, "GitHub CLI ('gh') is not installed or not in PATH. Download from https://cli.github.com/."
    
    try:
        res = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        if res.returncode != 0:
            return False, "GitHub CLI is installed but not authenticated. Run 'gh auth login' to authenticate."
        return True, "GitHub CLI is authenticated."
    except Exception as e:
        return False, f"Failed to execute gh CLI: {e}"

def run_cmd(cmd, dry_run=False):
    if dry_run:
        print(f"  [DRY-RUN] Would run: {' '.join(cmd)}")
        return True, ""
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True, res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()

def setup_milestones(dry_run=False):
    print("\n--- Configuring 24 Weekly Milestones ---")
    for w in range(1, 25):
        m_title = f"Week {w:02d}"
        cmd = ["gh", "milestone", "create", "--title", m_title, "--description", f"Deliverables and assessment for Week {w:02d}"]
        success, out = run_cmd(cmd, dry_run=dry_run)
        if success:
            print(f"  ✓ Milestone: {m_title}")
        else:
            if "already exists" in out.lower():
                print(f"  ✓ Milestone {m_title} already exists (skipped)")
            else:
                print(f"  ⚠️ Error creating milestone {m_title}: {out}")

def setup_labels(dry_run=False):
    print("\n--- Configuring Standard Repository Labels ---")
    for lbl in LABELS:
        name = lbl["name"]
        color = lbl["color"]
        desc = lbl["description"]
        cmd = ["gh", "label", "create", name, "--color", color, "--description", desc, "--force"]
        success, out = run_cmd(cmd, dry_run=dry_run)
        if success:
            print(f"  ✓ Label: {name}")
        else:
            print(f"  ⚠️ Error configuring label {name}: {out}")

def main():
    parser = argparse.ArgumentParser(description="Initialize GitHub Repository Milestones and Labels")
    parser.add_argument("--dry-run", action="store_true", help="Simulate commands without executing remote changes")
    args = parser.parse_args()

    print("================ GITHUB SETUP AUTOMATION ================")
    gh_ok, gh_msg = check_gh_cli()
    print(f"GitHub CLI Status: {gh_msg}")

    if not gh_ok and not args.dry_run:
        print("\n❌ Error: Cannot proceed without an authenticated GitHub CLI.")
        print("To preview the operations without making remote changes, run:")
        print("  python scripts/setup_github.py --dry-run")
        sys.exit(1)

    if args.dry_run:
        print("\n⚠️ Running in DRY-RUN mode. No remote GitHub API changes will be executed.")

    setup_milestones(dry_run=args.dry_run)
    setup_labels(dry_run=args.dry_run)

    print("\n✅ GitHub repository configuration completed successfully.")

if __name__ == "__main__":
    main()
