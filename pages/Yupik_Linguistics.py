import streamlit as st
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Yup'ik Numerals — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)

language_nav("Yupik", "linguistics")

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Yup'ik Numerals</div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal</span>
        <span class="ling-tag">Steps at 10 and 15</span>
        <span class="ling-tag">"Not Quite" Numbers</span>
        <span class="ling-tag">Dual and Plural</span>
        <span class="ling-tag">Eskimo–Aleut</span>
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
    <p>Central Alaskan Yup'ik counts in twenties. The word for twenty, <em>yuinaq</em>, is built
    on <em>yuk</em> 'person', and three numbers are named by what they fall short of:
    9 is <em>qulngunritaraan</em>, literally 'not quite ten', and 14 and 19 are built the same
    way on the words for fifteen and twenty.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Base</span>
        <span class="ling-prop-val"><strong>20</strong> — <em>yuinaq</em></span>
        <span class="ling-prop-key">Steps inside a twenty</span>
        <span class="ling-prop-val">5, 10 and 15 — <em>talliman</em>, <em>qula</em>, <em>akimiaq</em></span>
        <span class="ling-prop-key">"Not quite" numbers</span>
        <span class="ling-prop-val">9, 14 and 19</span>
        <span class="ling-prop-key">Multiples of twenty</span>
        <span class="ling-prop-val"><em>yuinaak</em> (dual) for 40, <em>yuinaat</em> (plural) from 60, or <em>ipiaq</em> 'unit of twenty'</span>
        <span class="ling-prop-key">Zero</span>
        <span class="ling-prop-val">No word recorded</span>
        <span class="ling-prop-key">Above 400</span>
        <span class="ling-prop-val">Scattered forms only; 1,000 is <em>tiissitsaaq</em>, from Russian</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Central Alaskan Yup'ik belongs to the Yupik branch of the Eskimo–Aleut family and is
    spoken in southwestern Alaska. The forms on this page follow Steven Jacobson's
    <em>Yup'ik Eskimo Dictionary</em> (2nd ed., 2012), which covers all its dialects and
    records where they differ — 8, for example, is <em>inglulgen</em> around Bristol Bay,
    the Nushagak River, Lake Iliamna and Egegik.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — ONE TO TWENTY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Twenty</div>', unsafe_allow_html=True)

