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
# CONFIGURATION – EDIT THESE LISTS AS NEEDED
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
    "Easy",
    "Medium",
    "Hard",
    "APLO",
    "IOL",
    "UKLO",
    "HKLO",
    "PLO",
    "NACLO",
    # add more tags as needed
]

try:
    ADMIN_PASSWORD = st.secrets.get("admin_password", "admin")
except StreamlitSecretNotFoundError:
    ADMIN_PASSWORD = "admin"

# ------------------------------------------------------------
# Page config and custom CSS
# ------------------------------------------------------------
st.set_page_config(
    page_title="Number System Problems Repository",
    layout="wide"
)

apply_global_styles()

# ------------------------------------------------------------
# Data paths and initialisation
# ------------------------------------------------------------
METADATA_FILE = "metadata.json"
PROBLEM_DIR = "problems"
SOLUTION_DIR = "solutions"

os.makedirs(PROBLEM_DIR, exist_ok=True)
os.makedirs(SOLUTION_DIR, exist_ok=True)

def load_metadata():
    if os.path.exists(METADATA_FILE):
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
    if not os.path.exists(file_path):
        st.warning(f"File not found: {file_path}")
        return

    ext = Path(file_path).suffix.lower()
    if ext in (".png", ".jpg", ".jpeg", ".gif", ".bmp"):
        st.image(file_path, use_container_width=True)
    elif ext == ".pdf":
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"Download {label} (PDF)",
                data=f,
                file_name=os.path.basename(file_path),
                mime="application/pdf"
            )
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            st.text(f.read())
    else:
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"Download {label}",
                data=f,
                file_name=os.path.basename(file_path)
            )

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
        display_file(prob["solution_file"], "Solution")

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
                    # Use a secondary button (black background via CSS)
                    if st.button("View", key=f"view_{row['id']}", type="secondary"):
                        st.session_state.selected_problem = row.to_dict()
                        st.session_state.show_solution = False
                        st.rerun()
else:
    st.info("No problems in the repository yet. Use the admin panel below to add some.")

st.divider()

# ------------------------------------------------------------
# ADMIN PANEL (unchanged, except for consistency)
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
                solution_file = st.file_uploader(
                    "Upload solution file (image/PDF/txt)",
                    type=["png", "jpg", "jpeg", "gif", "pdf", "txt"]
                )

                submitted = st.form_submit_button("Add Problem")

                if submitted:
                    if not (title and selected_tags and problem_file and solution_file):
                        st.error("All fields are required.")
                    else:
                        new_id = max([p["id"] for p in metadata], default=0) + 1

                        prob_ext = Path(problem_file.name).suffix
                        prob_filename = f"prob_{new_id}{prob_ext}"
                        prob_path = os.path.join(PROBLEM_DIR, prob_filename)
                        with open(prob_path, "wb") as f:
                            f.write(problem_file.getbuffer())

                        sol_ext = Path(solution_file.name).suffix
                        sol_filename = f"sol_{new_id}{sol_ext}"
                        sol_path = os.path.join(SOLUTION_DIR, sol_filename)
                        with open(sol_path, "wb") as f:
                            f.write(solution_file.getbuffer())

                        new_entry = {
                            "id": new_id,
                            "title": title,
                            "tags": selected_tags,
                            "problem_file": prob_path,
                            "solution_file": sol_path
                        }
                        metadata.append(new_entry)
                        save_metadata(metadata)

                        st.success(f"Problem '{title}' added successfully!")
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

                        st.markdown("**Replace solution file (optional)**")
                        new_solution_file = st.file_uploader(
                            "Upload new solution file",
                            type=["png", "jpg", "jpeg", "gif", "pdf", "txt"],
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

                            if new_problem_file is not None:
                                if os.path.exists(problem["problem_file"]):
                                    os.remove(problem["problem_file"])
                                prob_ext = Path(new_problem_file.name).suffix
                                prob_filename = f"prob_{problem['id']}{prob_ext}"
                                prob_path = os.path.join(PROBLEM_DIR, prob_filename)
                                with open(prob_path, "wb") as f:
                                    f.write(new_problem_file.getbuffer())
                                problem["problem_file"] = prob_path

                            if new_solution_file is not None:
                                if os.path.exists(problem["solution_file"]):
                                    os.remove(problem["solution_file"])
                                sol_ext = Path(new_solution_file.name).suffix
                                sol_filename = f"sol_{problem['id']}{sol_ext}"
                                sol_path = os.path.join(SOLUTION_DIR, sol_filename)
                                with open(sol_path, "wb") as f:
                                    f.write(new_solution_file.getbuffer())
                                problem["solution_file"] = sol_path

                            save_metadata(metadata)
                            st.session_state.edit_id = None
                            st.success("Changes saved!")
                            st.rerun()

                        if cancel:
                            st.session_state.edit_id = None
                            st.rerun()

                if st.button("🗑️ Delete this problem", type="primary"):
                    if st.checkbox("I understand this cannot be undone"):
                        if os.path.exists(problem["problem_file"]):
                            os.remove(problem["problem_file"])
                        if os.path.exists(problem["solution_file"]):
                            os.remove(problem["solution_file"])
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
st.caption("Problems are stored locally. For permanent hosting, consider cloud storage.")

