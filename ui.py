import streamlit as st


# --------------------------------------------------
# Language page registries
# --------------------------------------------------
LANG_PAGES_CONV = {
    "Basque":        "pages/Basque_Converter.py",
    "Bengali":       "pages/Bengali_Converter.py",
    "Chinese":       "pages/Chinese_Converter.py",
    "Esperanto":     "pages/Esperanto_Converter.py",
    "Greek":         "pages/Greek_Converter.py",
    "Hebrew":        "pages/Hebrew_Converter.py",
    "High Valyrian": "pages/High_Valyrian_Converter.py",
    "Hindi":         "pages/Hindi_Converter.py",
    "Igbo":          "pages/Igbo_Converter.py",
    "Inuktitut":     "pages/Inuktitut_Converter.py",
    "Klingon":       "pages/Klingon_Converter.py",
    "Quechua":       "pages/Quechua_Converter.py",
    "Roman":         "pages/Roman_Converter.py",
    "Swahili":       "pages/Swahili_Converter.py",
    "Tamil":         "pages/Tamil_Converter.py",
    "Thai":          "pages/Thai_Converter.py",
    "Tibetan":       "pages/Tibetan_Converter.py",
    "Yoruba":        "pages/Yoruba_Converter.py",
    "Yupik":         "pages/Yupik_Converter.py",
}

LANG_PAGES_LING = {
    "Basque":        "pages/Basque_Linguistics.py",
    "Bengali":       "pages/Bengali_Linguistics.py",
    "Chinese":       "pages/Chinese_Linguistics.py",
    "Esperanto":     "pages/Esperanto_Linguistics.py",
    "Greek":         "pages/Greek_Linguistics.py",
    "Hebrew":        "pages/Hebrew_Linguistics.py",
    "High Valyrian": "pages/High_Valyrian_Linguistics.py",
    "Hindi":         "pages/Hindi_Linguistics.py",
    "Igbo":          "pages/Igbo_Linguistics.py",
    "Inuktitut":     "pages/Inuktitut_Linguistics.py",
    "Klingon":       "pages/Klingon_Linguistics.py",
    "Quechua":       "pages/Quechua_Linguistics.py",
    "Roman":         "pages/Roman_Linguistics.py",
    "Swahili":       "pages/Swahili_Linguistics.py",
    "Tamil":         "pages/Tamil_Linguistics.py",
    "Thai":          "pages/Thai_Linguistics.py",
    "Tibetan":       "pages/Tibetan_Linguistics.py",
    "Yoruba":        "pages/Yoruba_Linguistics.py",
    "Yupik":         "pages/Yupik_Linguistics.py",
}


