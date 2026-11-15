import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Yoruba Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Yoruba", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Yoruba Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Adding and Subtracting</span>
        <span class="ling-tag">Counting Cowries</span>
        <span class="ling-tag">Tonal</span>
        <span class="ling-tag">Round Numbers Before the Noun</span>
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
    <p>Yoruba counts by twenties and builds most numbers from the nearest round number,
    adding up to four or taking away up to five: 21 is <em>oókàn lé lógún</em>, which Bowen
    (1858) glosses 'one laid on twenty', and 16 is <em>ẹẹ́rìn dín lógún</em>, 'four from
    twenty'.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val"><strong>20</strong> — <em>ogún</em></span>
        <span class="ling-prop-key">Adding</span>
        <span class="ling-prop-val">1 to 4 above a round number, with <em>lé</em></span>
        <span class="ling-prop-key">Subtracting</span>
        <span class="ling-prop-val">1 to 5 below the next one, with <em>dín</em>; 50, 70 and 90 are ten below 60, 80 and 100</span>
        <span class="ling-prop-key">Round numbers</span>
        <span class="ling-prop-val"><em>ogún</em> 20, <em>ọgbọ̀n</em> 30, <em>igba</em> 200, and multiples of these</span>
        <span class="ling-prop-key">Tone</span>
        <span class="ling-prop-val">Three level tones: high (á), low (à), mid (unmarked)</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No word in the sources consulted</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Yoruba is spoken by about 45 million people in southwestern Nigeria, Benin and Côte
    d'Ivoire, according to the note in Chan's numeral database. The tone-marked forms on this
    page are the ones Ethelbert Kari gave for that database (1998), taken from Robert G.
    Armstrong's <em>Yoruba Numerals</em> (1962).</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — ONE TO TEN
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Ten</div>', unsafe_allow_html=True)

