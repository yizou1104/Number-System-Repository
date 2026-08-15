import streamlit as st
from ui import apply_global_styles, home_nav, LING_CSS

st.set_page_config(page_title="Esperanto Numerals — Linguistics", layout="centered")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)

# ── MASTHEAD ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Esperanto Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Constructed Language</span>
        <span class="ling-tag">Fully Regular</span>
        <span class="ling-tag">No Irregularities</span>
        <span class="ling-tag">Compositional</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — SYSTEM OVERVIEW ──────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Esperanto's numeral system is the most regular in this repository.
    There are zero irregular forms, zero suppletive stems, and zero phonological
    alternations. Every number from 0 to billions is built from ten atom roots
    plus three magnitude words by transparent concatenation.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Created by</span>
        <span class="ling-prop-val"><strong>L. L. Zamenhof</strong>, 1887 (<em>Unua Libro</em>)</span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Decimal, multiplicative-additive</span>
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val">10</span>
        <span class="ling-prop-key">Irregularities</span>
        <span class="ling-prop-val">None — every form is compositional</span>
        <span class="ling-prop-key">Atom count</span>
        <span class="ling-prop-val">10 digits + 3 magnitude words (cent, mil, miliono)</span>
        <span class="ling-prop-key">Word boundaries</span>
        <span class="ling-prop-val">Tens 20–90 and hundreds 200–900 are <strong>one word</strong>; thousands and millions are written separately</span>
        <span class="ling-prop-key">Inflection</span>
        <span class="ling-prop-val">Cardinals invariable; <em>miliono</em>/<em>miliardo</em> behave as nouns and take plural <em>-j</em></span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — DIGITS & BASES ───────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Atomic Roots</div>', unsafe_allow_html=True)

st.table({
    "Number": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Esperanto": ["nul", "unu", "du", "tri", "kvar", "kvin", "ses", "sep", "ok", "naŭ", "dek"],
    "IPA": ["nul", "ˈunu", "du", "tri", "kvar", "kvin", "ses", "sep", "ok", "naw", "dek"],
})

st.markdown("""
<div class="ling-info">
    <p>The digit roots are drawn from various Romance, Germanic, and Slavic
    sources — <em>du</em> from Latin, <em>tri</em> from Slavic, <em>kvar</em>
    from Latin <em>quattuor</em>, <em>naŭ</em> from Latin <em>novem</em> via the
    intermediate form. The deliberate eclecticism reflects Zamenhof's design
    goal of broad recognisability.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Magnitude Words</div>', unsafe_allow_html=True)

st.table({
    "Value": ["100", "1,000", "1,000,000", "1,000,000,000"],
    "Esperanto": ["cent", "mil", "miliono", "miliardo"],
    "Type": ["root", "root", "noun", "noun"],
})

# ── SECTION 3 — COMPOSITIONAL RULES ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Tens — One Word</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[digit] + <em>dek</em> · written as a single word</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Tens</div>
    <div class="ling-ex-line"><span class="num">20</span><span class="word">dudek</span><span class="gloss">du + dek</span></div>
    <div class="ling-ex-line"><span class="num">30</span><span class="word">tridek</span><span class="gloss">tri + dek</span></div>
    <div class="ling-ex-line"><span class="num">90</span><span class="word">naŭdek</span><span class="gloss">naŭ + dek</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Hundreds — One Word</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[digit] + <em>cent</em> · written as a single word</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Hundreds</div>
    <div class="ling-ex-line"><span class="num">200</span><span class="word">ducent</span><span class="gloss">du + cent</span></div>
    <div class="ling-ex-line"><span class="num">500</span><span class="word">kvincent</span><span class="gloss">kvin + cent</span></div>
    <div class="ling-ex-line"><span class="num">900</span><span class="word">naŭcent</span><span class="gloss">naŭ + cent</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Thousands and Millions — Separate Words</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Spacing rule</div>
    <p>Tens (dudek) and hundreds (ducent) are written together as one word, but
    thousands (du mil) and millions (du milionoj) are written as separate words.
    This boundary distinguishes Esperanto's "compounded numerals" from
    "noun-like quantifiers" — <em>mil</em> behaves like an invariable element,
    while <em>miliono</em> behaves like a noun (taking plural <em>-j</em> when
    the multiplier is greater than one).</p>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Larger numbers</div>
    <div class="ling-ex-line"><span class="num">1000</span><span class="word">mil</span><span class="gloss">no multiplier needed</span></div>
    <div class="ling-ex-line"><span class="num">2000</span><span class="word">du mil</span><span class="gloss">two thousand</span></div>
    <div class="ling-ex-line"><span class="num">1M</span><span class="word">unu miliono</span><span class="gloss">one million (noun, singular)</span></div>
    <div class="ling-ex-line"><span class="num">2M</span><span class="word">du milionoj</span><span class="gloss">two millions — noun takes -j plural</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Compound Examples</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Worked examples</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">dudek unu</span><span class="gloss">two-ten one</span></div>
    <div class="ling-ex-line"><span class="num">234</span><span class="word">ducent tridek kvar</span><span class="gloss">two-hundred three-ten four</span></div>
    <div class="ling-ex-line"><span class="num">1234</span><span class="word">mil ducent tridek kvar</span><span class="gloss">thousand two-hundred three-ten four</span></div>
    <div class="ling-ex-line"><span class="num">1,234,567</span><span class="word">unu miliono ducent tridek kvar mil kvincent sesdek sep</span><span class="gloss">full structure</span></div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — DERIVED FORMS ────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Derived Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Productive Numeral Affixes</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Esperanto's productive affix system extends to numerals — any cardinal
    can take standard suffixes to create ordinals, fractions, multiples,
    collectives, and abstract nouns. This compositional power is unique among
    the languages in this repository.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Suffix patterns</div>
    <div class="ling-ex-line"><span class="num">-a</span><span class="word">kvara</span><span class="gloss">fourth (ordinal adjective)</span></div>
    <div class="ling-ex-line"><span class="num">-e</span><span class="word">kvare</span><span class="gloss">fourthly (ordinal adverb)</span></div>
    <div class="ling-ex-line"><span class="num">-on-</span><span class="word">kvarono</span><span class="gloss">a quarter (fraction)</span></div>
    <div class="ling-ex-line"><span class="num">-obl-</span><span class="word">kvarobla</span><span class="gloss">fourfold</span></div>
    <div class="ling-ex-line"><span class="num">-op-</span><span class="word">kvarope</span><span class="gloss">in groups of four</span></div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5 — DESIGN PHILOSOPHY ────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Design Philosophy</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Why So Regular?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Zamenhof published Esperanto's foundational sixteen grammar rules in
    <em>Unua Libro</em> (1887). Rule 5 covers numerals: cardinals are
    invariable; ordinals are formed with the adjectival ending <em>-a</em>;
    multiples take <em>-obl-</em>; fractions take <em>-on-</em>; collectives
    take <em>-op-</em>. There are no exceptions.</p>
    <p>Compare this to the natural languages in this repository: Thai has the
    irregular pair ยี่ / เอ็ด; Tibetan has decade-specific linker syllables;
    English itself has eleven, twelve, and thirteen. Esperanto's regularity is
    a deliberate counter-design — every irregularity in a natural language
    represents a hurdle for the learner.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Esperanto is the most-spoken constructed language in the world, with an
    estimated 2 million speakers and a small native-speaker community
    (children raised bilingually with Esperanto, called <em>denaskuloj</em>).
    Its numeral system has remained unchanged since 1887.</p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Esperanto_Converter.py", label="← Esperanto Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)