# --------------------------------------------------
# Global UI styles — Editorial Modernist Design System
# --------------------------------------------------
def apply_global_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

        :root {
            --ink:          #1a1612;
            --ink-soft:     #2e2a25;
            --ink-muted:    #6b6358;
            --ink-faint:    #9c9288;
            --parchment:    #faf7f2;
            --parchment-2:  #f3ede3;
            --parchment-3:  #e9e0d3;
            --accent:       #b85c38;
            --accent-light: #d4794f;
            --accent-pale:  #f2ddd3;
            --accent-glow:  rgba(184, 92, 56, 0.12);
            --rule:         rgba(26, 22, 18, 0.12);
            --rule-strong:  rgba(26, 22, 18, 0.25);
            --card-bg:      rgba(250, 247, 242, 0.92);
            --card-border:  rgba(26, 22, 18, 0.10);
            --card-shadow:  rgba(26, 22, 18, 0.07);
            --card-hover:   rgba(26, 22, 18, 0.13);
            --teal:         #2e6b7a;
            --teal-pale:    #d6eaee;
            --grad-warm:    linear-gradient(135deg, #faf7f2 0%, #f3ede3 60%, #e9e0d3 100%);
        }

        .stApp {
            background-color: var(--parchment);
            background-image:
                url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.022'/%3E%3C/svg%3E"),
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

        section.main > div {
            animation: pageIn 0.45s cubic-bezier(0.22, 1, 0.36, 1) both;
        }
        @keyframes pageIn {
            from { opacity: 0; transform: translateY(10px); }
            to   { opacity: 1; transform: translateY(0);    }
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Crimson Pro', Georgia, serif !important;
            color: var(--ink) !important;
            letter-spacing: -0.02em;
            line-height: 1.15;
        }
        h1 { font-size: 3.4rem !important; font-weight: 700 !important; letter-spacing: -0.035em !important; margin-bottom: 0.5rem !important; }
        h2 { font-size: 2.3rem !important; font-weight: 600 !important; margin-top: 2.5rem !important; margin-bottom: 0.75rem !important; padding-bottom: 0.35rem; border-bottom: 2px solid var(--rule-strong); }
        h3 { font-size: 1.7rem !important; font-weight: 600 !important; color: var(--ink-soft) !important; margin-top: 2rem !important; margin-bottom: 0.6rem !important; }
        h4 { font-size: 1.25rem !important; font-weight: 500 !important; color: var(--ink-muted) !important; font-style: italic; letter-spacing: 0.01em; }

        p, li, .stMarkdown p {
            font-family: 'Crimson Pro', Georgia, serif;
            font-size: 1.1rem;
            color: var(--ink-soft);
            line-height: 1.75;
            margin-bottom: 0.85rem;
        }

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

        em { color: var(--accent); font-style: italic; }

        /* ── BUTTONS ── */
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

        /* ── INPUTS ── */
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
            box-shadow: inset 0 1px 3px rgba(26,22,18,0.04), 0 0 0 3px var(--accent-glow) !important;
            outline: none !important;
        }
        input::placeholder, textarea::placeholder {
            color: var(--ink-faint) !important;
            font-style: italic;
        }

        /* ── CONTAINERS (no lift hover — too distracting on interactive pages) ── */
        div[data-testid="stContainer"] {
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: 6px !important;
            padding: 1.25rem 1.5rem !important;
            box-shadow:
                0 1px 3px var(--card-shadow),
                0 4px 16px rgba(26,22,18,0.05),
                inset 0 1px 0 rgba(255,255,255,0.7) !important;
            backdrop-filter: blur(8px);
            margin-bottom: 0.85rem !important;
        }

        /* ── EXPANDERS ── */
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

        /* ── TABS ── */
        .stTabs [role="tablist"] { border-bottom: 2px solid var(--rule-strong) !important; gap: 0 !important; }
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

        /* ── ALERTS ── */
        .stAlert { border-radius: 4px !important; border: none !important; border-left: 3px solid !important; }
        div[data-testid="stAlert"][data-type="success"] { background: rgba(46, 107, 122, 0.08) !important; border-left-color: var(--teal) !important; }
        div[data-testid="stAlert"][data-type="error"]   { background: rgba(184, 92, 56, 0.08) !important; border-left-color: var(--accent) !important; }
        div[data-testid="stAlert"][data-type="info"]    { background: rgba(26, 22, 18, 0.05) !important; border-left-color: var(--ink-muted) !important; }
        div[data-testid="stAlert"][data-type="warning"] { background: rgba(184, 92, 56, 0.06) !important; border-left-color: var(--accent-light) !important; }
        div[data-testid="stAlert"] p { font-family: 'Crimson Pro', serif !important; font-size: 1.2rem !important; color: var(--ink) !important; }

        /* ── TABLES ── */
        table { border-collapse: collapse !important; width: 100% !important; font-family: 'Crimson Pro', Georgia, serif !important; font-size: 1rem !important; border-radius: 4px !important; overflow: hidden !important; box-shadow: 0 1px 4px var(--card-shadow) !important; }
        th { font-family: 'DM Sans', sans-serif !important; font-size: 0.75rem !important; font-weight: 600 !important; text-transform: uppercase !important; letter-spacing: 0.09em !important; color: var(--ink-muted) !important; background: var(--parchment-2) !important; border-bottom: 2px solid var(--rule-strong) !important; padding: 0.6rem 1rem !important; }
        td { padding: 0.55rem 1rem !important; border-bottom: 1px solid var(--rule) !important; color: var(--ink-soft) !important; }
        tr:last-child td { border-bottom: none !important; }
        tr:hover td { background: var(--parchment-2) !important; }

        /* ── CODE ── */
        code { font-family: 'DM Mono', 'Courier New', monospace !important; font-size: 0.88em !important; background: var(--parchment-2) !important; color: var(--accent) !important; padding: 0.15em 0.4em !important; border-radius: 3px !important; border: 1px solid var(--rule) !important; }
        pre { font-family: 'DM Mono', 'Courier New', monospace !important; background: var(--parchment-2) !important; border: 1px solid var(--rule-strong) !important; border-left: 3px solid var(--accent) !important; border-radius: 4px !important; padding: 1.2rem 1.5rem !important; overflow-x: auto !important; font-size: 0.9rem !important; line-height: 1.6 !important; }
        pre code { background: none !important; border: none !important; padding: 0 !important; color: var(--ink-soft) !important; }

        /* ── DIVIDERS ── */
        hr { border: none !important; border-top: 1px solid var(--rule) !important; margin: 2.5rem 0 !important; }

        /* ── LINKS ── */
        a { color: var(--accent) !important; text-decoration: underline !important; text-decoration-color: var(--accent-pale) !important; text-underline-offset: 3px !important; transition: all 0.18s ease !important; }
        a:hover { color: var(--accent-light) !important; text-decoration-color: var(--accent) !important; }

        /* ── PAGE LINKS ── */
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
        .stPageLink a:hover { color: var(--accent) !important; border-bottom-color: var(--accent) !important; transform: translateX(3px) !important; }

        /* ── RADIO ── */
        div[data-testid="stRadio"] > div { gap: 0.5rem !important; }
        div[data-testid="stRadio"] label { font-family: 'DM Sans', sans-serif !important; font-size: 0.88rem !important; font-weight: 500 !important; color: var(--ink-soft) !important; text-transform: none !important; letter-spacing: 0.01em !important; }

        /* ── MULTISELECT ── */
        div[data-testid="stMultiSelect"] [data-baseweb="tag"] { background: var(--ink) !important; color: var(--parchment) !important; border-radius: 3px !important; font-family: 'DM Sans', sans-serif !important; font-size: 0.78rem !important; font-weight: 600 !important; letter-spacing: 0.05em !important; }

        /* ── SELECTBOX ── */
        div[data-testid="stSelectbox"] > div > div {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.85rem !important;
            background: var(--card-bg) !important;
            border: 1.5px solid var(--rule-strong) !important;
            border-radius: 4px !important;
        }

        /* ── SCROLLBAR ── */
        ::-webkit-scrollbar { width: 7px; height: 7px; }
        ::-webkit-scrollbar-track { background: var(--parchment-2); }
        ::-webkit-scrollbar-thumb { background: var(--parchment-3); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--ink-faint); }

        /* ── HIDE STREAMLIT CHROME ── */
        [data-testid="stSidebar"]                { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        [data-testid="stHeader"]                 { display: none !important; }
        [data-testid="stToolbar"]                { display: none !important; }
        #MainMenu                                { display: none !important; }
        footer                                   { display: none !important; }

        [data-testid="stAppViewContainer"] > section.main { padding-top: 0.5rem !important; }
        .main .block-container { max-width: 100% !important; padding-left: 2.5rem !important; padding-right: 2.5rem !important; }

        /* ── LANGUAGE NAV BAR ── */
        .lang-nav-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.55rem 0 0.75rem 0;
            margin-bottom: 0.25rem;
            border-bottom: 1px solid var(--rule);
        }
        .lang-nav-crumb {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: var(--ink-faint);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .lang-nav-crumb a {
            color: var(--ink-muted) !important;
            text-decoration: none !important;
            border-bottom: none !important;
            transition: color 0.15s ease !important;
        }
        .lang-nav-crumb a:hover { color: var(--accent) !important; }
        .lang-nav-crumb .sep { color: var(--rule-strong); }

        /* ── OLYMPIAD TAG PILLS ── */
        .tag-pill {
            display: inline-flex;
            align-items: center;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.65rem;
            font-weight: 600;
            letter-spacing: 0.07em;
            text-transform: uppercase;
            padding: 0.18rem 0.55rem;
            border-radius: 2px;
            background: var(--parchment-3);
            color: var(--ink-muted);
            border: 1px solid var(--rule);
            margin-right: 0.3rem;
            margin-bottom: 0.3rem;
        }
        .tag-pill.diff-easy   { background: rgba(46,107,122,0.12);  color: var(--teal);         border-color: rgba(46,107,122,0.25);  }
        .tag-pill.diff-medium { background: rgba(184,140,56,0.12);   color: #8a6520;             border-color: rgba(184,140,56,0.3);   }
        .tag-pill.diff-hard   { background: rgba(184,92,56,0.12);    color: var(--accent);       border-color: rgba(184,92,56,0.25);   }
        .tag-pill.comp        { background: rgba(26,22,18,0.06);      color: var(--ink-soft);     border-color: var(--rule-strong);     }

        </style>
        """,
        unsafe_allow_html=True,
    )
    # Footer nav cards are used by converter, linguistics and Olympiad pages.
    st.markdown(NAV_CARD_CSS, unsafe_allow_html=True)


# ── LANGUAGE NAV ─────────────────────────────────────────────
def language_nav(current: str, mode: str = "converter"):
    """
    Render a compact breadcrumb + language picker at the top of a page.
    current: the display name of the active language (e.g. "Hebrew")
    mode: "converter" or "linguistics"
    """
    pages = LANG_PAGES_CONV if mode == "converter" else LANG_PAGES_LING
    lang_list = sorted(pages.keys())
    idx = lang_list.index(current) if current in lang_list else 0
    mode_label = "Converter" if mode == "converter" else "Linguistics"

    crumb_col, pick_col = st.columns([3, 1])
    with crumb_col:
        st.markdown(
            f'<div class="lang-nav-crumb">'
            f'<a href="/" target="_self">Home</a>'
            f'<span class="sep">›</span>'
            f'{current}'
            f'<span class="sep">›</span>'
            f'{mode_label}'
            f'</div>',
            unsafe_allow_html=True,
        )
    with pick_col:
        selected = st.selectbox(
            "Jump to language",
            lang_list,
            index=idx,
            key=f"lnav_{current}_{mode}",
            label_visibility="collapsed",
        )
        if selected != current:
            st.switch_page(pages[selected])


# ── HOME NAV ─────────────────────────────────────────────────
def home_nav():
    st.markdown(
        '<div class="nav-card-footer">'
        '<a class="nav-card-home" href="/" target="_self">← Home</a>'
        '</div>',
        unsafe_allow_html=True,
    )


# ── SHARED LINGUISTICS CSS ────────────────────────────────────
LING_CSS = """
<style>
/* ── PAGE MASTHEAD ── */
.ling-masthead { border-top: 3px solid var(--ink); border-bottom: 1px solid var(--rule); padding: 1.75rem 0 1.4rem 0; margin-bottom: 1.75rem; }
.ling-masthead-eyebrow { font-family: 'DM Sans', sans-serif; font-size: .68rem; font-weight: 700; text-transform: uppercase; letter-spacing: .18em; color: var(--accent); display: flex; align-items: center; gap: .65rem; margin-bottom: .65rem; }
.ling-masthead-eyebrow::before { content: ''; display: inline-block; width: 1.75rem; height: 1.5px; background: var(--accent); flex-shrink: 0; }
.ling-masthead-title { font-family: 'Crimson Pro', Georgia, serif; font-size: 3rem; font-weight: 700; color: var(--ink); letter-spacing: -.04em; line-height: 1.05; margin-bottom: .9rem; }
.ling-masthead-sub { display: none; }
.ling-tags { display: flex; flex-wrap: wrap; gap: .45rem; }
.ling-tag { font-family: 'DM Sans', sans-serif; font-size: .68rem; font-weight: 600; letter-spacing: .07em; text-transform: uppercase; padding: .22rem .7rem; border: 1.5px solid var(--rule-strong); border-radius: 2px; color: var(--ink-soft); background: transparent; }
.ling-tag.accent { border-color: var(--accent); color: var(--accent); background: var(--accent-pale); }

/* ── SECTION DIVIDER ── */
.ling-section-label { font-family: 'DM Sans', sans-serif; font-size: .72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .16em; color: var(--ink-soft); display: flex; align-items: center; gap: 1rem; margin: 2.25rem 0 1.1rem 0; }
.ling-section-label::before { content: ''; display: inline-block; width: 2rem; height: 1px; background: var(--ink-muted); flex-shrink: 0; }
.ling-section-label::after  { content: ''; flex: 1; height: 1px; background: var(--rule); }

/* ── SECTION TITLE ── */
.ling-section-title { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.85rem; font-weight: 600; color: var(--ink); letter-spacing: -.025em; line-height: 1.15; margin-bottom: 1.1rem; padding-bottom: .45rem; border-bottom: 1px solid var(--rule); }
.ling-subsection-title { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.25rem; font-weight: 600; color: var(--ink-soft); letter-spacing: -.01em; margin-bottom: .7rem; margin-top: 0; }

/* ── CONTENT CARD ── */
.ling-card { background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 5px; padding: 1.3rem 1.55rem; margin-bottom: .85rem; box-shadow: 0 1px 3px rgba(26,22,18,.05), 0 3px 10px rgba(26,22,18,.04), inset 0 1px 0 rgba(255,255,255,.65); transition: transform .22s cubic-bezier(.4,0,.2,1), box-shadow .22s cubic-bezier(.4,0,.2,1); }
.ling-card:hover { transform: translateY(-2px); box-shadow: 0 2px 6px rgba(26,22,18,.07), 0 8px 24px rgba(26,22,18,.09), inset 0 1px 0 rgba(255,255,255,.8); border-color: rgba(26,22,18,.16); }
.ling-card p, .ling-card li { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.08rem; color: var(--ink-soft); line-height: 1.72; margin-bottom: .45rem; }
.ling-card p:last-child, .ling-card li:last-child { margin-bottom: 0; }
.ling-card ul { padding-left: 1.3rem; margin: 0; }
.ling-card li::marker { color: var(--accent); }

/* ── HIGHLIGHT CALLOUT ── */
.ling-callout { background: var(--accent-pale); border: 1px solid rgba(184,92,56,.2); border-left: 3px solid var(--accent); border-radius: 4px; padding: 1.05rem 1.45rem; margin-bottom: .85rem; transition: transform .2s ease, box-shadow .2s ease; }
.ling-callout:hover { transform: translateY(-1px); box-shadow: 0 4px 16px rgba(184,92,56,.1); }
.ling-callout-label { font-family: 'DM Sans', sans-serif; font-size: .6rem; font-weight: 700; text-transform: uppercase; letter-spacing: .14em; color: var(--accent); margin-bottom: .4rem; }
.ling-callout p { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.1rem; font-style: italic; color: var(--ink); line-height: 1.6; margin: 0; }

/* ── INFO PANEL ── */
.ling-info { background: rgba(46,107,122,.05); border: 1px solid rgba(46,107,122,.18); border-left: 3px solid var(--teal); border-radius: 4px; padding: .95rem 1.35rem; margin-bottom: .85rem; }
.ling-info p { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.05rem; color: var(--ink-soft); line-height: 1.68; margin: 0; }

/* ── FORMULA CARD ── */
.ling-formula { background: var(--parchment-2); border: 1px solid var(--rule-strong); border-radius: 4px; padding: 1.05rem 1.4rem; margin-bottom: .85rem; display: flex; align-items: flex-start; gap: 1.2rem; }
.ling-formula-label { font-family: 'DM Sans', sans-serif; font-size: .6rem; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--ink-faint); flex-shrink: 0; padding-top: .2rem; min-width: 3.5rem; text-align: right; }
.ling-formula-rule { font-family: 'DM Mono', 'Courier New', monospace; font-size: .98rem; color: var(--ink); line-height: 1.6; flex: 1; }
.ling-formula-rule em { font-style: normal; color: var(--accent); font-weight: 500; }

/* ── EXAMPLE BLOCK ── */
.ling-examples { background: var(--parchment-2); border: 1px solid var(--rule); border-left: 3px solid var(--ink-faint); border-radius: 4px; padding: .95rem 1.35rem; margin-bottom: .85rem; }
.ling-examples-label { font-family: 'DM Sans', sans-serif; font-size: .6rem; font-weight: 700; text-transform: uppercase; letter-spacing: .13em; color: var(--ink-faint); margin-bottom: .5rem; }
.ling-ex-line { font-family: 'DM Mono', 'Courier New', monospace; font-size: .95rem; color: var(--ink-soft); line-height: 1.75; }
.ling-ex-line .num { color: var(--accent); font-weight: 500; display: inline-block; min-width: 2.5rem; }
.ling-ex-line .word { color: var(--ink); }
.ling-ex-line .gloss { color: var(--ink-muted); font-style: italic; font-family: 'Crimson Pro', Georgia, serif; font-size: .92rem; margin-left: .75rem; }

/* ── TWO-COLUMN GRID ── */
.ling-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; margin-bottom: .85rem; }
@media (max-width: 600px) { .ling-grid-2 { grid-template-columns: 1fr; } }

