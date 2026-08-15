# pages/Olympiad_Problems.py

import streamlit as st
from ui import apply_global_styles, home_nav
from streamlit.errors import StreamlitSecretNotFoundError
import pandas as pd
import json
import os
import shutil
from pathlib import Path
apply_global_styles()

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------
TAGS = [
    "Chaos & Order",
    "Table",
    "Equations",
    "Special Format",
    "Time",
    "Overcounting",
    "Subtractive systems",
    "Body Part Counting",
    "Morphological Changes",
    "Easy",
    "Medium",
    "Hard",
    "APLO",
    "IOL",
    "UKLO",
    "HKLO",
    "PLO",
    "NACLO",
]

try:
    ADMIN_PASSWORD = st.secrets.get("admin_password", "admin")
except StreamlitSecretNotFoundError:
    ADMIN_PASSWORD = "admin"

# ------------------------------------------------------------
# Page config
# ------------------------------------------------------------
st.set_page_config(
    page_title="Number System Problems Repository",
    layout="wide"
)

apply_global_styles()

# ------------------------------------------------------------
# Data paths
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
METADATA_FILE = BASE_DIR / "static" / "metadata.json"
STATIC_DIR = BASE_DIR / "static"
PROBLEM_DIR = STATIC_DIR / "problems"
SOLUTION_DIR = STATIC_DIR / "solutions"
PROBLEM_DIR_REL = Path("static") / "problems"
SOLUTION_DIR_REL = Path("static") / "solutions"

os.makedirs(PROBLEM_DIR, exist_ok=True)
os.makedirs(SOLUTION_DIR, exist_ok=True)

def resolve_path(path_str: str) -> Path:
    path = Path(path_str)
    if not path.is_absolute():
        path = BASE_DIR / path
    return path

def load_metadata():
    if METADATA_FILE.exists():
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_metadata(metadata):
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

metadata = load_metadata()
df = pd.DataFrame(metadata) if metadata else pd.DataFrame()

# ------------------------------------------------------------
# Session state
# ------------------------------------------------------------
if "selected_problem" not in st.session_state:
    st.session_state.selected_problem = None
if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False
if "edit_id" not in st.session_state:
    st.session_state.edit_id = None
if "show_solution" not in st.session_state:
    st.session_state.show_solution = False

# ------------------------------------------------------------
# Helper to display a file
# ------------------------------------------------------------
def display_file(file_path, label="File"):
    resolved = resolve_path(file_path)
    if not resolved.exists():
        st.warning(f"File not found: {file_path}")
        return

    ext = resolved.suffix.lower()
    if ext in (".png", ".jpg", ".jpeg", ".gif", ".bmp"):
        st.image(str(resolved), use_container_width=True)
    elif ext == ".pdf":
        with open(resolved, "rb") as f:
            st.download_button(
                label=f"Download {label} (PDF)",
                data=f,
                file_name=resolved.name,
                mime="application/pdf"
            )
    elif ext == ".txt":
        with open(resolved, "r", encoding="utf-8") as f:
            st.text(f.read())
    else:
        with open(resolved, "rb") as f:
            st.download_button(
                label=f"Download {label}",
                data=f,
                file_name=resolved.name
            )

# ------------------------------------------------------------
# Helper to display multiple files with tabs
# ------------------------------------------------------------
def display_multiple_files(file_paths, base_label="File"):
    """Display multiple files with tabs"""
    if not file_paths:
        st.info(f"No {base_label} files available.")
        return
    
    if len(file_paths) == 1:
        # Single file - show directly
        display_file(file_paths[0], base_label)
    else:
        # Multiple files - show in tabs
        tab_names = [f"{base_label} Part {i+1}" for i in range(len(file_paths))]
        tabs = st.tabs(tab_names)
        
        for i, (tab, file_path) in enumerate(zip(tabs, file_paths)):
            with tab:
                display_file(file_path, f"{base_label} {i+1}")

# ------------------------------------------------------------
# Helper to display multiple solution files (kept for backward compatibility)
# ------------------------------------------------------------
def display_solution_files(solution_paths):
    """Display multiple solution files with tabs"""
    display_multiple_files(solution_paths, "Solution")

# ------------------------------------------------------------
# Helper to display multiple problem files
# ------------------------------------------------------------
def display_problem_files(problem_paths):
    """Display multiple problem files with tabs"""
    display_multiple_files(problem_paths, "Problem")

# ------------------------------------------------------------
# Main title and intro
# ------------------------------------------------------------
st.title("Number System Problems Repository")
st.markdown("""
Welcome! This repository contains Olympiad‑style problems from number systems and linguistics.  
Use the **tags** below to filter, then click **View** to see the problem and its solution.
""")

st.divider()

# ------------------------------------------------------------
# Detail view (if a problem is selected)
# ------------------------------------------------------------
if st.session_state.selected_problem is not None:
    prob = st.session_state.selected_problem

    if st.button("← Back to list"):
        st.session_state.selected_problem = None
        st.session_state.show_solution = False
        st.rerun()

    st.header(prob["title"])
    st.markdown(f"**Tags:** {', '.join(prob['tags'])}")

    # Display problem (handle both single and multiple files)
    st.subheader("Problem")
    if "problem_files" in prob:
        display_problem_files(prob["problem_files"])
    elif "problem_file" in prob:
        display_file(prob["problem_file"], "Problem")
    else:
        st.warning("No problem files found.")

    # Centered button to toggle solution
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("View Solution", use_container_width=True):
            st.session_state.show_solution = not st.session_state.show_solution

    if st.session_state.show_solution:
        st.subheader("Solution")
        # Handle both old format (single file) and new format (multiple files)
        if "solution_files" in prob:
            display_solution_files(prob["solution_files"])
        elif "solution_file" in prob:
            display_file(prob["solution_file"], "Solution")
        else:
            st.warning("No solution files found.")

    st.stop()

# ------------------------------------------------------------
# List view with tag filter
# ------------------------------------------------------------
if not df.empty:
    all_tags = sorted(set(tag for tags in df["tags"] for tag in tags))
    selected_tags = st.multiselect("Filter by tags", all_tags)

    if selected_tags:
        mask = df["tags"].apply(lambda tags: any(tag in tags for tag in selected_tags))
        filtered_df = df[mask]
    else:
        filtered_df = df

    if filtered_df.empty:
        st.info("No problems match the selected tags.")
    else:
        for _, row in filtered_df.iterrows():
            with st.container(border=True):
                cols = st.columns([3, 1])
                with cols[0]:
                    st.markdown(f"**{row['title']}**")
                    st.markdown(f"*Tags:* {', '.join(row['tags'])}")
                with cols[1]:
                    if st.button("View", key=f"view_{row['id']}", type="secondary"):
                        st.session_state.selected_problem = row.to_dict()
                        st.session_state.show_solution = False
                        st.rerun()
else:
    st.info("No problems in the repository yet.")

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("---")
st.caption("Problems are sourced from various Olympiads and are for educational purposes. If you have a problem to contribute, please contact the administrator at yizou1104@gmail.com.")
st.caption("Mention to Vlad A. Neacșu's book Linguistics Olympiad Training Guide for contributing the sources for some of the problems.")
home_nav()