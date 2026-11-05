import streamlit as st

from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Maya Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Maya", "linguistics")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Mayan+Numerals&display=swap');
.ling-ex-line .num { min-width: 6.6rem; }
.ling-ex-line .word { font-family: 'DM Mono', 'Noto Sans Mayan Numerals', 'Courier New', monospace; font-size: 1.6rem; letter-spacing: .15em; }
.maya-glyph { font-family: 'Noto Sans Mayan Numerals', sans-serif; }
.maya-signs { display: grid; grid-template-columns: repeat(auto-fill, minmax(4.4rem, 1fr)); gap: .5rem; margin: .2rem 0 .3rem 0; }
.maya-sign { background: var(--parchment-2); border: 1px solid var(--rule); border-radius: 4px; padding: .55rem .3rem .4rem; text-align: center; }
.maya-sign-glyph { font-family: 'Noto Sans Mayan Numerals', sans-serif; font-size: 1.9rem; color: var(--ink); line-height: 1.2; min-height: 2.4rem; }
.maya-sign-num { font-family: 'DM Mono', 'Courier New', monospace; font-size: .8rem; color: var(--accent); }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Maya Numerals</div>
    <div class="ling-masthead-sub">
        The bar-and-dot numerals of the Classic Maya and the Long Count — a place-value count
        of days with a zero, in base twenty except for one place, which counts eighteen.
    </div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Positional</span>
        <span class="ling-tag">Quinary Sub-base</span>
        <span class="ling-tag">Zero</span>
        <span class="ling-tag">Calendrical</span>
        <span class="ling-tag">Classic Mayan &amp; Yucatec</span>
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
    <p>Maya scribes wrote every digit from 0 to 19 with three signs — a dot, a bar and a sign
    for zero — and stacked the digits in places, highest at the top. Every place-value number
    that survives counts days, and in that count the third place is worth 360, not 400.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20 (vigesimal)</strong>, positional in the count of days</span>
        <span class="ling-prop-key">Sub-base</span>
        <span class="ling-prop-val">5, inside each digit — bars of five and dots of one</span>
        <span class="ling-prop-key">Signs</span>
        <span class="ling-prop-val">Three: the dot (1), the bar (5) and a sign for zero</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">Yes — a shell and several other signs, in any place including the last</span>
        <span class="ling-prop-key">Place values</span>
        <span class="ling-prop-val">1, 20, 360, 7,200 and 144,000 days</span>
        <span class="ling-prop-key">Main period</span>
        <span class="ling-prop-val">Classic, late 3rd to 9th century CE</span>
        <span class="ling-prop-key">Earliest Maya dates</span>
        <span class="ling-prop-val">Tikal Stela 29, 292 CE, and the Leiden Plaque, 320 CE. Earlier Long Counts, from 36 BCE, come from outside the Maya tradition</span>
        <span class="ling-prop-key">Writers</span>
        <span class="ling-prop-val">Scribes writing Classic Mayan; number words survive in Yucatec</span>
        <span class="ling-prop-key">Medium</span>
        <span class="ling-prop-val">Carved stone, painted pottery and bark-paper books</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>"Maya numerals" here means the written notation of Classic Maya inscriptions and of
    the four surviving books, the codices, which were painted later, after 1000 CE. The spoken counterpart is shown below from two
    sources: the Classic Mayan words read from the glyphs, and the Yucatec words written down
    after the Spanish conquest.</p>
    <p>Long Counts are transcribed in the modern literature with dots between places, highest
    place first — <em>9.12.11.5.18</em>. That convention is a modern editor's. The
    inscriptions write each digit beside a sign naming its period; the codices often stack
    the digits alone, in columns, so that position gives the value.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — DIGITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Three Signs, Twenty Digits</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[bars, 0–3 × <em>5</em>] + [dots, 0–4 × <em>1</em>] = one digit, 1–19 — and a separate sign for 0</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="maya-signs">
        <div class="maya-sign"><div class="maya-sign-glyph">𝋠</div><div class="maya-sign-num">0</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋡</div><div class="maya-sign-num">1</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋢</div><div class="maya-sign-num">2</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋣</div><div class="maya-sign-num">3</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋤</div><div class="maya-sign-num">4</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋥</div><div class="maya-sign-num">5</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋦</div><div class="maya-sign-num">6</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋧</div><div class="maya-sign-num">7</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋨</div><div class="maya-sign-num">8</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋩</div><div class="maya-sign-num">9</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋪</div><div class="maya-sign-num">10</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋫</div><div class="maya-sign-num">11</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋬</div><div class="maya-sign-num">12</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋭</div><div class="maya-sign-num">13</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋮</div><div class="maya-sign-num">14</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋯</div><div class="maya-sign-num">15</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋰</div><div class="maya-sign-num">16</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋱</div><div class="maya-sign-num">17</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋲</div><div class="maya-sign-num">18</div></div>
        <div class="maya-sign"><div class="maya-sign-glyph">𝋳</div><div class="maya-sign-num">19</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Dots stand above bars</div>
    <div class="ling-ex-line"><span class="num">7</span><span class="word">𝋧</span><span class="gloss">two dots over one bar — 2 + 5</span></div>
    <div class="ling-ex-line"><span class="num">13</span><span class="word">𝋭</span><span class="gloss">three dots over two bars — 3 + 10</span></div>
    <div class="ling-ex-line"><span class="num">19</span><span class="word">𝋳</span><span class="gloss">the largest digit — four dots over three bars</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>The written digits are quinary inside a vigesimal system: they group by fives, while
    the spoken words for 13 to 19 group by tens (Lounsbury 1978). The forms shown are the
    standardised Unicode shapes of the codices. On monuments the bars often stand upright with
    the dots to their left, and a scribe could replace any digit with a portrait head — each
    number had its own (Kettunen &amp; Helmke 2025). Zero, too, had several signs besides the
    shell.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — PLACE VALUE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Place Value</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The Long Count</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Days</span>
    <span class="ling-formula-rule">d₄ × <em>144,000</em> + d₃ × <em>7,200</em> + d₂ × <em>360</em> + d₁ × <em>20</em> + d₀ — d₁ from 0 to 17, every other digit from 0 to 19</span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Period":        ["bak'tun", "k'atun", "tun", "winal", "k'in"],
    "Classic Mayan": ["pik / pikhaab?", "winikhaab?", "haab", "winik", "k'in"],
    "Days":          ["144,000", "7,200", "360", "20", "1"],
    "Made of":       ["20 k'atuns", "20 tuns", "18 winals", "20 k'ins", "—"],
})

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Places read left to right here, top to bottom on the stone</div>
    <div class="ling-ex-line"><span class="num">20</span><span class="word">𝋡 𝋠</span><span class="gloss">1 winal, 0 k'in — zero holds the last place</span></div>
    <div class="ling-ex-line"><span class="num">360</span><span class="word">𝋡 𝋠 𝋠</span><span class="gloss">1 tun — eighteen winals, not twenty</span></div>
    <div class="ling-ex-line"><span class="num">145,600</span><span class="word">𝋡 𝋠 𝋤 𝋨 𝋠</span><span class="gloss">1.0.4.8.0 — 400 × 364, the top of a table in the Dresden Codex</span></div>
    <div class="ling-ex-line"><span class="num">1,386,478</span><span class="word">𝋩 𝋬 𝋫 𝋥 𝋲</span><span class="gloss">9.12.11.5.18 — the death of K'inich Janaab Pakal of Palenque, 683 CE</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The names <em>bak'tun</em> and <em>k'atun</em> are the ones most books use, but they
    come from colonial Yucatec, not from the glyphs: <em>k'atun</em> is well attested after the
    conquest, <em>bak'tun</em> is not (Lounsbury 1978). The Classic Mayan readings in the table
    follow Kettunen &amp; Helmke (2025); their question marks are kept. Higher periods,
    each twenty times the last, appear in long projections into the mythical past and
    future; their usual names — "piktun", "kalabtun" and so on — are modern compounds.</p>
    <p>Distance numbers, which count the days between two events in a text, run the other
    way: k'ins first, then winals, then tuns (Kettunen &amp; Helmke 2025).</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — EIGHTEEN, NOT TWENTY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Eighteen, Not Twenty</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">The 400 That Was Never Written</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">A common error</div>
    <p>Many textbooks give Maya place values as 1, 20, 400 and 8,000. No surviving inscription
    or book writes a number that way.</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "Place":         ["1st", "2nd", "3rd", "4th", "5th"],
    "Plain base 20": ["1", "20", "400", "8,000", "160,000"],
    "Long Count":    ["1", "20", "360", "7,200", "144,000"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">What the record shows</div>
        <p>Stuart (2012) points out that columns of place-value digits appear only in counts
        of days — on monuments, in the Dresden Codex and in the wall paintings of Xultun.
        Large counts of goods were written differently: tribute at Bonampak in round numbers,
        offerings in the codices with the sign for twenty plus bars and dots. Chrisomalis
        (2010) makes the same argument.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">The other view</div>
        <p>Lounsbury (1978) describes the written places as twenties, four-hundreds and
        eight-thousands, and calls the exception in the day count "only superficially" one.
        Above the tun the count is plain base 20 again — a k'atun is 20 tuns, a bak'tun 400 —
        so the eighteen can be seen as a detail of how days fit into years.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Both views accept that the spoken numbers are plainly base 20. They differ on whether
    a plain base-20 written place system existed; Stuart and Chrisomalis find no example of
    one. Kettunen &amp; Helmke (2025) explain the
    eighteen as a compromise: 360 is a multiple of twenty close to the 365-day year. The
    converter on this site implements only the attested form.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — THE CALENDAR
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Numbers &amp; Time</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Count from Creation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">The base date</div>
        <p>A Long Count gives the number of days since a mythological starting point,
        written <em>13.0.0.0.0 4 Ajaw 8 Kumk'u</em> — the completion of thirteen bak'tuns of
        an earlier era. Under the usual correlation it falls on 11 August 3114 BCE. Some texts
        count back into that era: the Temple of the Cross at Palenque opens with
        <em>12.19.13.4.0 8 Ajaw 18 Sek</em>, 2,440 days before creation (Lounsbury 1978).</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">The Calendar Round</div>
        <p>Each Long Count is followed by the day's place in two cycles: the 260-day
        Tzolk'in, 13 numbers turning against 20 day names, and the 365-day Haab, 18 months of
        20 days plus 5. A pair such as <em>6 Etz'nab 11 Yax</em> repeats every 18,980 days,
        about 52 years (Kettunen &amp; Helmke 2025). The converter computes it for every
        date.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>Correlation.</strong> Fixing the base date to a European date takes a
    correlation constant: the Julian Day Number of 13.0.0.0.0. The GMT constant, 584283,
    gives 11 August 3114 BCE and puts 13.0.0.0.0 on 21 December 2012. Kettunen &amp; Helmke
    (2025) use 584285, two days later. Radiocarbon dating of a carved wooden lintel from Tikal
    supports this family of correlations (Kennett et al. 2013), but radiocarbon cannot
    separate constants two days apart. Lounsbury (1978) called the correlation still
    uncertain. The converter offers both.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — SPOKEN NUMBERS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Language &amp; Notation</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Base Twenty in Speech</div>', unsafe_allow_html=True)

st.table({
    "Quantity": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
    "Classic Mayan": ["mih? / minan?", "jun", "cha'", "ux", "chan", "ho'", "wak", "huk",
                      "waxak", "balun?", "lajun", "buluch", "lajunchan?", "uxlajun",
                      "chanlajun", "ho'lajun", "waklajun", "huklajun", "waxaklajun",
                      "balunlajun?", "—"],
    "Colonial Yucatec": ["—", "hun", "caa, ca", "ox", "can", "hoo, ho", "uac", "uuc", "uaxac",
                         "bolon", "lahun", "buluc", "lahca", "oxlahun", "canlahun",
                         "hoolahun, hoolhun", "uaclahun", "uuclahun", "uaxaclahun",
                         "bolonlahun", "hun kal"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Powers of twenty</div>
        <p>Colonial Yucatec named each power of twenty: <em>kal</em> 20, <em>bak</em> 400,
        <em>pic</em> 8,000, <em>calab</em> 160,000, <em>kinchil</em> 3,200,000 and
        <em>alau</em> 64,000,000 (Lounsbury 1978). In Classic texts the sign <em>PIK</em>
        stands for 8,000 when counting objects (Stuart 2012) — and <em>pik</em> is also the
        Classic reading proposed for the bak'tun.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Counting into the next score</div>
        <p>Fifty-one could be <em>ca kal catac buluc</em>, "two score and eleven", or
        <em>buluc tu yox kal</em>, "eleven in the third score" (Lounsbury 1978). The second
        names the score being filled, not the ones completed. Ainu, on this site, also
        names a number by the score it falls in, but subtracts from it. Thirty is
        <em>lahun ca kal</em>, "ten [in] two score".</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Yucatec words are given in the colonial spelling Lounsbury follows, in which
    <em>c</em> is [k], <em>k</em> is the glottalised [kʼ] and <em>u</em> before a vowel is
    [w]. Question marks in the Classic column are Kettunen &amp; Helmke's: those readings are
    uncertain. The table shows citation forms; in use, Mayan numbers take a numeral
    classifier naming the kind of thing counted.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — CHANGE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Language Change</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Five</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Endangered counting</div>
    <p>Yucatec Maya is still a living language, but its own number words have nearly gone.
    Briceño Chel (1994), drawing on fieldwork from 1988 to 1990 and on earlier studies,
    reports that speakers no longer count in Maya beyond three or four, and only rarely to
    five.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Above five, speakers use Spanish numbers spoken with Maya intonation. The words
    <em>wuk</em> (7), <em>bolon</em> (9) and <em>óoxlajun</em> (13) survive in agricultural
    and other ceremonies. When speakers rebuilt larger numbers, they did so the Spanish
    way — <em>junk'aal yéetel jun</em>, "one twenty and one", a word-for-word translation
    of the Spanish. The classifiers that once marked what was being counted were
    disappearing too (Briceño Chel 1994).</p>
    <p>The language lives on; its base-twenty count is what has gone.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature":   ["Five-place Long Count, 0 to 19.19.19.17.19",
                  "European dates",
                  "Calendar Round",
                  "Plain base-20 place notation",
                  "Places above the bak'tun",
                  "Sign shapes",
                  "Spoken numbers"],
    "Status":    ["Implemented", "Implemented, two correlations", "Implemented",
                  "Not implemented", "Not implemented", "Standardised", "Not implemented"],
    "Basis":     ["The day count of Classic inscriptions and the codices",
                  "GMT 584283 and 584285; proleptic Gregorian and Julian",
                  "Tzolk'in and Haab from the base date, 4 Ajaw 8 Kumk'u; Haab days from 0",
                  "No written example survives",
                  "Found only in a few cosmological texts; their names are modern",
                  "Unicode bar-and-dot forms in Noto Sans Mayan Numerals; monuments vary, "
                  "and often use head forms",
                  "Shown in the table above; the converter works with the written notation"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 9 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Kettunen, Harri &amp; Christophe Helmke.</strong> 2025. <em>Introduction to Maya
    Hieroglyphs: Workshop Handbook</em>, 20th ed. Wayeb, European Association of Mayanists.
    Period, day and month names; the Classic Mayan numerals; the Calendar Round; distance
    numbers; the 584285 correlation.</p>
    <p><strong>Lounsbury, Floyd G.</strong> 1978. "Maya Numeration, Computation, and Calendrical
    Astronomy." In <em>Dictionary of Scientific Biography</em>, vol. 15, ed. C. C. Gillispie.
    New York: Scribner's. The Yucatec number words, the zero signs, the attestation of the
    period names, the earliest dates and the Temple of the Cross.</p>
    <p><strong>Stuart, David.</strong> 2012. "The Misunderstanding of Maya Math."
    <em>Maya Decipherment</em>, 2 May 2012. Place notation restricted to counts of days.</p>
    <p><strong>Chrisomalis, Stephen.</strong> 2010. <em>Numerical Notation: A Comparative
    History</em>. Cambridge University Press. Cited for the same argument as Stuart, as its
    author summarises it in a reply to Stuart (2012).</p>
    <p><strong>Kennett, Douglas J. et al.</strong> 2013. "Correlating the Ancient Maya and
    Modern European Calendars with High-Precision AMS <sup>14</sup>C Dating."
    <em>Scientific Reports</em> 3: 1597.</p>
    <p><strong>Briceño Chel, Fidencio.</strong> 1994. "La cuantificación actual en el maya
    yucateco." <em>Estudios de Lingüística Aplicada</em> 19/20. The loss of the vigesimal
    count in modern Yucatec.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> Popular accounts often credit either the
    Olmec or the Maya with inventing zero. The surviving record does not settle who first used
    it, so neither claim is made here. Nor does any Maya text predict that the world would end
    in 2012, when the count reached 13.0.0.0.0 again: Lounsbury (1978) found no evidence that
    the current era was expected to last thirteen bak'tuns like the one before it.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Maya", "linguistics")
