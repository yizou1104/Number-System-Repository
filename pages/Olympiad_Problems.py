# pages/Olympiad_Problems.py

import streamlit as st
from ui import apply_global_styles
from streamlit.errors import StreamlitSecretNotFoundError
import pandas as pd
import json
import os
import shutil
from pathlib import Path

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
BASE_DIR = Path(__file__).resolve().parent.parent
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
# Helper to display multiple solution files
# ------------------------------------------------------------
def display_solution_files(solution_paths):
    """Display multiple solution files with tabs or expanders"""
    if not solution_paths:
        st.info("No solution files available.")
        return
    
    if len(solution_paths) == 1:
        # Single solution - show directly
        display_file(solution_paths[0], "Solution")
    else:
        # Multiple solutions - show in tabs
        tab_names = [f"Solution Part {i+1}" for i in range(len(solution_paths))]
        tabs = st.tabs(tab_names)
        
        for i, (tab, sol_path) in enumerate(zip(tabs, solution_paths)):
            with tab:
                display_file(sol_path, f"Solution {i+1}")

# ------------------------------------------------------------
# Main title and intro
# ------------------------------------------------------------
st.title("Number System Problems Repository")
st.markdown("""
Welcome! This repository contains Olympiad‑style problems from number systems and linguistics.  
Use the **tags** below to filter, then click **View** to see the problem and its solution.
""")

