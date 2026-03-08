import streamlit as st
from ui import apply_global_styles

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="The Number System Repository",
    layout="wide"
)

apply_global_styles()

# --------------------------------------------------
# Additional page-specific styles
# --------------------------------------------------
st.markdown(
    """
    <style>
    .hero {
        padding: 1.5rem 1.75rem;
        border: 2px solid #111827;
        border-radius: 22px;
        background: rgba(255, 255, 255, 0.95);
        box-shadow: 12px 12px 0 rgba(17, 24, 39, 0.18);
        margin-bottom: 1.5rem;
        position: relative;
    }

    .hero-badge {
        display: inline-block;
        padding: 0.35rem 0.75rem;
        border-radius: 999px;
        background: #ffe066;
        border: 2px solid #111827;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.02em;
        color: #111827;
    }

    .hero-title {
        font-size: 2.75rem;
        font-weight: 800;
        margin: 0.75rem 0 0.5rem 0;
        color: #111827;
        line-height: 1.1;
    }

    .hero-sub {
        font-size: 1.1rem;
        color: #1f2937;
        margin-bottom: 1rem;
    }

    .hero-chips {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-top: 0.5rem;
    }

    .hero-chip {
        padding: 0.35rem 0.65rem;
        border-radius: 999px;
        border: 2px solid #111827;
        font-weight: 600;
        font-size: 0.85rem;
        background: #e0fbfc;
        color: #111827;
    }

    .family-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 16px;
        color: #111827;
        letter-spacing: -0.01em;
    }

    .language-box {
        padding: 14px 20px;
        border-radius: 12px;
        border: 1px solid rgba(99, 102, 241, 0.15);
        margin-bottom: 12px;
        font-size: 1rem;
        font-weight: 500;
        color: #0f172a;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.08);
        position: relative;
        overflow: hidden;
    }

    .language-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(224, 231, 255, 0.5), transparent);
        transition: left 0.5s ease;
    }

    .language-box:hover::before {
        left: 100%;
    }

    .language-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.18);
        border-color: rgba(99, 102, 241, 0.3);
        background: rgba(255, 255, 255, 0.98);
    }

    .purpose-box {
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 12px rgba(99, 102, 241, 0.1);
        color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Hero section
# --------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <span class="hero-badge">Number Systems Studio</span>
        <div class="hero-title">Explore how cultures count, speak, and reason with numbers.</div>
        <div class="hero-sub">
            Converters, linguistic explanations, and Olympiad-style problems curated for deep learning and playful discovery.
        </div>
        <div class="hero-chips">
            <span class="hero-chip">Converters</span>
            <span class="hero-chip">Linguistics</span>
            <span class="hero-chip">Olympiad Problems</span>
            <span class="hero-chip">Multicultural</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("The Number System Repository")

# --------------------------------------------------
# Purpose
# --------------------------------------------------
st.markdown("### Purpose of the App")
st.write(
    "Explore how different cultures represent numbers. "
    "This repository combines numeral converters, linguistic explanations, "
    "and Olympiad-style problems to support both rigorous study and "
    "general exploration."
)

st.write("")

# --------------------------------------------------
# Helper: boxed language link
# --------------------------------------------------
def language_box(label, page):
    with st.container(border=True):
        st.page_link(page, label=label)

# --------------------------------------------------
# Helper: family card
# --------------------------------------------------
def family_card(title, languages, family_page=None):
    with st.container(border=True):
        st.markdown(f"<div class='family-title'>{title}</div>", unsafe_allow_html=True)

        for lang_name, lang_page in languages:
            language_box(lang_name, lang_page)

        st.write("")
        if family_page:
            st.page_link(family_page, label="Explore all languages →")

# --------------------------------------------------
# Language Families
# --------------------------------------------------
st.header("Language Families")

col1, col2 = st.columns(2, gap="large")

with col1:
    family_card(
        "Sino-Tibetan & East Asian Systems",
        [
            ("Chinese", "pages/Chinese_Converter.py"),
            ("Tibetan", "pages/Tibetan_Converter.py"),
            ("Thai", "pages/Thai_Converter.py"),
        ],
        None
    )

    family_card(
        "Niger-Congo Systems (Africa)",
        [
            ("Yoruba", "pages/Yoruba_Converter.py"),
            ("Igbo", "pages/Igbo_Converter.py"),
            ("Swahili", "pages/Swahili_Converter.py"),
        ],
        None
    )

with col2:
    family_card(
        "Indo-Aryan & Dravidian (South Asia)",
        [
            ("Hindi", "pages/Hindi_Converter.py"),
            ("Bengali", "pages/Bengali_Converter.py"),
            ("Tamil", "pages/Tamil_Converter.py"),
        ],
        None
    )

    family_card(
        "Ancient & Classical Systems",
        [
            ("Roman", "pages/Roman_Converter.py"),
            ("Greek", "pages/Greek_Converter.py"),
        ],
        None
    )

# --------------------------------------------------
# Language Isolates
# --------------------------------------------------
family_card(
    "Language Isolates",
    [
        ("Basque", "pages/Basque_Converter.py"),
    ],
    None
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Numeral systems explored for linguistic structure, cultural context, "
    "and Olympiad-level problem solving."
)
