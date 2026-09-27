import streamlit as st
import pandas as pd
from ui import apply_global_styles, LING_CSS, LING_WIDTH_CSS

# ============================================================
# NUMERAL CONTACT & TRANSMISSION
# A repository of documented numeral borrowing, sorted by the
# pattern of transfer.
#
# Structure follows the distinction Comrie draws:
#   1. Borrowed words        - forms travel
#   2. Inherited look-alikes - forms only APPEAR to travel
#   3. Borrowed systems      - structure travels, words do not
#
# EVIDENCE POLICY
# Every row carries a confidence marker. "Established" means the
# direction and mechanism of transfer are uncontroversial in the
# descriptive literature. "Proposed" means the borrowing is argued
# but contested. Nothing is listed on the strength of resemblance
# alone - see the methodological warning at the top of the page.
#
# Sources: Comrie (2005, p.c. 2026); Souag (2007) The Typology of
# Number Borrowing in Berber; Campbell, Kaufman & Smith-Stark
# (1986); Matras (2009) Language Contact; Ashton (1944).
# ============================================================

st.set_page_config(page_title="Numeral Contact & Transmission", layout="wide")
apply_global_styles()
st.markdown(LING_CSS, unsafe_allow_html=True)
st.markdown(LING_WIDTH_CSS, unsafe_allow_html=True)

# ── Data ─────────────────────────────────────────────────────────────────────
# pattern: how the transfer is shaped
#   "Partial"      native low numerals kept, higher ones borrowed
#   "Parallel"     both systems retained and used side by side
#   "Near-total"   almost the whole inventory replaced
#   "Single"       one numeral borrowed in isolation
#   "Structure"    the architecture travels, the words do not
PATTERNS = ["Partial", "Parallel", "Near-total", "Single", "Structure"]
VITALITIES = ["Vigorous", "Threatened", "Endangered", "Mixed"]

