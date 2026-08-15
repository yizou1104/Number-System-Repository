import streamlit as st
from ui import apply_global_styles, home_nav
from streamlit.errors import StreamlitSecretNotFoundError
import pandas as pd
import json
import os
from pathlib import Path

st.set_page_config(page_title="Number System Problems Repository", layout="wide")
apply_global_styles()

# ── PAGE-SPECIFIC STYLES ─────────────────────────────────────
st.markdown("""
<style>
.main .block-container { max-width: 1100px !important; padding-left: 3rem !important; padding-right: 3rem !important; margin: 0 auto !important; }

/* Olympiad masthead */
.olym-masthead { border-top: 3px solid var(--ink); border-bottom: 1px solid var(--rule); padding: 1.75rem 0 1.4rem 0; margin-bottom: 1.75rem; }
.olym-masthead-eyebrow { font-family: 'DM Sans', sans-serif; font-size: .68rem; font-weight: 700; text-transform: uppercase; letter-spacing: .18em; color: var(--accent); display: flex; align-items: center; gap: .65rem; margin-bottom: .65rem; }
.olym-masthead-eyebrow::before { content: ''; display: inline-block; width: 1.75rem; height: 1.5px; background: var(--accent); flex-shrink: 0; }
.olym-masthead-title { font-family: 'Crimson Pro', Georgia, serif; font-size: 3rem; font-weight: 700; color: var(--ink); letter-spacing: -.04em; line-height: 1.05; margin-bottom: .5rem; }
.olym-masthead-desc { font-family: 'Crimson Pro', Georgia, serif; font-style: italic; font-size: 1.05rem; color: var(--ink-muted); line-height: 1.55; margin: 0; }

/* Problem card */
.prob-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 6px;
    padding: 1.2rem 1.5rem;
    margin-bottom: .75rem;
    box-shadow: 0 1px 3px rgba(26,22,18,.04), inset 0 1px 0 rgba(255,255,255,.65);
    transition: all .2s cubic-bezier(.4,0,.2,1);
    display: flex; align-items: flex-start; gap: 1.25rem;
}
.prob-card:hover { transform: translateY(-2px); box-shadow: 0 4px 18px rgba(26,22,18,.09); border-color: rgba(26,22,18,.16); }
.prob-card-body { flex: 1; min-width: 0; }
.prob-card-title { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.25rem; font-weight: 600; color: var(--ink); letter-spacing: -.02em; margin-bottom: .4rem; line-height: 1.25; }
.prob-card-tags { display: flex; flex-wrap: wrap; gap: .3rem; margin-top: .45rem; }
.prob-card-action { flex-shrink: 0; align-self: center; }

/* Difficulty badge in card left border */
.prob-card.diff-easy   { border-left: 4px solid var(--teal); }
.prob-card.diff-medium { border-left: 4px solid #c49a26; }
.prob-card.diff-hard   { border-left: 4px solid var(--accent); }

/* Tag pills */
.tag-pill { display: inline-flex; align-items: center; font-family: 'DM Sans', sans-serif; font-size: .63rem; font-weight: 600; letter-spacing: .07em; text-transform: uppercase; padding: .17rem .5rem; border-radius: 2px; background: var(--parchment-3); color: var(--ink-muted); border: 1px solid var(--rule); }
.tag-pill.diff-easy   { background: rgba(46,107,122,.12);  color: var(--teal);     border-color: rgba(46,107,122,.25); }
.tag-pill.diff-medium { background: rgba(196,154,38,.12);  color: #8a6a10;         border-color: rgba(196,154,38,.3);  }
.tag-pill.diff-hard   { background: rgba(184,92,56,.12);   color: var(--accent);   border-color: rgba(184,92,56,.25);  }
.tag-pill.comp        { background: rgba(26,22,18,.06);    color: var(--ink-soft); border-color: var(--rule-strong);   }

/* Filter bar */
.filter-bar { background: var(--parchment-2); border: 1px solid var(--rule); border-radius: 5px; padding: 1rem 1.35rem; margin-bottom: 1.5rem; }
.filter-label { font-family: 'DM Sans', sans-serif; font-size: .68rem; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--ink-faint); margin-bottom: .5rem; }

/* Detail view */
.prob-detail-header { border-top: 3px solid var(--ink); padding-top: 1.5rem; margin-bottom: 1.5rem; }
.prob-detail-title { font-family: 'Crimson Pro', Georgia, serif; font-size: 2.2rem; font-weight: 700; color: var(--ink); letter-spacing: -.035em; line-height: 1.1; margin-bottom: .75rem; }
.prob-back-btn { font-family: 'DM Sans', sans-serif; font-size: .78rem; font-weight: 700; text-transform: uppercase; letter-spacing: .09em; color: var(--ink-muted); background: transparent; border: 1.5px solid var(--rule-strong); border-radius: 3px; padding: .45rem .9rem; text-decoration: none; display: inline-flex; align-items: center; gap: .4rem; cursor: pointer; transition: all .18s ease; margin-bottom: 1.25rem; }
.prob-back-btn:hover { color: var(--ink); border-color: var(--ink); background: var(--parchment-2); }

/* Solution toggle */
.sol-toggle-wrap { display: flex; justify-content: center; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ── CONFIGURATION ────────────────────────────────────────────
DIFF_TAGS = {"Easy", "Medium", "Hard"}
COMP_TAGS = {"APLO", "IOL", "UKLO", "HKLO", "PLO", "NACLO"}

try:
    ADMIN_PASSWORD = st.secrets.get("admin_password", "admin")
except StreamlitSecretNotFoundError:
    ADMIN_PASSWORD = "admin"

# ── DATA PATHS ───────────────────────────────────────────────
# File is at pages/Olympiad_Problems.py → parent.parent = capstone root
BASE_DIR = Path(__file__).resolve().parent.parent
METADATA_FILE = BASE_DIR / "static" / "metadata.json"
STATIC_DIR    = BASE_DIR / "static"
PROBLEM_DIR   = STATIC_DIR / "problems"
SOLUTION_DIR  = STATIC_DIR / "solutions"

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


metadata = load_metadata()
df = pd.DataFrame(metadata) if metadata else pd.DataFrame()

# ── SESSION STATE ─────────────────────────────────────────────
for key, default in [
    ("selected_problem", None),
    ("admin_authenticated", False),
    ("edit_id", None),
    ("show_solution", False),
]:
    if key not in st.session_state:
        st.session_state[key] = default


# ── FILE DISPLAY HELPERS ──────────────────────────────────────
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
            st.download_button(label=f"Download {label} (PDF)", data=f, file_name=resolved.name, mime="application/pdf")
    elif ext == ".txt":
        with open(resolved, "r", encoding="utf-8") as f:
            st.text(f.read())
    else:
        with open(resolved, "rb") as f:
            st.download_button(label=f"Download {label}", data=f, file_name=resolved.name)


def display_multiple_files(file_paths, base_label="File"):
    if not file_paths:
        st.info(f"No {base_label} files available.")
        return
    if len(file_paths) == 1:
        display_file(file_paths[0], base_label)
    else:
        tabs = st.tabs([f"{base_label} Part {i+1}" for i in range(len(file_paths))])
        for tab, fp in zip(tabs, file_paths):
            with tab:
                display_file(fp, base_label)


# ── TAG PILL RENDERER ─────────────────────────────────────────
def render_tag_pill(tag: str) -> str:
    cls = "diff-easy" if tag == "Easy" else \
          "diff-medium" if tag == "Medium" else \
          "diff-hard" if tag == "Hard" else \
          "comp" if tag in COMP_TAGS else ""
    return f'<span class="tag-pill {cls}">{tag}</span>'


def render_tags(tags) -> str:
    return "".join(render_tag_pill(t) for t in tags)


# ── MASTHEAD ──────────────────────────────────────────────────
st.markdown("""
<div class="olym-masthead">
    <div class="olym-masthead-eyebrow">Competition Repository</div>
    <div class="olym-masthead-title">Olympiad Problems</div>
    <div class="olym-masthead-desc">
        Curated problems from IOL, UKLO, NACLO, PLO, and other linguistics olympiads —
        with full worked solutions. Filter by topic or difficulty, then work through each problem.
    </div>
</div>
""", unsafe_allow_html=True)

# ── DETAIL VIEW ───────────────────────────────────────────────
if st.session_state.selected_problem is not None:
    prob = st.session_state.selected_problem

    if st.button("← Back to problems"):
        st.session_state.selected_problem = None
        st.session_state.show_solution = False
        st.rerun()

    tags_html = render_tags(prob.get("tags", []))
    st.markdown(f"""
    <div class="prob-detail-header">
        <div class="prob-detail-title">{prob['title']}</div>
        <div class="prob-card-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Problem")
    if "problem_files" in prob:
        display_multiple_files(prob["problem_files"], "Problem")
    elif "problem_file" in prob:
        display_file(prob["problem_file"], "Problem")
    else:
        st.warning("No problem files found.")

    st.markdown('<div class="sol-toggle-wrap">', unsafe_allow_html=True)
    if st.button("View Solution" if not st.session_state.show_solution else "Hide Solution", use_container_width=False):
        st.session_state.show_solution = not st.session_state.show_solution
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.show_solution:
        st.markdown("#### Solution")
        if "solution_files" in prob:
            display_multiple_files(prob["solution_files"], "Solution")
        elif "solution_file" in prob:
            display_file(prob["solution_file"], "Solution")
        else:
            st.warning("No solution files found.")

    st.stop()

