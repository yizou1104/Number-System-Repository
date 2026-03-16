import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="Swahili Numerals — Linguistics", layout="centered")
apply_global_styles()

LING_CSS = """<style>
.ling-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}
.ling-masthead-eyebrow{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}
.ling-masthead-eyebrow::before{content:'';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}
.ling-masthead-title{font-family:'Crimson Pro',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.9rem}
.ling-masthead-sub{display:none}
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
.ling-callout{background:var(--accent-pale);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:4px;padding:1.05rem 1.45rem;margin-bottom:.85rem;transition:transform .2s ease,box-shadow .2s ease}
.ling-callout:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(184,92,56,.1)}
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
.ling-morph-table{margin-bottom:0}
.ling-morph-row{display:grid;grid-template-columns:6rem 1.5rem 6rem 1fr;align-items:center;gap:.5rem 1rem;padding:.45rem 0;border-bottom:1px solid var(--rule)}
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

st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Swahili_Converter">← Swahili Converter</a>
    <a class="ling-nav-btn active" href="/Swahili_Linguistics">Swahili Linguistics</a>
</div>
""", unsafe_allow_html=True)
home_nav()