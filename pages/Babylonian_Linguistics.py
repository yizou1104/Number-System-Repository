import streamlit as st

from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Babylonian Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Babylonian", "linguistics")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Cuneiform&display=swap');
.ling-ex-line .num { min-width: 3.6rem; }
.ling-ex-line .word { font-family: 'DM Mono', 'Noto Sans Cuneiform', 'Courier New', monospace; font-size: 1.15rem; }
.bab-cun { font-family: 'Noto Sans Cuneiform', sans-serif; }
.bab-signs { display: grid; grid-template-columns: repeat(auto-fill, minmax(4.4rem, 1fr)); gap: .5rem; margin: .2rem 0 .3rem 0; }
.bab-sign { background: var(--parchment-2); border: 1px solid var(--rule); border-radius: 4px; padding: .55rem .3rem .4rem; text-align: center; }
.bab-sign-glyph { font-family: 'Noto Sans Cuneiform', sans-serif; font-size: 1.7rem; color: var(--ink); line-height: 1.3; min-height: 2.3rem; }
.bab-sign-num { font-family: 'DM Mono', 'Courier New', monospace; font-size: .8rem; color: var(--accent); }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Babylonian Numerals</div>
    <div class="ling-masthead-sub">
        The sexagesimal place-value notation of Old Babylonian mathematics — the earliest
        known positional numeral system, written with two wedge shapes and no zero.
    </div>
    <div class="ling-tags">
        <span class="ling-tag">Sexagesimal</span>
        <span class="ling-tag">Positional</span>
        <span class="ling-tag">Decimal Sub-base</span>
        <span class="ling-tag">Floating Point</span>
        <span class="ling-tag">Cuneiform</span>
        <span class="ling-tag">Sumerian &amp; Akkadian</span>
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
    <p>Babylonian scribes wrote every digit from 1 to 59 with just two signs, then let a
    sign's position decide its value — the earliest positional numeral system in the
    surviving record. The same vertical wedge means one, sixty or one-sixtieth depending on
    where it stands. What they never wrote was a mark for where the whole number ends, so
    the reader had to supply the scale.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>60 (sexagesimal)</strong>, positional</span>
        <span class="ling-prop-key">Sub-base</span>
        <span class="ling-prop-val">10, inside each place — tens and units grouped additively</span>
        <span class="ling-prop-key">Signs</span>
        <span class="ling-prop-val">Two: the vertical wedge <span class="bab-cun">𒁹</span> (1) and the corner wedge <span class="bab-cun">𒌋</span> (10)</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No numeral. Empty places left blank; a placeholder appears c. 300 BCE, only between digits</span>
        <span class="ling-prop-key">Sexagesimal point</span>
        <span class="ling-prop-val">None — the scale of a number was fixed by context</span>
        <span class="ling-prop-key">Earliest systematic use</span>
        <span class="ling-prop-val">Mathematical texts of the Ur III period, c. 2112–2004 BCE</span>
        <span class="ling-prop-key">Main period</span>
        <span class="ling-prop-val">Old Babylonian, c. 2000–1600 BCE</span>
        <span class="ling-prop-key">Writers</span>
        <span class="ling-prop-val">Scribes trained in both Sumerian and Akkadian</span>
        <span class="ling-prop-key">Medium</span>
        <span class="ling-prop-val">A reed stylus pressed into damp clay</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>"Babylonian" here names a written notation, not a spoken numeral system. The scribes
    who used it spoke Akkadian and trained in Sumerian, which by this period survived mainly
    as a written language of learning; the notation served both. "Old Babylonian" is a period
    label: it covers the bulk of the surviving mathematical tablets, including the two
    discussed below.</p>
    <p>Numbers in the modern literature are transliterated with commas between places and a
    semicolon before the fractional part — <em>1;24,51,10</em>. That convention is
    Neugebauer's. The tablets themselves mark neither.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Two Signs, Fifty-Nine Digits</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[corner wedges, 0–5 × <em>10</em>] + [vertical wedges, 0–9 × <em>1</em>] = one place, 1–59</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title" style="font-size:1.05rem">Units</div>
    <div class="bab-signs">
        <div class="bab-sign"><div class="bab-sign-glyph">𒐕</div><div class="bab-sign-num">1</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒐖</div><div class="bab-sign-num">2</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒐗</div><div class="bab-sign-num">3</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒐘</div><div class="bab-sign-num">4</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒐙</div><div class="bab-sign-num">5</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒐚</div><div class="bab-sign-num">6</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒑂</div><div class="bab-sign-num">7</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒑄</div><div class="bab-sign-num">8</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒑆</div><div class="bab-sign-num">9</div></div>
    </div>
    <div class="ling-subsection-title" style="font-size:1.05rem;margin-top:.9rem">Tens</div>
    <div class="bab-signs">
        <div class="bab-sign"><div class="bab-sign-glyph">𒌋</div><div class="bab-sign-num">10</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒎙</div><div class="bab-sign-num">20</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒌍</div><div class="bab-sign-num">30</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒐏</div><div class="bab-sign-num">40</div></div>
        <div class="bab-sign"><div class="bab-sign-glyph">𒐐</div><div class="bab-sign-num">50</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Within a place, tens come first, then units</div>
    <div class="ling-ex-line"><span class="num">7</span><span class="word">𒑂</span><span class="gloss">seven wedges, stacked three, three and one</span></div>
    <div class="ling-ex-line"><span class="num">23</span><span class="word">𒎙𒐗</span><span class="gloss">two corner wedges, three vertical</span></div>
    <div class="ling-ex-line"><span class="num">59</span><span class="word">𒐐𒑆</span><span class="gloss">the largest digit — five tens, nine units</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Inside a single place the system is additive and decimal: a scribe simply pressed in
    as many corner wedges and vertical wedges as needed. From four upward the units are
    stacked in rows so they can be counted at a glance. The arrangement varied from scribe to
    scribe; the forms shown here are the standardised Unicode shapes.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — PLACE VALUE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Place Value</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Positional Above Fifty-Nine</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Value</span>
    <span class="ling-formula-rule">… + d₂ × <em>3600</em> + d₁ × <em>60</em> + d₀ — each dᵢ from 0 to 59, an empty place left unwritten</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Once a place is full, the count moves one place left</div>
    <div class="ling-ex-line"><span class="num">60</span><span class="word">𒐕</span><span class="gloss">1 × 60 — the same sign as 1</span></div>
    <div class="ling-ex-line"><span class="num">61</span><span class="word">𒐕 𒐕</span><span class="gloss">1 × 60 + 1</span></div>
    <div class="ling-ex-line"><span class="num">2024</span><span class="word">𒌍𒐗 𒐏𒐘</span><span class="gloss">33 × 60 + 44</span></div>
    <div class="ling-ex-line"><span class="num">3601</span><span class="word">𒐕&nbsp;&nbsp;&nbsp;&nbsp;𒐕</span><span class="gloss">1 × 3600 + 0 × 60 + 1 — the gap is the empty place</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The notation needs only fifty-nine digit shapes, all built from two signs, to write any
    number at all. Compare Roman numerals on this site, which need a new letter for each
    larger unit and eventually run out of them: here the place does the work a new letter
    would.</p>
    <p>The cost is visible in the last two examples. 61 and 3601 differ only in the width of a
    gap, and 60 cannot be told apart from 1. A system with place value but no zero leaves the
    reader to resolve these from context.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — NO ZERO, NO POINT
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">No Zero, No Point</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Where Does the Number Sit?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Floating point</div>
    <p><span class="bab-cun">𒐕</span> is one. It is also sixty, three thousand six hundred,
    and one-sixtieth. Nothing on the tablet says which.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Empty places</div>
        <p>Old Babylonian scribes left a space where a place was empty, and sometimes not even
        that. From around 300 BCE, scribes wrote a placeholder instead — two slanting wedges,
        <span class="bab-cun">𒑲</span>, borrowed from punctuation. It appears only between two
        digits, never at the end of a number, so it never became a true zero: 1 and 60 still
        looked exactly alike.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">The missing point</div>
        <p>No mark separates the whole number from the fraction. <em>1;24,51,10</em> and
        <em>1,24,51,10</em> are written with identical signs. The semicolon is a modern editor's
        addition; a scribe would have known from the problem whether the number was about
        1.4 or about 305,000.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Knuth (1972) compares this to floating-point arithmetic in a computer: the scribe
    carries the significant digits and keeps track of the scale separately. For calculation
    this was an advantage, not a flaw — multiplying by 30 and multiplying by 0;30 (one half)
    are the same operation, so a single multiplication table serves both.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — RECIPROCALS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Fractions &amp; Reciprocals</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Division as Multiplication</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Rule</span>
    <span class="ling-formula-rule">a ÷ b = a × <em>(1/b)</em> — with 1/b read from a table of reciprocals</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Babylonian scribes did not divide directly. They multiplied by the reciprocal, which
    they looked up in a standard table that every student copied. The table lists only
    <strong>regular numbers</strong> — those with no prime factors other than 2, 3 and 5 —
    from 2 up to 1,21 (81), because only these have reciprocals that end. Reciprocals are
    written in the floating style: 30 for 2 means 0;30, one half.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Divisor":                  ["2", "3", "4", "5", "6", "8", "9", "10", "16", "45", "64", "81"],
    "Divisor (base 60)":        ["2", "3", "4", "5", "6", "8", "9", "10", "16", "45", "1,4", "1,21"],
    "Reciprocal (base 60)":     ["30", "20", "15", "12", "10", "7,30", "6,40", "6", "3,45",
                                 "1,20", "56,15", "44,26,40"],
    "Reciprocal (decimal)":     ["0.5", "0.333…", "0.25", "0.2", "0.1666…", "0.125",
                                 "0.111…", "0.1", "0.0625", "0.0222…", "0.015625",
                                 "0.012345…"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Why sixty helps</div>
        <p>Sixty is divisible by 2, 3, 4, 5, 6, 10, 12, 15, 20 and 30. Thirds, sixths and
        twelfths, which never end in decimal, end after one place in base 60: one third is
        simply <em>0;20</em>. Whether that is <em>why</em> sixty was chosen is a hypothesis;
        no text records the reason.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Where it fails</div>
        <p>Seven, eleven and thirteen divide neither 10 nor 60, so their reciprocals never end in
        either base: one seventh is <em>0;8,34,17,8,34,17…</em> for ever. They are simply absent
        from the standard table. Try 1/7 in the converter.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — TABLETS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">The Tablets</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Mathematics in the Clay</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">YBC 7289 — the square root of two</div>
        <p>A small, round tablet in the Yale Babylonian Collection, c. 1800–1600 BCE, probably a
        student's rough work. It shows a square with its diagonals. One side is labelled 30;
        along the diagonal are <em>1;24,51,10</em> and <em>42;25,35</em>.</p>
        <p>The first is √2 to within less than one part in two million — about 1.41421296. The
        second is 30 times the first: the length of the diagonal for a side of 30 (Fowler &amp;
        Robson 1998).</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Plimpton 322 — a table of triples</div>
        <p>A broken tablet at Columbia University, c. 1800 BCE, with fifteen rows of numbers.
        Row 1 gives <em>1,59</em> and <em>2,49</em> — 119 and 169 — and with 120 these form a
        right triangle: 119² + 120² = 169².</p>
        <p>The arithmetic is agreed; the purpose is not. Robson (2001) argues against reading
        it as a trigonometric table and for a construction from reciprocal pairs, the same
        tables described above.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — LANGUAGE AND NOTATION
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Language &amp; Notation</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Two Spoken Systems Behind One Written One</div>', unsafe_allow_html=True)

st.table({
    "Quantity": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "20", "30", "40", "50", "60", "600", "3,600"],
    "Sumerian": ["diš, aš", "min", "eš", "limmu", "ia", "aš", "imin", "ussu", "ilimmu", "u",
                 "niš", "ušu", "nimin", "ninnu", "giš, geš", "gešu", "šar"],
    "Akkadian": ["išten", "šina", "šalaš", "erbe", "hamiš", "šediš", "sebe", "samane", "tiše",
                 "ešer", "ešra", "šalaša", "erba", "hamša", "šuši", "nerum", "šarum"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Sumerian counts like the notation</div>
        <p>Sumerian's counting units run 1, 10, 60, 600, 3,600 — <em>diš</em>, <em>u</em>,
        <em>geš</em>, <em>gešu</em>, <em>šar</em> — multiplying alternately by ten and by six.
        That is exactly the structure of the written system: corner wedges count tens inside
        each sixty-place.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Akkadian counts in tens</div>
        <p>Akkadian, a Semitic language, is decimal, with words for 100 (<em>me'at</em>) and
        1,000 (<em>limum</em>). Yet it also has <em>šuši</em>, <em>nerum</em> and
        <em>šarum</em> for 60, 600 and 3,600. A Babylonian scribe could say a number in a
        decimal language and write it in a sexagesimal script.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Forms follow Melville (2003), who cautions that the pronunciation of some numerals is
    still debated, that both languages varied by region and period, and that number words
    changed form with grammatical context. Those inflected forms are omitted here. Numbers in
    economic and school texts were rarely written out as words at all.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — LEGACY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Legacy</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Sixty Survives</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Greek astronomers adopted Babylonian sexagesimal fractions for calculation; Ptolemy's
    <em>Almagest</em> in the second century CE works in them throughout (Neugebauer 1957).
    Through that tradition, sixty still divides the hour into minutes and seconds, and the
    degree of a circle into minutes and seconds of arc. Writing a time as 1:24:51 is,
    structurally, writing <em>1,24,51</em>.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 9 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature":   ["Place-value notation, whole numbers and fractions",
                  "Empty places",
                  "Sexagesimal point",
                  "Sign shapes",
                  "Metrological number systems"],
    "Status":    ["Implemented", "Implemented, both conventions", "Not written",
                  "Standardised", "Not implemented"],
    "Basis":     ["The notation of Old Babylonian mathematical texts",
                  "A gap (Old Babylonian) or the placeholder between digits (c. 300 BCE onward)",
                  "Shown only in the transliteration, as on the tablets",
                  "Unicode forms set in Noto Sans Cuneiform; real tablets vary by scribe",
                  "Administrative texts also used separate counting systems for particular "
                  "commodities and measures, with their own signs"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 10 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Neugebauer, Otto.</strong> 1957. <em>The Exact Sciences in Antiquity</em>, 2nd ed.
    Providence: Brown University Press. The transliteration convention used here, and the
    transmission of sexagesimal fractions into Greek astronomy.</p>
    <p><strong>Robson, Eleanor.</strong> 2008. <em>Mathematics in Ancient Iraq: A Social
    History</em>. Princeton University Press. The development of the place-value system and the
    scribal school curriculum.</p>
    <p><strong>Robson, Eleanor.</strong> 2001. "Neither Sherlock Holmes nor Babylon: A
    Reassessment of Plimpton 322." <em>Historia Mathematica</em> 28: 167–206.</p>
    <p><strong>Fowler, David &amp; Eleanor Robson.</strong> 1998. "Square Root Approximations in
    Old Babylonian Mathematics: YBC 7289 in Context." <em>Historia Mathematica</em> 25(4):
    366–378.</p>
    <p><strong>Chrisomalis, Stephen.</strong> 2010. <em>Numerical Notation: A Comparative
    History</em>. Cambridge University Press, 247–248.</p>
    <p><strong>Boyer, Carl B.</strong> 1944. "Zero: The Symbol, the Concept, the Number."
    <em>National Mathematics Magazine</em> 18(8): 323–330. On the placeholder and why it was
    not yet a zero.</p>
    <p><strong>Knuth, Donald E.</strong> 1972. "Ancient Babylonian Algorithms."
    <em>Communications of the ACM</em> 15(7): 671–677.</p>
    <p><strong>Melville, Duncan J.</strong> 2003. "Sumerian and Akkadian Numerals."
    <em>Mesopotamian Mathematics</em>, St. Lawrence University. The Sumerian and Akkadian number words above.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> Popular accounts often explain base 60 by a
    finger-counting method — the thumb counting the twelve finger joints of one hand, five
    times over — or state as fact that sixty was chosen for its many divisors. Neither is
    recorded in any ancient text, and both are omitted as explanations here.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Babylonian", "linguistics")
