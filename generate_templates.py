#!/usr/bin/env python3
"""
Project / Program Management Toolkit – Template Generator

Usage:
    python generate_templates.py            # generate all templates in ./templates
    python generate_templates.py --out my_templates
    python generate_templates.py --only raid_log raci_matrix
"""

import argparse
from pathlib import Path
from textwrap import dedent

TEMPLATES = {
    "raid_log": {
        "filename": "raid_log.csv",
        "description": "RAID log (Risks, Assumptions, Issues, Dependencies)",
        "content": dedent("""\
            ID,Date Logged,Category (Risk/Assumption/Issue/Dependency),Title,Description,Impact (Low/Med/High),Probability (Low/Med/High),Owner,Target Resolution Date,Status (Open/Monitoring/Closed),Mitigation / Action Plan,Comments
            1,,Risk,"Example: Vendor delay","Describe the risk here",High,Medium,Owner Name,,Open,"High-level mitigation plan",""
        """),
    },
    "raci_matrix": {
        "filename": "raci_matrix.csv",
        "description": "RACI matrix for roles & responsibilities",
        "content": dedent("""\
            Task / Deliverable,Project Manager,Sponsor,Tech Lead,Business Owner,QA Lead
            Define requirements,R/A,C,I,I,I
            Design solution,R,C,A,I,I
            Build & config,I,I,R/A,C,I
            Testing,I,I,C,I,R/A
            Go-live decision,C,A,R,C,I
        """),
    },
    "project_charter": {
        "filename": "project_charter.md",
        "description": "Project Charter template (Markdown)",
        "content": dedent("""\
            # Project Charter

            ## 1. Project Overview
            - **Project Name**: 
            - **Sponsor**: 
            - **Project Manager**: 
            - **Date**: 

            ### 1.1 Background
            Brief context and why this project exists.

            ### 1.2 Objectives & Success Criteria
            - Objective 1:
            - Objective 2:
            - Success will be measured by:

            ## 2. Scope

            ### 2.1 In-Scope
            - Item 1
            - Item 2

            ### 2.2 Out-of-Scope
            - Item 1
            - Item 2

            ## 3. Key Deliverables & Milestones
            | Deliverable | Owner | Due Date | Status |
            |------------|-------|----------|--------|
            |            |       |          |        |

            ## 4. Stakeholders
            | Name | Role | Department | Interest / Influence |
            |------|------|------------|----------------------|
            |      |      |            |                      |

            ## 5. Assumptions & Constraints
            - Assumption 1
            - Constraint 1

            ## 6. Risks (High-Level)
            - Risk 1 – description and potential impact

            ## 7. Budget (High-Level)
            - Estimated budget:
            - Key cost categories:

            ## 8. Governance & Communication
            - Meeting cadence:
            - Decision-making process:
            - Reporting (status, steering committee, etc.):

            ## 9. Approvals
            - Sponsor:
            - PMO:
            - Date:
        """),
    },
    "sprint_board": {
        "filename": "sprint_board.csv",
        "description": "Sprint board (backlog / in progress / done) as CSV",
        "content": dedent("""\
            ID,Title,Description,Status (Backlog/In Progress/Blocked/Done),Assignee,Story Points,Priority (Low/Med/High),Sprint,Start Date,Due Date,Tags
            US-1,"Sample user story","As a <role>, I want <capability> so that <benefit>","Backlog",,,Medium,,,
            BUG-1,"Sample bug","Describe bug","Backlog",,,High,,,
        """),
    },
    "weekly_status": {
        "filename": "weekly_status.md",
        "description": "Weekly status report (Markdown)",
        "content": dedent("""\
            # Weekly Status Report

            - **Project**: 
            - **Reporting Period**: 
            - **Prepared By**: 
            - **Overall RAG**: 🟢 / 🟡 / 🔴

            ## 1. Executive Summary
            2–3 bullet points summarizing this week.

            ## 2. Progress This Week
            - Item 1
            - Item 2
            - Item 3

            ## 3. Plan for Next Week
            - Item 1
            - Item 2

            ## 4. Risks & Issues (Top 3)
            | ID | Type (Risk/Issue) | Description | Impact | Owner | Status | Mitigation / Action |
            |----|-------------------|-------------|--------|-------|--------|---------------------|
            |    |                   |             |        |       |        |                     |

            ## 5. Decisions Needed / Escalations
            - Decision / Escalation 1
            - Decision / Escalation 2

            ## 6. Dependencies
            - Dependency 1
            - Dependency 2
        """),
    },
    "executive_summary": {
        "filename": "executive_summary.md",
        "description": "1-page Executive Summary template (Markdown)",
        "content": dedent("""\
            # Executive Summary

            ## 1. Context
            Brief description of the initiative, why it exists, and how it ties to business strategy.

            ## 2. Key Outcomes & KPIs
            - Outcome 1 (KPI / Target)
            - Outcome 2 (KPI / Target)

            ## 3. Current Status
            - Overall status: 🟢 / 🟡 / 🔴
            - Schedule: On track / At risk / Delayed
            - Budget: On track / Over / Under

            ## 4. Highlights (Last 2–4 Weeks)
            - Highlight 1
            - Highlight 2

            ## 5. Risks & Issues – What Executives Should Know
            - Risk / Issue 1 – description, impact, mitigation
            - Risk / Issue 2 – description, impact, mitigation

            ## 6. Decisions / Support Needed
            - Decision 1
            - Decision 2

            ## 7. Next Steps (4–8 Weeks)
            - Step 1
            - Step 2
        """),
    },
}


def write_template(output_dir: Path, key: str):
    meta = TEMPLATES[key]
    filepath = output_dir / meta["filename"]
    filepath.write_text(meta["content"], encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Generate PM toolkit templates.")
    parser.add_argument(
        "--out",
        type=str,
        default="templates",
        help="Output directory for templates (default: ./templates)",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        help=f"Generate only specific templates (options: {', '.join(TEMPLATES.keys())})",
    )
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.only:
        keys = [k for k in args.only if k in TEMPLATES]
        if not keys:
            print("No valid templates specified. Exiting.")
            return
    else:
        keys = list(TEMPLATES.keys())

    print(f"Generating templates in: {out_dir.resolve()}")
    for key in keys:
        path = write_template(out_dir, key)
        print(f"  - {key}: {path.name}")

    print("\nDone. You can now open the templates in Excel, Notion, or your PM tool of choice.")


if __name__ == "__main__":
    main()
