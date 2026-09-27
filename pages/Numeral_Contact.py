import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS

# ============================================================
# NUMERAL CONTACT & TRANSMISSION
# Comparative page: how numeral words and numeral SYSTEMS move
# between languages, and how to tell borrowing (horizontal
# transmission) apart from common ancestry (vertical).
#
# Structure follows the distinction Comrie draws:
#   1. Borrowed words       - forms travel
#   2. Inherited look-alikes - forms only APPEAR to travel
#   3. Borrowed systems      - structure travels, words do not
#
# Sources: Comrie (2005, p.c. 2026); Campbell, Kaufman &
# Smith-Stark (1986) on the Mesoamerican linguistic area;
# Matras (2009) Language Contact.
# ============================================================

st.set_page_config(page_title="Numeral Contact & Transmission", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)

st.markdown("""
<style>
.nc-sub {
    font-family:'Crimson Pro',Georgia,serif; font-style:italic;
    font-size:1.05rem; color:var(--ink-muted); line-height:1.55;
    max-width:62ch; margin:.15rem 0 .9rem 0;
}
.nc-warn {
    background:rgba(184,92,56,.055); border:1px solid rgba(184,92,56,.24);
    border-left:3px solid var(--accent); border-radius:0 5px 5px 0;
    padding:1rem 1.25rem; margin:.6rem 0 1.2rem 0;
}
.nc-warn-label {
    font-family:'DM Sans',sans-serif; font-size:.62rem; font-weight:700;
    letter-spacing:.14em; text-transform:uppercase; color:var(--accent);
    margin-bottom:.45rem;
}
.nc-warn p { margin:0 0 .5rem 0; font-family:'Crimson Pro',Georgia,serif;
    font-size:1.02rem; line-height:1.6; color:var(--ink-soft); }
.nc-warn p:last-child { margin-bottom:0; }

.nc-split { display:grid; grid-template-columns:1fr 1fr; gap:1.1rem; margin-top:.5rem; }
@media (max-width:820px){ .nc-split { grid-template-columns:1fr; } }
.nc-col {
    background:var(--card-bg); border:1px solid var(--card-border);
    border-radius:6px; padding:1.1rem 1.3rem;
    box-shadow:0 1px 3px rgba(26,22,18,.04);
}
.nc-col.vertical { border-top:3px solid var(--teal); }
.nc-col.horizontal { border-top:3px solid var(--accent); }
.nc-col-title {
    font-family:'Crimson Pro',Georgia,serif; font-size:1.2rem; font-weight:600;
    color:var(--ink); margin-bottom:.15rem;
}
.nc-col-sub {
    font-family:'DM Sans',sans-serif; font-size:.68rem; font-weight:600;
    letter-spacing:.1em; text-transform:uppercase; margin-bottom:.7rem;
}
.nc-col.vertical .nc-col-sub { color:var(--teal); }
.nc-col.horizontal .nc-col-sub { color:var(--accent); }
.nc-col p { font-family:'Crimson Pro',Georgia,serif; font-size:.98rem;
    line-height:1.6; color:var(--ink-soft); margin:0 0 .6rem 0; }
.nc-col p:last-child { margin-bottom:0; }
.nc-col ul { margin:.2rem 0 .6rem 0; padding-left:1.1rem; }
.nc-col li { font-family:'Crimson Pro',Georgia,serif; font-size:.95rem;
    line-height:1.5; color:var(--ink-soft); margin-bottom:.3rem; }

.nc-chain {
    display:flex; align-items:center; gap:.7rem; flex-wrap:wrap;
    padding:.9rem 1.1rem; background:var(--parchment-2);
    border:1px solid var(--rule); border-radius:5px; margin:.5rem 0;
}
.nc-chain-node {
    font-family:'Crimson Pro',Georgia,serif; font-size:1.05rem; font-weight:600;
    color:var(--ink); padding:.3rem .7rem; background:var(--card-bg);
    border:1px solid var(--rule-strong); border-radius:3px;
}
.nc-chain-arrow { color:var(--accent); font-size:1.1rem; }
.nc-chain-note {
    font-family:'DM Sans',sans-serif; font-size:.72rem; color:var(--ink-faint);
    margin-left:auto;
}
.nc-debated {
    display:inline-block; font-family:'DM Sans',sans-serif; font-size:.6rem;
    font-weight:700; letter-spacing:.1em; text-transform:uppercase;
    color:#8a6a10; background:rgba(196,154,38,.13);
    border:1px solid rgba(196,154,38,.3); border-radius:2px;
    padding:.14rem .42rem; margin-left:.5rem; vertical-align:middle;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="lang-nav-crumb">'
    '<a href="/" target="_self">Home</a>'
    '<span class="sep">›</span>Cross-Linguistic'
    '<span class="sep">›</span>Contact &amp; Transmission'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Cross-Linguistic Comparison</div>
    <div class="ling-masthead-title">Contact &amp; Transmission</div>
    <div class="nc-sub">How numeral words and numeral structures move between languages — and why similar-looking numerals are so often not evidence of contact at all.</div>
    <div class="ling-tags">
        <span class="ling-tag">Borrowing</span>
        <span class="ling-tag">Areal Diffusion</span>
        <span class="ling-tag">Inheritance</span>
        <span class="ling-tag">Sprachbund</span>
        <span class="ling-tag">Methodology</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── The caveat, stated first ─────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Before Anything Else</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Two Reasons Numerals Look Alike</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="nc-warn">
    <div class="nc-warn-label">Methodological warning</div>
    <p>Resemblance between the numerals of two languages is <strong>not</strong> in itself
    evidence of contact. Two languages may share numeral forms because one borrowed from the
    other, or because both inherited them from a shared ancestor. These are entirely
    different historical events, and confusing them is the commonest error in amateur
    comparison.</p>
    <p>Every claim of borrowing on this page is one for which the direction and mechanism of
    transmission are documented in the literature. Where a case is disputed, it is marked
    as such.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="nc-split">
    <div class="nc-col vertical">
        <div class="nc-col-title">Vertical transmission</div>
        <div class="nc-col-sub">Inheritance · common ancestor</div>
        <p>The forms descend independently in each language from a shared parent. Nothing
        moved between them.</p>
        <p><strong>English</strong> <em>two</em> · <strong>Latin</strong> <em>duo</em> ·
        <strong>Greek</strong> <em>dúo</em> · <strong>Sanskrit</strong> <em>dvá</em> ·
        <strong>Russian</strong> <em>dva</em></p>
        <p>All continue Proto-Indo-European <em>*dwóh₁ </em>. English did not borrow
        <em>two</em> from Latin, and Sanskrit did not borrow from Greek. The similarity is
        inherited.</p>
        <p><strong>How you can tell:</strong> the forms obey the regular sound
        correspondences that hold across the entire inherited vocabulary, not just the
        numerals.</p>
    </div>
    <div class="nc-col horizontal">
        <div class="nc-col-title">Horizontal transmission</div>
        <div class="nc-col-sub">Borrowing · contact</div>
        <p>Forms passed from one language into another through speaker contact, often long
        after the languages diverged — or between languages that never shared an ancestor
        at all.</p>
        <p><strong>Swahili</strong> <em>sita</em> (6), <em>saba</em> (7), <em>tisa</em> (9)
        ← <strong>Arabic</strong> <em>sitta</em>, <em>sab’a</em>, <em>tis’a</em></p>
        <p>Swahili is Bantu and Arabic is Semitic; they share no ancestor. The borrowing is
        the result of centuries of Indian Ocean trade contact.</p>
        <p><strong>How you can tell:</strong> the borrowed forms sit oddly against the
        language's own patterns, and typically occupy only part of the range.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Borrowed words ───────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Pattern One</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Borrowed Words</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Numeral borrowing is frequently <em>partial</em>. A language may keep its inherited
    forms for the lowest values — which are used most often and learned earliest —
    while importing higher or less frequent ones.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Swahili: a split inventory</div>',
            unsafe_allow_html=True)

st.table({
    "Value": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "Swahili": ["moja", "mbili", "tatu", "nne", "tano",
                "sita", "saba", "nane", "tisa", "kumi"],
    "Origin": ["Bantu", "Bantu", "Bantu", "Bantu", "Bantu",
               "Arabic", "Arabic", "Bantu", "Arabic", "Bantu"],
})

st.markdown("""
<div class="ling-card">
    <p style="margin:0">Three slots — 6, 7 and 9 — are Arabic; the rest are
    inherited Bantu. The pattern is not random: these are exactly the values that several
    Bantu languages express with compound or quinary forms, and the shorter Arabic words
    displaced them. Swahili's numerals are in this repository's
    <a href="/Swahili_Converter" target="_self">converter</a>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Dual inventories in East Asia</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Japanese, Korean and Vietnamese each borrowed the complete Chinese numeral series
    while retaining their own. Both sets remain in active use, selected by context rather
    than one replacing the other.</p>
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">Japanese</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">hitotsu, futatsu, mittsu</span>
            <span class="ling-morph-gloss">native — versus Sino-Japanese <em>ichi, ni, san</em></span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Korean</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">hana, dul, set</span>
            <span class="ling-morph-gloss">native — versus Sino-Korean <em>il, i, sam</em></span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Vietnamese</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">một, hai, ba</span>
            <span class="ling-morph-gloss">native — versus Sino-Vietnamese <em>nhất, nhị, tam</em></span>
        </div>
    </div>
    <p style="margin:.8rem 0 0 0">A single language can therefore carry two complete numeral
    systems at once, with speakers switching between them according to what is being counted.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">A smaller case</div>
    <div class="ling-ex-line"><span class="num">10⁶</span><span class="word">English <em>million</em> ← Italian <em>milione</em>, an augmentative of <em>mille</em> &ldquo;thousand&rdquo;</span></div>
</div>
""", unsafe_allow_html=True)

# ── Borrowed systems ─────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Pattern Two</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Borrowed Systems, Native Words</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>A language can adopt the <em>architecture</em> of a neighbouring numeral system
    — its base, or which powers receive a name — without taking any of its
    vocabulary. Structure and vocabulary travel independently.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Vigesimal counting in Mesoamerica</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Base-20 counting is near-universal across Mesoamerica, in languages belonging to
    families with no demonstrable relationship to one another:</p>
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">Nahuatl</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">Uto-Aztecan</span>
            <span class="ling-morph-gloss">base 20</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Yucatec Maya</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">Mayan</span>
            <span class="ling-morph-gloss">base 20</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Mixtec, Zapotec</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">Oto-Manguean</span>
            <span class="ling-morph-gloss">base 20</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Totonac</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">Totonacan</span>
            <span class="ling-morph-gloss">base 20</span>
        </div>
    </div>
    <p style="margin:.8rem 0 0 0">The numeral <em>words</em> are unrelated across these
    families. What they share is the organising principle. Vigesimal counting is one of the
    defining features used to establish Mesoamerica as a linguistic area — a region
    where prolonged contact has produced shared structure across genetic boundaries.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">The Indic large-number series travels east</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The tradition of naming successive powers described on the
    <a href="/Large_Numbers" target="_self">Naming Large Numbers</a> page did not stay put.
    The Sanskrit scheme spread into Tibetan, which adopted the structure while using its own
    vocabulary; some of those Tibetan terms were then borrowed onward into Buryat, a
    Mongolic language.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="nc-chain">
    <span class="nc-chain-node">Sanskrit</span>
    <span class="nc-chain-arrow">→</span>
    <span class="nc-chain-node">Tibetan</span>
    <span class="nc-chain-arrow">→</span>
    <span class="nc-chain-node">Buryat</span>
    <span class="nc-chain-note">structure, then terms</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">Sanskrit → Tibetan</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">structure only</span>
            <span class="ling-morph-gloss">Tibetan names successive powers on the Indic model, using native forms — <em>stong</em> 10³, <em>khri</em> 10⁴, <em>'bum</em> 10⁵, <em>bye ba</em> 10⁷</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Tibetan → Buryat</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">terms</span>
            <span class="ling-morph-gloss">Buryat took several Tibetan large-number words directly, a second transmission step along the same chain</span>
        </div>
    </div>
    <p style="margin:.8rem 0 0 0">The two steps are of different kinds. Sanskrit gave Tibetan
    a <em>pattern</em>; Tibetan gave Buryat <em>words</em>. A single diffusion chain can
    change mode as it travels. Tibetan numerals are in this repository's
    <a href="/Tibetan_Converter" target="_self">converter</a> and
    <a href="/Tibetan_Linguistics" target="_self">grammar page</a>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p style="margin:0">A frequently cited European parallel is the vigesimal residue in
    French <em>quatre-vingts</em> (80), sometimes attributed to contact with a Celtic or
    Basque-like substrate.<span class="nc-debated">Disputed</span> The substrate account is
    contested and the internal development of Romance may be sufficient to explain it; it is
    listed here as a hypothesis rather than an established case.</p>
</div>
""", unsafe_allow_html=True)

