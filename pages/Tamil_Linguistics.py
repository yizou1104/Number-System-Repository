import streamlit as st
from ui import apply_global_styles

st.set_page_config(page_title="Thai Numerals — Linguistics", layout="centered")
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

# ── MASTHEAD ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Thai Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Decimal</span>
        <span class="ling-tag">Multiplicative–Additive</span>
        <span class="ling-tag">Non-Subtractive</span>
        <span class="ling-tag">Position-Sensitive Forms</span>
        <span class="ling-tag">Morphologically Invariant</span>
        <span class="ling-tag">Classifier-Dependent</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1 — SYSTEM OVERVIEW ─────────────────────────────────────────────
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Thai has two lexically irregular numeral forms that are positionally conditioned:
    <em>ยี่</em> replaces <em>สอง</em> (2) exclusively in the tens position, and <em>เอ็ด</em>
    replaces <em>หนึ่ง</em> (1) when it appears as the final unit of a compound number.</p>
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
        <span class="ling-prop-key">Position-sensitive forms</span>
        <span class="ling-prop-val"><em>ยี่</em> (2 in tens) · <em>เอ็ด</em> (1 as final unit)</span>
        <span class="ling-prop-key">Morphology</span>
        <span class="ling-prop-val">Invariant — no gender, case, or agreement</span>
        <span class="ling-prop-key">Syntax</span>
        <span class="ling-prop-val">Numeral + Classifier + Noun (classifier obligatory)</span>
        <span class="ling-prop-key">Script</span>
        <span class="ling-prop-val">Own numeral glyphs (๐–๙); Arabic numerals also widely used</span>
        <span class="ling-prop-key">Large-number pivot</span>
        <span class="ling-prop-val">ล้าน (10⁶) — recursive million-based grouping</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 2 — DIGITS & BASES ───────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Basic Digits (0–10)</div>', unsafe_allow_html=True)

st.table({
    "Number": ["0","1","2","3","4","5","6","7","8","9","10"],
    "Glyph":  ["๐","๑","๒","๓","๔","๕","๖","๗","๘","๙","๑๐"],
    "Form":   ["ศูนย์","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า","สิบ"],
})