CASES = [
    # --- Arabic into Afroasiatic & Nilo-Saharan ---
    dict(recipient="Swahili", rfam="Atlantic-Congo (Bantu)", source="Arabic",
         sfam="Afroasiatic (Semitic)", borrowed="6, 7, 9",
         detail="sita, saba, tisa. 1–5, 8 and 10 remain Bantu.",
         pattern="Partial", vitality="Vigorous", confidence="Established"),
    dict(recipient="Korandje", rfam="Songhay", source="Arabic",
         sfam="Afroasiatic (Semitic)", borrowed="4 and above",
         detail="Only a-ffu '1', inka '2' and inẓa '3' survive in normal use; "
                "everything above is Arabic.",
         pattern="Near-total", vitality="Endangered", confidence="Established"),
    dict(recipient="Figuig Berber", rfam="Afroasiatic (Berber)", source="Arabic",
         sfam="Afroasiatic (Semitic)", borrowed="3 and above",
         detail="1 and 2 are Berber; the rest of the inventory is Arabic throughout.",
         pattern="Near-total", vitality="Threatened", confidence="Established"),
    dict(recipient="South Oran Berber", rfam="Afroasiatic (Berber)", source="Arabic",
         sfam="Afroasiatic (Semitic)", borrowed="3 and above",
         detail="Same cut-off as Figuig. Berber varieties differ in how deep the "
                "borrowing runs, forming a gradient rather than one pattern.",
         pattern="Near-total", vitality="Threatened", confidence="Established"),
    dict(recipient="Kabyle", rfam="Afroasiatic (Berber)", source="Arabic",
         sfam="Afroasiatic (Semitic)", borrowed="higher numerals",
         detail="Retains a fuller native inventory than the Saharan varieties — the "
                "conservative end of the Berber gradient.",
         pattern="Partial", vitality="Vigorous", confidence="Established"),

    # --- Chinese into East & Southeast Asia ---
    dict(recipient="Japanese", rfam="Japonic", source="Middle Chinese",
         sfam="Sino-Tibetan", borrowed="full series",
         detail="Sino-Japanese ichi, ni, san beside native hitotsu, futatsu, mittsu. "
                "Choice is governed by the counter used.",
         pattern="Parallel", vitality="Vigorous", confidence="Established"),
    dict(recipient="Korean", rfam="Koreanic", source="Middle Chinese",
         sfam="Sino-Tibetan", borrowed="full series",
         detail="Sino-Korean il, i, sam beside native hana, dul, set. Both inventories "
                "are in daily use.",
         pattern="Parallel", vitality="Vigorous", confidence="Established"),
    dict(recipient="Vietnamese", rfam="Austroasiatic", source="Middle Chinese",
         sfam="Sino-Tibetan", borrowed="full series",
         detail="Sino-Vietnamese nhất, nhị, tam beside native một, hai, ba; "
                "the borrowed set is now largely confined to compounds.",
         pattern="Parallel", vitality="Vigorous", confidence="Established"),

    # --- Indic outward ---
    dict(recipient="Tibetan", rfam="Sino-Tibetan", source="Sanskrit",
         sfam="Indo-European (Indic)", borrowed="the large-number scheme",
         detail="Names successive powers on the Indic model using native vocabulary — "
                "stong 10³, khri 10⁴, 'bum 10⁵, bye ba 10⁷.",
         pattern="Structure", vitality="Vigorous", confidence="Established"),
    dict(recipient="Buryat", rfam="Mongolic", source="Tibetan",
         sfam="Sino-Tibetan", borrowed="large-number terms",
         detail="Took Tibetan high-value words directly — a second step along the same "
                "diffusion chain, transferring words rather than structure.",
         pattern="Single", vitality="Endangered", confidence="Established"),
    dict(recipient="Hindi / Urdu", rfam="Indo-European (Indic)", source="Persian",
         sfam="Indo-European (Iranian)", borrowed="1,000",
         detail="hazār displaced the inherited Indic word for a thousand.",
         pattern="Single", vitality="Vigorous", confidence="Established"),
    dict(recipient="Malay / Indonesian", rfam="Austronesian", source="Sanskrit",
         sfam="Indo-European (Indic)", borrowed="high values",
         detail="juta 'million' and other high-value terms entered from Indic sources.",
         pattern="Single", vitality="Vigorous", confidence="Established"),
    dict(recipient="Thai", rfam="Kra-Dai", source="Sanskrit / Pali",
         sfam="Indo-European (Indic)", borrowed="high values",
         detail="Indic vocabulary supplies part of the high-value series; low numerals "
                "are Kra-Dai, with Chinese influence on the decade structure.",
         pattern="Partial", vitality="Vigorous", confidence="Established"),

    # --- Colonial contact in the Americas & Pacific ---
    dict(recipient="Nahuatl (modern)", rfam="Uto-Aztecan", source="Spanish",
         sfam="Indo-European (Romance)", borrowed="most of the range",
         detail="The classical vigesimal series has largely given way to Spanish numerals "
                "in everyday counting, though the language itself persists.",
         pattern="Near-total", vitality="Threatened", confidence="Established"),
    dict(recipient="Quechua", rfam="Quechuan", source="Spanish",
         sfam="Indo-European (Romance)", borrowed="higher numerals",
         detail="Spanish forms are widespread for larger values and in commerce, "
                "alongside a surviving native decimal system.",
         pattern="Partial", vitality="Threatened", confidence="Established"),
    dict(recipient="Tagalog", rfam="Austronesian", source="Spanish",
         sfam="Indo-European (Romance)", borrowed="full series",
         detail="uno, dos, tres beside native isa, dalawa, tatlo — distributed by "
                "register and by what is counted, notably time and money.",
         pattern="Parallel", vitality="Vigorous", confidence="Established"),
    dict(recipient="Chamorro", rfam="Austronesian", source="Spanish",
         sfam="Indo-European (Romance)", borrowed="most of the range",
         detail="Spanish numerals largely replaced the inherited Austronesian set.",
         pattern="Near-total", vitality="Endangered", confidence="Established"),

    # --- Within Europe ---
    dict(recipient="Finnish", rfam="Uralic", source="Proto-Baltic",
         sfam="Indo-European (Baltic)", borrowed="1,000",
         detail="tuhat, from Proto-Baltic *tūˀsantis (compare Lithuanian "
                "tūkstantis). The rest of the inventory is Uralic.",
         pattern="Single", vitality="Vigorous", confidence="Established"),
    dict(recipient="English", rfam="Indo-European (Germanic)", source="Italian",
         sfam="Indo-European (Romance)", borrowed="1,000,000",
         detail="million, from Italian milione, an augmentative of mille — borrowed in "
                "the fourteenth century as commerce required larger values.",
         pattern="Single", vitality="Vigorous", confidence="Established"),
    dict(recipient="Hungarian", rfam="Uralic", source="Iranian",
         sfam="Indo-European (Iranian)", borrowed="1,000",
         detail="ezer is widely derived from an Iranian source, but the derivation is "
                "argued rather than settled.",
         pattern="Single", vitality="Vigorous", confidence="Proposed"),
    dict(recipient="French", rfam="Indo-European (Romance)", source="substrate",
         sfam="Celtic or pre-Indo-European", borrowed="vigesimal counting",
         detail="quatre-vingts '80' is sometimes attributed to a Celtic or Basque-like "
                "substrate; internal Romance development may suffice to explain it.",
         pattern="Structure", vitality="Vigorous", confidence="Proposed"),

    # --- Areal, no words transferred ---
    dict(recipient="Mesoamerican languages", rfam="Multiple unrelated families",
         source="areal diffusion", sfam="—", borrowed="base-20 counting",
         detail="Nahuatl, Mayan, Mixtec, Zapotec and Totonac share vigesimal structure "
                "while their numeral words are unrelated.",
         pattern="Structure", vitality="Mixed", confidence="Established"),
]

