import streamlit as st

from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS, language_nav, footer_nav

st.set_page_config(page_title="Breton — Linguistics", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)
language_nav("Breton", "linguistics")

st.markdown("""
<style>
/* Charis SIL, subset to the characters in Denis's transcriptions: Google's default
   Latin subsets leave out combining marks such as U+032F. */
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=%20%28%29%5B%5Dadehiklmnoprstuvwxyz~%C5%93%C9%91%C9%94%C9%9B%C9%A1%CB%88%CB%90%CC%83%CC%AF%E2%80%94&display=swap');
.ling-ex-line .num { min-width: 4.2rem; }
/* IPA needs a font with combining marks such as U+032F; the 0-20 table is the
   only one with 21 rows, and its last column holds the transcriptions. */
div[data-testid="stTable"]:has(tbody tr:nth-child(21)) td:last-child,
div[data-testid="stTable"]:has(tbody tr:nth-child(21)) td:last-child p { font-family: 'Charis SIL', serif !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# MASTHEAD
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ling-masthead">
    <div class="ling-masthead-eyebrow">Linguistic Structure</div>
    <div class="ling-masthead-title">Breton</div>
    <div class="ling-masthead-sub">
        A Celtic language of Brittany that counts in twenties up to a hundred, names fifty
        as half a hundred and eighteen as three sixes, and lets a noun split a number in two.
    </div>
    <div class="ling-tags">
        <span class="ling-tag">Vigesimal to 100</span>
        <span class="ling-tag">Unit First</span>
        <span class="ling-tag">Half-Hundred</span>
        <span class="ling-tag">18 = 3 × 6</span>
        <span class="ling-tag">Gender on 2–4</span>
        <span class="ling-tag">Initial Mutation</span>
        <span class="ling-tag">Discontinuous Numerals</span>
        <span class="ling-tag">Severely Endangered</span>
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
    <p>Breton counts in twenties up to a hundred and puts the unit before the twenty:
    21 is <em>unan warn-ugent</em>, "one on twenty", and 75 is <em>pemzek ha tri-ugent</em>,
    "fifteen and three twenties". Two numbers break the pattern: 50 is <em>hanter-kant</em>,
    "half a hundred", and 18 is <em>triwec'h</em>, "three sixes".</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-props">
        <span class="ling-prop-key">Primary base</span>
        <span class="ling-prop-val"><strong>20</strong> for the tens from 40 to 99; 10 for 11 to 19 and above 100</span>
        <span class="ling-prop-key">Exceptions</span>
        <span class="ling-prop-val"><em>tregont</em> 30; <em>hanter-kant</em> 50, "half a hundred"; <em>triwec'h</em> 18, "three sixes"</span>
        <span class="ling-prop-key">Order</span>
        <span class="ling-prop-val">Unit first, then the ten: <em>pemp ha tregont</em>, "five and thirty", 35</span>
        <span class="ling-prop-key">Linking words</span>
        <span class="ling-prop-val"><em>warn-</em> "on" before twenty; <em>ha</em> "and" before the other tens</span>
        <span class="ling-prop-key">Gender</span>
        <span class="ling-prop-val">2, 3 and 4 have feminine forms: <em>div</em>, <em>teir</em>, <em>peder</em></span>
        <span class="ling-prop-key">Mutation</span>
        <span class="ling-prop-val">Numerals change the first sound of the next word, and <em>kant</em> and <em>mil</em> change after some numerals</span>
        <span class="ling-prop-key">Family</span>
        <span class="ling-prop-val">Celtic, Brythonic branch, with Welsh and Cornish</span>
        <span class="ling-prop-key">Speakers</span>
        <span class="ling-prop-val">About 107,000 in 2024, half the 2018 estimate of 214,000 (Région Bretagne 2025)</span>
        <span class="ling-prop-key">Status</span>
        <span class="ling-prop-val">Severely endangered (UNESCO; Moseley 2010)</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Breton is an Insular Celtic language: it came to the Continent from Britain with
    migrants between roughly the fourth and eighth centuries CE. Four dialects are traditionally
    recognised, Kerneveg, Leoneg, Tregerieg and Gwenedeg (Vannetais), the last the most
    divergent (Press 2009). Forms on this page are in the standard spelling,
    <em>peurunvan</em> (Favereau 1997); speech varies by region in sounds, in mutations after
    numerals and in which of the alternative forms below is preferred.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 2 — ONE TO TWENTY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Digits &amp; Bases</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">One to Twenty</div>', unsafe_allow_html=True)

st.table({
    "Number": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
    "Breton": ["mann", "unan", "daou", "tri", "pevar", "pemp", "c'hwec'h", "seizh", "eizh",
               "nav", "dek", "unnek", "daouzek", "trizek", "pevarzek", "pemzek", "c'hwezek",
               "seitek", "triwec'h", "naontek", "ugent"],
    "Pronunciation": ["—", "[ˈyːnɑ̃n]", "[dou̯]", "[triː]", "[ˈpɛːvar]", "[pɛm(p)]", "[xwɛːx]",
                      "[sei̯s]", "[ei̯s]", "[nao̯]", "[dek] ~ [deːɡ]", "[ˈœ̃nɛk] ~ [ˈœ̃nɛɡ]",
                      "[ˈdɔu̯zɛk] ~ [ˈdɔu̯zɛɡ]", "[ˈtriːzɛk] ~ [ˈtriːzɛɡ]",
                      "[pɛˈvarzɛk] ~ [pɛˈvarzɛɡ]", "[ˈpɛmzɛk] ~ [ˈpɛmzɛɡ]",
                      "[ˈxweːzɛk] ~ [ˈxweːzɛɡ]", "[ˈsei̯tɛk] ~ [ˈsei̯tɛɡ]", "[ˈtriwɛx]",
                      "[ˈnao̯tɛk]", "[ˈyːɡɛn(t)]"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Feminine two, three and four</div>
        <p><em>daou</em>, <em>tri</em> and <em>pevar</em> become <em>div</em>, <em>teir</em>
        and <em>peder</em> before a feminine noun: <em>div vag</em>, <em>teir bag</em>,
        <em>peder bag</em>, "two, three, four boats" (Jouin 1984). The feminine also appears
        inside larger numbers: <em>div warn-ugent</em>, 22 (Denis). No other numeral changes
        for gender.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Built on ten</div>
        <p>Eleven to nineteen are compounds of a unit and <em>dek</em> "ten", which becomes
        <em>-zek</em> (Favereau 1997), or <em>-tek</em> in <em>seitek</em> 17 and
        <em>naontek</em> 19: <em>daouzek</em> 12, <em>pemzek</em> 15. Eighteen is the
        exception. Zero is <em>mann</em>, which also
        means "nothing" (Press 2009).</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>Pronunciations are Gwendal Denis's (Université Rennes 2), recorded in Chan's
    numeral database; where he gives two forms, both are shown. Before a noun, <em>unan</em> is replaced by the article
    <em>ur</em>, <em>un</em> or <em>ul</em> (Jouin 1984).</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 3 — COUNTING BY TWENTIES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Vigesimal Structure</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Counting by Twenties</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[unit] <em>warn-ugent</em> for 21–29 · [unit, 1–19] <em>ha</em> [ten] for 31–99 — the ten is <em>tregont</em>, <em>daou-ugent</em>, <em>hanter-kant</em>, <em>tri-ugent</em> or <em style="white-space:nowrap">pevar-ugent</em></span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Number": ["20", "30", "40", "50", "60", "70", "80", "90", "100"],
    "Breton": ["ugent", "tregont", "daou-ugent", "hanter-kant", "tri-ugent",
               "dek ha tri-ugent", "pevar-ugent", "dek ha pevar-ugent", "kant"],
    "Literally": ["twenty", "thirty", "two twenties", "half a hundred", "three twenties",
                  "ten and three twenties", "four twenties", "ten and four twenties", "a hundred"],
})

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">The unit comes first</div>
    <div class="ling-ex-line"><span class="num">21</span><span class="word">unan warn-ugent</span><span class="gloss">one on twenty</span></div>
    <div class="ling-ex-line"><span class="num">35</span><span class="word">pemp ha tregont</span><span class="gloss">five and thirty</span></div>
    <div class="ling-ex-line"><span class="num">75</span><span class="word">pemzek ha tri-ugent</span><span class="gloss">fifteen and three twenties</span></div>
    <div class="ling-ex-line"><span class="num">99</span><span class="word">naontek ha pevar-ugent</span><span class="gloss">nineteen and four twenties</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Above sixty, the unit added to a score runs all the way to nineteen, so the decade
    boundary falls at the score, not at the ten: 71 is <em>unnek ha tri-ugent</em>, "eleven
    and three twenties", and 92 is <em>daouzek ha pevar-ugent</em> (Favereau 1997).
    <em>warn-</em> is the form the preposition <em>war</em> "on" takes before an ending, as
    in <em>warnon</em> "on me" (ARBRES). Welsh builds its traditional numbers the same way, with the unit placed on the twenty:
    <em>saith ar hugain</em>, "seven on twenty", 27 (Awbery 2009).</p>
    <p>Counting by twenty can carry on past a hundred. Press (2009) gives
    <em>c'hwec'h-ugent</em>, "six twenties", for 120 beside <em>kant ugent</em>, and
    <em>dek ha nav-ugent</em>, "ten and nine twenties", for 190. Favereau (1997) says it can
    run to 200 and beyond, citing <em>daouzeg-ugent</em>, "twelve twenties", for 240, and
    Jouitteau's ARBRES atlas finds it most productive in Trégor, where a 1910 text has
    <em>nav ugent manac'h</em>, "180 monks".</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 4 — EIGHTEEN AND FIFTY
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Irregular Forms</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Three Sixes and Half a Hundred</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Eighteen</div>
        <p><em>triwec'h</em> is <em>tri</em> "three" and <em>c'hwec'h</em> "six". It replaced a
        regular form: Brittonic <em>*oktundekan</em> had given Old Breton <em>eithnec</em>,
        "eight-ten" (Greene 1992, cited in ARBRES). Favereau (1997) notes that a regular
        <em>eitek</em> is attested, written <em>eittec</em> in older texts and
        <em>eizdec</em> in the 1499 <em>Catholicon</em>. Welsh has its own irregular 18,
        <em>deunaw</em>, "two nines" (Awbery 2009).</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Fifty</div>
        <p><em>hanter-kant</em> is "half a hundred"; Welsh says the same, <em>hanner
        cant</em>, and 150 is <em>cant a hanner</em>, "a hundred and a half" (Awbery 2009).
        Breton adds the half the same way: Favereau (1997, §870) quotes <em>trizek kant
        hanter</em> for 1,350, and Verdier (2010) gives <em>kant hanter</em> for 150. Before
        <em>hanter-kant</em>, "and" may be <em>ha</em> or <em>hag</em> by region: Press
        (2009) writes <em>ha(g)</em>.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-examples">
    <div class="ling-examples-label">Both inside larger numbers</div>
    <div class="ling-ex-line"><span class="num">18</span><span class="word">triwec'h</span><span class="gloss">three sixes</span></div>
    <div class="ling-ex-line"><span class="num">55</span><span class="word">pemp ha hanter-kant</span><span class="gloss">five and half a hundred</span></div>
    <div class="ling-ex-line"><span class="num">78</span><span class="word">triwec'h ha tri-ugent</span><span class="gloss">three sixes and three twenties</span></div>
    <div class="ling-ex-line"><span class="num">98</span><span class="word">triwec'h ha pevar-ugent</span><span class="gloss">three sixes and four twenties</span></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 5 — ABOVE A HUNDRED
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Hundreds &amp; Thousands</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">More Than One Right Answer</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-formula">
    <span class="ling-formula-label">Form</span>
    <span class="ling-formula-rule">[thousands] [hundreds] [rest below 100] — <em>mil nav c'hant pevar ha pevar-ugent</em>, 1984 (Press 2009)</span>
</div>
""", unsafe_allow_html=True)

