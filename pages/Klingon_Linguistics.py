import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Klingon Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Klingon", "linguistics")

# ── MASTHEAD ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Klingon Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Constructed Language</span>
        <span class="ling-tag">Magnitude Suffix</span>
        <span class="ling-tag">Case-Sensitive</span>
        <span class="ling-tag">Retconned History</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — SYSTEM OVERVIEW ──────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Klingon has no standalone word for "ten" — instead, magnitude is
    expressed by suffixes (<em>maH</em> = 10, <em>vatlh</em> = 100, <em>SaD</em>
    = 1,000) attached directly to digit roots. Compound numbers like
    <em>cha'maH</em> ("two-ten" = 20) are single phonological words formed
    by suffixation, not by separate digit + place-name.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Created by</span>
        <span class="ling-prop-val"><strong>Marc Okrand</strong>, 1984 (for <em>Star Trek III</em>)</span>
        <span class="ling-prop-key">Native name</span>
        <span class="ling-prop-val">tlhIngan Hol — "Klingon language"</span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Decimal (post-1992 retcon — see history below)</span>
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val">10</span>
        <span class="ling-prop-key">Magnitude marking</span>
        <span class="ling-prop-val">Suffixes attached to digit roots — no standalone "ten"</span>
        <span class="ling-prop-key">Word formation</span>
        <span class="ling-prop-val">Each magnitude unit = one word; multi-magnitude numbers use spaces</span>
        <span class="ling-prop-key">Orthography</span>
        <span class="ling-prop-val">Strictly case-sensitive — capitals denote phonemes</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — DIGITS & SUFFIXES ────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Digits &amp; Magnitude Suffixes</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The Building Blocks</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Digit Roots (0–9)</div>', unsafe_allow_html=True)
st.table({
    "Number": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Klingon": ["pagh", "wa'", "cha'", "wej", "loS",
                "vagh", "jav", "Soch", "chorgh", "Hut"],
})

st.markdown("""
<div class="ling-info">
    <p>Note the apostrophe <em>'</em> in <em>wa'</em> and <em>cha'</em> — this
    is the glottal stop, a full consonant in Klingon (not punctuation). Capital
    letters mark distinct phonemes: <em>S</em> is a retroflex sibilant,
    <em>H</em> is a uvular fricative, <em>Q</em> is a different sound from
    <em>q</em>, <em>D</em> is retroflex. The orthography is unforgiving —
    typing "soch" is incorrect; only "Soch" parses as the digit 7.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Magnitude Suffixes</div>', unsafe_allow_html=True)
st.table({
    "Value": ["10", "100", "1,000", "10,000", "100,000", "1,000,000"],
    "Suffix": ["maH", "vatlh", "SaD", "netlh", "bIp", "'uy'"],
})

st.markdown("""
<div class="ling-info">
    <p>Klingon's magnitude system is unique among the languages here:
    powers of ten 10¹–10⁶ each have their own dedicated suffix (no
    grouping by 10⁴ as in Chinese, no decimal-only as in Esperanto).
    The suffix <em>'uy'</em> for "million" begins and ends with glottal stops —
    a phonologically marked form for a phonologically marked magnitude.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 3 — COMPOSITIONAL RULES ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Single Magnitude</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[digit] + <em>[suffix]</em> · written as ONE word</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative</div>
    <div class="ling-ex-line"><span class="num">10</span><span class="word">wa'maH</span><span class="gloss">one-ten</span></div>
    <div class="ling-ex-line"><span class="num">30</span><span class="word">wejmaH</span><span class="gloss">three-ten</span></div>
    <div class="ling-ex-line"><span class="num">200</span><span class="word">cha'vatlh</span><span class="gloss">two-hundred</span></div>
    <div class="ling-ex-line"><span class="num">5,000</span><span class="word">vaghSaD</span><span class="gloss">five-thousand</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Multiple Magnitudes</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[high segment] [middle segment] [low segment] · descending order, space-separated</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound numbers</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">cha'maH wa'</span><span class="gloss">two-ten one</span></div>
    <div class="ling-ex-line"><span class="num">234</span><span class="word">cha'vatlh wejmaH loS</span><span class="gloss">two-hundred three-ten four</span></div>
    <div class="ling-ex-line"><span class="num">1,234</span><span class="word">wa'SaD cha'vatlh wejmaH loS</span><span class="gloss">one-thousand two-hundred three-ten four</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>When a magnitude is "skipped" (i.e. that place is zero), no token
    appears in its position. So 101 = <em>wa'vatlh wa'</em> (one-hundred one),
    not <em>wa'vatlh pagh wa'</em>. The zero word <em>pagh</em> appears only
    when the whole number is zero.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — HISTORY ──────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">History</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The 1992 Retcon</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>In <em>The Klingon Dictionary</em> (1985), Marc Okrand presented a
    relatively conventional decimal numeral system. In the 1992 second-edition
    addendum, he revised it: the numbers in the original edition were now said
    to belong to a "scholarly" or "ceremonial" register, while everyday spoken
    Klingon used the magnitude-suffix system documented here.</p>
    <p>This in-universe explanation lets the language evolve while preserving
    older fan-published material. It is rare in linguistics — natural languages
    don't get retconned — but it reflects the hybrid status of Klingon as a
    crafted artifact maintained over decades by an actively-engaged author.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Cultural framing</div>
    <p>Okrand designed Klingon to feel "alien" and "warlike" through phonology
    (heavy use of guttural consonants, retroflexes, glottal stops) and
    morphology (object-verb-subject word order, agglutinative suffix stacking).
    The numeral system reflects this — magnitude suffixes are dense, sounds
    are harsh, and even the digits themselves include glottal-stopped forms
    like <em>wa'</em>, <em>cha'</em>, and the millions suffix <em>'uy'</em>.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5 — STATUS ───────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Community &amp; Status</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Living Constructed Language</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Klingon is one of the most-developed fictional languages, sustained by
    the Klingon Language Institute (KLI), founded in 1992. KLI publishes the
    journal <em>HolQeD</em>, organises annual <em>qep'a'</em> meetings, and has
    overseen translations of Shakespeare's <em>Hamlet</em> and <em>Much Ado
    About Nothing</em>, the <em>Tao Te Ching</em>, and <em>Gilgamesh</em> into
    Klingon.</p>
    <p>Estimates of fluent speakers are low — perhaps 20–30 worldwide — but the
    language has a few children raised partially with Klingon, making it one of
    very few constructed languages with native-like learners besides Esperanto.</p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Klingon", "linguistics")