# ── Why it matters ───────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Implications</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Why This Matters for Endangerment</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Borrowing is the principal mechanism by which a numeral system is lost. A language can
    keep its grammar, its lexicon and its speakers while its inherited counting system is
    displaced by a neighbour's — which is why numeral systems can be more endangered
    than the languages that carry them.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The shift is typically generational and gradual: borrowed numerals appear first in
    commerce and schooling, then spread to everyday counting, and a traditional vigesimal or
    body-part system falls out of use while the language around it remains perfectly healthy.
    Documentation of a language therefore does not guarantee documentation of its numerals.</p>
    <p style="margin-bottom:0">This is the reasoning behind including the
    <a href="/Olympiad_Problems" target="_self">problem repository</a>'s focus on
    structurally unusual systems: the systems most worth recording are frequently the ones
    under most pressure to disappear.</p>
</div>
""", unsafe_allow_html=True)

# ── Sources ──────────────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-card">
    <p style="margin:0 0 .5rem 0">Comrie, B. (2005). <em>Endangered numeral systems.</em> In
    Wohlgemuth &amp; Dirksmeyer (eds.), <em>Bedrohte Vielfalt</em>, 203–230. Berlin:
    Weißensee Verlag — and personal communication, 2026.</p>
    <p style="margin:0 0 .5rem 0">Campbell, L., Kaufman, T. &amp; Smith-Stark, T. (1986).
    Meso-America as a Linguistic Area. <em>Language</em> 62(3), 530–570.</p>
    <p style="margin:0 0 .5rem 0">Matras, Y. (2009). <em>Language Contact.</em> Cambridge
    University Press.</p>
    <p style="margin:0">Ashton, E. O. (1944). <em>Swahili Grammar.</em> Longman.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="nav-card-footer">'
    '<a class="nav-card" href="/Large_Numbers" target="_self">'
    '<div class="nav-card-eyebrow">Cross-Linguistic Comparison</div>'
    '<div class="nav-card-title">Naming large numbers</div>'
    '<div class="nav-card-desc">Four traditions for deciding which powers deserve a word '
    'of their own — and what happens at 10,000.</div>'
    '<div class="nav-card-cta">Naming Large Numbers →</div>'
    '</a>'
    '<a class="nav-card-home" href="/" target="_self">← Home</a>'
    '</div>',
    unsafe_allow_html=True,
)
