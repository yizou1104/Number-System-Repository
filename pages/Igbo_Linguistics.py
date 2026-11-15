import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Igbo Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
st.markdown("""
<style>
/* Charis SIL, subset to the characters in Ndimele's transcriptions, for the Échiè table */
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=%20%28%29abeilmnorstu~%C3%A0%C3%AC%C3%B9%C4%81%C5%AB%C7%B9%C9%94%C9%A3%CA%83%CA%8A%CA%B0%CC%80%CC%81%CC%84&display=swap');
div[data-testid="stTable"]:has(tbody tr:nth-child(12)) td:nth-child(2),
div[data-testid="stTable"]:has(tbody tr:nth-child(12)) td:nth-child(2) p { font-family: 'Charis SIL', serif !important; }
</style>
""", unsafe_allow_html=True)
language_nav("Igbo", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Igbo Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Multiplier Follows</span>
        <span class="ling-tag">Counting by Scores</span>
        <span class="ling-tag">'One' and 'Twenty' Are Nouns</span>
        <span class="ling-tag">Benue–Congo</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 1 — SYSTEM OVERVIEW
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Standard Igbo counts in tens, and the multiplier comes after the unit it multiplies:
    <em>iri abụọ</em>, 'ten two', is 20, just as <em>narị abụọ</em> is 200 and
    <em>puku abụọ</em> 2,000. Counting by scores appears in <em>ọgụ</em>, which a 1964
    course gives as the word for twenty, and in the Igboid variety Échiè it runs on through
    four hundred.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val"><strong>10</strong> — <em>iri</em></span>
        <span class="ling-prop-key">Higher units</span>
        <span class="ling-prop-val"><em>narị</em> 100, <em>puku</em> 1,000</span>
        <span class="ling-prop-key">Order</span>
        <span class="ling-prop-val">Unit first, then the multiplier: <em>narị atọ</em> 300</span>
        <span class="ling-prop-key">Joining</span>
        <span class="ling-prop-val"><em>na</em> 'and': <em>iri abụọ na otu</em> 21</span>
        <span class="ling-prop-key">Counting by scores</span>
        <span class="ling-prop-val"><em>ọgụ</em> 20; in Échiè, <em>nnʊ̀</em> 400</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No word in the sources consulted</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Igbo is a Benue–Congo language of southeastern Nigeria, spoken by about 31 million people
    according to the note in Chan's numeral database. The standard forms on this page are the
    ones Emma Asonye and Queenette Okwaraji (2018) and Ethelbert Kari (1997) gave for that
    database, written here without tone marks.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — ONE TO TEN
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Ten</div>', unsafe_allow_html=True)

st.table({
    "Number": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "Form": ["otu", "abụọ", "atọ", "anọ", "ise", "isii", "asaa", "asatọ", "itoolu", "iri"],
    "Also recorded": ["ofu (Onitsha)", "—", "—", "—", "—", "—", "—", "—", "iteghete", "—"],
})

st.markdown("""
<div class="ling-info">
    <p>Welmers and Welmers's Peace Corps course (1964) notes that counting varies by dialect:
    <em>ofu</em> 'one' comes from the Onitsha area but is often heard elsewhere, and two
    quite different words for nine, one of them <em>iteghete</em>, are each used in fairly
    large areas.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — COMPOSITIONAL RULES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[unit] [multiplier] <em>na</em> [the rest]</span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Value": ["11", "20", "21", "30", "100", "200", "400", "1,000", "2,000"],
    "Form": ["iri na otu", "iri abụọ", "iri abụọ na otu", "iri atọ", "narị", "narị abụọ",
             "narị anọ", "puku", "puku abụọ"],
    "Structure": ["10 + 1", "10 × 2", "10 × 2 + 1", "10 × 3", "100", "100 × 2",
                  "100 × 4", "1,000", "1,000 × 2"],
})

st.markdown("""
<div class="ling-card">
    <p>All three decimal lists in Chan's database put the multiplier after <em>iri</em>,
    <em>narị</em> and <em>puku</em>. Larger numbers join their parts with <em>na</em>,
    largest first; the converter builds them this way, so 1,234 is <em>puku na narị abụọ na
    iri atọ na anọ</em>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Two Numbers That Are Nouns</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Welmers and Welmers (1964) point out that <em>otu</em> 'one' and <em>ọgụ</em>
    'twenty' behave differently from the other numbers. They are nouns — <em>otu</em> means
    something like 'a unit', and <em>ọgụ</em> is a noun the way 'score' is in English — so
    they come before the noun they count, with the tone changes that nouns undergo. The
    other numbers come after the noun.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — COUNTING BY SCORES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Counting by Scores</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Twenty and Four Hundred</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>In the 1964 course the word for twenty is <em>ọgụ</em> (Onitsha <em>ọrụ</em>), not
    <em>iri abụọ</em>. A fuller count by scores is recorded for Échiè, an Igboid variety
    described by Ozo-mekuri Ndimele (2010). It adds the remainder with <em>na</em> and
    multiplies the score by a following number, as Standard Igbo does with ten.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Value": ["20", "21", "25", "30", "40", "50", "60", "100", "200", "400", "800", "1,000"],
    "Échiè (Ndimele)": ["ɔɣʰʊ̄", "ɔɣʰʊ̄ na otù", "ɔɣʰʊ̄ nà ìse", "ɔɣʰʊ̄ na ìri", "ɔɣʰʊ̄ nam̀",
                        "ɔɣʰʊ̄ nam̀ na ìri", "ɔɣʰʊ̄ atɔ", "ɔɣʰʊ̄ ise", "ɔɣʰʊ̄ ìri", "nnʊ̀",
                        "nnʊ̀ nam̀", "nnʊ̀ nam̀ nà ɔɣʰʊ̄ ìri"],
    "Structure": ["20", "20 + 1", "20 + 5", "20 + 10", "20 × 2", "20 × 2 + 10", "20 × 3",
                  "20 × 5", "20 × 10", "400", "400 × 2", "400 × 2 + 20 × 10"],
})