st.markdown("""
<div class="ling-info">
    <p>Thai numeral glyphs (๐–๙) appear in manuscripts, official documents, and traditional contexts.
    In everyday writing and digital contexts, Arabic numerals (0–9) are equally standard.
    <em>ศูนย์</em> (zero) is borrowed from Sanskrit <em>śūnya</em>, the same root as Arabic "zero" via Persian.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Bases and Higher Units</div>', unsafe_allow_html=True)

st.table({
    "Value":     ["20","30","100","1,000","10,000","100,000","1,000,000"],
    "Form":      ["ยี่สิบ","สามสิบ","ร้อย","พัน","หมื่น","แสน","ล้าน"],
    "Structure": ["2 × 10 (irregular ยี่)","3 × 10","independent unit","independent unit",
                  "10⁴ unit","10⁵ unit","10⁶ recursive pivot"],
})

# ── SECTION 3 — COMPOSITIONAL RULES ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How Numbers Are Built</div>', unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Multiplicative Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">Digit + <em>Base unit</em> · left-to-right in descending order</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Multiplicative examples</div>
    <div class="ling-ex-line"><span class="num">300</span><span class="word">สามร้อย</span><span class="gloss">3 × 100</span></div>
    <div class="ling-ex-line"><span class="num">5,000</span><span class="word">ห้าพัน</span><span class="gloss">5 × 1,000</span></div>
    <div class="ling-ex-line"><span class="num">70,000</span><span class="word">เจ็ดหมื่น</span><span class="gloss">7 × 10,000</span></div>
    <div class="ling-ex-line"><span class="num">3,000,000</span><span class="word">สามล้าน</span><span class="gloss">3 × 1,000,000</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>ล้าน (10⁶) is a recursive pivot: larger values are expressed as multiples of ล้าน,
    not as separate named units. 10,000,000 = สิบล้าน (10 × million),
    1,000,000,000 = หนึ่งพันล้าน (1,000 × million).</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Additive Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[Higher unit] + [Lower unit] · strict descending order, no connector word</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Compound examples</div>
    <div class="ling-ex-line"><span class="num">32</span><span class="word">สามสิบสอง</span><span class="gloss">30 + 2</span></div>
    <div class="ling-ex-line"><span class="num">1,234</span><span class="word">หนึ่งพันสองร้อยสามสิบสี่</span><span class="gloss">1000 + 200 + 30 + 4</span></div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4 — POSITIONAL IRREGULARITIES ────────────────────────────────────
st.markdown('<div class="ling-section-label">Positional Irregularities</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">ยี่ and เอ็ด</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">ยี่ — "2" in the tens</div>
        <p>When 2 occupies the tens position (forming 20), <em>สอง</em> is replaced by
        <em>ยี่</em>. This is a lexical suppletive form, not a phonological rule —
        it applies only to the decade word for 20.</p>
        <div class="ling-morph-row" style="margin-top:.65rem">
            <span class="ling-morph-source">สอง + สิบ</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ยี่สิบ</span>
            <span class="ling-morph-gloss">20 (not *สองสิบ)</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">สาม + สิบ</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">สามสิบ</span>
            <span class="ling-morph-gloss">30 (regular)</span>
        </div>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">เอ็ด — "1" as final unit</div>
        <p>When 1 appears as the terminal unit in a compound number (not standalone),
        <em>หนึ่ง</em> is replaced by <em>เอ็ด</em>. The form <em>หนึ่ง</em>
        is retained when 1 stands alone or precedes a higher base unit.</p>
        <div class="ling-morph-row" style="margin-top:.65rem">
            <span class="ling-morph-source">ยี่สิบ + หนึ่ง</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ยี่สิบเอ็ด</span>
            <span class="ling-morph-gloss">21</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">ร้อย + หนึ่ง</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">ร้อยเอ็ด</span>
            <span class="ling-morph-gloss">101</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Why it matters for Olympiad problems</div>
    <p>The Olympiad question "why is 21 written ยี่สิบเอ็ด and not สองสิบหนึ่ง?" requires
    knowing both rules simultaneously: ยี่ replaces สอง in tens, and เอ็ด replaces หนึ่ง as
    final unit — two independent suppletive substitutions applying in the same word.</p>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5 — SYNTAX & MORPHOLOGY ──────────────────────────────────────────
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Grammatical Integration</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Numeral–Classifier–Noun</div>
        <p>Thai numerals are post-nominal in most counting contexts, with a classifier
        intervening between the numeral and noun. Classifiers are grammatically obligatory
        in standard counted noun phrases.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.88rem;color:var(--ink-muted);margin-top:.5rem">หนึ่งคน &nbsp;<em style="font-family:'Crimson Pro',serif">(one person)</em><br>สามเล่ม &nbsp;<em style="font-family:'Crimson Pro',serif">(three [volumes])</em></p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:.5rem">Digit-by-Digit Reading</div>
        <p>Serial numbers, telephone numbers, and years are often read one digit at a time,
        using the base forms (not compound forms). This is a distinct register from
        cardinal counting.</p>
        <p style="font-family:'DM Mono',monospace;font-size:.88rem;color:var(--ink-muted);margin-top:.5rem">1984 → หนึ่ง เก้า แปด สี่</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.5rem">Ordinal Formation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Ordinals are formed analytically by prefixing <em>ที่</em> to the cardinal.
    The construction is productive and regular with no suppletive forms.</p>
    <div class="ling-morph-row" style="margin-top:.65rem">
        <span class="ling-morph-source">1 (หนึ่ง)</span>
        <span class="ling-morph-arrow">→</span>
        <span class="ling-morph-target">ที่หนึ่ง</span>
        <span class="ling-morph-gloss">first</span>
    </div>
    <div class="ling-morph-row">
        <span class="ling-morph-source">2 (สอง)</span>
        <span class="ling-morph-arrow">→</span>
        <span class="ling-morph-target">ที่สอง</span>
        <span class="ling-morph-gloss">second</span>
    </div>
    <div class="ling-morph-row">
        <span class="ling-morph-source">3 (สาม)</span>
        <span class="ling-morph-arrow">→</span>
        <span class="ling-morph-target">ที่สาม</span>
        <span class="ling-morph-gloss">third</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Reduplication of base units (<em>ร้อย ๆ</em> "hundreds of", <em>พัน ๆ</em> "thousands of")
    expresses rough approximation or large quantities — a distinct grammatical pattern
    not available in, for example, Chinese or Hindi.</p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="ling-nav-footer">
    <a class="ling-nav-btn" href="/Thai_Converter">← Thai Converter</a>
    <a class="ling-nav-btn active" href="/Thai_Linguistics">Thai Linguistics</a>
</div>
""", unsafe_allow_html=True)