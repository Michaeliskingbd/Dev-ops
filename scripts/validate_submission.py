#!/usr/bin/env python3
"""
validate_submission.py - Comprehensive Submission & Integrity Validator
Validates learner weekly submissions, reports, and file structures.
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')

# Sensitive regex patterns to block accidental secret leaks
SECRET_PATTERNS = [
    (re.compile(r'AKIA[0-9A-Z]{16}'), "AWS Access Key ID"),
    (re.compile(r'-----BEGIN (?:RSA|OPENSSH|DSA|EC) PRIVATE KEY-----'), "SSH/TLS Private Key"),
    (re.compile(r'ghp_[a-zA-Z0-9]{36}'), "GitHub Personal Access Token"),
    (re.compile(r'password\s*=\s*[\'"][^\'"]+[\'"]', re.IGNORECASE), "Plaintext password string")
]

REQUIRED_REPORT_SECTIONS = [
    "## 1. Administrative Information",
    "## 2. Time & Effort Tracking",
    "## 3. Topics Covered & Assignments Completed",
    "## 4. Practical Engineering Challenge Result",
    "## 5. Assessment Score & Outcomes",
    "## 6. Conceptual Mastery: In My Own Words",
    "## 7. What Remains Unclear or Confusing",
    "## 8. Major Problems Encountered & Debugging Methodology",
    "## 9. External Assistance & AI Disclosure",
    "## 10. Specific Items for Mentor Review",
    "## 11. Goals for Next Week & Self-Assessment Rating"
]

def scan_file_for_secrets(filepath):
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        for pattern, desc in SECRET_PATTERNS:
            if pattern.search(content):
                # Ignore this validation script itself
                if "validate_submission.py" in str(filepath):
                    continue
                return desc
    except Exception:
        pass
    return None

def validate_week_submission(repo_root, week_num):
    errors = []
    warnings = []
    
    week_str = f"week-{week_num:02d}"
    sub_dir = repo_root / "submissions" / week_str
    report_file = repo_root / "weekly-reports" / f"{week_str}-report.md"
    
    # Check submissions directory
    if not sub_dir.exists():
        errors.append(f"Submissions directory missing: {sub_dir}")
    else:
        # Check files inside submission directory
        sub_files = list(sub_dir.rglob("*"))
        real_files = [f for f in sub_files if f.is_file() and f.name != ".gitkeep" and f.name != "README.md"]
        if not real_files:
            warnings.append(f"No learner assignment deliverables found in {sub_dir.name}")
            
        for f in real_files:
            secret_detected = scan_file_for_secrets(f)
            if secret_detected:
                errors.append(f"CRITICAL SECURITY VIOLATION: {secret_detected} detected in {f.relative_to(repo_root)}")

    # Check weekly report
    if report_file.exists():
        report_text = report_file.read_text(encoding='utf-8', errors='ignore')
        for sec in REQUIRED_REPORT_SECTIONS:
            if sec not in report_text:
                warnings.append(f"Weekly report missing required section: '{sec}' in {report_file.name}")
        if "[Your Full Name]" in report_text or "[Start Date]" in report_text:
            warnings.append(f"Weekly report contains unedited placeholder text in {report_file.name}")
    else:
        warnings.append(f"Weekly report not yet created: {report_file.name}")

    return errors, warnings

def validate_json_files(repo_root):
    errors = []
    for p in repo_root.rglob("*.json"):
        if ".git" in p.parts:
            continue
        try:
            with open(p, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            errors.append(f"Invalid JSON syntax in {p.relative_to(repo_root)}: {e}")
    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate DevOps Mentorship Submissions")
    parser.add_argument("--week", type=int, help="Week number (1-24) to validate")
    parser.add_argument("--all", action="store_true", help="Validate all weeks")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    total_errors = []
    total_warnings = []

    # Syntax validation of JSON files
    json_errors = validate_json_files(repo_root)
    total_errors.extend(json_errors)

    if args.week:
        errs, warns = validate_week_submission(repo_root, args.week)
        total_errors.extend(errs)
        total_warnings.extend(warns)
    else:
        # Default to validating all
        for w in range(1, 25):
            errs, warns = validate_week_submission(repo_root, w)
            total_errors.extend(errs)
            total_warnings.extend(warns)

    print("================ VALIDATION SUMMARY ================")
    if total_warnings:
        print(f"⚠️  {len(total_warnings)} Status Warning(s) (Pending learner work):")
        for w in total_warnings[:8]:
            print(f"   [INFO] {w}")
        if len(total_warnings) > 8:
            print(f"   ... and {len(total_warnings) - 8} more.")

    if total_errors:
        print(f"\n❌ {len(total_errors)} Fatal Error(s):")
        for e in total_errors:
            print(f"   [ERROR] {e}")
        sys.exit(1)
    else:
        print("\n✅ All structural, syntax, and security validation checks passed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