/* ── PROPERTY LIST ── */
.ling-props { display: grid; grid-template-columns: auto 1fr; gap: .5rem 1.25rem; align-items: baseline; margin: 0; padding: 0; }
.ling-prop-key { font-family: 'DM Sans', sans-serif; font-size: .68rem; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--ink-faint); white-space: nowrap; }
.ling-prop-val { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.05rem; color: var(--ink-soft); line-height: 1.45; }
.ling-prop-val strong { color: var(--ink); font-weight: 600; }

/* ── MORPHEME ROW ── */
.ling-morph-table { margin-bottom: 0; }
.ling-morph-row { display: grid; grid-template-columns: 6rem 1.5rem 6rem 1fr; align-items: center; gap: .5rem 1rem; padding: .45rem 0; border-bottom: 1px solid var(--rule); }
.ling-morph-row:last-child { border-bottom: none; }
.ling-morph-source { font-family: 'DM Mono', 'Courier New', monospace; font-size: .93rem; color: var(--ink); }
.ling-morph-arrow  { color: var(--ink-faint); font-size: .85rem; text-align: center; }
.ling-morph-target { font-family: 'DM Mono', 'Courier New', monospace; font-size: .93rem; color: var(--accent); font-weight: 500; }
.ling-morph-gloss  { font-family: 'Crimson Pro', Georgia, serif; font-style: italic; font-size: .92rem; color: var(--ink-muted); }