st.table({
    "Number": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
    "Yup'ik": ["atauciq", "malruk", "pingayun", "cetaman", "talliman",
               "arvinlegen", "malrunlegen", "pingayunlegen", "qulngunritaraan", "qula",
               "qula atauciq", "qula malruk", "qula pingayun", "akimiarunritaraan", "akimiaq",
               "akimiaq atauciq", "akimiaq malruk", "akimiaq pingayun", "yuinaunritaraan", "yuinaq"],
    "Literally": ["one", "two", "three", "four", "five",
                  "'crossing over' to the other hand", "seven", "eight", "not quite ten", "ten",
                  "ten + one", "ten + two", "ten + three", "not quite fifteen", "fifteen",
                  "fifteen + one", "fifteen + two", "fifteen + three", "not quite twenty", "twenty"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Six: Crossing Over</div>
        <p>Jacobson traces <em>arvinlegen</em> to the verb <em>arvir-</em> 'to cross over',
        from crossing from one hand to the other when counting on the fingers. Seven and
        eight, <em>malrunlegen</em> and <em>pingayunlegen</em>, carry the same ending on the
        words for two and three.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Nine, Fourteen, Nineteen</div>
        <p>Jacobson glosses <em>qulngunritaraan</em> as 'not quite ten'. He derives
        <em>akimiarunritaraan</em> (14) and <em>yuinaunritaraan</em> (19) the same way from
        <em>akimiaq</em> (15) and <em>yuinaq</em> (20), so each names the step it falls just
        short of.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Counting Aloud and Counting Things</div>
    <p>Each "not quite" number has a shorter form used when reciting:
    <em>pingayunlegen, qulngunrita'ar, qula</em> 'eight, nine, ten', but
    <em>qulngunritaraan yuut taillruut</em> 'nine people came'. Likewise <em>akimiaq</em>
    is the counting form of fifteen, while a phrase uses the plural: <em>akimiaret yuut
    taillruut</em> 'fifteen people came' (Jacobson 2012).</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A second way of counting the teens.</strong> Two lists in Chan's
    <em>Numeral Systems of the World's Languages</em> — one by Carl Rubino and Kanaqluk George
    Charles (1999), and one by Lawrence Kaplan (2007), taken from Jacobson's 1995 grammar —
    build every number from 11 to 19 on ten: <em>qula cetaman</em> 14, <em>qula talliman</em> 15,
    on to <em>qula</em> + the word for nine for 19. The converter follows the 2012 dictionary
    and lists the ten-based forms as alternatives.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — TWENTIES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Compositional Rules</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Counting by Twenties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[twenties] + [remainder, 1–19]</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Jacobson derives <em>yuinaq</em> from <em>yuk</em> 'person' and the suffix
    <em>-nginaq</em> 'merely, nothing more'. From 21 to 39 the remainder follows
    <em>yuinaq</em>, but inside a larger number his table uses other forms for 9, 14 and 19:
    the reciting form <em>qulngunrita'ar</em>, <em>qula cetaman</em> 'ten four' and
    <em>akimiaq cetaman</em> 'fifteen four'.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples (Jacobson 2012, Appendix 6)</div>
    <div class="ling-ex-line"><span class="num">29</span><span class="word">yuinaq qulngunrita'ar</span><span class="gloss">20 + 9</span></div>
    <div class="ling-ex-line"><span class="num">34</span><span class="word">yuinaq qula cetaman</span><span class="gloss">20 + 10 + 4</span></div>
    <div class="ling-ex-line"><span class="num">37</span><span class="word">yuinaq akimiaq malruk</span><span class="gloss">20 + 15 + 2</span></div>
    <div class="ling-ex-line"><span class="num">39</span><span class="word">yuinaq akimiaq cetaman</span><span class="gloss">20 + 15 + 4</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">Two Twenties, Three Twenties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Number words carry grammatical number themselves: Jacobson describes <em>malruk</em>
    'two' as a dual, and <em>cetaman</em> 'four', <em>arvinlegen</em> 'six' and
    <em>malrunlegen</em> 'seven' as plurals with a special ending <em>-n</em> used for
    numbers. Multiples of twenty agree:
    <em>yuinaak malruk</em> 'two twenties' takes the dual of <em>yuinaq</em>, and
    <em>yuinaat pingayun</em> 'three twenties' the plural. A second pattern uses
    <em>ipiaq</em> 'unit of twenty', which stays singular however many twenties there are:
    <em>malruk ipiaq</em> 40, <em>cetaman ipiaq pingayunlegen</em> 88.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Examples</div>
    <div class="ling-ex-line"><span class="num">40</span><span class="word">yuinaak malruk</span><span class="gloss">2 × 20</span></div>
    <div class="ling-ex-line"><span class="num">41</span><span class="word">yuinaak malruk atauciq</span><span class="gloss">2 × 20 + 1</span></div>
    <div class="ling-ex-line"><span class="num">60</span><span class="word">yuinaat pingayun</span><span class="gloss">3 × 20</span></div>
    <div class="ling-ex-line"><span class="num">88</span><span class="word">cetaman ipiaq pingayunlegen</span><span class="gloss">4 × 20 + 8</span></div>
    <div class="ling-ex-line"><span class="num">100</span><span class="word">yuinaat talliman</span><span class="gloss">5 × 20</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>Where the sources differ.</strong> Jacobson's numeral table prints 60 as
    <em>yuinaak pingayun</em>, with the dual. Kaplan's list has <em>yuinaat pingayun</em>, and
    so does an example sentence in Jacobson's own entry for <em>yuinaq</em>: <em>Yuinaat
    pingayun arvinlegnek cipluku allrakunglua maa-i</em> 'I'm sixty-six years old now'. The converter
    uses the plural and lists the dual as an alternative.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title" style="margin-top:1.75rem">"With Some Left Over"</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>A number can also be phrased with <em>cipluku</em> 'having some left over', the
    remainder taking the ablative-modalis case: <em>qula ataucimek cipluku</em> 'eleven',
    literally 'ten with one left over', and <em>yuinaat cetaman arvinlegnek cipluku</em>
    'eighty-six', 'four twenties with six left over'. Jacobson quotes a 1998 text that uses
    it for a census of the language: in 1982 thirteen thousand people spoke Yup'ik
    — <em>tiissicaat qula pingayunek cipluku</em>, 'thousands, ten with three left over'.
    The converter gives only the plain forms.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — HUNDREDS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Larger Numbers</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One Hundred and Beyond</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">One Hundred</div>
        <p>Besides <em>yuinaat talliman</em> 'five twenties', Jacobson records two words of
        uncertain origin. <em>Kavluun</em> (Lower Yukon, Nunivak) is said to have named
        percussion caps, which came in packages of a hundred. <em>Negavaq</em> (Bristol Bay,
        Nushagak River) also means a twenty-dollar bill, because the basic money unit there is
        twenty cents, and a hundred of them make twenty dollars.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Four Hundred</div>
        <p>Twenty twenties is <em>yuinaam yuum ipia</em>, recorded by E. W. Nelson (1899) and
        Francis Barnum (1901) and also found in Naukan Yupik in Siberia. A text Jacobson
        quotes says <em>yuinaat yuinaat</em>, 'twenty twenties'. For 1,000 he gives
        <em>tiissitsaaq</em>, a Russian loan.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>Why the converter stops at 199.</strong> From ten twenties up, the multiplier is
    itself a phrase, and no source shows how the two parts are kept apart:
    <em>yuinaat qula atauciq</em> could mean 10 × 20 + 1 = 201 or 11 × 20 = 220. Rather than
    guess, the converter gives 1 to 199 and the recorded 400.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — MORPHOLOGY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax &amp; Morphology</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Numbers in a Sentence</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-subsection-title">Case</div>
    <p>Numerals take case endings like nouns. With 'have' and with ages they appear in the
    ablative-modalis: <em>malrugnek irniangqertua</em> 'I have two children',
    <em>tallimanek allrakungqertua</em> 'I'm five years old' (Jacobson 2012).</p>
</div>
""", unsafe_allow_html=True)

st.table({
    "": ["1", "2", "3", "4", "5", "10"],
    "Their nth (of them)": ["atauciat / ciugliat", "malruat / aipaat", "pingayuat",
                            "cetamiit", "tallimiit", "quliit"],
    "The nth one": ["ciuqliq", "tungliq / kinguqliq", "pingayuqliq",
                    "cetamaqliq", "tallimaqliq", "quleqliq"],
    "n times": ["ataucirqumek", "malrurqugnek", "pingayurqunek",
                "cetamarqunek", "tallimarqunek", "qulerqunek"],
})

st.markdown("""
<div class="ling-info">
    <p>Ordinals and repetition numerals from Jacobson's Appendix 6. The first column is
    possessed — <em>Angutet pingayuat taillruuq</em> 'The third man came over' — and the
    second stands alone: <em>Pingayuqliq taillruuq</em> 'The third one came over'.
    The third column is built with <em>-rqu-</em>: <em>Malrurqugnek taillruuq</em>
    'He came twice'.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — WRITING AND ZERO
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Writing &amp; Special Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Script &amp; Zero</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card">
        <div class="ling-subsection-title">Writing System</div>
        <p>Yup'ik is written in the Latin alphabet; this page uses the standard spelling of
        Jacobson's dictionary.</p>
    </div>
    <div class="ling-card">
        <div class="ling-subsection-title">Zero</div>
        <p>Jacobson's dictionary has no word for zero, so the converter gives none.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature": ["1 to 199", "400", "0", "200 to 399, and above 400",
                "Alternative forms", "The cipluku construction", "Case endings"],
    "Status": ["Implemented", "Implemented", "Not implemented", "Not implemented",
               "Shown and accepted", "Not implemented", "Not implemented"],
    "Basis": ["Jacobson's table to 41, 50, 60 and 100, with multiples of twenty from his examples",
              "yuinaam yuum ipia, recorded since 1899",
              "No word recorded",
              "Two-word multipliers would be ambiguous; only scattered forms recorded",
              "Ten-based teens, ipiaq, yuinaak pingayun, dialect words, spelling variants",
              "Described above",
              "Numerals are given in their plain form"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 8 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Jacobson, Steven A.</strong> 2012. <em>Yup'ik Eskimo Dictionary</em>, 2nd ed.
    2 vols. Fairbanks: Alaska Native Language Center. Appendix 6, "Numerals", pp. 976–977, and
    the entries <em>akimiaq</em>, <em>akimiarunritar(aq)</em>, <em>arvinlegen</em>,
    <em>cetaman</em>, <em>cipluku</em>, <em>inglulgen</em>, <em>ipiaq</em>, <em>kavluun</em>,
    <em>malruk</em>, <em>malrunlegen</em>, <em>negavaq</em>, <em>qulngunritara(aq)</em>,
    <em>tiissitsaaq</em>, <em>yuinaq</em> and <em>yuinaunritaraan</em>.</p>
    <p><strong>Chan, Eugene S. L.</strong> <em>Numeral Systems of the World's Languages</em>:
    Central Yupik. Max Planck Institute for Evolutionary Anthropology. Two lists: Carl Rubino
    and Kanaqluk George Charles (1999), and Lawrence Kaplan (2007), "taken from Jacobson
    (1995)".</p>
    <p><strong>Jacobson, Steven A.</strong> 1995. <em>A Practical Grammar of the Central
    Alaskan Yup'ik Eskimo Language</em>. Fairbanks: Alaska Native Language Center. Cited
    through Kaplan's list; not consulted directly.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> An earlier version of this page and its
    converter gave <em>imkuk</em> for zero; in Jacobson's examples it is a demonstrative,
    'those two', so it was removed. It also described 9 as five plus four and 13 as ten plus
    five plus three; both were wrong. The popular explanation of <em>yuinaq</em> as one
    person's fingers and toes is not given by Jacobson, who records only the derivation from
    <em>yuk</em>, so it is left out. Miyaoka's <em>A Grammar of Central Alaskan Yupik</em>
    (2012) was cited by the earlier version but was not consulted for this one.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Yupik", "linguistics")