# Most vulnerable first: the ordering is itself part of the argument.
VITALITY_ORDER = {"Endangered": 0, "Threatened": 1, "Vigorous": 2, "Mixed": 3}

# ── Page-specific styles ─────────────────────────────────────────────────────
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
.filter-bar {
    background:var(--parchment-2); border:1px solid var(--rule);
    border-radius:5px; padding:1rem 1.35rem; margin-bottom:1.1rem;
}
.filter-label {
    font-family:'DM Sans',sans-serif; font-size:.68rem; font-weight:700;
    text-transform:uppercase; letter-spacing:.12em; color:var(--ink-faint);
    margin-bottom:.5rem;
}
.nc-hier { display:flex; align-items:stretch; gap:0; margin:.6rem 0 .3rem 0; overflow-x:auto; }
.nc-hier-cell {
    flex:1 1 0; min-width:6.2rem; padding:.7rem .6rem; text-align:center;
    border:1px solid var(--rule); border-right:none;
    font-family:'Crimson Pro',Georgia,serif; font-size:1rem; color:var(--ink);
}
.nc-hier-cell:last-child { border-right:1px solid var(--rule); }
.nc-hier-cell .lab {
    display:block; font-family:'DM Sans',sans-serif; font-size:.56rem;
    font-weight:700; letter-spacing:.09em; text-transform:uppercase;
    color:var(--ink-faint); margin-top:.25rem;
}
.nc-hier-cell.keep { background:rgba(46,107,122,.10); }
.nc-hier-cell.mid  { background:rgba(196,154,38,.11); }
.nc-hier-cell.go   { background:rgba(184,92,56,.11); }
.nc-scale-note {
    font-family:'DM Sans',sans-serif; font-size:.7rem; color:var(--ink-faint);
    display:flex; justify-content:space-between; margin-bottom:1rem; gap:1rem;
}

