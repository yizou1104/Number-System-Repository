import streamlit as st


# --------------------------------------------------
# Global UI styles — Editorial Modernist Design System
# Aesthetic: Academic journal × museum catalogue
# Fonts: Crimson Pro (body/display) + DM Sans (UI labels)
# Palette: Ink, parchment, warm slate, terracotta accent
# --------------------------------------------------

def apply_global_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

        /* ─────────────────────────────────────────
           DESIGN TOKENS
        ───────────────────────────────────────── */
        :root {
            /* Core palette — ink & parchment */
            --ink:          #1a1612;
            --ink-soft:     #2e2a25;
            --ink-muted:    #6b6358;
            --ink-faint:    #9c9288;

            /* Parchment surfaces */
            --parchment:    #faf7f2;
            --parchment-2:  #f3ede3;
            --parchment-3:  #e9e0d3;

            /* Warm accent — terracotta */
            --accent:       #b85c38;
            --accent-light: #d4794f;
            --accent-pale:  #f2ddd3;
            --accent-glow:  rgba(184, 92, 56, 0.12);

            /* Structural lines */
            --rule:         rgba(26, 22, 18, 0.12);
            --rule-strong:  rgba(26, 22, 18, 0.25);

            /* Card surfaces */
            --card-bg:      rgba(250, 247, 242, 0.92);
            --card-border:  rgba(26, 22, 18, 0.10);
            --card-shadow:  rgba(26, 22, 18, 0.07);
            --card-hover:   rgba(26, 22, 18, 0.13);

            /* Secondary blue-grey accent */
            --teal:         #2e6b7a;
            --teal-pale:    #d6eaee;

            /* Gradients */
            --grad-warm:    linear-gradient(135deg, #faf7f2 0%, #f3ede3 60%, #e9e0d3 100%);
            --grad-card:    linear-gradient(160deg, #fdfbf8 0%, #f7f1e8 100%);
        }

        /* ─────────────────────────────────────────
           APP BASE
        ───────────────────────────────────────── */
        .stApp {
            background-color: var(--parchment);
            background-image:
                /* Subtle grain texture via SVG data URI */
                url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.022'/%3E%3C/svg%3E"),
                /* Warm radial vignette */
                radial-gradient(ellipse 120% 80% at 50% 0%,  rgba(242, 221, 211, 0.35) 0%, transparent 65%),
                radial-gradient(ellipse 80%  60% at 0%  100%, rgba(214, 234, 238, 0.20) 0%, transparent 60%),
                linear-gradient(170deg, #faf7f2 0%, #f5efe4 50%, #f0e9db 100%);
            background-attachment: fixed;
            color: var(--ink);
            font-family: 'Crimson Pro', Georgia, 'Times New Roman', serif;
            font-size: 18px;
            line-height: 1.68;
            min-height: 100vh;
        }

        /* Page-in animation */
        section.main > div {
            animation: pageIn 0.55s cubic-bezier(0.22, 1, 0.36, 1) both;
        }
        @keyframes pageIn {
            from { opacity: 0; transform: translateY(14px); }
            to   { opacity: 1; transform: translateY(0);     }
        }

        /* ─────────────────────────────────────────
           TYPOGRAPHY HIERARCHY
        ───────────────────────────────────────── */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Crimson Pro', Georgia, serif !important;
            color: var(--ink) !important;
            letter-spacing: -0.02em;
            line-height: 1.15;
        }

        h1 {
            font-size: 3.4rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.035em !important;
            margin-bottom: 0.5rem !important;
        }

        h2 {
            font-size: 2.3rem !important;
            font-weight: 600 !important;
            margin-top: 2.5rem !important;
            margin-bottom: 0.75rem !important;
            /* editorial underline rule */
            padding-bottom: 0.35rem;
            border-bottom: 2px solid var(--rule-strong);
        }

        h3 {
            font-size: 1.7rem !important;
            font-weight: 600 !important;
            color: var(--ink-soft) !important;
            margin-top: 2rem !important;
            margin-bottom: 0.6rem !important;
        }

        h4 {
            font-size: 1.25rem !important;
            font-weight: 500 !important;
            color: var(--ink-muted) !important;
            font-style: italic;
            letter-spacing: 0.01em;
        }

        p, li, .stMarkdown p {
            font-family: 'Crimson Pro', Georgia, serif;
            font-size: 1.1rem;
            color: var(--ink-soft);
            line-height: 1.75;
            margin-bottom: 0.85rem;
        }

        /* UI labels use DM Sans */
        label, .stCaption, .stText,
        div[data-testid="stTextInput"] label,
        div[data-testid="stSelectbox"] label,
        div[data-testid="stRadio"] label,
        div[data-testid="stCheckbox"] label,
        div[data-testid="stMultiSelect"] label {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.82rem !important;
            font-weight: 500 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.08em !important;
            color: var(--ink-muted) !important;
        }

        .stCaption {
            font-size: 0.875rem !important;
            line-height: 1.5 !important;
            color: var(--ink-faint) !important;
        }

        /* Italic emphasis */
        em { color: var(--accent); font-style: italic; }

        /* ─────────────────────────────────────────
           BUTTONS
        ───────────────────────────────────────── */
        .stButton > button {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            letter-spacing: 0.06em !important;
            text-transform: uppercase !important;
            background: var(--ink) !important;
            color: var(--parchment) !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 0.65rem 1.6rem !important;
            box-shadow: 3px 3px 0 var(--accent) !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }

        .stButton > button:hover {
            background: var(--ink-soft) !important;
            box-shadow: 5px 5px 0 var(--accent) !important;
            transform: translate(-1px, -1px) !important;
        }

        .stButton > button:active {
            transform: translate(2px, 2px) !important;
            box-shadow: 1px 1px 0 var(--accent) !important;
        }

        button[kind="secondary"] {
            background: transparent !important;
            color: var(--ink) !important;
            border: 1.5px solid var(--rule-strong) !important;
            box-shadow: none !important;
        }

        button[kind="secondary"]:hover {
            background: var(--parchment-3) !important;
            border-color: var(--ink) !important;
            transform: translate(-1px, -1px) !important;
            box-shadow: 3px 3px 0 var(--ink-muted) !important;
        }

        /* ─────────────────────────────────────────
           INPUTS & FORM ELEMENTS
        ───────────────────────────────────────── */
        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stNumberInput"] input,
        div[data-testid="stSelectbox"] select {
            font-family: 'Crimson Pro', Georgia, serif !important;
            font-size: 1.05rem !important;
            background: rgba(250, 247, 242, 0.9) !important;
            border: 1.5px solid var(--rule-strong) !important;
            border-radius: 4px !important;
            padding: 0.7rem 1rem !important;
            color: var(--ink) !important;
            transition: all 0.25s ease !important;
            box-shadow: inset 0 1px 3px rgba(26,22,18,0.04) !important;
        }

        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stTextArea"] textarea:focus,
        div[data-testid="stNumberInput"] input:focus {
            border-color: var(--accent) !important;
            box-shadow: inset 0 1px 3px rgba(26,22,18,0.04),
                        0 0 0 3px var(--accent-glow) !important;
            outline: none !important;
        }

        /* Placeholder text */
        input::placeholder, textarea::placeholder {
            color: var(--ink-faint) !important;
            font-style: italic;
        }

        /* ─────────────────────────────────────────
           CARDS & CONTAINERS
        ───────────────────────────────────────── */
        div[data-testid="stContainer"] {
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: 6px !important;
            padding: 1.5rem 1.75rem !important;
            box-shadow:
                0 1px 3px var(--card-shadow),
                0 4px 16px rgba(26,22,18,0.05),
                inset 0 1px 0 rgba(255,255,255,0.7) !important;
            transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1) !important;
            backdrop-filter: blur(8px);
            margin-bottom: 1rem !important;
        }

        div[data-testid="stContainer"]:hover {
            transform: translateY(-3px) !important;
            box-shadow:
                0 2px 6px var(--card-shadow),
                0 12px 32px rgba(26,22,18,0.10),
                inset 0 1px 0 rgba(255,255,255,0.8) !important;
            border-color: var(--card-hover) !important;
        }

        /* ─────────────────────────────────────────
           EXPANDERS
        ───────────────────────────────────────── */
        div[data-testid="stExpander"] {
            border: 1px solid var(--card-border) !important;
            border-radius: 6px !important;
            background: var(--card-bg) !important;
            box-shadow: 0 2px 8px rgba(26,22,18,0.05) !important;
            margin-bottom: 1rem !important;
            overflow: hidden;
        }

        div[data-testid="stExpander"] summary {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            letter-spacing: 0.04em !important;
            text-transform: uppercase !important;
            color: var(--ink-soft) !important;
            padding: 1rem 1.25rem !important;
        }

        /* ─────────────────────────────────────────
           TABS
        ───────────────────────────────────────── */
        .stTabs [role="tablist"] {
            border-bottom: 2px solid var(--rule-strong) !important;
            gap: 0 !important;
        }

        .stTabs [role="tablist"] button {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.82rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.08em !important;
            color: var(--ink-muted) !important;
            border-radius: 0 !important;
            border: none !important;
            padding: 0.75rem 1.5rem !important;
            transition: all 0.2s ease !important;
            background: transparent !important;
        }

        .stTabs [role="tablist"] button[aria-selected="true"] {
            color: var(--accent) !important;
            border-bottom: 2px solid var(--accent) !important;
            margin-bottom: -2px !important;
            font-weight: 700 !important;
        }

        .stTabs [role="tablist"] button:hover {
            color: var(--ink) !important;
            background: var(--parchment-2) !important;
        }

        /* ─────────────────────────────────────────
           ALERTS & MESSAGES
        ───────────────────────────────────────── */
        .stAlert {
            border-radius: 4px !important;
            border: none !important;
            border-left: 3px solid !important;
        }

        div[data-testid="stAlert"][data-type="success"] {
            background: rgba(46, 107, 122, 0.08) !important;
            border-left-color: var(--teal) !important;
        }

        div[data-testid="stAlert"][data-type="error"] {
            background: rgba(184, 92, 56, 0.08) !important;
            border-left-color: var(--accent) !important;
        }

        div[data-testid="stAlert"][data-type="info"] {
            background: rgba(26, 22, 18, 0.05) !important;
            border-left-color: var(--ink-muted) !important;
        }

        div[data-testid="stAlert"][data-type="warning"] {
            background: rgba(184, 92, 56, 0.06) !important;
            border-left-color: var(--accent-light) !important;
        }

        /* Success text output */
        div[data-testid="stAlert"] p {
            font-family: 'Crimson Pro', serif !important;
            font-size: 1.2rem !important;
            font-weight: 400 !important;
            line-height: 1.6 !important;
            color: var(--ink) !important;
        }

        /* ─────────────────────────────────────────
           TABLES
        ───────────────────────────────────────── */
        table {
            border-collapse: collapse !important;
            width: 100% !important;
            font-family: 'Crimson Pro', Georgia, serif !important;
            font-size: 1rem !important;
            border-radius: 4px !important;
            overflow: hidden !important;
            box-shadow: 0 1px 4px var(--card-shadow) !important;
        }

        th {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.09em !important;
            color: var(--ink-muted) !important;
            background: var(--parchment-2) !important;
            border-bottom: 2px solid var(--rule-strong) !important;
            padding: 0.6rem 1rem !important;
        }

        td {
            padding: 0.55rem 1rem !important;
            border-bottom: 1px solid var(--rule) !important;
            color: var(--ink-soft) !important;
        }

        tr:last-child td { border-bottom: none !important; }
        tr:hover td { background: var(--parchment-2) !important; }

        /* ─────────────────────────────────────────
           CODE BLOCKS
        ───────────────────────────────────────── */
        code {
            font-family: 'DM Mono', 'Courier New', monospace !important;
            font-size: 0.88em !important;
            background: var(--parchment-2) !important;
            color: var(--accent) !important;
            padding: 0.15em 0.4em !important;
            border-radius: 3px !important;
            border: 1px solid var(--rule) !important;
        }

        pre {
            font-family: 'DM Mono', 'Courier New', monospace !important;
            background: var(--parchment-2) !important;
            border: 1px solid var(--rule-strong) !important;
            border-left: 3px solid var(--accent) !important;
            border-radius: 4px !important;
            padding: 1.2rem 1.5rem !important;
            overflow-x: auto !important;
            font-size: 0.9rem !important;
            line-height: 1.6 !important;
        }

        pre code {
            background: none !important;
            border: none !important;
            padding: 0 !important;
            font-size: inherit !important;
            color: var(--ink-soft) !important;
        }

        /* ─────────────────────────────────────────
           DIVIDERS
        ───────────────────────────────────────── */
        hr {
            border: none !important;
            border-top: 1px solid var(--rule) !important;
            margin: 2.5rem 0 !important;
        }

        /* ─────────────────────────────────────────
           LINKS
        ───────────────────────────────────────── */
        a {
            color: var(--accent) !important;
            text-decoration: underline !important;
            text-decoration-color: var(--accent-pale) !important;
            text-underline-offset: 3px !important;
            transition: all 0.18s ease !important;
        }

        a:hover {
            color: var(--accent-light) !important;
            text-decoration-color: var(--accent) !important;
        }

        /* ─────────────────────────────────────────
           PAGE LINKS (st.page_link)
        ───────────────────────────────────────── */
        .stPageLink a {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.85rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.04em !important;
            text-transform: uppercase !important;
            color: var(--ink) !important;
            text-decoration: none !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 0.4rem !important;
            padding: 0.4rem 0 !important;
            border-bottom: 1.5px solid var(--rule-strong) !important;
            transition: all 0.2s ease !important;
        }

        .stPageLink a:hover {
            color: var(--accent) !important;
            border-bottom-color: var(--accent) !important;
            transform: translateX(3px) !important;
        }

        /* ─────────────────────────────────────────
           RADIO & MULTISELECT
        ───────────────────────────────────────── */
        div[data-testid="stRadio"] > div {
            gap: 0.5rem !important;
        }

        div[data-testid="stRadio"] label {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.88rem !important;
            font-weight: 500 !important;
            color: var(--ink-soft) !important;
            text-transform: none !important;
            letter-spacing: 0.01em !important;
        }

        /* ─────────────────────────────────────────
           SIDEBAR — hidden (navigation is manual)
           See the HIDE STREAMLIT CHROME block below
           for the display:none rule.
        ───────────────────────────────────────── */

        /* ─────────────────────────────────────────
           MULTISELECT
        ───────────────────────────────────────── */
        div[data-testid="stMultiSelect"] [data-baseweb="tag"] {
            background: var(--ink) !important;
            color: var(--parchment) !important;
            border-radius: 3px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.78rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.05em !important;
        }

        /* ─────────────────────────────────────────
           SCROLLBAR
        ───────────────────────────────────────── */
        ::-webkit-scrollbar { width: 7px; height: 7px; }
        ::-webkit-scrollbar-track { background: var(--parchment-2); }
        ::-webkit-scrollbar-thumb {
            background: var(--parchment-3);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover { background: var(--ink-faint); }

        /* ─────────────────────────────────────────
           SPINNER / PROGRESS
        ───────────────────────────────────────── */
        div[data-testid="stSpinner"] {
            color: var(--accent) !important;
        }

        /* ─────────────────────────────────────────
           HIDE STREAMLIT CHROME
           ─────────────────────────────────────────
           Removes all default Streamlit UI shell
           elements so the app presents as a clean,
           custom standalone web interface:

             • stSidebar              — left nav panel
             • stSidebarCollapsedControl — collapse arrow
             • stHeader               — top white bar
             • stToolbar              — deploy/settings icons
             • #MainMenu              — hamburger menu
             • footer                 — "Made with Streamlit"

           Companion requirement in every page file:
             st.set_page_config(layout="wide")
           This ensures the content fills the full
           viewport width once the sidebar is hidden.
        ───────────────────────────────────────── */
        [data-testid="stSidebar"]                { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        [data-testid="stHeader"]                 { display: none !important; }
        [data-testid="stToolbar"]                { display: none !important; }
        #MainMenu                                { display: none !important; }
        footer                                   { display: none !important; }

        /* Reclaim the top padding Streamlit reserves
           for the now-hidden header bar */
        [data-testid="stAppViewContainer"] > section.main {
            padding-top: 1rem !important;
        }

        /* Full-width content area — no sidebar offset,
           consistent horizontal breathing room */
        .main .block-container {
            max-width: 100% !important;
            padding-left:  2.5rem !important;
            padding-right: 2.5rem !important;
        }

        /* ─────────────────────────────────────────
           HOME NAV BUTTON
           Shared class used by home_nav() below.
        ───────────────────────────────────────── */
        .home-nav-wrap {
            display: flex;
            justify-content: flex-start;
            padding: 1.6rem 0 0.5rem 0;
            border-top: 1px solid var(--rule);
            margin-top: 2.5rem;
        }
        .home-nav-btn {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.09em;
            color: var(--ink);
            background: var(--parchment-2);
            border: 1.5px solid var(--rule-strong);
            border-radius: 3px;
            padding: 0.55rem 1.1rem;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            white-space: nowrap;
            cursor: pointer;
            box-shadow: 2px 2px 0 rgba(26,22,18,0.08);
            transition: all 0.18s cubic-bezier(0.4,0,0.2,1);
        }
        .home-nav-btn:hover {
            background: var(--ink);
            color: var(--parchment);
            border-color: var(--ink);
            box-shadow: 3px 3px 0 var(--accent);
            transform: translate(-1px,-1px);
            text-decoration: none;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HOME NAVIGATION COMPONENT
# ============================================================
#
# TWO WAYS TO USE IT
# ──────────────────
#
# OPTION A — Standalone footer (adds its own ruled divider)
# Use on pages that have NO existing nav footer, or where
# you want the Home button to sit alone on its own row.
#
#   from ui import apply_global_styles, home_nav
#   ...
#   home_nav()          # call at the bottom of the page
#
# Renders:
#   ─────────────────────────────────
#   [ ← Return to Home ]
#
#
# OPTION B — Inline button (slot into an existing nav footer)
# Use on pages that already have a conv-nav-footer or
# ling-nav-footer. Just prepend HOME_BTN inside the existing
# nav footer HTML string so all buttons sit on one row.
#
#   from ui import apply_global_styles, HOME_BTN
#   ...
#   st.markdown(f'''
#   <div class="conv-nav-footer">
#       {HOME_BTN}
#       <a class="conv-nav-btn active" href="/Basque_Converter">Basque Converter</a>
#       <a class="conv-nav-btn" href="/Basque_Linguistics">Basque Linguistics →</a>
#   </div>
#   ''', unsafe_allow_html=True)
#
# Renders:
#   ─────────────────────────────────────────────────────────
#   [ ← Home ]  [ Basque Converter ]  [ Basque Linguistics → ]
#
# ============================================================

# Inline anchor — visually identical to conv-nav-btn / ling-nav-btn.
# Import this constant and drop it into any nav footer HTML string.
HOME_BTN = '<a class="conv-nav-btn" href="/">← Home</a>'


def home_nav():
    """
    Render a standalone Return-to-Home footer with its own ruled divider.

    Use when the page has no existing nav footer, or when you want the
    Home button isolated on its own row at the bottom of the page.

    For pages that already have a conv-nav-footer or ling-nav-footer,
    use the HOME_BTN constant instead (see module docstring above).
    """
    st.markdown(
        '<div class="home-nav-wrap">'
        '<a class="home-nav-btn" href="/">← Return to Home</a>'
        '</div>',
        unsafe_allow_html=True,
    )


# Shared stylesheet for all linguistics pages.
# Defined here so linguistics pages can import it without triggering
# each other's Streamlit rendering code.
LING_CSS = """
<style>
/* ─────────────────────────────────────────────────────────────
   PAGE MASTHEAD
───────────────────────────────────────────────────────────── */
.ling-masthead {
    border-top: 3px solid var(--ink);
    border-bottom: 1px solid var(--rule);
    padding: 1.75rem 0 1.4rem 0;
    margin-bottom: 1.75rem;
}
.ling-masthead-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: var(--accent);
    display: flex;
    align-items: center;
    gap: 0.65rem;
    margin-bottom: 0.65rem;
}
.ling-masthead-eyebrow::before {
    content: '';
    display: inline-block;
    width: 1.75rem;
    height: 1.5px;
    background: var(--accent);
    flex-shrink: 0;
}
.ling-masthead-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 3rem;
    font-weight: 700;
    color: var(--ink);
    letter-spacing: -0.04em;
    line-height: 1.05;
    margin-bottom: 0.9rem;
}
.ling-masthead-sub { display: none; }
.ling-tags { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.ling-tag {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 0.22rem 0.7rem;
    border: 1.5px solid var(--rule-strong);
    border-radius: 2px;
    color: var(--ink-soft);
    background: transparent;
}
.ling-tag.accent {
    border-color: var(--accent);
    color: var(--accent);
    background: var(--accent-pale);
}

/* ─────────────────────────────────────────────────────────────
   SECTION DIVIDER
───────────────────────────────────────────────────────────── */
.ling-section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: var(--ink-soft);
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2.25rem 0 1.1rem 0;
}
.ling-section-label::before {
    content: '';
    display: inline-block;
    width: 2rem;
    height: 1px;
    background: var(--ink-muted);
    flex-shrink: 0;
}
.ling-section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--rule);
}

/* ─────────────────────────────────────────────────────────────
   SECTION TITLE
───────────────────────────────────────────────────────────── */
.ling-section-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.85rem;
    font-weight: 600;
    color: var(--ink);
    letter-spacing: -0.025em;
    line-height: 1.15;
    margin-bottom: 1.1rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid var(--rule);
}
.ling-subsection-title {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--ink-soft);
    letter-spacing: -0.01em;
    margin-bottom: 0.7rem;
    margin-top: 0;
}

/* ─────────────────────────────────────────────────────────────
   CONTENT CARD
───────────────────────────────────────────────────────────── */
.ling-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 5px;
    padding: 1.3rem 1.55rem;
    margin-bottom: 0.85rem;
    box-shadow:
        0 1px 3px rgba(26,22,18,0.05),
        0 3px 10px rgba(26,22,18,0.04),
        inset 0 1px 0 rgba(255,255,255,0.65);
    transition: transform 0.22s cubic-bezier(0.4,0,0.2,1),
                box-shadow 0.22s cubic-bezier(0.4,0,0.2,1),
                border-color 0.22s ease;
}
.ling-card:hover {
    transform: translateY(-2px);
    box-shadow:
        0 2px 6px rgba(26,22,18,0.07),
        0 8px 24px rgba(26,22,18,0.09),
        inset 0 1px 0 rgba(255,255,255,0.8);
    border-color: rgba(26,22,18,0.16);
}
.ling-card p, .ling-card li {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.08rem;
    color: var(--ink-soft);
    line-height: 1.72;
    margin-bottom: 0.45rem;
}
.ling-card p:last-child, .ling-card li:last-child { margin-bottom: 0; }
.ling-card ul { padding-left: 1.3rem; margin: 0; }
.ling-card li::marker { color: var(--accent); }

/* ─────────────────────────────────────────────────────────────
   HIGHLIGHT CALLOUT (terracotta accent)
───────────────────────────────────────────────────────────── */
.ling-callout {
    background: var(--accent-pale);
    border: 1px solid rgba(184,92,56,0.2);
    border-left: 3px solid var(--accent);
    border-radius: 4px;
    padding: 1.05rem 1.45rem;
    margin-bottom: 0.85rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.ling-callout:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(184,92,56,0.1);
}
.ling-callout-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: var(--accent);
    margin-bottom: 0.4rem;
}
.ling-callout p {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.1rem;
    font-style: italic;
    color: var(--ink);
    line-height: 1.6;
    margin: 0;
}

/* ─────────────────────────────────────────────────────────────
   INFO PANEL (teal, neutral observation)
───────────────────────────────────────────────────────────── */
.ling-info {
    background: rgba(46,107,122,0.05);
    border: 1px solid rgba(46,107,122,0.18);
    border-left: 3px solid var(--teal);
    border-radius: 4px;
    padding: 0.95rem 1.35rem;
    margin-bottom: 0.85rem;
}
.ling-info p {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.05rem;
    color: var(--ink-soft);
    line-height: 1.68;
    margin: 0;
}

/* ─────────────────────────────────────────────────────────────
   FORMULA CARD
───────────────────────────────────────────────────────────── */
.ling-formula {
    background: var(--parchment-2);
    border: 1px solid var(--rule-strong);
    border-radius: 4px;
    padding: 1.05rem 1.4rem;
    margin-bottom: 0.85rem;
    display: flex;
    align-items: flex-start;
    gap: 1.2rem;
}
.ling-formula-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--ink-faint);
    flex-shrink: 0;
    padding-top: 0.2rem;
    min-width: 3.5rem;
    text-align: right;
}
.ling-formula-rule {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.98rem;
    color: var(--ink);
    line-height: 1.6;
    flex: 1;
}
.ling-formula-rule em {
    font-style: normal;
    color: var(--accent);
    font-weight: 500;
}

/* ─────────────────────────────────────────────────────────────
   EXAMPLE BLOCK
───────────────────────────────────────────────────────────── */
.ling-examples {
    background: var(--parchment-2);
    border: 1px solid var(--rule);
    border-left: 3px solid var(--ink-faint);
    border-radius: 4px;
    padding: 0.95rem 1.35rem;
    margin-bottom: 0.85rem;
}
.ling-examples-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.13em;
    color: var(--ink-faint);
    margin-bottom: 0.5rem;
}
.ling-ex-line {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.95rem;
    color: var(--ink-soft);
    line-height: 1.75;
}
.ling-ex-line .num {
    color: var(--accent);
    font-weight: 500;
    display: inline-block;
    min-width: 2.5rem;
}
.ling-ex-line .word { color: var(--ink); }
.ling-ex-line .gloss {
    color: var(--ink-muted);
    font-style: italic;
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 0.92rem;
    margin-left: 0.75rem;
}

/* ─────────────────────────────────────────────────────────────
   TWO-COLUMN GRID
───────────────────────────────────────────────────────────── */
.ling-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    margin-bottom: 0.85rem;
}
@media (max-width: 600px) { .ling-grid-2 { grid-template-columns: 1fr; } }

/* ─────────────────────────────────────────────────────────────
   PROPERTY LIST
───────────────────────────────────────────────────────────── */
.ling-props {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0.5rem 1.25rem;
    align-items: baseline;
    margin: 0;
    padding: 0;
}
.ling-prop-key {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--ink-faint);
    white-space: nowrap;
}
.ling-prop-val {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.05rem;
    color: var(--ink-soft);
    line-height: 1.45;
}
.ling-prop-val strong { color: var(--ink); font-weight: 600; }

/* ─────────────────────────────────────────────────────────────
   MORPHEME ROW
───────────────────────────────────────────────────────────── */
.ling-morph-table { margin-bottom: 0; }
.ling-morph-row {
    display: grid;
    grid-template-columns: 6rem 1.5rem 6rem 1fr;
    align-items: center;
    gap: 0.5rem 1rem;
    padding: 0.45rem 0;
    border-bottom: 1px solid var(--rule);
}
.ling-morph-row:last-child { border-bottom: none; }
.ling-morph-source {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.93rem;
    color: var(--ink);
}
.ling-morph-arrow {
    color: var(--ink-faint);
    font-size: 0.85rem;
    text-align: center;
}
.ling-morph-target {
    font-family: 'DM Mono', 'Courier New', monospace;
    font-size: 0.93rem;
    color: var(--accent);
    font-weight: 500;
}
.ling-morph-gloss {
    font-family: 'Crimson Pro', Georgia, serif;
    font-style: italic;
    font-size: 0.92rem;
    color: var(--ink-muted);
}

/* ─────────────────────────────────────────────────────────────
   NAVIGATION FOOTER
───────────────────────────────────────────────────────────── */
.ling-nav-footer {
    display: flex;
    gap: 0.75rem;
    padding: 1.4rem 0 0.5rem 0;
    border-top: 1px solid var(--rule);
    margin-top: 2.5rem;
    flex-wrap: wrap;
}
.ling-nav-btn {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: var(--ink);
    background: var(--parchment-2);
    border: 1.5px solid var(--rule-strong);
    border-radius: 3px;
    padding: 0.55rem 1.1rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    white-space: nowrap;
    cursor: pointer;
    box-shadow: 2px 2px 0 rgba(26,22,18,0.08);
    transition: all 0.18s cubic-bezier(0.4,0,0.2,1);
}
.ling-nav-btn:hover {
    background: var(--ink);
    color: var(--parchment);
    border-color: var(--ink);
    box-shadow: 3px 3px 0 var(--accent);
    transform: translate(-1px, -1px);
    text-decoration: none;
}
.ling-nav-btn.active {
    background: var(--parchment-3);
    color: var(--ink-muted);
    cursor: default;
    box-shadow: none;
}
.ling-nav-btn.active:hover {
    transform: none;
    background: var(--parchment-3);
    color: var(--ink-muted);
    border-color: var(--rule-strong);
    box-shadow: none;
}
</style>
"""