</style>
"""

# ── SHARED FOOTER NAV CARDS (converter + linguistics pages) ───
NAV_CARD_CSS = """
<style>
/* Footer navigation block: a full-width destination card + a short Home card */
.nav-card-footer {
    border-top: 1px solid var(--rule);
    margin-top: 2.75rem;
    padding-top: 1.75rem;
}

/* Large destination card — white background, soft shadow border */
.nav-card {
    display: block;
    background: rgba(255,255,255,.96);
    border: 1px solid var(--card-border);
    border-top: 3px solid var(--accent);
    border-radius: 6px;
    padding: 1.5rem 1.8rem;
    text-decoration: none !important;
    box-shadow:
        0 1px 3px rgba(26,22,18,.05),
        0 5px 18px rgba(26,22,18,.06),
        inset 0 1px 0 rgba(255,255,255,.8);
    transition: all .22s cubic-bezier(.4,0,.2,1);
}
.nav-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 26px rgba(26,22,18,.11);
    border-color: rgba(26,22,18,.17);
    text-decoration: none !important;
}
.nav-card-eyebrow { font-family: 'DM Sans', sans-serif; font-size: .62rem; font-weight: 700; text-transform: uppercase; letter-spacing: .14em; color: var(--accent); margin-bottom: .4rem; }
.nav-card-title   { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.45rem; font-weight: 600; color: var(--ink); margin-bottom: .3rem; letter-spacing: -.02em; }
.nav-card-desc    { font-family: 'Crimson Pro', Georgia, serif; font-size: 1.02rem; color: var(--ink-muted); line-height: 1.55; margin: 0 0 .6rem 0; }
.nav-card-cta     { font-family: 'DM Sans', sans-serif; font-size: .74rem; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: var(--accent); }

