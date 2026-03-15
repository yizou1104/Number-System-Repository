import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Roman Numerals — Linguistics", layout="centered")
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
.ling-ex-line .num{color:var(--accent);font-weight:500;display:inline-block;min-width:4rem}
.ling-ex-line .word{color:var(--ink)}
.ling-ex-line .gloss{color:var(--ink-muted);font-style:italic;font-family:'Crimson Pro',Georgia,serif;font-size:.92rem;margin-left:.75rem}
.ling-grid-2{display:grid;grid-template-columns:1fr 1fr;gap:.75rem;margin-bottom:.85rem}
@media(max-width:600px){.ling-grid-2{grid-template-columns:1fr}}
.ling-props{display:grid;grid-template-columns:auto 1fr;gap:.5rem 1.25rem;align-items:baseline;margin:0;padding:0}
.ling-prop-key{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint);white-space:nowrap}
.ling-prop-val{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;color:var(--ink-soft);line-height:1.45}
.ling-prop-val strong{color:var(--ink);font-weight:600}
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

st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Roman_Converter">← Roman Converter</a>
    <a class="ling-nav-btn active" href="/Roman_Linguistics">Roman Linguistics</a>
</div>
""", unsafe_allow_html=True)