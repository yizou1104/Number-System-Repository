import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Tibetan Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Tibetan", "linguistics")

# ── MASTHEAD ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Tibetan Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Decade Linkers</span>
        <span class="ling-tag">Orthography–Pronunciation Gap</span>
        <span class="ling-tag">Independent Script</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — SYSTEM OVERVIEW ──────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Tibetan is distinctive in using mandatory <em>decade linkers</em> — unique syllables
    that fuse the tens word to the following unit digit within each decade. Each decade
    has its own linker: 20 uses <em>རྩ་</em> (tsa), 30 uses <em>སོ་</em> (so), etc.
    No other language in this repository has this feature.</p>
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
        <span class="ling-prop-key">Decade linkers</span>
        <span class="ling-prop-val">Each decade has a unique fusing syllable between tens and units</span>
        <span class="ling-prop-key">Coordinator</span>
        <span class="ling-prop-val"><em>དང་</em> (dang) — connects major magnitude units</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Independent Tibetan glyphs (༠–༩); Arabic numerals also used</span>
        <span class="ling-prop-key">Script–speech gap</span>
        <span class="ling-prop-val">Written clusters often simplified drastically in Lhasa spoken Tibetan</span>
        <span class="ling-prop-key">Morphology</span>
        <span class="ling-prop-val">Invariant — no gender, case, or agreement on numerals</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — DIGITS & BASES ────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (0–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Glyph":  ["༠","༡","༢","༣","༤","༥","༦","༧","༨","༩","༡༠"],
    "Script": ["ཀླད་ཀོར་","གཅིག་","གཉིས་","གསུམ་","བཞི་","ལྔ་","དྲུག་","བདུན་","བརྒྱད་","དགུ་","བཅུ་"],
    "Romanized": ["laykor","chig","nyi","sum","shi","nga","trug","dün","gyay","gu","chu"],
})

st.markdown("""
<div class="ling-info">
    <p>Tibetan numeral glyphs (༠–༩) appear in manuscripts, calendar systems, folio numbering,
    and religious texts. The script preserves historical consonant clusters that are
    drastically simplified in spoken Lhasa Tibetan — <em>བརྒྱད་</em> is written with five
    consonants but spoken as a single syllable <em>gyay</em>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Teens (10–19)</div>', unsafe_allow_html=True)

st.table({
    "Number":    ["10","11","12","13","14","15","16","17","18","19"],
    "Script":    ["བཅུ་","བཅུ་གཅིག་","བཅུ་གཉིས་","བཅུ་གསུམ་","བཅུ་བཞི་","བཅོ་ལྔ་","བཅུ་དྲུག་","བཅུ་བདུན་","བཅོ་བརྒྱད་","བཅུ་དགུ་"],
    "Romanized": ["chu","chu chig","chu nyi","chu sum","chu shi","cho nga","chu trug","chu dün","cho gyay","chu gu"],
})

st.markdown("""
<div class="ling-info">
    <p>15 and 18 show a phonological variant: the tens form shifts from <em>chu</em> to
    <em>cho</em>. This is a sandhi process conditioned by the following consonant cluster,
    not a lexical irregularity. All other teens use the regular <em>chu + unit</em> pattern.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Decades (20–90)</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["20","30","40","50","60","70","80","90"],
    "Script":    ["ཉི་ཤུ་","སུམ་ཅུ","བཞི་བཅུ","ལྔ་བཅུ","དྲུག་ཅུ","བདུན་ཅུ","བརྒྱད་ཅུ","དགུ་བཅུ"],
    "Romanized": ["nyi shu","sum ju","shi ju","nga ju","trug chu","dün ju","gyay ju","gu ju"],
    "Linker":    ["རྩ་ tsa","སོ་ so","ཞེ་ shey","ང་ nga","རེ་ rey","དོན་ dön","གྱ་ gya","གོ་ go"],
})

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Higher Bases</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["100","1,000","10,000","100,000"],
    "Script":    ["བརྒྱ་","སྟོང་","ཁྲི་","འབུམ"],
    "Romanized": ["gya","tong","thri","bum"],
    "Structure": ["independent unit","independent unit","independent 10⁴","independent 10⁵"],
})

