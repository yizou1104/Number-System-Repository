import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Roman Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Roman", "linguistics")

st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Roman Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Conceptually Decimal</span>
        <span class="ling-tag">Additive–Subtractive</span>
        <span class="ling-tag">Non-Positional</span>
        <span class="ling-tag">Symbolic</span>
        <span class="ling-tag">Zero-Less</span>
        <span class="ling-tag">No Inflection</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Roman numerals are the only system in this repository that is non-positional — symbol values do not change based on their position in the sequence. X always means 10, regardless of where it appears.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Conceptual base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Additive–Subtractive</span>
        <span class="ling-prop-key">Positional value</span>
        <span class="ling-prop-val">Absent — symbols carry fixed values</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">None in classical system; medieval <em>N</em> (nulla) is non-standard</span>
        <span class="ling-prop-key">Inflection</span>
        <span class="ling-prop-val">None — glyphs are invariant symbols, not words</span>
        <span class="ling-prop-key">Max classical form</span>
        <span class="ling-prop-val">3,999 = MMMCMXCIX</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Latin alphabet letters repurposed as numeral symbols</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Symbols &amp; Values</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Symbols</div>', unsafe_allow_html=True)

st.table({
    "Symbol": ["I","V","X","L","C","D","M"],
    "Value":  ["1","5","10","50","100","500","1,000"]
})

st.markdown("""
<div class="ling-info">
    <p>Symbols derive historically from tally marks and Latin abbreviations: I (a single tally stroke), V (hand, five fingers), X (two crossed tallies), C from <em>centum</em> (hundred), M from <em>mille</em> (thousand).</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Standard Subtractive Forms</div>', unsafe_allow_html=True)

st.table({
    "Form":      ["IV","IX","XL","XC","CD","CM"],
    "Value":     ["4","9","40","90","400","900"],
    "Structure": ["5 − 1","10 − 1","50 − 10","100 − 10","500 − 100","1000 − 100"]
})

st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Additive &amp; Subtractive Rules</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Additive Rule</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Rule</span>
    <span class="ling-formula-rule">Symbols in descending order from left to right are <em>summed</em></span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Additive examples</div>
    <div class="ling-ex-line"><span class="num">II</span><span class="word">= 1 + 1 = 2</span></div>
    <div class="ling-ex-line"><span class="num">VIII</span><span class="word">= 5 + 3 = 8</span></div>
    <div class="ling-ex-line"><span class="num">LX</span><span class="word">= 50 + 10 = 60</span></div>
    <div class="ling-ex-line"><span class="num">MMXXVI</span><span class="word">= 1000 + 1000 + 10 + 10 + 5 + 1 = 2026</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Subtractive Rule</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Rule</span>
    <span class="ling-formula-rule">A <em>smaller</em> symbol immediately before a larger one is <em>subtracted</em></span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Subtractive notation is subject to strict constraints — not every smaller-before-larger combination is valid.</p>
    <ul>
        <li>Only <strong>I, X, C</strong> may be used subtractively</li>
        <li><strong>V, L, D</strong> are never subtractive</li>
        <li>Only one smaller symbol may precede a larger one</li>
        <li>I may only precede V or X; X may only precede L or C; C may only precede D or M</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Special Conventions</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Repetition, Limits &amp; Extensions</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Repetition Rules</div>
        <ul>
            <li>I, X, C, M may be repeated up to <strong>three</strong> times consecutively</li>
            <li>V, L, D may <strong>never</strong> be repeated</li>
        </ul>
        <div class="ling-examples" style="margin-top:.65rem;margin-bottom:0">
            <div class="ling-ex-line"><span class="num">III</span><span class="word">= 3</span></div>
            <div class="ling-ex-line"><span class="num">MMM</span><span class="word">= 3,000</span></div>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Vinculum (Overline)</div>
        <p>A bar over a symbol multiplies its value by 1,000, allowing representation beyond 3,999 — used in inscriptions and manuscripts.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.9rem;color:var(--ink-muted)">V̅ = 5,000 &nbsp;·&nbsp; X̅ = 10,000</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Historical Additive-Only Forms</div>
        <p>Earlier inscriptions used purely additive forms before subtractive notation became standardized in the medieval period.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.9rem;color:var(--ink-muted)">IIII instead of IV<br>VIIII instead of IX</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">No Morphological Inflection</div>
        <p>Roman numeral glyphs are invariant symbols. In Latin texts, ordinals are written as fully inflected adjectives (<em>primus, secundus</em>) — separate words, not numeral glyphs.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Roman", "linguistics")
