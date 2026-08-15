import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Swahili Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Swahili", "linguistics")

st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Swahili Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Noun-Class Agreement (1–5)</span>
        <span class="ling-tag">Arabic-Derived Decades</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Swahili combines a native Bantu agreement system (affecting numerals 1–5) with a borrowed Arabic lexicon for all decades (20–90), producing a grammatically layered numeral system unlike any other in this repository.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>10 (decimal)</strong></span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Multiplicative–Additive</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Absent</span>
        <span class="ling-prop-key">Agreement</span>
        <span class="ling-prop-val">Present — numerals 1–5 agree with noun class; 6+ invariant</span>
        <span class="ling-prop-key">Additive connector</span>
        <span class="ling-prop-val"><em>na</em> — links components in compound numbers</span>
        <span class="ling-prop-key">Decade origin</span>
        <span class="ling-prop-val">20–90 are Arabic loanwords (ishirini, thelathini, etc.)</span>
        <span class="ling-prop-key">Noun–numeral order</span>
        <span class="ling-prop-val">Noun precedes numeral (post-nominal)</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Latin alphabet; historically also Ajami (Arabic script)</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (0–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Form":   ["sifuri","moja","mbili","tatu","nne","tano","sita","saba","nane","tisa","kumi"]
})

st.markdown("""
<div class="ling-info">
    <p><em>Sifuri</em> (zero) is a loanword from Arabic <em>ṣifr</em>, the same root that gives English "cipher" and "zero." Historically, Swahili was also written in Arabic script (Ajami), particularly in coastal East African manuscripts.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Decades and Higher Bases</div>', unsafe_allow_html=True)

st.table({
    "Value":   ["20","30","40","50","60","70","80","90","100","1,000"],
    "Form":    ["ishirini","thelathini","arobaini","hamsini","sitini","sabini",
                "themanini","tisini","mia","elfu"],
    "Origin":  ["Arabic","Arabic","Arabic","Arabic","Arabic","Arabic",
                "Arabic","Arabic","Bantu","Bantu/Arabic"]
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Arabic Lexical Layer</div>
    <p>All Swahili decades from 20–90 are Arabic loanwords that have been fully integrated into the grammar. They are no longer transparently compositional — <em>ishirini</em> (20) does not parse as "2 × 10" in modern Swahili.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Multiplicative Structure (100+)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule"><em>mia / elfu / milioni</em> + Digit multiplier</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative examples</div>
    <div class="ling-ex-line"><span class="num">100</span><span class="word">mia moja</span><span class="gloss">1 × 100</span></div>
    <div class="ling-ex-line"><span class="num">300</span><span class="word">mia tatu</span><span class="gloss">3 × 100</span></div>
    <div class="ling-ex-line"><span class="num">2,000</span><span class="word">elfu mbili</span><span class="gloss">2 × 1,000</span></div>
    <div class="ling-ex-line"><span class="num">2,000,000</span><span class="word">milioni mbili</span><span class="gloss">2 × 1,000,000</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Additive Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Higher unit] + <em>na</em> + [Lower unit]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Additive examples</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">ishirini na moja</span><span class="gloss">20 + 1</span></div>
    <div class="ling-ex-line"><span class="num">32</span><span class="word">thelathini na mbili</span><span class="gloss">30 + 2</span></div>
    <div class="ling-ex-line"><span class="num">105</span><span class="word">mia moja na tano</span><span class="gloss">100 + 5</span></div>
    <div class="ling-ex-line"><span class="num">1,234</span><span class="word">elfu moja mia mbili thelathini na nne</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><em>Na</em> appears before the final unit component. In longer compounds, the higher magnitude components are juxtaposed directly (no connector), and only the last addition uses <em>na</em>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-section-label">Noun-Class Agreement</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Agreement &amp; Syntax</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Noun-Class System</div>
    <p>Swahili has 15+ noun classes, each with its own agreement prefix. Numerals 1–5 take the class prefix of the noun they modify — making them the only fully agreement-sensitive numerals in the repository.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The stem forms of the agreeing numerals are: <em>-moja, -wili, -tatu, -nne, -tano</em>. The class prefix attaches to the left of these stems.</p>
    <div class="ling-examples" style="margin-top:.75rem;margin-bottom:0">
        <div class="ling-examples-label">Agreement across noun classes — "two"</div>
        <div class="ling-ex-line"><span class="word">watu wawili</span><span class="gloss">Class 1/2 (humans): wa- prefix</span></div>
        <div class="ling-ex-line"><span class="word">vitabu viwili</span><span class="gloss">Class 7/8 (objects): vi- prefix</span></div>
        <div class="ling-ex-line"><span class="word">miti miwili</span><span class="gloss">Class 3/4 (trees): mi- prefix</span></div>
        <div class="ling-ex-line"><span class="word">maneno mawili</span><span class="gloss">Class 6 (mass): ma- prefix</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Noun–Numeral Order</div>
        <p>Swahili numerals are post-nominal — they follow the noun, the opposite of Hindi, Bengali, and Tamil.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.88rem;color:var(--ink-muted)">vitabu vitatu<br><em style="font-family:'Crimson Pro',serif;font-size:.9rem">books three</em></p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Ordinals</div>
        <p>Ordinals are formed analytically. <em>Kwanza</em> (first) is a common loanform. Higher ordinals use a noun + modifier construction: <em>siku ya pili</em> (second day).</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Swahili", "linguistics")
