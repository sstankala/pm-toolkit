#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from pathlib import Path

TEMPLATE_DIR = Path("templates")

TEMPLATE_FILES = {
    "RAID Log": ("raid_log.csv", "csv"),
    "RACI Matrix": ("raci_matrix.csv", "csv"),
    "Project Charter": ("project_charter.md", "md"),
    "Sprint Board": ("sprint_board.csv", "csv"),
    "Weekly Status Report": ("weekly_status.md", "md"),
    "Executive Summary": ("executive_summary.md", "md"),
}

st.set_page_config(
    page_title="PM Toolkit – Templates",
    layout="wide",
)

st.title("📦 Project / Program Management Toolkit")
st.caption("Reusable templates for PMO excellence, Agile/Waterfall delivery, and executive reporting.")

st.sidebar.header("Templates")
selected = st.sidebar.selectbox(
    "Choose a template",
    list(TEMPLATE_FILES.keys()),
)

# Ensure templates exist
if not TEMPLATE_DIR.exists():
    st.warning(
        "`templates/` folder not found. Run `python generate_templates.py` first.",
        icon="⚠️",
    )
else:
    filename, ftype = TEMPLATE_FILES[selected]
    path = TEMPLATE_DIR / filename

    if not path.exists():
        st.error(f"`{filename}` not found in `templates/`. Generate templates first.")
    else:
        st.subheader(selected)

        if ftype == "csv":
            df = pd.read_csv(path)
            st.markdown("**Preview as table**")
            st.dataframe(df, use_container_width=True)

            with st.expander("Show raw CSV"):
                st.code(path.read_text(encoding="utf-8"), language="csv")

        elif ftype == "md":
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            tab1, tab2 = st.tabs(["Rendered", "Raw Markdown"])
            with tab1:
                st.markdown(content)
            with tab2:
                st.code(content, language="markdown")

st.sidebar.markdown("---")
st.sidebar.markdown(
    "* Check Github https://github.com/sstankala/pm-toolkit |  " \
    "Create templates using python generate_templates.py; " \
    "fill in content per your project needs ")
    