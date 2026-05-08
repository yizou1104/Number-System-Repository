import streamlit as st
from ui import apply_global_styles, home_nav

st.set_page_config(page_title="Yoruba Numerals — Linguistics", layout="centered")
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

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Yoruba Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Multiplicative</span>
        <span class="ling-tag">Additive</span>
        <span class="ling-tag">Subtractive</span>
        <span class="ling-tag">Tonal</span>
        <span class="ling-tag">Morphologically Invariant</span>
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
    <p>Yoruba is the only language in this repository that uses all three arithmetic operations — multiplication, addition, and subtraction — as grammatically productive strategies for forming numerals.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20 (vigesimal)</strong></span>
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val">Mixed — Multiplicative + Additive + Subtractive</span>
        <span class="ling-prop-key">Subtractive</span>
        <span class="ling-prop-val">Productive — used for 15–19, 25–29, and odd decades (50, 70, 90)</span>
        <span class="ling-prop-key">Additive</span>
        <span class="ling-prop-val">Restricted — units 1–4 above vigesimal bases</span>
        <span class="ling-prop-key">Tone</span>
        <span class="ling-prop-val">Three-level tonal (High, Mid, Low) — phonemically contrastive</span>
        <span class="ling-prop-key">Gender / case</span>
        <span class="ling-prop-val">Absent — numerals are morphologically invariant</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No indigenous zero term — modern mathematical contexts use loanforms</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS & BASES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (1–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": [1,2,3,4,5,6,7,8,9,10],
    "Form":   ["ọ̀kan","èjì","ẹ̀ta","ẹ̀rin","àrún","ẹ̀fà","èje","ẹ̀jọ","ẹ̀sán","ẹ̀wá"]
})

st.markdown("""
<div class="ling-info">
    <p>Yoruba is written in the Latin alphabet with tone diacritics. Tone distinctions on numerals are phonemically meaningful — changing the tone of a numeral can alter the word entirely. There are no indigenous numeral glyphs.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Vigesimal Bases</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["20","30","40","60","80","100","200","400"],
    "Form":      ["ogún","ọgbọ̀n","ogójì","ọgọ́ta","ọgọ́rin","ọgọ́rùn-ún","igba","irinwo"],
    "Structure": ["Base unit","Lexicalized decade","2 × 20","3 × 20","4 × 20","5 × 20","10 × 20","20 × 20"]
})

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Odd Decades</div>
    <p>50, 70, and 90 are not formed additively but subtractively: 50 = àádọ́ta ("10 less than 60"), 70 = àádọ́rin ("10 less than 80"), 90 = àádọ́rùn-ún ("10 less than 100"). The prefix <em>àádọ́-</em> is a fossilized subtractive morpheme.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — THREE ARITHMETIC OPERATIONS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Arithmetic Operations</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Multiplication, Addition, Subtraction</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Multiplicative Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">Multiplier × <em>20</em> (or higher vigesimal base)</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative examples</div>
    <div class="ling-ex-line"><span class="num">40</span><span class="word">ogójì</span><span class="gloss">2 × 20</span></div>
    <div class="ling-ex-line"><span class="num">60</span><span class="word">ọgọ́ta</span><span class="gloss">3 × 20</span></div>
    <div class="ling-ex-line"><span class="num">200</span><span class="word">igba</span><span class="gloss">10 × 20</span></div>
    <div class="ling-ex-line"><span class="num">400</span><span class="word">irinwo</span><span class="gloss">20 × 20</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Additive Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Addition is restricted to units 1–4 appearing above a vigesimal base. The connector <em>lé / lá</em> links the unit to the base.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">Unit (1–4) + <em>lé / lá</em> + Base</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Additive examples (teens and 20s)</div>
    <div class="ling-ex-line"><span class="num">11</span><span class="word">ọ̀kanlá</span><span class="gloss">1 + 10</span></div>
    <div class="ling-ex-line"><span class="num">12</span><span class="word">èjìlá</span><span class="gloss">2 + 10</span></div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">ọ̀kan lé ogún</span><span class="gloss">1 + 20</span></div>
    <div class="ling-ex-line"><span class="num">22</span><span class="word">èjìlélógún</span><span class="gloss">2 + 20</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Subtractive Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Subtractive Dominance</div>
    <p>Yoruba strongly prefers subtraction for 15–19 and 25–29. These are not alternative forms — subtraction is the grammatically primary strategy for these numbers.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Subtracted quantity] + <em>dín</em> + Base</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Subtractive examples</div>
    <div class="ling-ex-line"><span class="num">15</span><span class="word">ẹ̀ẹ́dógún</span><span class="gloss">5 from 20</span></div>
    <div class="ling-ex-line"><span class="num">16</span><span class="word">ẹ̀rìndínlógún</span><span class="gloss">4 less than 20</span></div>
    <div class="ling-ex-line"><span class="num">19</span><span class="word">ọ̀kàndínlógún</span><span class="gloss">1 less than 20</span></div>
    <div class="ling-ex-line"><span class="num">50</span><span class="word">àádọ́ta</span><span class="gloss">10 less than 60</span></div>
    <div class="ling-ex-line"><span class="num">90</span><span class="word">àádọ́rùn-ún</span><span class="gloss">10 less than 100</span></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — CONNECTORS & SPECIAL FORMS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Connectors &amp; Special Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Operators and Special Cases</div>', unsafe_allow_html=True)

st.table({
    "Element":  ["lé / lá","dín","àádọ́-"],
    "Function": ["Additive connector ('plus')","Subtractive marker ('less than')","Fossilized subtractive prefix (10 less than base)"]
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Lexicalization</div>
        <p>Some forms are historically compositional but now lexicalized: <em>ọgbọ̀n</em> (30) no longer transparently means "10 + 20." Lexicalization is most common in the lower decades.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Modern Simplification</div>
        <p>In urban and commercial contexts, subtractive constructions are sometimes replaced with decimal-style counting. This is a contact-driven simplification, not grammatical change.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Inflection &amp; Ordinals</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Inflection</span>
        <span class="ling-prop-val">Absent — numerals are invariant lexical items</span>
        <span class="ling-prop-key">Gender</span>
        <span class="ling-prop-val">No grammatical gender</span>
        <span class="ling-prop-key">Case</span>
        <span class="ling-prop-val">No case marking</span>
        <span class="ling-prop-key">Agreement</span>
        <span class="ling-prop-val">No agreement morphology</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Ordinal Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Ordinals are formed derivationally, not inflectionally — the ordinal prefix <em>è-/ẹ̀-</em> attaches to the cardinal root.</p>
    <div class="ling-morph-table" style="margin-top:.75rem">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1st</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">àkọ́kọ́</span>
            <span class="ling-morph-gloss">suppletive</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">2nd</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">èkejì</span>
            <span class="ling-morph-gloss">è- + cardinal root</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">3rd</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ẹ̀kẹta</span>
            <span class="ling-morph-gloss">ẹ̀- + cardinal root</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ──────────────────────────────────────────────
st.markdown('<div class="nav-row">', unsafe_allow_html=True)
st.page_link("pages/Yoruba_Converter.py", label="← Yoruba Converter")
st.page_link("Home.py", label="← Home")
st.markdown('</div>', unsafe_allow_html=True)