st.table({
    "Number": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "Form": ["oókan", "eéjì", "ẹẹ́ta", "ẹẹ́rin", "aárùn", "ẹẹ́fà", "ẹẹ́je", "ẹẹ́jọ", "ẹẹ́sàn", "ẹẹ́wàá"],
})

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Counted in Cowries</div>
    <p>Bowen noticed that the first vowel of each of these words is long, and explained it as
    a trace of counting money: they are contractions of <em>owo kan</em>, <em>owo eji</em>
    (his spelling, without tones), 'one cowry, two cowries'. He also suspected that
    seven is five plus two, but left the question open.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — ADDING AND SUBTRACTING
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Arithmetic Operations</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Laid On and Taken From</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[1–4] <em>lé</em> [round number] &nbsp;·&nbsp; [1–4] <em>dín</em> [next round number]</span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Number": ["11", "15", "16", "19", "21", "24", "25", "26", "29"],
    "Form": ["oókàn làá", "ẹ̀ẹ́dogún", "ẹẹ́rìn dín lógún", "oókàn dín lógún", "oókàn lé lógún",
             "ẹẹ́rìn lé lógún", "ẹ̀ẹ́dọ̀ọ́gbọ̀ǹ", "ẹẹ́rìn dín lọgbọ̀n", "oókàn dín lọgbọ̀n"],
    "Built as": ["1 + 10", "20 − 5", "20 − 4", "20 − 1", "20 + 1", "20 + 4", "30 − 5", "30 − 4", "30 − 1"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Eleven to Fourteen</div>
        <p>Bowen analyses 11 to 14 as the first four numbers with <em>lá</em> 'large'
        appended — eleven is 'great one' — rather than as additions to ten.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Fifteen and Twenty-Five</div>
        <p>Five below a round number is a single fused word in Kari's list —
        <em>ẹ̀ẹ́dogún</em> 15, <em>ẹ̀ẹ́dọ̀ọ́gbọ̀ǹ</em> 25 — which Bowen analyses as 'five from
        twenty' and thirty less five. The other subtractions keep <em>dín</em> as a separate
        word.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Bowen's table carries the same pattern far beyond thirty: 35 is 'five from forty', 45
    'five from fifty', 101 'one laid on a hundred', 190 'ten from two hundred' and 210 'ten
    laid on two hundred'. He writes without tone marks, so the converter does not generate
    these numbers.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — ROUND NUMBERS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Round Numbers</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Twenties, Heaps and Heads</div>', unsafe_allow_html=True)

st.table({
    "Value": ["20", "30", "40", "50", "60", "70", "80", "90", "100", "200", "400", "1,000", "2,000"],
    "Form": ["ogún", "ọgbọ̀n", "ogoji", "àádọ́ta", "ọgọ́ta", "àádọ́rin", "ọgọ́rin", "àádọ́rùń",
             "ọgọ́rùn", "igba", "irínwó", "ẹgbẹ̀rún", "ẹgbẹ̀wá"],
    "Built as": ["base", "base", "20 × 2", "60 − 10", "20 × 3", "80 − 10", "20 × 4", "100 − 10",
                 "20 × 5", "base", "—", "200 × 5", "200 × 10"],
})

st.markdown("""
<div class="ling-info">
    <p>Forms from Kari (1998), who also gives <em>ọ̀rún</em> for 100 and <em>ẹgbàá</em> for 2,000.
    His 40 is printed <em>ọgbọ̀ji</em>, which runs the word for thirty into forty; Crowther
    (1852) and Bowen (1858) both give <em>ogoji</em>, from <em>ogún èjì</em> 'twenty two', so
    that spelling is used here, without tone marks.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Two Hundred: a Heap</div>
        <p>Bowen derives <em>igba</em> from <em>gbá</em> 'to sweep together', because cowries
        were counted by sweeping each two hundred into a separate heap.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">The Cowry Table</div>
        <p>Forty cowries made a string, five strings a bunch of 200, ten bunches a 'head' of
        2,000, and ten heads a bag of 20,000 — which, Bowen explains, is why 200, 2,000 and
        20,000 are round numbers in Yoruba.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — WITH A NOUN
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Numbers with Nouns</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Before or After the Noun</div>
        <p>According to Bowen, round numbers such as twenty and thirty generally come before
        the noun — 'twenty men' puts the word for twenty first — while the others follow it,
        and two to ten then take a prefix <em>m-</em>.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Ordinals</div>
        <p>Ordinals from one to nineteen add <em>ek-</em> to the cardinal, and the vowel is
        often dropped: Bowen gives 'second' and 'third' both ways, <em>ekedzi</em> or
        <em>kedzi</em> and <em>eketa</em> or <em>keta</em>, in his 1858 spelling. They follow
        the noun, as in 'the second day'.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature": ["1 to 30", "Tens to 100", "200, 400, 1,000, 2,000", "Other numbers", "0",
                "Yoruba to Arabic"],
    "Status": ["Implemented", "Implemented", "Implemented", "Not implemented",
               "Not implemented", "Not implemented"],
    "Basis": ["Kari (1998)", "Kari (1998); 40 from Crowther (1852) and Bowen (1858)",
              "Kari (1998)", "Described by Bowen (1858), but without tone marks",
              "No word in the sources consulted", "Not built"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 7 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Kari, Ethelbert E.</strong> 1998. Yoruba. In Eugene S. L. Chan, <em>Numeral
    Systems of the World's Languages</em>. Max Planck Institute for Evolutionary Anthropology.
    Source given: Robert G. Armstrong, <em>Yoruba Numerals</em> (Oxford University Press,
    1962).</p>
    <p><strong>Bowen, T. J.</strong> 1858. <em>Grammar and Dictionary of the Yoruba
    Language</em>. Washington: Smithsonian Institution. §§209–216 on the numerals.</p>
    <p><strong>Crowther, Samuel.</strong> 1852. <em>A Vocabulary of the Yoruba Language</em>.
    London: Seeleys. Entry <em>Ogoji</em>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> An earlier version of this page said that
    Yoruba was the only language on the site to use all three operations; Ainu subtracts too,
    so this was removed. Its converter generated every number to 1,999 by rule and joined the
    parts with <em>lélọ́</em>, which matches no source; Bowen, for example, gives 140 as
    'twenty seven times', where the old rule produced 120 + 20. Claims about zero loanwords,
    modern simplification, and the suppletive ordinal <em>àkọ́kọ́</em> were not checked against
    a source and are left out.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Yoruba", "linguistics")