st.table({
    "Number": ["101", "103", "120", "190", "200", "1200", "1984", "2000"],
    "Breton": ["kant unan", "kant tri", "kant ugent", "kant dek ha pevar-ugent",
               "daou c'hant", "mil daou c'hant", "mil nav c'hant pevar ha pevar-ugent",
               "daou vil"],
    "Also attested": ["unan ha kant", "tri ha kant", "c'hwec'h-ugent", "dek ha nav-ugent",
                      "daou gant", "daouzek kant", "naontek kant pevar ha pevar-ugent", "—"],
    "Source": ["Press 2009", "Favereau 1997", "Press 2009; Denis", "Press 2009",
               "Press 2009 (daou gant: Gwenedeg)", "Press 2009", "Press 2009", "Press 2009"],
})

st.markdown("""
<div class="ling-card">
    <p>Press (2009) lists <em>kant</em> first and the rest after it, and the converter
    follows that order. For small additions he and Favereau (1997) also give the reverse,
    <em>unan ha kant</em>, "one and a hundred". Between 1001 and 1999, Press calls counting in
    hundreds normal: <em>daouzek kant</em>, "twelve hundred", for 1200. The converter shows
    every attested form beside the main one.</p>
    <p><em>kant</em> becomes <em>c'hant</em> after <em>daou</em>, <em>tri</em>,
    <em>pevar</em> and <em>nav</em> (<em>daou c'hant</em>, <em>nav c'hant</em>), and
    <em>mil</em> becomes <em>vil</em> after <em>daou</em> (<em>daou vil</em>). After
    <em>daou</em> the change in <em>kant</em> is an archaic mutation, also kept in
    <em>daoufarzh</em> "two thirds"; Gwenedeg says <em>daou gant</em> (Favereau 1997).</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 6 — MUTATION AND THE NOUN
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Numerals &amp; Nouns</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">How a Number Changes the Next Word</div>', unsafe_allow_html=True)

st.table({
    "After": ["daou", "tri", "pevar", "nav", "pemp, c'hwec'h, seizh, eizh"],
    "ti 'house'": ["daou di", "tri zi", "pevar zi", "nav zi", "pemp ti"],
    "kazh 'cat'": ["daou gazh", "tri c'hazh", "pevar c'hazh", "nav c'hazh", "c'hwec'h kazh"],
    "penn 'head'": ["daou benn", "tri fenn", "pevar fenn", "nav fenn", "seizh penn"],
    "Change": ["softening (lenition)", "spirant mutation", "spirant mutation",
               "spirant mutation", "none"],
})

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">One noun, always singular</div>
        <p>A noun after a numeral stays singular, "ten book" rather than "ten books":
        <em>dek levr</em>. To use the plural, Breton adds <em>a</em> "of": <em>dek a
        levrioù</em> (Press 2009). The table above follows Press's examples in the standard
        language.</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Regional variation</div>
        <p>In Trégor the spirant mutation after 3, 4 and 9 has given way to softening,
        <em>tri benn</em>, "three heads", and survives in <em>tri c'hant</em> and a few fixed
        phrases; it was lost there around the middle of the twentieth century. In parts of
        the Vannetais area there may be no mutation at all (Hewitt 2001; Konan 2017; the
        ALBB dialect atlas; all cited in ARBRES).</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 7 — DISCONTINUOUS NUMERALS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Syntax</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">A Number Split by Its Noun</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Discontinuous numerals</div>
    <p>When a number has a unit and a ten, the noun goes straight after the unit, so the
    numeral is split in two: <em>tri den warn-ugent</em>, "three person on twenty", is 23
    people, and <em>pemp kador ha tregont</em> is 35 chairs (Jouin 1984).</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The split is the standard construction, not a poetic one. ARBRES cites <em>peder
    c'humun ha tregont</em>, "thirty-four communes", from a 2016 text of the Morbihan
    regional park. With
    one, the article takes the unit's place: <em>unan ha tregont</em> is 31, but "thirty-one
    years" is <em>ur bloaz ha tregont</em>. Press (2009) gives the split singular and the
    plural with <em>a</em> as alternatives: <em>un ti warn-ugent</em> or <em>unan warn-ugent
    a diez</em>, 21 houses. Welsh does the same with its traditional numbers: <em>saith
    bachgen ar hugain</em>, "seven boy on twenty" (Awbery 2009).</p>
    <p>The construction is under pressure. ARBRES reports a traditional speaker used to
    counting in French who found no comfortable Breton for "these thirty-one rocks", and
    notes that in Trégor less common nouns keep the numeral whole (Hewitt 2001).</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p>This is also why the converter stops at 9,999. Press (2009) treats <em>milion</em> as a
    noun, and Favereau (1997) says <em>mil</em> often behaves like one. Round thousands are
    attested (<em>deg mil</em>, 10,000; <em>kant mil</em>, 100,000, both cited in ARBRES), but
    none of the sources used here shows where <em>mil</em> goes in a number like 25,000, so the
    converter does not guess.</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 8 — CONTACT AND ENDANGERMENT
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Contact &amp; Change</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Twenties in France</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-grid-2">
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">French <em>quatre-vingts</em></div>
        <p>Breton's <em>pevar-ugent</em> and French <em>quatre-vingts</em> both mean "four
        twenties". Favereau (1997) holds that French counting by twenty comes from Gaulish.
        That account is contested, and internal Romance development may be enough to explain
        it; the <a href="/Numeral_Contact" target="_self">contact page</a> lists it as a
        hypothesis. Breton itself descends from the Celtic of Britain, not from Gaulish
        (Press 2009).</p>
    </div>
    <div class="ling-card" style="margin-bottom:0">
        <div class="ling-subsection-title" style="font-size:1.05rem;margin-bottom:0.6rem">Half the speakers in six years</div>
        <p>A regional survey of 8,336 people in 2024 estimated about 107,000 speakers (between
        93,000 and 120,500), 2.7% of people aged 15 and over in historic Brittany, against
        214,000 in 2018. Their average age fell from 70 to 58.5, because older speakers are
        dying while more people under 40 speak it; native speakers are fewer, and most new
        speakers learn at school (Région Bretagne 2025).</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SECTION 9 — LIMITS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Limits of the Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">What Is and Is Not Implemented</div>', unsafe_allow_html=True)

st.table({
    "Feature": ["0 to 1,999", "2,000 to 9,999", "10,000 and above",
                "Feminine 2, 3, 4", "Alternative forms", "Pronunciation",
                "Mutation of a following noun", "Regional forms"],
    "Status": ["Implemented", "Implemented", "Not implemented", "Implemented",
               "Shown and accepted", "Partial", "Not implemented", "Partial"],
    "Basis": ["Press (2009) and Favereau (1997) give every structure",
              "Press's round thousands, built like his 1984",
              "No source gives the order for compound thousands",
              "Shown whenever the last unit is 2, 3 or 4",
              "ha or hag hanter-kant, unit before kant, twenties to 199, hundreds from 1100, "
              "eitek, kant hanter, daouzeg-ugent",
              "Denis's transcriptions, only for the numbers he recorded",
              "Depends on the noun and on the dialect; described above",
              "Gwenedeg daou gant only; spoken dialects differ further"],
})

# ══════════════════════════════════════════════════════════════
# SECTION 10 — SOURCES
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">References</div>', unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p><strong>Press, Ian.</strong> 2009. "Breton." In Martin J. Ball &amp; Nicole Müller (eds.),
    <em>The Celtic Languages</em>, 2nd ed., 427–487. London: Routledge. The numerals to 1999
    and their alternatives; history and dialects; mutation after numerals.</p>
    <p><strong>Favereau, Francis.</strong> 1997. <em>Grammaire du breton contemporain</em>.
    Morlaix: Skol Vreizh. §292 on the cardinals, <em>eitek</em>, <em>daou c'hant</em>,
    counting by twenty past 100; §870 for <em>trizek kant hanter</em>.</p>
    <p><strong>Jouitteau, Mélanie (ed.).</strong> <em>ARBRES, wikigrammaire des dialectes du
    breton</em>. IKER, CNRS. Online; pages "Les numéraux cardinaux" and "War, ar", consulted
    November 2026. Discontinuous numerals, mutation and its regional variation, with the
    sources it cites: Greene (1992), Gourmelon (2014), Hewitt (2001), Konan (2017), Le Clerc
    (1910).</p>
    <p><strong>Jouin, Béatrice.</strong> 1984. <em>Petite grammaire du breton</em>. Rennes:
    Ouest-France. Feminine forms and the noun inside the numeral.</p>
    <p><strong>Denis, Gwendal.</strong> 2002, 2013. Breton numerals. In Eugene S. L. Chan,
    <em>Numeral Systems of the World's Languages</em>. Max Planck Institute for Evolutionary
    Anthropology. Pronunciations.</p>
    <p><strong>Awbery, Gwenllian.</strong> 2009. "Welsh." In Ball &amp; Müller (eds.),
    <em>The Celtic Languages</em>, 359–426. The Welsh parallels.</p>
    <p><strong>Région Bretagne.</strong> 2025. <em>Enquête sociolinguistique 2024 sur les
    langues de Bretagne: présentation des principaux résultats</em>. Survey by TMO, press
    conference of 20 January 2025.</p>
    <p><strong>Moseley, Christopher (ed.).</strong> 2010. <em>Atlas of the World's Languages in
    Danger</em>, 3rd ed. Paris: UNESCO.</p>
    <p><strong>Verdier, Jacques.</strong> 2010. "Les noms des nombres de 10 à 100 : étude de
    quelques « anomalies »." <em>Le Petit Vert</em> 101 (APMEP Lorraine). A teachers'
    bulletin, used only for <em>kant hanter</em>, 150, which matches Favereau's 1,350.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-info">
    <p><strong>A note on claims not used.</strong> Verdier (2010) says that some areas call 18
    "two nines", as Welsh does; none of the grammars mentions this, so it is left out.
    Popular number tables online give some forms that differ from the grammars and were not
    used. Favereau's view that French counting by twenty is Gaulish is reported as his view,
    not as fact.</p>
</div>
""", unsafe_allow_html=True)

footer_nav("Breton", "linguistics")
