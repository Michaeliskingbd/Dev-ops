#!/usr/bin/env python3
"""
generate_progress.py - Reads structured learner records and generates the progress dashboard.
"""

import os
import sys
import json
import argparse
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='backslashreplace')

def load_learner_data(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_markdown_report(data):
    learner = data.get("learner", {})
    progress = data.get("progress", {})
    competencies = data.get("competencies", {})
    
    total_weeks = 24
    completed_weeks = progress.get("completed_weeks", 0)
    total_assignments = 120
    completed_assignments = progress.get("completed_assignments", 0)
    completion_pct = (completed_assignments / total_assignments) * 100
    
    avg_score = progress.get("average_assessment_score", 0.0)
    current_stage = progress.get("current_stage", 1)
    
    lines = [
        "# Automated Learner Progress Dashboard",
        "",
        f"> **Generated at:** {data.get('last_updated', 'N/A')}",
        f"> **Data Source:** `{data.get('record_id', 'SAMPLE-RECORD')}` *(Status: {data.get('sample_notice', 'Official Record')})*",
        "",
        "---",
        "",
        "## 👤 Learner Profile",
        f"- **Name:** {learner.get('name', 'N/A')}",
        f"- **Mentor:** {learner.get('mentor', 'N/A')}",
        f"- **Current Week:** Week {progress.get('current_week', 1):02d}",
        f"- **Current Stage:** Stage {current_stage} ({progress.get('stage_name', 'Technical Foundations')})",
        f"- **Total Learning Hours Logged:** {progress.get('total_hours_logged', 0)} hrs",
        "",
        "---",
        "",
        "## 📊 Completion Metrics",
        "",
        "| Metric | Completed | Total | Percentage |",
        "|---|:---:|:---:|:---:|",
        f"| **Curriculum Weeks** | {completed_weeks} | {total_weeks} | {(completed_weeks/total_weeks)*100:.1f}% |",
        f"| **Assignments** | {completed_assignments} | {total_assignments} | {completion_pct:.1f}% |",
        f"| **Average Score** | {avg_score:.1f} pts | 100 pts | Pass Bar >= 80.0 |",
        "",
        "---",
        "",
        "## 🚪 Progression Gates Status",
        "",
        "| Gate | Stage | Status | Evaluation Date | Score | Sign-Off |",
        "|---|---|:---:|:---:|:---:|:---:|"
    ]
    
    for gate in progress.get("progression_gates", []):
        lines.append(f"| **{gate['name']}** | Stage {gate['stage']} | `{gate['status']}` | {gate.get('date', 'Pending')} | {gate.get('score', 'N/A')} | {gate.get('signed_by', 'Pending')} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🧠 Competency Tracking Matrix",
        "",
        "| Domain | Skill | Status | Demonstrated Evidence |",
        "|---|---|:---:|---|"
    ])

    for domain, skills in competencies.items():
        for skill_name, detail in skills.items():
            status_emoji = {
                "INDEPENDENT": "🟢 INDEPENDENT",
                "GUIDED": "🟡 GUIDED",
                "LEARNING": "🔵 LEARNING",
                "NEEDS_REASSESSMENT": "🔴 NEEDS_REASSESSMENT",
                "NOT_STARTED": "⚪ NOT_STARTED"
            }.get(detail.get("status"), detail.get("status"))
            
            lines.append(f"| {domain.title()} | {skill_name} | {status_emoji} | {detail.get('evidence', 'None')} |")

    lines.append("")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Generate Learner Progress Dashboard")
    parser.add_argument("--data", default="scripts/data/sample_learner_progress.json", help="Path to structured learner data JSON")
    parser.add_argument("--output", help="Optional output markdown file path")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    data_path = (repo_root / args.data) if not Path(args.data).is_absolute() else Path(args.data)

    if not data_path.exists():
        print(f"Error: Data file not found at {data_path}")
        sys.exit(1)

    data = load_learner_data(data_path)
    report_md = generate_markdown_report(data)

    if args.output:
        out_path = (repo_root / args.output) if not Path(args.output).is_absolute() else Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report_md, encoding="utf-8")
        print(f"✅ Dashboard generated successfully at: {out_path}")
    else:
        print(report_md)

if __name__ == "__main__":
    main()