# ── LIST VIEW ─────────────────────────────────────────────────
if not df.empty:
    all_tags = sorted(set(tag for tags in df["tags"] for tag in tags))

    st.markdown('<div class="filter-bar"><div class="filter-label">Filter by tag</div>', unsafe_allow_html=True)
    selected_tags = st.multiselect("Filter by tags", all_tags, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    filtered_df = df[df["tags"].apply(lambda tags: any(t in tags for t in selected_tags))] \
        if selected_tags else df

    if filtered_df.empty:
        st.info("No problems match the selected tags.")
    else:
        # Detect difficulty for left-border color
        def diff_class(tags):
            if "Hard" in tags:   return "diff-hard"
            if "Medium" in tags: return "diff-medium"
            if "Easy" in tags:   return "diff-easy"
            return ""

        for _, row in filtered_df.iterrows():
            dc = diff_class(row["tags"])
            tags_html = render_tags(row["tags"])
            # Render card HTML then place the View button separately
            st.markdown(f"""
            <div class="prob-card {dc}">
                <div class="prob-card-body">
                    <div class="prob-card-title">{row['title']}</div>
                    <div class="prob-card-tags">{tags_html}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("View →", key=f"view_{row['id']}", type="secondary"):
                st.session_state.selected_problem = row.to_dict()
                st.session_state.show_solution = False
                st.rerun()
else:
    st.info("No problems in the repository yet.")

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "Problems sourced from various linguistics olympiads for educational purposes. "
    "Thanks to Vlad A. Neacșu's Linguistics Olympiad Training Guide for contributing sources."
)
home_nav()
