import streamlit as st
from ui import apply_global_styles, home_nav, LING_CSS

st.set_page_config(page_title="High Valyrian Numerals — Linguistics", layout="centered")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)

# ── MASTHEAD ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">High Valyrian Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Constructed Language</span>
        <span class="ling-tag">Limited Canon</span>
        <span class="ling-tag">Inflectional</span>
        <span class="ling-tag">Macron Vowels</span>
        <span class="ling-tag">Range 1–10 only</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — SYSTEM OVERVIEW ──────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Language With Limited Numbers</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Honest Caveat</div>
    <p>High Valyrian (Valyrio) is the most extensively-developed of the
    languages created for HBO's <em>Game of Thrones</em>, but its numeral
    system is sparse. Numerals 1–10 are documented; <strong>no canonical
    compositional system has been published for numbers above 10</strong>.
    This page restricts itself to the published canon — we do not invent
    forms.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Created by</span>
        <span class="ling-prop-val"><strong>David J. Peterson</strong>, 2012 — for HBO's <em>Game of Thrones</em></span>
        <span class="ling-prop-key">Native name</span>
        <span class="ling-prop-val">Valyrio · Valyrio Eglio ("High Valyrian")</span>
        <span class="ling-prop-key">In-fiction status</span>
        <span class="ling-prop-val">Liturgical and historical language of the Targaryen dynasty</span>
        <span class="ling-prop-key">Real-world status</span>
        <span class="ling-prop-val">Active development; Duolingo course since 2017</span>
        <span class="ling-prop-key">Numeral range published</span>
        <span class="ling-prop-val">1–10 attested · 11+ not canonically defined</span>
        <span class="ling-prop-key">Morphology</span>
        <span class="ling-prop-val">Heavily inflectional — numerals likely take case in real use</span>
        <span class="ling-prop-key">Orthography</span>
        <span class="ling-prop-val">Latin-based with macrons (ē, ā, ī, ō, ū) for long vowels; ñ for palatal nasal</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — NUMERALS ─────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Attested Numerals</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The Published Forms</div>', unsafe_allow_html=True)

st.table({
    "Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Valyrian": ["mēre", "tymptir", "hāre", "rytsas", "tōme",
                 "byssa", "jēdar", "ōñoso", "glaeson", "vōre"],
    "Confidence": ["HIGH", "HIGH", "HIGH",
                   "MEDIUM", "MEDIUM", "MEDIUM",
                   "MEDIUM", "MEDIUM", "MEDIUM", "MEDIUM"],
})

st.markdown("""
<div class="ling-info">
    <p>HIGH-confidence forms (1–3) appear directly in Peterson's published
    materials and the Duolingo course. MEDIUM-confidence forms (4–10) are
    consistent across community sources but with less direct attestation.
    Where a form has dialect variants in the sources (e.g. <em>tymptir</em> /
    <em>tymī</em> in compound contexts), the most commonly cited
    citation form is shown.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 3 — PHONOLOGY ────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Phonology &amp; Orthography</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Reading the Forms</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Valyrian phonology uses a set of features unfamiliar to many natural
    European languages, including:</p>
    <ul>
        <li><strong>Long vowels marked with macrons</strong> — <em>mēre</em>,
        <em>hāre</em>, <em>tōme</em>, <em>jēdar</em>, <em>ōñoso</em>,
        <em>vōre</em>. Vowel length is phonemic — <em>ē</em> is a different
        phoneme from <em>e</em>.</li>
        <li><strong>The palatal nasal <em>ñ</em></strong> — appears in
        <em>ōñoso</em> ("eight"). Sounds like the Spanish <em>ñ</em> in
        <em>mañana</em>, or the <em>ny</em> in English "canyon."</li>
        <li><strong>Consonant clusters</strong> — <em>tymptir</em> for "two"
        contains the cluster /mpt/, which is phonotactically marked in many
        languages.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Peterson designed Valyrian's phonology to feel "ancient" and
    "ceremonial" — appropriate for a language whose in-fiction role is
    similar to that of Latin in medieval Europe (a learned, liturgical,
    and high-prestige language no longer in everyday spoken use).</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — INFLECTION ───────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Inflection</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Numerals in Sentences</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Caveat for converter use</div>
    <p>This converter shows citation (uninflected) forms only. In actual
    Valyrian sentences, numerals from 1–4 are reported by Peterson to inflect
    for case, number, and gender of the noun they modify, while higher numbers
    behave somewhat like nouns. Specifics for numerals are not fully published —
    inflectional output is intentionally not attempted here.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Valyrian has eight noun classes (referred to as "genders" in Peterson's
    grammar): lunar, solar, terrestrial, aquatic, plus four collective and
    paucal forms. Numerals 1–4 agreeing with a noun should match the noun's
    class — meaning <em>mēre</em> "one" appears in different forms depending
    on whether you are counting dragons, stars, ships, or fires. A complete
    inflectional paradigm for the lower numerals has not been published,
    though Peterson has discussed the system in general terms.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5 — DEVELOPMENT HISTORY ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Development</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">From Page to Screen to Duolingo</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>George R. R. Martin used a few Valyrian phrases in <em>A Song of Ice
    and Fire</em> (e.g. <em>valar morghulis</em> "all men must die",
    <em>valar dohaeris</em> "all men must serve"), but did not develop a
    grammar. When HBO commissioned a full language for the TV adaptation,
    they hired David J. Peterson, who had earlier built Dothraki for the
    same series.</p>
    <p>Peterson reverse-engineered the canonical phrases into a grammatical
    system, then expanded the language with several thousand vocabulary items.
    The Duolingo High Valyrian course launched in 2017, with Peterson's
    direct involvement, and remains the most accessible introduction.
    Peterson continues to publish material on his blog and via interviews,
    occasionally clarifying or extending the documented language.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Compared to Esperanto (135 years old, 2 million speakers) or Klingon
    (40 years, an active institute and translated literature), High Valyrian
    is young — but it has the advantage of a steady stream of new content
    from a still-active creator. Its numeral system above 10 may yet receive
    a canonical extension. For now, this converter respects the published
    boundaries.</p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/High_Valyrian_Converter.py", label="← High Valyrian Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)
