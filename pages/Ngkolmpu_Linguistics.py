import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Ngkolmpu Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)

language_nav("Ngkolmpu", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Ngkolmpu Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Senary (Base 6)</span>
        <span class="ling-tag">Powers of Six</span>
        <span class="ling-tag">Yam Counting</span>
        <span class="ling-tag">Two Values for One Word</span>
        <span class="ling-tag">Southern New Guinea</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 1 — OVERVIEW
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">System Overview</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Structural Properties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Ngkolmpu counts in sixes, and it has a single word for every power of six up to the
    fifth: <em>ptae</em> 36, <em>tarumpao</em> 216, <em>ntamnao</em> 1,296 and
    <em>ulamaeke</em> 7,776. The system belongs to the counting of yams, which have to be stored
    in exact numbers from one year to the next.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val"><strong>6</strong> — <em>traowo</em></span>
        <span class="ling-prop-key">Powers of six</span>
        <span class="ling-prop-val">6² to 6⁵, each a single word</span>
        <span class="ling-prop-key">Seven to thirty-five</span>
        <span class="ling-prop-val">[sixes] <em>traowo</em> [ones]: <em>yempoka traowo naempr</em>, 'two six and one', is 13</span>
        <span class="ling-prop-key">Older system</span>
        <span class="ling-prop-val">In 1996 the power words could also mean 6, 12, 18 and 24</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No word recorded</span>
        <span class="ling-prop-key">Speakers</span>
        <span class="ling-prop-val">About 150 adults (Carroll 2016)</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Ngkolmpu, also called Kanum in older work, is spoken in Wasur National Park, east of
    Merauke in the Indonesian province of Papua, near the border with Papua New Guinea. Matthew
    Carroll's grammar (2016) describes the Ngkontar variety, spoken by around 150 adults in the
    village of Yanggandur; the other variety, Baedi, is reportedly spoken only by a handful of
    elderly people who no longer use it day to day.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — ONE TO SIX
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Six</div>', unsafe_allow_html=True)

st.table({
    "Number": ["1", "2", "3", "4", "5", "6"],
    "Ngkolmpu": ["naempr", "yempoka", "yuow", "eser", "tampui", "traowo"],
    "Donohue, simple": ["naempr", "yempoka", "ywow", "eser", "swabra", "swy"],
    "Donohue, moderate": ["aempy", "ynaoaempy", "ylla", "eser", "tampwy", "traowao"],
    "Donohue, complex": ["aempy", "ynaoaempy", "ylla", "eser", "tamp", "ptae"],
})

st.markdown("""
<div class="ling-info">
    <p>The first column is Carroll's (2016, Table 1.3). Mark Donohue, working in the same village
    in 1996, recorded three series (Donohue 2008, reproduced by Carroll in his own Table 1.2 and in
    Donohue's spelling). Carroll found that the words speakers confirmed match Donohue's simple
    series for one to four and his moderate series for five and six.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — SIXES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Counting in Sixes</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[number of sixes] <em>traowo</em> [ones]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples (Carroll 2018, 2019)</div>
    <div class="ling-ex-line"><span class="num">7</span><span class="word">naempr traowo naempr</span><span class="gloss">one six and one</span></div>
    <div class="ling-ex-line"><span class="num">8</span><span class="word">naempr traowo yempoka</span><span class="gloss">one six and two</span></div>
    <div class="ling-ex-line"><span class="num">13</span><span class="word">yempoka traowo naempr</span><span class="gloss">two six and one</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Carroll gives these three and presents the rest as following the same pattern, which the
    converter applies up to 35, <em>tampui traowo tampui</em>, 'five six and five'. The next
    number, six sixes, is <em>ptae</em>. In base-six notation the pattern is plain: 13 is
    21<sub>6</sub>, two sixes and one.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — POWERS OF SIX
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Powers of Six</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Words Shared Across a Region</div>', unsafe_allow_html=True)

st.table({
    "Value": ["36", "216", "1,296", "7,776"],
    "Power": ["6²", "6³", "6⁴", "6⁵"],
    "Ngkolmpu": ["ptae", "tarumpao", "ntamnao", "ulamaeke"],
    "Nen": ["prta", "taromba", "damno", "wèrèmaka"],
    "Arammba": ["feté", "tarumba", "ndamno", "wermeke"],
    "Agöb (Buzi)": ["purta", "tarumba", "damuno", "waramakai"],
})

st.markdown("""
<div class="ling-info">
    <p>Ngkolmpu from Carroll (2016); the other columns from Evans (2009, Table 3), who notes that
    all these power words are formally related, though the sound correspondences that would show
    inheritance or borrowing are not yet worked out. Agöb belongs to a different family, which
    suggests the system has spread between neighbours. Keraakie goes up to 6⁷, and Carroll notes
    that the related language Komnzo has <em>wi</em> for 6⁶, 46,656.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — TWO VALUES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">The Older System</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Two Values for One Word</div>', unsafe_allow_html=True)

st.table({
    "Word (Donohue)": ["ptae", "tarwmpao", "ntamnao", "wramaekr"],
    "As a power": ["36", "216", "1,296", "7,776"],
    "As a step": ["6", "12", "18", "24"],
    "Example": ["ylla ptae, 3 + 6 = 9", "ylla tarwmpao, 3 + 12 = 15",
                "aempy ntamnao, 1 + 18 = 19", "aempy wramaekr, 1 + 24 = 25"],
})

st.markdown("""
<div class="ling-card">
    <p>In Donohue's 1996 data each power word had a second, smaller value. Evans (2009) points
    out the system behind it: a word that is the <em>n</em>th power of six is also the
    <em>n</em>th count through a cycle of six, so <em>ptae</em>, the second power, also marks
    the second round, from 7 to 11. Past 29 the data turn additive: 30 is <em>ptae wramaekr</em>,
    6 + 24, and 31 is <em>aempy ptae wramaekr</em>. The converter shows these older forms
    beside Carroll's.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Carroll's speakers use the power words only as powers. Older speakers who still recite
    the larger numbers mostly follow Donohue's complex series, but without <em>ntamnao</em> for 18
    or <em>wramaekr</em> for 24. Evans's table gives "+ 18" for <em>wramaekr</em> where his
    example, 25, shows + 24; the converter follows the example.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — YAMS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Culture &amp; History</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Counting Yams</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Why Six?</div>
        <p>Evans (2009) agrees with Hammarström (2009) that the system grew from yam growing,
        which requires storing exact numbers of yams from one year to the next. The one
        Morehead-Maro language without power-of-six words, Yei, is spoken in wetter country
        where sago, not yams, is the staple.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Counting Today</div>
        <p>Carroll observed that yam counts now mix languages: speakers count the first batch
        of 36 in Ngkolmpu and then continue in Indonesian, and most people know only the first
        six numbers. In a gardening story he recorded, a speaker counts up to "216, which is
        what we count to".</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — IN A SENTENCE
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Numbers in a Sentence</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Carroll classes numerals as nominals: they can head a noun phrase and take case endings
    like nouns. In a phrase the numeral comes before the noun — <em>naempr konsopor</em> 'one
    day' — and fills the same slot as the language's only quantifier, <em>yimpurmpurt</em>
    'all', so the two never occur together.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature": ["1 to 6", "7 to 35", "36, 216, 1,296, 7,776", "Other numbers to 7,776",
                "Donohue's older series", "0, and above 7,776"],
    "Status": ["Implemented", "Implemented", "Implemented", "Not implemented",
               "Shown and accepted", "Not implemented"],
    "Basis": ["Carroll (2016)", "Carroll's pattern; 7, 8 and 13 recorded",
              "Carroll (2016)", "No source shows how they are built",
              "1 to 35 and the powers, as Carroll (2016) and Evans (2009) give them",
              "No word recorded"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 9 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Carroll, Matthew J.</strong> 2016. <em>The Ngkolmpu Language with Special Reference
    to Distributed Exponence</em>. PhD thesis, Australian National University. §1.1 on the
    speakers, §1.4 and Tables 1.2–1.3 on the numerals, §4.1.3 on numerals in the noun phrase,
    text A.3.54.</p>
    <p><strong>Carroll, Matthew.</strong> 2018. "How to count to 1296 in Ngkolmpu". Surrey
    Morphology Group blog, 20 June 2018; and his 2019 entry in Eugene S. L. Chan,
    <em>Numeral Systems of the World's Languages</em>. The forms for 7, 8 and 13.</p>
    <p><strong>Evans, Nicholas.</strong> 2009. "Two pus one makes thirteen: Senary numerals in the
    Morehead-Maro region." <em>Linguistic Typology</em> 13: 321–335. Tables 3 and 4 and note 11.</p>
    <p><strong>Donohue, Mark.</strong> 2008. "Complexities with restricted numeral systems."
    <em>Linguistic Typology</em> 12: 423–429. Cited through Carroll (2016) and Evans (2009); not
    consulted directly.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> Chan's database gives about 100 speakers in
    three villages, against Carroll's 150 adults in one; the page follows the grammar. No source
    consulted shows how numbers between the powers of six, such as 37 or 100, were said, so the
    converter does not build them, although a regular pattern is easy to imagine.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Ngkolmpu", "linguistics")