/* --- repository table --- */
.nc-tablewrap {
    overflow-x:auto; border:1px solid var(--card-border); border-radius:6px;
    background:var(--card-bg); box-shadow:0 1px 3px rgba(26,22,18,.04);
    margin-bottom:.9rem;
}
.nc-table { border-collapse:collapse; width:100%; min-width:940px; }
.nc-table th {
    text-align:left; padding:.62rem .8rem;
    font-family:'DM Sans',sans-serif; font-size:.6rem; font-weight:700;
    letter-spacing:.12em; text-transform:uppercase; color:var(--ink-faint);
    background:var(--parchment-3); border-bottom:1px solid var(--rule-strong);
    white-space:nowrap;
}
.nc-table td {
    padding:.62rem .8rem; border-bottom:1px solid var(--rule);
    font-family:'Crimson Pro',Georgia,serif; font-size:.93rem;
    line-height:1.45; color:var(--ink-soft); vertical-align:top;
}
.nc-table tbody tr:last-child td { border-bottom:none; }
.nc-table tbody tr:hover td { background:var(--parchment-2); }
.nc-table td.rec { white-space:nowrap; color:var(--ink); }
.nc-table td.rec .fam {
    display:block; font-family:'DM Sans',sans-serif; font-size:.64rem;
    color:var(--ink-faint); margin-top:.15rem; letter-spacing:.02em;
}
.nc-table td.what { white-space:nowrap; font-style:italic; color:var(--ink); }
.nc-table td.det { min-width:20rem; }
.nc-table .pat, .nc-table .vit, .nc-table .conf {
    display:inline-block; font-family:'DM Sans',sans-serif; font-size:.6rem;
    font-weight:700; letter-spacing:.07em; text-transform:uppercase;
    padding:.16rem .45rem; border-radius:2px; white-space:nowrap;
}
.nc-table .pat { background:var(--parchment-3); color:var(--ink-soft); border:1px solid var(--rule-strong); }
.nc-table .vit-end { background:rgba(184,92,56,.14); color:#8d3f22; border:1px solid rgba(184,92,56,.32); }
.nc-table .vit-thr { background:rgba(196,154,38,.14); color:#7d5d0f; border:1px solid rgba(196,154,38,.32); }
.nc-table .vit-vig { background:rgba(46,107,122,.12); color:var(--teal); border:1px solid rgba(46,107,122,.28); }
.nc-table .vit-mix { background:var(--parchment-3); color:var(--ink-faint); border:1px solid var(--rule-strong); }
.nc-table .conf-est { background:transparent; color:var(--ink-faint); border:1px solid var(--rule-strong); }
.nc-table .conf-prop { background:rgba(196,154,38,.13); color:#7d5d0f; border:1px solid rgba(196,154,38,.3); }
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
    <div class="ling-masthead-eyebrow">Cross-Linguistic Repository</div>
    <div class="ling-masthead-title">Contact &amp; Transmission</div>
    <div class="nc-sub">A sorted record of documented numeral borrowing — which words travelled, which structures travelled without them, and why similar-looking numerals are so often not evidence of contact at all.</div>
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
    <p>Every entry in the repository below is marked <em>Established</em> or
    <em>Proposed</em>. Nothing is listed on the strength of resemblance alone.</p>
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
        <p>All continue Proto-Indo-European <em>*dwóh₁</em>. English did not borrow
        <em>two</em> from Latin, and Sanskrit did not borrow from Greek.</p>
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
        <p>Swahili is Bantu and Arabic is Semitic; they share no ancestor. The borrowing
        follows centuries of Indian Ocean trade contact.</p>
        <p><strong>How you can tell:</strong> the borrowed forms sit oddly against the
        language's own patterns, and typically occupy only part of the range.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── The hierarchy ────────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">The Governing Pattern</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Borrowing Runs Downwards</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Key Fact</div>
    <p>Numerals are not borrowed at random. High values go first and low values last, so a
    language under pressure loses its counting system <em>from the top down</em>. The
    numerals 1 and 2 are the most resistant of all — in the most heavily borrowed
    systems on record they are frequently the only survivors.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="nc-hier">
    <div class="nc-hier-cell keep">1–2<span class="lab">most resistant</span></div>
    <div class="nc-hier-cell keep">3–5<span class="lab">usually kept</span></div>
    <div class="nc-hier-cell mid">6–10<span class="lab">often borrowed</span></div>
    <div class="nc-hier-cell mid">tens<span class="lab">frequently</span></div>
    <div class="nc-hier-cell go">100<span class="lab">readily</span></div>
    <div class="nc-hier-cell go">1,000+<span class="lab">borrowed first</span></div>
</div>
<div class="nc-scale-note"><span>Learned earliest, used most</span><span>Learned late, used in trade and administration</span></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>The explanation is usage rather than grammar. Low numerals are acquired in infancy
    and used constantly; high numerals are learned later, used less, and are exactly the
    values needed for trade, taxation and schooling — the domains in which a dominant
    language operates. Borrowing therefore enters at the top of the range and works down.</p>
    <p style="margin-bottom:0">The clearest demonstration is the Berber gradient. Different
    varieties have stopped at different points along the same path: Kabyle retains a fuller
    native inventory, Figuig and South Oran keep only 1 and 2, and Korandje — a Songhay
    language of the Algerian Sahara — has been pushed back to three native forms. The
    same process, caught at different stages.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-callout">
    <div class="ling-callout-label">Two further findings</div>
    <p><strong>Synonymy is a transitional stage.</strong> Native and borrowed forms coexist
    for a period before one wins. A language showing both is usually mid-shift — though
    the East Asian cases below show the unstable stage can last a millennium.</p>
    <p style="margin-bottom:0"><strong>Syntax travels with the word.</strong> In Korandje,
    borrowed higher numerals take the word order of Arabic rather than of Korandje. What is
    borrowed is not simply a form but a fragment of another grammar.</p>
</div>
""", unsafe_allow_html=True)

# ── The repository ───────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Repository</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Documented Cases</div>', unsafe_allow_html=True)

df = pd.DataFrame(CASES)

st.markdown('<div class="filter-bar"><div class="filter-label">Filter</div>',
            unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
with f1:
    sel_pattern = st.multiselect("Pattern of transfer", PATTERNS, default=[], key="nc_pat")
with f2:
    sel_vit = st.multiselect("Vitality of recipient", VITALITIES, default=[], key="nc_vit")
with f3:
    sel_conf = st.multiselect("Evidence status", ["Established", "Proposed"],
                              default=[], key="nc_conf")
st.markdown('</div>', unsafe_allow_html=True)

view = df.copy()
if sel_pattern:
    view = view[view["pattern"].isin(sel_pattern)]
if sel_vit:
    view = view[view["vitality"].isin(sel_vit)]
if sel_conf:
    view = view[view["confidence"].isin(sel_conf)]

view = view.assign(_v=view["vitality"].map(VITALITY_ORDER).fillna(9)) \
           .sort_values(["_v", "recipient"]).drop(columns="_v")

if view.empty:
    st.markdown(
        '<div class="ling-card"><p style="margin:0">No cases match those filters.</p></div>',
        unsafe_allow_html=True,
    )
else:
    st.caption(f"Showing {len(view)} of {len(df)} documented cases, "
               f"most vulnerable recipients first.")

    def esc(t):
        return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

    rows_html = []
    for _, r in view.iterrows():
        vit_cls = {"Endangered": "vit-end", "Threatened": "vit-thr",
                   "Vigorous": "vit-vig", "Mixed": "vit-mix"}.get(r["vitality"], "vit-mix")
        conf_cls = "conf-est" if r["confidence"] == "Established" else "conf-prop"
        rows_html.append(
            f'<tr>'
            f'<td class="rec"><strong>{esc(r["recipient"])}</strong>'
            f'<span class="fam">{esc(r["rfam"])}</span></td>'
            f'<td class="rec">{esc(r["source"])}'
            f'<span class="fam">{esc(r["sfam"])}</span></td>'
            f'<td class="what">{esc(r["borrowed"])}</td>'
            f'<td class="det">{esc(r["detail"])}</td>'
            f'<td><span class="pat">{esc(r["pattern"])}</span></td>'
            f'<td><span class="vit {vit_cls}">{esc(r["vitality"])}</span></td>'
            f'<td><span class="conf {conf_cls}">{esc(r["confidence"])}</span></td>'
            f'</tr>'
        )

    st.markdown(
        '<div class="nc-tablewrap"><table class="nc-table">'
        '<thead><tr>'
        '<th>Recipient</th><th>Source</th><th>Borrowed</th><th>Detail</th>'
        '<th>Pattern</th><th>Vitality</th><th>Evidence</th>'
        '</tr></thead><tbody>' + "".join(rows_html) + '</tbody></table></div>',
        unsafe_allow_html=True,
    )

st.markdown("""
<div class="ling-card">
    <p style="margin:0"><strong>Reading the table.</strong> <em>Pattern</em> describes the
    shape of the transfer, not its size. <em>Partial</em> keeps native low numerals and
    borrows above them; <em>Parallel</em> means two complete systems coexist;
    <em>Near-total</em> means the inventory has almost gone; <em>Single</em> is one isolated
    numeral; <em>Structure</em> means the architecture moved without any words.
    <em>Evidence</em> separates cases that are uncontroversial from those that are argued
    but contested.</p>
</div>
""", unsafe_allow_html=True)

# ── Deep dives ───────────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Case Studies</div>', unsafe_allow_html=True)
st.markdown('<div class="ling-section-title">Four Patterns in Detail</div>',
            unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Partial — Swahili’s split inventory</div>',
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
    inherited. The pattern is not arbitrary: these are the values that several Bantu
    languages express with longer compound or quinary forms, and the shorter Arabic words
    displaced them. Swahili is in this repository's
    <a href="/Swahili_Converter" target="_self">converter</a>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Near-total — Korandje at the far end</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Korandje is a Songhay language spoken in the oasis of Tabelbala in the Algerian
    Sahara, surrounded by Arabic and Berber and with a small, declining speaker community.
    Its numeral system has been reduced to three native forms:</p>
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">1</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">a-ffu</span>
            <span class="ling-morph-gloss">native Songhay</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">2</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">inka</span>
            <span class="ling-morph-gloss">native Songhay</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">3</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">inẓa</span>
            <span class="ling-morph-gloss">native Songhay</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">4 and above</span>
            <span class="ling-morph-arrow">←</span>
            <span class="ling-morph-target">Arabic</span>
            <span class="ling-morph-gloss">borrowed, and carrying Arabic word order</span>
        </div>
    </div>
    <p style="margin:.8rem 0 0 0">This is what the end of the process looks like. The
    language is still spoken; its counting system is very nearly gone. It is the clearest
    single illustration of why numeral systems can be more endangered than the languages
    that carry them.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Parallel — two systems, indefinitely</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Japanese, Korean and Vietnamese each borrowed the complete Chinese series while
    keeping their own. Both sets remain in use, selected by context rather than one
    replacing the other — synonymy that has lasted more than a millennium.</p>
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
        <div class="ling-morph-row">
            <span class="ling-morph-source">Tagalog</span>
            <span class="ling-morph-arrow">·</span>
            <span class="ling-morph-target">isa, dalawa, tatlo</span>
            <span class="ling-morph-gloss">native — versus Spanish <em>uno, dos, tres</em>, used for time and money</span>
        </div>
    </div>
    <p style="margin:.8rem 0 0 0">In Japanese the choice is governed by the counter attached
    to the numeral; in Tagalog by register and by what is being counted. Both are stable
    divisions of labour rather than competitions.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">Structure — architecture without vocabulary</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p>Base-20 counting is near-universal across Mesoamerica, in languages from families with
    no demonstrable relationship to one another:</p>
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
    families. What they share is the organising principle — one of the features used to
    establish Mesoamerica as a linguistic area. The two best-documented members treat that
    shared base differently: Nahuatl keeps it regular, while the Mayan Long Count bends it,
    as set out on the <a href="/Large_Numbers" target="_self">Naming Large Numbers</a> page.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ling-subsection-title">A chain that changes mode</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="nc-chain">
    <span class="nc-chain-node">Sanskrit</span>
    <span class="nc-chain-arrow">→</span>
    <span class="nc-chain-node">Tibetan</span>
    <span class="nc-chain-arrow">→</span>
    <span class="nc-chain-node">Buryat</span>
    <span class="nc-chain-note">structure, then words</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <div class="ling-morph-table">
        <div class="ling-morph-row">
            <span class="ling-morph-source">Sanskrit → Tibetan</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">structure only</span>
            <span class="ling-morph-gloss">Tibetan names successive powers on the Indic model using native forms — <em>stong</em> 10³, <em>khri</em> 10⁴, <em>'bum</em> 10⁵, <em>bye ba</em> 10⁷</span>
        </div>
        <div class="ling-morph-row">
            <span class="ling-morph-source">Tibetan → Buryat</span>
            <span class="ling-morph-arrow">→</span>
            <span class="ling-morph-target">words</span>
            <span class="ling-morph-gloss">Buryat took Tibetan high-value words directly, a second step along the same chain</span>
        </div>
    </div>
    <p style="margin:.8rem 0 0 0">The two steps are of different kinds. Sanskrit gave Tibetan
    a <em>pattern</em>; Tibetan gave Buryat <em>words</em>. A single diffusion chain can
    change mode as it travels. Tibetan is in this repository's
    <a href="/Tibetan_Converter" target="_self">converter</a> and
    <a href="/Tibetan_Linguistics" target="_self">grammar page</a>.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ling-card">
    <p style="margin:0">A frequently cited European parallel is the vigesimal residue in
    French <em>quatre-vingts</em> (80), sometimes attributed to contact with a Celtic or
    Basque-like substrate.<span class="nc-debated">Proposed</span> The substrate account is
    contested and internal Romance development may be sufficient to explain it; it is listed
    as a hypothesis rather than an established case.</p>
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
    <p>The repository above is sorted with the most vulnerable recipients first, and the
    pattern is visible in that ordering: the languages that have lost most of their numerals
    are small, surrounded, and under sustained pressure from a dominant language of trade and
    administration. Korandje, Chamorro and modern Nahuatl sit at the far end of the same
    process that has taken only three slots from Swahili.</p>
    <p style="margin-bottom:0">Because the shift runs from the top of the range downwards, a
    well-documented language may still have an undocumented numeral system: fieldwork
    recording everyday speech will capture 1 to 5 long after the higher values have gone.
    Documentation of a language is not documentation of its numerals.</p>
</div>
""", unsafe_allow_html=True)

# ── Sources ──────────────────────────────────────────────────────────────────
st.markdown('<div class="ling-section-label">Sources</div>', unsafe_allow_html=True)
st.markdown("""
<div class="ling-card">
    <p style="margin:0 0 .5rem 0">Comrie, B. (2005). <em>Endangered numeral systems.</em> In
    Wohlgemuth &amp; Dirksmeyer (eds.), <em>Bedrohte Vielfalt</em>, 203–230. Berlin:
    Weißensee Verlag — and personal communication, 2026.</p>
    <p style="margin:0 0 .5rem 0">Souag, L. (2007). <em>The Typology of Number Borrowing in
    Berber.</em> Source for the Berber gradient, the Korandje data, and the observation that
    borrowed numerals carry source-language syntax.</p>
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
    '<div class="nav-card-desc">Six traditions for deciding which powers deserve a word '
    'of their own — and what happens at 10,000.</div>'
    '<div class="nav-card-cta">Naming Large Numbers →</div>'
    '</a>'
    '<a class="nav-card-home" href="/" target="_self">← Home</a>'
    '</div>',
    unsafe_allow_html=True,
)