/* Short Home card — same treatment, sized to its label */
.nav-card-home {
    display: inline-flex;
    align-items: center;
    gap: .5rem;
    margin-top: .85rem;
    background: rgba(255,255,255,.96);
    border: 1px solid var(--card-border);
    border-top: 3px solid var(--ink-muted);
    border-radius: 6px;
    padding: .8rem 1.7rem;
    font-family: 'DM Sans', sans-serif;
    font-size: .78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--ink) !important;
    text-decoration: none !important;
    box-shadow:
        0 1px 3px rgba(26,22,18,.05),
        0 5px 18px rgba(26,22,18,.06),
        inset 0 1px 0 rgba(255,255,255,.8);
    transition: all .22s cubic-bezier(.4,0,.2,1);
}
.nav-card-home:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 26px rgba(26,22,18,.11);
    border-color: rgba(26,22,18,.17);
    color: var(--accent) !important;
    text-decoration: none !important;
}
</style>
"""


# ── CONVERTER CSS ADDITIONS (appended by each converter page) ─
CONV_CSS_ADDITIONS = """
<style>
/* Two-pane layout: give converter pages room for a large result panel */
.main .block-container { max-width: 1500px !important; padding-left: 3rem !important; padding-right: 3rem !important; margin: 0 auto !important; }