# ── SECTION 3 — COMPOSITIONAL RULES ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Multiplicative Structure (tens and above)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">Digit + <em>base unit</em> · e.g. གཉིས་ + བརྒྱ་ = 200</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative examples</div>
    <div class="ling-ex-line"><span class="num">20</span><span class="word">ཉི་ཤུ་</span><span class="gloss">nyi shu · 2 × 10</span></div>
    <div class="ling-ex-line"><span class="num">300</span><span class="word">གསུམ་བརྒྱ་</span><span class="gloss">sum gya · 3 × 100</span></div>
    <div class="ling-ex-line"><span class="num">4,000</span><span class="word">བཞི་སྟོང་</span><span class="gloss">shi tong · 4 × 1,000</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Additive Structure Within Decades</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">The Linker System</div>
    <p>Unlike any other language in this repository, Tibetan uses a unique
    <em>linker syllable</em> between the decade word and the unit. The linker
    fuses directly onto the decade, and each decade has its own linker form.
    The resulting compound is written and pronounced as a single unit.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Decade] + <em>[linker]</em> + [unit] · linker fuses directly onto decade</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Within-decade examples with linkers</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">ཉི་ཤུ་རྩ་གཅིག་</span><span class="gloss">nyi shu tsa chig · 20 + [tsa] + 1</span></div>
    <div class="ling-ex-line"><span class="num">37</span><span class="word">སུམ་ཅུ་སོ་བདུན་</span><span class="gloss">sum ju so dün · 30 + [so] + 7</span></div>
    <div class="ling-ex-line"><span class="num">45</span><span class="word">བཞི་བཅུ་ཞེ་ལྔ་</span><span class="gloss">shi ju shey nga · 40 + [shey] + 5</span></div>
    <div class="ling-ex-line"><span class="num">99</span><span class="word">དགུ་བཅུ་གོ་དགུ་</span><span class="gloss">gu ju go gu · 90 + [go] + 9</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">The Coordinator དང་ (dang)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>At larger structural boundaries — between a major magnitude unit and the
    remainder — Tibetan uses the coordinator <em>དང་</em> (dang). This is distinct
    from the within-decade linkers: linkers fuse phonetically, while <em>དང་</em>
    is a separate syntactic word.</p>
    <div class="ling-examples" style="margin-top:.75rem;margin-bottom:0">
        <div class="ling-examples-label">Coordinator examples</div>
        <div class="ling-ex-line"><span class="num">108</span><span class="word">བརྒྱ་དང་བཅུ་གཅིག་</span><span class="gloss">gya dang chu chig · 100 dang 11</span></div>
        <div class="ling-ex-line"><span class="num">1,045</span><span class="word">སྟོང་དང་བཞི་བཅུ་ཞེ་ལྔ་</span><span class="gloss">tong dang shi ju shey nga · 1000 dang 45</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — SCRIPT & PRONUNCIATION ───────────────────────────────────────
st.markdown('<div class="ling-section-label">Script &amp; Pronunciation</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The Orthography–Speech Gap</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">A Unique Challenge</div>
    <p>Tibetan script preserves the phonology of an earlier stage of the language.
    Spoken Lhasa Tibetan has dramatically simplified the consonant clusters, producing
    forms that bear little surface resemblance to the written forms. This is not
    inflectional morphology — the written form is unchanged — but it means learners
    must treat script and speech as partially independent systems.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.6rem">Written → Spoken examples</div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">བརྒྱད་</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">gyay</span>
            <span class="ling-morph-gloss">8 — 5 written consonants, 1 spoken syllable</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">གཅིག་</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">chig</span>
            <span class="ling-morph-gloss">1 — initial cluster reduced</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">བཞི་</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">shi</span>
            <span class="ling-morph-gloss">4 — initial b-zh cluster → sh</span>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.6rem">Tibetan Numeral Glyphs</div>
        <p style="font-family:'DM Mono',monospace;font-size:1.4rem;letter-spacing:.25em;color:var(--ink);line-height:2">༠ ༡ ༢ ༣ ༤ ༥ ༦ ༧ ༨ ༩</p>
        <p>These glyphs appear in folio numbering, calendars, and religious texts.
        Modern administrative and digital contexts use Arabic numerals.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5 — SYNTAX & MORPHOLOGY ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Grammatical Integration</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Cardinals</div>
        <ul>
            <li>Invariant — no inflection of any kind</li>
            <li>No gender, case, or number marking</li>
            <li>Numeral precedes classifier and noun</li>
            <li>Classifiers are used especially in colloquial speech</li>
        </ul>
        <p style="font-family:'DM Mono',monospace;font-size:.88rem;color:var(--ink-muted);margin-top:.5rem">གཅིག མི<br><em style="font-family:'Crimson Pro',serif">chig mi — one person</em></p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Ordinals</div>
        <p>Formed by adding a suffix to the cardinal. The suffix varies
        phonologically: <em>-pa</em>, <em>-ba</em>, or <em>-ma</em> depending
        on the final sound of the cardinal.</p>
        <div class="ling-morph-row" style="margin-top:.65rem">
            <span class="ling-morph-source">གཅིག་</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">དང་པོ་</span>
            <span class="ling-morph-gloss">first (suppletive)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">གཉིས་</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">གཉིས་པ་</span>
            <span class="ling-morph-gloss">second (-pa suffix)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">གསུམ་</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">གསུམ་པ་</span>
            <span class="ling-morph-gloss">third (-pa suffix)</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Tibetan", "linguistics")
