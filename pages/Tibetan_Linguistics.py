import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="Tibetan Numerals — Linguistics", layout="centered")
apply_global_styles()

LING_CSS = """<style>
.ling-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}
.ling-masthead-eyebrow{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}
.ling-masthead-eyebrow::before{content:'';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}
.ling-masthead-title{font-family:'Crimson Pro',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.9rem}
.ling-tags{display:flex;flex-wrap:wrap;gap:.45rem}
.ling-tag{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:600;letter-spacing:.07em;text-transform:uppercase;padding:.22rem .7rem;border:1.5px solid var(--rule-strong);border-radius:2px;color:var(--ink-soft);background:transparent}
.ling-section-label{font-family:'DM Sans',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2.25rem 0 1.1rem 0}
.ling-section-label::before{content:'';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}
.ling-section-label::after{content:'';flex:1;height:1px;background:var(--rule)}
.ling-section-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.85rem;font-weight:600;color:var(--ink);letter-spacing:-.025em;line-height:1.15;margin-bottom:1.1rem;padding-bottom:.45rem;border-bottom:1px solid var(--rule)}
.ling-subsection-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.25rem;font-weight:600;color:var(--ink-soft);letter-spacing:-.01em;margin-bottom:.7rem;margin-top:0}
.ling-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:5px;padding:1.3rem 1.55rem;margin-bottom:.85rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 3px 10px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);transition:transform .22s cubic-bezier(.4,0,.2,1),box-shadow .22s cubic-bezier(.4,0,.2,1),border-color .22s ease}
.ling-card:hover{transform:translateY(-2px);box-shadow:0 2px 6px rgba(26,22,18,.07),0 8px 24px rgba(26,22,18,.09),inset 0 1px 0 rgba(255,255,255,.8);border-color:rgba(26,22,18,.16)}
.ling-card p,.ling-card li{font-family:'Crimson Pro',Georgia,serif;font-size:1.08rem;color:var(--ink-soft);line-height:1.72;margin-bottom:.45rem}
.ling-card p:last-child,.ling-card li:last-child{margin-bottom:0}
.ling-card ul{padding-left:1.3rem;margin:0}
.ling-card li::marker{color:var(--accent)}
.ling-callout{background:var(--accent-pale);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:4px;padding:1.05rem 1.45rem;margin-bottom:.85rem}
.ling-callout-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--accent);margin-bottom:.4rem}
.ling-callout p{font-family:'Crimson Pro',Georgia,serif;font-size:1.1rem;font-style:italic;color:var(--ink);line-height:1.6;margin:0}
.ling-info{background:rgba(46,107,122,.05);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:4px;padding:.95rem 1.35rem;margin-bottom:.85rem}
.ling-info p{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;color:var(--ink-soft);line-height:1.68;margin:0}
.ling-formula{background:var(--parchment-2);border:1px solid var(--rule-strong);border-radius:4px;padding:1.05rem 1.4rem;margin-bottom:.85rem;display:flex;align-items:flex-start;gap:1.2rem}
.ling-formula-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--ink-faint);flex-shrink:0;padding-top:.2rem;min-width:3.5rem;text-align:right}
.ling-formula-rule{font-family:'DM Mono','Courier New',monospace;font-size:.98rem;color:var(--ink);line-height:1.6;flex:1}
.ling-formula-rule em{font-style:normal;color:var(--accent);font-weight:500}
.ling-examples{background:var(--parchment-2);border:1px solid var(--rule);border-left:3px solid var(--ink-faint);border-radius:4px;padding:.95rem 1.35rem;margin-bottom:.85rem}
.ling-examples-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.5rem}
.ling-ex-line{font-family:'DM Mono','Courier New',monospace;font-size:.95rem;color:var(--ink-soft);line-height:1.75}
.ling-ex-line .num{color:var(--accent);font-weight:500;display:inline-block;min-width:2.5rem}
.ling-ex-line .word{color:var(--ink)}
.ling-ex-line .gloss{color:var(--ink-muted);font-style:italic;font-family:'Crimson Pro',Georgia,serif;font-size:.92rem;margin-left:.75rem}
.ling-grid-2{display:grid;grid-template-columns:1fr 1fr;gap:.75rem;margin-bottom:.85rem}
@media(max-width:600px){.ling-grid-2{grid-template-columns:1fr}}
.ling-props{display:grid;grid-template-columns:auto 1fr;gap:.5rem 1.25rem;align-items:baseline;margin:0;padding:0}
.ling-prop-key{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint);white-space:nowrap}
.ling-prop-val{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;color:var(--ink-soft);line-height:1.45}
.ling-prop-val strong{color:var(--ink);font-weight:600}
.ling-morph-row{display:grid;grid-template-columns:8rem 1.5rem 8rem 1fr;align-items:center;gap:.5rem 1rem;padding:.45rem 0;border-bottom:1px solid var(--rule)}
.ling-morph-row:last-child{border-bottom:none}
.ling-morph-source{font-family:'DM Mono','Courier New',monospace;font-size:.93rem;color:var(--ink)}
.ling-morph-arrow{color:var(--ink-faint);font-size:.85rem;text-align:center}
.ling-morph-target{font-family:'DM Mono','Courier New',monospace;font-size:.93rem;color:var(--accent);font-weight:500}
.ling-morph-gloss{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:.92rem;color:var(--ink-muted)}
.ling-nav-footer{display:flex;gap:.75rem;padding:1.4rem 0 .5rem 0;border-top:1px solid var(--rule);margin-top:2.5rem;flex-wrap:wrap}
.ling-nav-btn{font-family:'DM Sans',sans-serif;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--ink);background:var(--parchment-2);border:1.5px solid var(--rule-strong);border-radius:3px;padding:.55rem 1.1rem;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;white-space:nowrap;cursor:pointer;box-shadow:2px 2px 0 rgba(26,22,18,.08);transition:all .18s cubic-bezier(.4,0,.2,1)}
.ling-nav-btn:hover{background:var(--ink);color:var(--parchment);border-color:var(--ink);box-shadow:3px 3px 0 var(--accent);transform:translate(-1px,-1px);text-decoration:none}
.ling-nav-btn.active{background:var(--parchment-3);color:var(--ink-muted);cursor:default;box-shadow:none}
.ling-nav-btn.active:hover{transform:none;background:var(--parchment-3);color:var(--ink-muted);border-color:var(--rule-strong);box-shadow:none}
</style>"""
st.markdown(LING_CSS, unsafe_allow_html=True)

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

# ── NAVIGATION ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Tibetan_Converter">← Tibetan Converter</a>
    <a class="ling-nav-btn active" href="/Tibetan_Linguistics">Tibetan Linguistics</a>
</div>
""", unsafe_allow_html=True)
home_nav()