/* The direction selector now lives at the top of the right pane */
.conv-section-label.conv-direction-label { margin-top: 0 !important; }

/* Empty state shown in right pane before user types — matches result height */
.conv-empty-state {
    background: var(--parchment-2);
    border: 1px dashed var(--rule-strong);
    border-radius: 6px;
    padding: 2.5rem 1.75rem;
    text-align: center;
    margin-top: 0.5rem;
    min-height: 340px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.conv-empty-state p {
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 1.25rem;
    font-style: italic;
    color: var(--ink-faint);
    margin: 0;
    line-height: 1.55;
}

/* ── ENLARGED RESULT PANEL ── */
.conv-result-card {
    min-height: 340px !important;
    margin-top: .5rem !important;
    padding: 1.75rem 2rem !important;
    border-radius: 0 6px 6px 0 !important;
    display: flex !important;
    flex-direction: column;
    justify-content: center;
}
.conv-result-label {
    font-size: .72rem !important;
    letter-spacing: .16em !important;
    margin-bottom: 1.15rem !important;
}
.conv-result-row {
    grid-template-columns: 7.5rem 1fr !important;
    gap: .4rem 1.25rem !important;
    padding: .6rem 0 !important;
    border-bottom: 1px solid rgba(46,107,122,.13);
}
.conv-result-row:last-child { border-bottom: none; }
.conv-result-sublabel { font-size: .68rem !important; letter-spacing: .12em !important; }
.conv-result-subvalue { font-size: 1.55rem !important; line-height: 1.4 !important; }
/* Single-value results — .conv-result-value is the older class name, still
   used by most converters; both render one value, so they share the styling. */
.conv-result-single,
.conv-result-value {
    font-size: 2.2rem !important;
    font-weight: 600 !important;
    line-height: 1.25 !important;
    text-align: center;
    word-break: break-word;
}
.conv-error-card { min-height: 340px; display: flex; align-items: center; justify-content: center; }
.conv-error-text { font-size: 1.2rem !important; text-align: center; }
</style>
"""

# ── LINGUISTICS PAGE WIDTH CSS ────────────────────────────────
LING_WIDTH_CSS = """
<style>
/* Constrain linguistics pages to comfortable reading width */
.main .block-container { max-width: 900px !important; padding-left: 3rem !important; padding-right: 3rem !important; margin: 0 auto !important; }
</style>
"""


# ── FOOTER NAV ────────────────────────────────────────────────
def footer_nav(lang: str, mode: str = "converter"):
    """
    Render the page footer: a full-width card linking to the companion page,
    with a shorter Home card beneath it.

    lang: display name of the language (e.g. "High Valyrian")
    mode: the page this is rendered on — "converter" links out to linguistics,
          "linguistics" links back to the converter.
    """
    slug = lang.replace(" ", "_")
    if mode == "converter":
        href, eyebrow = f"/{slug}_Linguistics", "Linguistic Structure"
        title = f"How do {lang} numerals work?"
        desc = (f"Explore the grammar rules, morphological patterns, "
                f"and cultural context behind {lang} numbers.")
        cta = f"Explore {lang} Linguistics →"
    else:
        href, eyebrow = f"/{slug}_Converter", "Numeral Converter"
        title = f"Convert {lang} numerals"
        desc = (f"Try the rules in practice — convert between Arabic numerals "
                f"and {lang} in both directions.")
        cta = f"Open the {lang} Converter →"

    st.markdown(
        f'<div class="nav-card-footer">'
        f'<a class="nav-card" href="{href}" target="_self">'
        f'<div class="nav-card-eyebrow">{eyebrow}</div>'
        f'<div class="nav-card-title">{title}</div>'
        f'<div class="nav-card-desc">{desc}</div>'
        f'<div class="nav-card-cta">{cta}</div>'
        f'</a>'
        f'<a class="nav-card-home" href="/" target="_self">← Home</a>'
        f'</div>',
        unsafe_allow_html=True,
    )