with st.expander("📌 Sample problems (static examples)"):
    st.markdown("""
    **1. Babylonian fractions**  
    *Tags: base‑60, positional*  
    Convert 2/5 into a sexagesimal fraction.

    **2. Roman numeral puzzle**  
    *Tags: subtractive, additive*  
    Find the largest number that can be written with exactly four symbols (I, V, X, L, C, D, M).

    **3. Thai numeral irregularities**  
    *Tags: positional, special forms*  
    Explain why 21 is written *ยี่สิบเอ็ด* and not *สองสิบหนึ่ง*.
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

    # Display problem full width
    st.subheader("Problem")
    display_file(prob["problem_file"], "Problem")

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
# ADMIN PANEL – UPDATED FOR MULTIPLE SOLUTION FILES
# ------------------------------------------------------------
with st.expander("🛠️ Admin Panel (manage problems)"):
    password = st.text_input("Enter admin password", type="password")
    if password == ADMIN_PASSWORD:
        st.session_state.admin_authenticated = True
    else:
        st.session_state.admin_authenticated = False

    if st.session_state.admin_authenticated:
        st.success("Authenticated. You can add, edit, or delete problems.")

        admin_mode = st.radio(
            "Admin actions",
            ["➕ Add new problem", "✏️ Edit / Delete existing"],
            horizontal=True
        )

        # ADD NEW PROBLEM
        if admin_mode == "➕ Add new problem":
            with st.form("upload_form", clear_on_submit=True):
                title = st.text_input("Problem title")
                selected_tags = st.multiselect("Select tags", TAGS)

                problem_file = st.file_uploader(
                    "Upload problem file (image/PDF)",
                    type=["png", "jpg", "jpeg", "gif", "pdf"]
                )
                
                st.markdown("**Solution files** (you can upload multiple)")
                solution_files = st.file_uploader(
                    "Upload solution files (image/PDF/txt)",
                    type=["png", "jpg", "jpeg", "gif", "pdf", "txt"],
                    accept_multiple_files=True,
                    key="solution_uploader"
                )

                submitted = st.form_submit_button("Add Problem")

                if submitted:
                    if not (title and selected_tags and problem_file and solution_files):
                        st.error("Problem title, tags, problem file, and at least one solution file are required.")
                    else:
                        new_id = max([p["id"] for p in metadata], default=0) + 1

                        # Save problem file
                        prob_ext = Path(problem_file.name).suffix
                        prob_filename = f"prob_{new_id}{prob_ext}"
                        prob_path = PROBLEM_DIR / prob_filename
                        with open(prob_path, "wb") as f:
                            f.write(problem_file.getbuffer())

                        # Save all solution files
                        solution_paths = []
                        for i, sol_file in enumerate(solution_files):
                            sol_ext = Path(sol_file.name).suffix
                            sol_filename = f"sol_{new_id}_{i+1}{sol_ext}"
                            sol_path = SOLUTION_DIR / sol_filename
                            with open(sol_path, "wb") as f:
                                f.write(sol_file.getbuffer())
                            solution_paths.append(str(SOLUTION_DIR_REL / sol_filename))

                        new_entry = {
                            "id": new_id,
                            "title": title,
                            "tags": selected_tags,
                            "problem_file": str(PROBLEM_DIR_REL / prob_filename),
                            "solution_files": solution_paths
                        }
                        metadata.append(new_entry)
                        save_metadata(metadata)

                        st.success(f"Problem '{title}' added successfully with {len(solution_paths)} solution files!")
                        st.rerun()

        # EDIT / DELETE EXISTING PROBLEMS
        else:
            if not metadata:
                st.info("No problems to manage.")
            else:
                problem_options = {p["id"]: p["title"] for p in metadata}
                selected_id = st.selectbox(
                    "Choose a problem to edit/delete",
                    options=list(problem_options.keys()),
                    format_func=lambda x: problem_options[x]
                )

                problem = next(p for p in metadata if p["id"] == selected_id)

                if st.button("Edit this problem"):
                    st.session_state.edit_id = selected_id

                if st.session_state.edit_id == selected_id:
                    st.markdown("---")
                    st.subheader(f"Editing: {problem['title']}")

                    with st.form("edit_form"):
                        new_title = st.text_input("Title", value=problem["title"])
                        new_tags = st.multiselect(
                            "Tags",
                            options=TAGS,
                            default=problem["tags"]
                        )

                        st.markdown("**Replace problem file (optional)**")
                        new_problem_file = st.file_uploader(
                            "Upload new problem file",
                            type=["png", "jpg", "jpeg", "gif", "pdf"],
                            key="edit_prob"
                        )

                        st.markdown("**Replace solution files (optional)**")
                        st.markdown("*Leave empty to keep existing solution files*")
                        new_solution_files = st.file_uploader(
                            "Upload new solution files",
                            type=["png", "jpg", "jpeg", "gif", "pdf", "txt"],
                            accept_multiple_files=True,
                            key="edit_sol"
                        )

                        col1, col2 = st.columns(2)
                        with col1:
                            save_changes = st.form_submit_button("💾 Save changes")
                        with col2:
                            cancel = st.form_submit_button("Cancel")

                        if save_changes:
                            problem["title"] = new_title
                            problem["tags"] = new_tags

                            # Handle problem file replacement
                            if new_problem_file is not None:
                                # Delete old file
                                old_prob_path = resolve_path(problem["problem_file"])
                                if old_prob_path.exists():
                                    os.remove(old_prob_path)
                                
                                # Save new file
                                prob_ext = Path(new_problem_file.name).suffix
                                prob_filename = f"prob_{problem['id']}{prob_ext}"
                                prob_path = PROBLEM_DIR / prob_filename
                                with open(prob_path, "wb") as f:
                                    f.write(new_problem_file.getbuffer())
                                problem["problem_file"] = str(PROBLEM_DIR_REL / prob_filename)

                            # Handle solution files replacement
                            if new_solution_files:
                                # Delete old solution files
                                if "solution_files" in problem:
                                    for old_sol in problem["solution_files"]:
                                        old_sol_path = resolve_path(old_sol)
                                        if old_sol_path.exists():
                                            os.remove(old_sol_path)
                                elif "solution_file" in problem:
                                    old_sol_path = resolve_path(problem["solution_file"])
                                    if old_sol_path.exists():
                                        os.remove(old_sol_path)
                                
                                # Save new solution files
                                solution_paths = []
                                for i, sol_file in enumerate(new_solution_files):
                                    sol_ext = Path(sol_file.name).suffix
                                    sol_filename = f"sol_{problem['id']}_{i+1}{sol_ext}"
                                    sol_path = SOLUTION_DIR / sol_filename
                                    with open(sol_path, "wb") as f:
                                        f.write(sol_file.getbuffer())
                                    solution_paths.append(str(SOLUTION_DIR_REL / sol_filename))
                                problem["solution_files"] = solution_paths
                                
                                # Remove old single solution field if it exists
                                if "solution_file" in problem:
                                    del problem["solution_file"]

                            save_metadata(metadata)
                            st.session_state.edit_id = None
                            st.success("Changes saved!")
                            st.rerun()

                        if cancel:
                            st.session_state.edit_id = None
                            st.rerun()

                if st.button("🗑️ Delete this problem", type="primary"):
                    if st.checkbox("I understand this cannot be undone"):
                        # Delete problem file
                        prob_path = resolve_path(problem["problem_file"])
                        if prob_path.exists():
                            os.remove(prob_path)
                        
                        # Delete all solution files
                        if "solution_files" in problem:
                            for sol_file in problem["solution_files"]:
                                sol_path = resolve_path(sol_file)
                                if sol_path.exists():
                                    os.remove(sol_path)
                        elif "solution_file" in problem:
                            sol_path = resolve_path(problem["solution_file"])
                            if sol_path.exists():
                                os.remove(sol_path)
                        
                        metadata.remove(problem)
                        save_metadata(metadata)
                        st.session_state.edit_id = None
                        st.success("Problem deleted.")
                        st.rerun()
                    else:
                        st.warning("Please confirm deletion.")

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("---")
st.caption("Problems are stored in the static/ folder. For permanent hosting, commit files to GitHub.")