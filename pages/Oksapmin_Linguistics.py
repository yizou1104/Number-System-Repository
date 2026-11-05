import streamlit as st

from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav
from Oksapmin import UPPER, LOWER, SAXE, OK_SVG_CSS, body_svg, gloss

st.set_page_config(page_title="Oksapmin Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
st.markdown(OK_SVG_CSS, unsafe_allow_html=True)
language_nav("Oksapmin", "linguistics")

st.markdown("""
<style>
.ok-figure-pair { display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; margin-bottom: .85rem; }
@media (max-width: 700px) { .ok-figure-pair { grid-template-columns: 1fr; } }
.ok-figure-cap { font-family: 'DM Sans', sans-serif; font-size: .62rem; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--ink-faint); text-align: center; margin-top: .3rem; }
.ling-ex-line .num { min-width: 2.2rem; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Oksapmin Numerals</div>
    <div class="ling-masthead-sub">
        A body-part tally from the highlands of Papua New Guinea: twenty-seven named points
        from one thumb, over the face, to the other hand.
    </div>
    <div class="ling-tags">
        <span class="ling-tag">Body-Part Tally</span>
        <span class="ling-tag">27-Point Cycle</span>
        <span class="ling-tag">Numbers Are Nouns</span>
        <span class="ling-tag">Two Dialects</span>
        <span class="ling-tag">Trans New Guinea Isolate</span>
        <span class="ling-tag">Giving Way to Tok Pisin</span>
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
    <p>Above five, Oksapmin's own numbers are the names of body parts. A speaker counts by
    touching the body in a fixed order — thumb, fingers, wrist, up the arm, across the face to
    the nose — and naming each point, so that <em>nata</em> 'ear' means twelve. The count then
    runs down the other side, and <em>tən nata</em> 'side ear' means sixteen. One full circuit
    of the body is twenty-seven.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">System type</span>
        <span class="ling-prop-val"><strong>Body-part tally</strong> — numbers are names of points on the body</span>
        <span class="ling-prop-key">Cycle</span>
        <span class="ling-prop-val">27 points; one circuit is <em>tit pu</em> 'once around the body'</span>
        <span class="ling-prop-key">Turning point</span>
        <span class="ling-prop-val">The nose, 14 — the only point without a partner</span>
        <span class="ling-prop-key">Second-side marker</span>
        <span class="ling-prop-val"><em>tən</em> 'side', from 15 to 27</span>
        <span class="ling-prop-key">Counting things</span>
        <span class="ling-prop-val">Body part + possessive: <em>amun=xe dik</em> 'elbow's nights', eight nights</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">None — the count begins at the thumb</span>
        <span class="ling-prop-key">Language</span>
        <span class="ling-prop-val">Oksapmin — a family-level isolate within Trans New Guinea, not an Ok language despite its name</span>
        <span class="ling-prop-key">Speakers</span>
        <span class="ling-prop-val">About 8,000 (Lawrence 1993, in Loughnane 2009); Lawrence's 2018 estimate is about 12,000</span>
        <span class="ling-prop-key">Location</span>
        <span class="ling-prop-val">Tekin Valley, Sandaun Province (formerly West Sepik), Papua New Guinea</span>
        <span class="ling-prop-key">Dialects</span>
        <span class="ling-prop-val">Upper and Lower — mutually intelligible, about 87% shared basic vocabulary</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>"Oksapmin" is the name the neighbouring Telefomin gave to the people of the Tekin Valley,
    meaning 'the bush people of the water'; speakers call their language simply <em>nuxule
    meŋ</em> 'our language' (Loughnane 2009: 1). It is still the first language most children
    in the valley learn. Primary school, however, is taught largely in Tok Pisin and high
    school in English — and counting is shifting with them (Saxe &amp; Esmonde 2004).</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — THE COUNT
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">The Count</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Twenty-Seven Points</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="ok-figure-pair">
    <div class="ling-card" style="margin-bottom:0">{body_svg("upper")}<div class="ok-figure-cap">Upper Oksapmin — second hand thumb first</div></div>
    <div class="ling-card" style="margin-bottom:0">{body_svg("lower")}<div class="ok-figure-cap">Lower Oksapmin — second hand little finger first</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Thirteen points climb the first side, the nose stands alone at 14, and thirteen points
    descend the other side. The figures put the first side on the viewer's left; the sources do
    not say which hand begins. The two dialects agree on every point except the last five,
    where they count the second hand in opposite directions, as the next section explains.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Number":            [str(n) for n in range(1, 28)],
    "Upper Oksapmin":    [UPPER[n][0][0] for n in range(1, 28)],
    "Saxe's spelling":   [SAXE[n] for n in range(1, 28)],
    "Lower Oksapmin":    [LOWER[n][0][0] for n in range(1, 28)],
    "Gloss":             [gloss(n, "upper") if gloss(n, "upper") == gloss(n, "lower")
                          else f"{gloss(n, 'upper')} / {gloss(n, 'lower')}"
                          for n in range(1, 28)],
})

st.markdown("""
<div class="ling-info">
    <p>Upper Oksapmin is Marshall Lawrence's 2018 transcription; Saxe's spelling is the same
    dialect as Saxe recorded it in the late 1970s, with <em>^</em> for the central vowel written <em>ə</em>
    by Lawrence. Lower Oksapmin is Robyn Loughnane's: her grammar (2009: 16) gives 1–16, and
    her 2008 database entry the rest. Where two glosses appear, the first is Upper and the
    second Lower. Each source also records shorter variants — <em>kina ~ kin</em>, <em>nata ~
    nat</em> — which the converter lists.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — STRUCTURE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Structure</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Up One Side, Down the Other</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">1–14: [body part] &nbsp;·&nbsp; 15–27: <em>tən</em> 'side' + [body part]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Upper Oksapmin — the same word, either side of the nose</div>
    <div class="ling-ex-line"><span class="num">12</span><span class="word">nata</span><span class="gloss">ear</span></div>
    <div class="ling-ex-line"><span class="num">13</span><span class="word">kina</span><span class="gloss">eye</span></div>
    <div class="ling-ex-line"><span class="num">14</span><span class="word">ɾuma</span><span class="gloss">nose — the turning point</span></div>
    <div class="ling-ex-line"><span class="num">15</span><span class="word">tən kina</span><span class="gloss">side eye</span></div>
    <div class="ling-ex-line"><span class="num">16</span><span class="word">tən nata</span><span class="gloss">side ear</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>There is no addition, multiplication or base here. Each number is a position, and the
    word for it is simply the name of the place where the count has arrived. The only
    structure is the symmetry: every point from 1 to 13 has a mirror point from 15 to 27,
    distinguished by <em>tən</em> 'side'. Fourteen, the nose, has no partner.</p>
    <p>Because the second half repeats the first half's words, the marker carries all the
    information — and Lawrence notes that from 23 onward it is often dropped, so that the word
    for 23 is the same as the word for 1. The pointing hand resolves it.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — DIALECTS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Dialects</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Two Ways Down the Second Arm</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Upper: repeat the order</div>
        <p>At the second wrist the count jumps to the thumb and runs to the little finger again:
        23 is the thumb, 27 the little finger. Saxe's 1981 list and Lawrence's 2018 list agree on
        this, nearly forty years apart. Lawrence's prose summary describes the reverse
        order; his numbered list, and his separate list of quantity forms, do not.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Lower: mirror the first side</div>
        <p>The count continues along the hand without a jump — little finger, ring, middle,
        index, thumb — so 23 is the little finger and 27 the thumb, a mirror image of 1–5. The
        only record is Loughnane's 2008 entry; her grammar's table stops at 16, so this rests
        on a single source.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">The same number, two dialects — words and word order both differ</div>
    <div class="ling-ex-line"><span class="num">1</span><span class="word">tiβəna</span><span class="gloss">Upper — thumb</span></div>
    <div class="ling-ex-line"><span class="num">1</span><span class="word">tipun</span><span class="gloss">Lower — thumb</span></div>
    <div class="ling-ex-line"><span class="num">8</span><span class="word">kiɾ</span><span class="gloss">Upper — elbow</span></div>
    <div class="ling-ex-line"><span class="num">8</span><span class="word">amun</span><span class="gloss">Lower — elbow</span></div>
    <div class="ling-ex-line"><span class="num">23</span><span class="word">tən tiβəna</span><span class="gloss">Upper — side + thumb</span></div>
    <div class="ling-ex-line"><span class="num">23</span><span class="word">xətxət tən</span><span class="gloss">Lower — little finger + side</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Word order differs too: Upper puts <em>tən</em> first (<em>tən kina</em>), while Lower
    usually puts it after the body part (<em>kin tən</em>). Loughnane records both orders in
    Lower Oksapmin at 15 and 16. Lawrence (1980) estimates the two dialects share 80–90% of
    their basic vocabulary. Among the fourteen body-part words, four are different words
    altogether — thumb, index finger, wrist and elbow — while most of the rest are close
    variants, often with Upper <em>ɾ</em> where Lower has <em>l</em>: <em>bumɾup</em> and
    <em>bumlip</em>, <em>gweɾa</em> and <em>gwel</em>.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — GRAMMAR
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Grammar</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Numbers That Are Nouns</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Quantity</span>
    <span class="ling-formula-rule">[body part]<em>=xe</em> 'POSS' + [noun] — 'the elbow's nights' = eight nights</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>A body-part numeral is grammatically an ordinary noun. To count something it becomes
    the possessor of that thing, with the possessive clitic <em>=xe</em>: <em>amun=xe dik</em>
    'elbow's nights' means eight nights, <em>kat=xe dik</em> 'shoulder's nights' ten nights,
    <em>xətxət=xe xan</em> 'little finger's men' five men (Loughnane 2009, ex. 1-6, 7-43,
    7-42). Nothing distinguishes it, Loughnane notes, from any other possessive construction.
    On its own, with the definite article, the same noun is an ordinal: <em>təwət jox</em>
    'the upper arm' — the ninth night.</p>
    <p>Upper Oksapmin has a parallel pattern with what Lawrence calls the quantity marker <em>-xeⁱ</em>:
    <em>kiɾxeⁱ</em> 'eight (of them)', <em>tən kinxeⁱ</em> 'fifteen' (Lawrence 2018).
    Loughnane suggests that the question word <em>kinxe</em> 'how many' may itself come from
    <em>kjan=xe</em> 'what (body part)'s' — the counting system written into the grammar of
    asking.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Below Six: Words That Are Only Numbers</div>', unsafe_allow_html=True)

st.table({
    "Quantity":       ["1", "2", "3", "4", "5"],
    "Upper Oksapmin": ["tita ~ tit", "yota ~ yot", "yitiɾ", "yotayota ~ yotyot",
                       "xətxət timbəs ~ xanin"],
    "Lower Oksapmin": ["pitle ~ pitil", "—", "ot=a tit=a", "xətxət tibəs", "xanengon"],
    "Literal":        ["one", "two", "three / two-and-one", "two-two / no little finger",
                       "five / fist"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">A count in twos</div>
        <p>Upper <em>yotayota</em> 'two-two' for four, and Lower <em>ot=a tit=a</em> 'two and one'
        for three, belong to what Loughnane calls a base-two count, separate from the body
        tally. In Lower Oksapmin she traces the indefinite word <em>tit</em> to a numeral 'one'
        no longer used there as a number — Lower now says <em>pitle</em> — yet Upper Oksapmin
        still counts <em>tita</em> 'one'.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">A disagreement at four and five</div>
        <p>Loughnane gives <em>xətxət tibəs</em> 'no little finger' as <strong>four</strong> —
        four fingers, the little one not yet counted — with a text example. Lawrence gives the
        Upper equivalent <em>xətxət timbəs</em> as <strong>five</strong>. Both are reported
        here as their sources give them; the difference may be dialectal.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — CHANGE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Beyond 27 &amp; Change</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Count Under Pressure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Why this matters</div>
    <p>Oksapmin is still the language children learn first. Its counting system is not. The
    body tally is giving way to Tok Pisin and English numbers through school and the cash
    economy — a case of a numeral system more endangered than the language that carries it.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Past twenty-seven</div>
        <p>A full circuit is <em>pu</em> 'unit' — <em>tit pu</em>, 'once around the body'
        (Lawrence 2018). To count further, Saxe and Esmonde (2004) describe a speaker turning back
        up the second arm: 28 is the wrist again, 29 the forearm. The 21st and 29th points are
        therefore both <em>tan-besa</em>, and only the course of the count distinguishes them.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Shortened to twenty</div>
        <p>Saxe and Esmonde found many people using variants that stop at the 20th point, <em>tan-kir</em> 'other elbow', continuing to <em>tan-besa</em> or starting
        again at the thumb to go higher. Twenty was also the number of shillings in the old
        Australian pound.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Saxe's studies, from fieldwork in 1978, 1980 and 2001, follow the system through the
    arrival of money. In trade stores, older customers quantified with the body tally while
    younger and schooled customers used Tok Pisin (Saxe &amp; Esmonde 2004). The word
    <em>fu</em> shifted from an intensifier meaning 'a complete group of plenty' to an
    arithmetic operation, 'double a value' (Saxe &amp; Esmonde 2005). Lawrence reports that by
    2005, <em>pu</em> — 'once around the body' — was commonly used for a two-kina note, worth
    twenty of the old shillings.</p>
    <p>Saxe spells the word <em>fu</em>, Lawrence <em>pu</em>; in Lawrence's orthography
    <em>p</em> covers a sound pronounced [pɸ], so they are plausibly the same word heard
    through two transcription systems. That identification is this page's inference, not a
    claim either source makes.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Record</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What the Converter Shows and Why</div>', unsafe_allow_html=True)

st.table({
    "Range":  ["1–16", "17–27 (Upper)", "17–27 (Lower)", "28–29 (Upper)", "30 and above"],
    "Status": ["Corroborated", "Corroborated", "Single source", "Described", "Not given"],
    "Basis":  ["Saxe, Lawrence and Loughnane's grammar all agree on the points",
               "Saxe (1981) and Lawrence (2018) agree point for point",
               "Loughnane's 2008 database entry only",
               "Saxe & Esmonde (2004): the count turns back up the arm",
               "No source describes the count beyond the second forearm"],
})

st.markdown("""
<div class="ling-info">
    <p>Forms are reproduced as each source prints them, apart from writing the script letter
    <em>ɡ</em> as an ordinary <em>g</em>. Where Loughnane's database entry and her later
    grammar spell a word differently — <em>xədəp</em> and <em>armun</em> in 2008,
    <em>xadəp</em> and <em>amun</em> in 2009 — the grammar is followed. Quantity forms are
    given only where a source records them or states the rule that produces them.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Loughnane, Robyn.</strong> 2009. <em>A Grammar of Oksapmin</em>. PhD thesis,
    University of Melbourne. Open access. §1.1 (dialects, speakers), §1.2.5 and Table 1-5 (the
    body-part counting system), §1.3.1 (classification), §4 and §6.3.2 (numerals in the
    possessive construction).</p>
    <p><strong>Lawrence, Marshall.</strong> 2018. Oksapmin (Upper dialect), counting and quantity
    numerals. In Eugene S. L. Chan, <em>Numeral Systems of the World's Languages</em>. Max Planck
    Institute for Evolutionary Anthropology.</p>
    <p><strong>Loughnane, Robyn.</strong> 2008. Oksapmin (Lower dialect), numerals. In Chan,
    <em>Numeral Systems of the World's Languages</em>.</p>
    <p><strong>Saxe, Geoffrey B.</strong> 1981. "Body Parts as Numerals: A Developmental
    Analysis of Numeration among the Oksapmin in Papua New Guinea." <em>Child Development</em>
    52: 306–316.</p>
    <p><strong>Saxe, Geoffrey B. &amp; Indigo Esmonde.</strong> 2004. "Making Change in Oksapmin
    Tradestores: A Study of Shifting Practices of Quantification under Conditions of Rapid Shift
    towards a Cash Economy." <em>South Pacific Journal of Psychology</em> 15: 11–28. Figure 1
    reproduces Saxe's 1981 list.</p>
    <p><strong>Saxe, Geoffrey B. &amp; Indigo Esmonde.</strong> 2005. "Studying Cognition in
    Flux: A Historical Treatment of <em>Fu</em> in the Shifting Structure of Oksapmin
    Mathematics." <em>Mind, Culture, and Activity</em> 12(3–4).</p>
    <p><strong>Saxe, Geoffrey B.</strong> 2012. <em>Cultural Development of Mathematical Ideas:
    Papua New Guinea Studies</em>. Cambridge University Press.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on sources not used.</strong> Several popular websites and blog posts
    reproduce Oksapmin body-part words second-hand, sometimes with silent changes to spelling or
    order. They were used only to locate the primary sources above, never as evidence.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Oksapmin", "linguistics")