st.markdown("""
<div class="ling-info">
    <p>Forms in Ndimele's transcription, with his tone marks. His entries for 80 and 90 repeat
    the forms for 60 and 70, with <em>atɔ</em> 'three' where four is meant, so the converter
    leaves them out and shows Échiè only for the numbers he recorded consistently.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature": ["1 to 9,999", "0", "10,000 and above", "Alternative forms",
                "Échiè counting by scores", "Tone marks"],
    "Status": ["Implemented", "Not implemented", "Not implemented", "Shown and accepted",
               "Recorded numbers only", "Accepted, not shown"],
    "Basis": ["Asonye and Okwaraji (2018), Kari (1997)",
              "No word in the sources consulted",
              "No word above puku in the sources",
              "ofu, iteghete and ọgụ (Welmers and Welmers 1964)",
              "Ndimele (2010): 1 to 30, 40 to 70, 100, 200, 400, 800, 1,000",
              "Input with or without tone marks and dots is read"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 6 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Chan, Eugene S. L.</strong> <em>Numeral Systems of the World's Languages</em>:
    Igbo. Max Planck Institute for Evolutionary Anthropology. Three lists: Emma Asonye and
    Queenette Okwaraji (2018), Ethelbert E. Kari (1997), and Ozo-mekuri Ndimele (2010) for
    Échiè.</p>
    <p><strong>Welmers, Beatrice F. &amp; William E. Welmers.</strong> 1964. <em>Igbo</em>.
    Preliminary edition. Washington, DC: Peace Corps. ERIC ED233567. Lesson 7: the numbers
    one to twenty, dialect forms, and <em>otu</em> and <em>ọgụ</em> as nouns.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> An earlier version of this page and its
    converter gave subtractive forms such as <em>bere ise n'ọgụ</em> 'take five from a score'
    for 15; no source consulted records them, and Ndimele's count by scores only adds, so they
    were removed. It also listed five words for zero (<em>efu, oruoghoro, ncha, adịgị,
    okpokoro</em>), <em>otu nde</em> for a million and ordinals with <em>nke</em>; these come
    from popular lists rather than the sources above and are left out. The earlier converter
    put the multiplier first (<em>abụọ narị</em>), against every list consulted.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Igbo", "linguistics")
