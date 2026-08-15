import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Thai Numerals — Linguistics", layout="wide")
apply_global_styles()

st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Thai", "linguistics")

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

# ── NAVIGATION ──────────────────────────────────────────────
footer_nav("Thai", "linguistics")
