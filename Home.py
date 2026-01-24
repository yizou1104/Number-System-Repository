import streamlit as st

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="The Number System Repository",
    layout="wide"
)

# --------------------------------------------------
# Minimal typography polish (NO italics)
# --------------------------------------------------
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Source Serif 4", "Georgia", serif;
    }

    .family-title {
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 12px;
    }

    .language-box {
        padding: 8px 14px;
        border-radius: 10px;
        border: 1px solid #DDD;
        margin-bottom: 8px;
        font-size: 16px;
    }

    .language-box:hover {
        background-color: #F7F7F7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("The Number System Repository")

# --------------------------------------------------
# Purpose box
# --------------------------------------------------
with st.container(border=True):
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
def family_card(title, languages, family_page):
    with st.container(border=True):
        st.markdown(f"<div class='family-title'>{title}</div>", unsafe_allow_html=True)

        for lang_name, lang_page in languages:
            language_box(lang_name, lang_page)

        st.write("")
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
        "pages/Family_Sino_Tibetan.py"
    )

    family_card(
        "Niger-Congo Systems (Africa)",
        [
            ("Yoruba", "pages/Yoruba_Converter.py"),
            ("Igbo", "pages/Igbo_Converter.py"),
            ("Swahili", "pages/Swahili_Converter.py"),
        ],
        "pages/Family_Niger_Congo.py"
    )

with col2:
    family_card(
        "Indo-Aryan & Dravidian (South Asia)",
        [
            ("Hindi", "pages/Hindi_Converter.py"),
            ("Bengali", "pages/Bengali_Converter.py"),
            ("Tamil", "pages/Tamil_Converter.py"),
        ],
        "pages/Family_Indo_Aryan.py"
    )

    family_card(
        "Ancient & Classical Systems",
        [
            ("Roman", "pages/Roman_Converter.py"),
            ("Greek", "pages/Greek_Converter.py"),
            ("Babylonian", "pages/Babylonian_Converter.py"),
        ],
        "pages/Family_Ancient_Classical.py"
    )

# --------------------------------------------------
# Language Isolates
# --------------------------------------------------
family_card(
    "Language Isolates",
    [
        ("Basque", "pages/Basque_Converter.py"),
        ("Ainu", "pages/Ainu_Converter.py"),
        ("Sumerian", "pages/Sumerian_Converter.py"),
    ],
    "pages/Family_Language_Isolates.py"
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Numeral systems explored for linguistic structure, cultural context, "
    "and Olympiad-level problem solving."
)