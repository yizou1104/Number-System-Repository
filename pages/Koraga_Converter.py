import streamlit as st
from urllib.parse import quote

from ui import apply_global_styles, language_nav, CONV_CSS_ADDITIONS, footer_nav
from Koraga import (
    SOURCES, KORRA, BHAT, KERALA, LAKH, forms, missing_sources, koraga_lookup, grouped,
)
from Koraga import all_forms_strings, number_to_koraga, koraga_to_number  # noqa: F401 — entry points for the audits
import Tulu

# ============================================================
# KORAGA CONVERTER
# Data, sources and logic live in Koraga.py. Only recorded forms are shown.
# ============================================================

st.set_page_config(page_title="Koraga Numeral Converter", layout="wide")
apply_global_styles()

# Charis SIL, subset to the characters the IPA and Bhat's spellings use
_IPA_CHARS = "".join(sorted({c for f in list(KORRA.values())
                             + [f for d in BHAT.values() for f, _ in d.values()]
                             + [v[0] for v in KERALA.values()] for c in f} | set(" ·")))

CONV_CSS = """<style>
/* Malayalam for the Kerala forms, Kannada for the Tulu comparison */
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Malayalam:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Kannada:wght@400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Charis+SIL&text=""" + quote(_IPA_CHARS) + """&display=swap');
.conv-masthead{border-top:3px solid var(--ink);border-bottom:1px solid var(--rule);padding:1.75rem 0 1.4rem 0;margin-bottom:1.75rem}
.conv-masthead-eyebrow{font-family:'DM Sans',sans-serif;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.18em;color:var(--accent);display:flex;align-items:center;gap:.65rem;margin-bottom:.65rem}
.conv-masthead-eyebrow::before{content:'';display:inline-block;width:1.75rem;height:1.5px;background:var(--accent);flex-shrink:0}
.conv-masthead-title{font-family:'Crimson Pro',Georgia,serif;font-size:3rem;font-weight:700;color:var(--ink);letter-spacing:-.04em;line-height:1.05;margin-bottom:.5rem}
.conv-masthead-desc{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:1.05rem;color:var(--ink-muted);line-height:1.55;margin:0}
.conv-section-label{font-family:'DM Sans',sans-serif;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;color:var(--ink-soft);display:flex;align-items:center;gap:1rem;margin:2rem 0 1rem 0}
.conv-section-label::before{content:'';display:inline-block;width:2rem;height:1px;background:var(--ink-muted);flex-shrink:0}
.conv-section-label::after{content:'';flex:1;height:1px;background:var(--rule)}
div[data-testid="stRadio"]>div{display:flex;gap:0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.35rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 4px 14px rgba(26,22,18,.04),inset 0 1px 0 rgba(255,255,255,.65);width:fit-content;flex-wrap:wrap}
div[data-testid="stRadio"] label{display:flex!important;align-items:center!important;font-family:'DM Sans',sans-serif!important;font-size:.9rem!important;font-weight:600!important;letter-spacing:.02em!important;text-transform:none!important;color:var(--ink-soft)!important;background:transparent!important;border:1.5px solid transparent!important;border-radius:4px!important;padding:.55rem 1.35rem!important;cursor:pointer!important;transition:all .18s cubic-bezier(.4,0,.2,1)!important;white-space:nowrap!important}
div[data-testid="stRadio"] label>span:first-child{display:none!important}
div[data-testid="stRadio"] label:hover{background:var(--parchment-3)!important;border-color:var(--rule-strong)!important;color:var(--ink)!important}
div[data-testid="stRadio"] label:has(input:checked){background:var(--ink)!important;border-color:var(--ink)!important;box-shadow:3px 3px 0 var(--accent)!important;transform:translate(-1px,-1px)!important}
div[data-testid="stRadio"] label:has(input:checked) p,div[data-testid="stRadio"] label:has(input:checked) span{color:var(--parchment)!important}
div[data-testid="stRadio"] label p{font-family:'DM Sans',sans-serif!important;font-size:.9rem!important;font-weight:600!important;margin:0!important;line-height:1!important}
.conv-presets-sublabel{font-family:'DM Sans',sans-serif;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--ink-faint);margin-bottom:.65rem;margin-top:0}
.conv-input-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:1.3rem 1.5rem 1.4rem;margin-bottom:.5rem;box-shadow:0 1px 3px rgba(26,22,18,.05),0 6px 20px rgba(26,22,18,.06),inset 0 1px 0 rgba(255,255,255,.7)}
.conv-input-title{font-family:'Crimson Pro',Georgia,serif;font-size:1.3rem;font-weight:600;color:var(--ink);letter-spacing:-.02em;margin:0 0 .25rem 0;line-height:1.2}
.conv-input-hint{font-family:'Crimson Pro',Georgia,serif;font-style:italic;font-size:.93rem;color:var(--ink-faint);margin:0 0 .8rem 0;line-height:1.4}
.conv-result-card{background:rgba(46,107,122,.04);border:1px solid rgba(46,107,122,.18);border-left:3px solid var(--teal);border-radius:0 4px 4px 0;padding:.85rem 1.1rem;margin-top:.8rem}
.conv-result-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--teal);margin-bottom:.55rem}
.conv-result-row{display:grid;grid-template-columns:8.5rem 1fr;gap:.35rem .9rem;align-items:baseline;padding:.12rem 0}
.conv-result-sublabel{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink-faint)}
.conv-result-subvalue{font-family:'Crimson Pro',Georgia,serif;font-size:1.05rem;font-weight:400;color:var(--ink);line-height:1.55;word-break:break-word}
.conv-error-card{background:rgba(184,92,56,.05);border:1px solid rgba(184,92,56,.2);border-left:3px solid var(--accent);border-radius:0 4px 4px 0;padding:.75rem 1.1rem;margin-top:.8rem}
.conv-error-text{font-family:'Crimson Pro',Georgia,serif;font-size:1rem;color:var(--accent);font-style:italic;margin:0}
.conv-empty-state{font-family:'Crimson Pro',Georgia,serif;font-style:italic;color:var(--ink-faint);padding:1.1rem 0}
.conv-caption{font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--ink-faint);line-height:1.55;margin-top:1rem}
.ko-main{font-family:'Charis SIL','Crimson Pro',serif;font-size:1.5rem;font-weight:400;line-height:1.35}
.ko-big{font-family:'Crimson Pro',Georgia,serif;font-size:1.95rem;font-weight:600;letter-spacing:-.01em;line-height:1.25}
.ko-ml{font-family:'Noto Serif Malayalam',serif;font-size:1.25rem;margin-left:.45rem}
.ko-kn{font-family:'Noto Serif Kannada','Crimson Pro',serif;font-size:1.25rem}
.ko-ipa{font-family:'Charis SIL','Crimson Pro',serif}
.ko-muted{font-family:'DM Sans',sans-serif;font-size:.74rem;color:var(--ink-faint);letter-spacing:.02em}
.ko-alt{display:block;padding:.1rem 0}
.ko-compare{background:var(--card-bg);border:1px solid var(--card-border);border-radius:6px;padding:.75rem 1.05rem;margin-top:.8rem}
.ko-compare-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-faint);margin-bottom:.4rem}
.ko-note{border:1px solid var(--rule);border-left:3px solid var(--ink-muted);background:var(--parchment-2);border-radius:0 4px 4px 0;padding:.7rem 1.05rem;margin-top:.8rem}
.ko-note-label{font-family:'DM Sans',sans-serif;font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-soft);margin-bottom:.3rem}
.ko-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.97rem;color:var(--ink-muted);line-height:1.55;margin:0}
.ko-spelling-note{border:1px solid rgba(184,92,56,.35);border-left:3px solid var(--accent);background:rgba(184,92,56,.05);border-radius:0 4px 4px 0;padding:.75rem 1.05rem;margin:.9rem 0 .2rem}
.ko-spelling-note-label{font-family:'DM Sans',sans-serif;font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.13em;color:var(--accent);margin-bottom:.3rem}
.ko-spelling-note p{font-family:'Crimson Pro',Georgia,serif;font-size:.98rem;color:var(--ink-muted);line-height:1.55;margin:0}
</style>"""
st.markdown(CONV_CSS, unsafe_allow_html=True)
st.markdown(CONV_CSS_ADDITIONS, unsafe_allow_html=True)

st.markdown("""
<div class="conv-masthead">
    <div class="conv-masthead-eyebrow">Numeral Converter</div>
    <div class="conv-masthead-title">Koraga Numerals</div>
    <div class="conv-masthead-desc">Look up the numbers recorded for Koraga, a critically endangered Dravidian language of coastal Karnataka and Kerala. Only forms printed in a source are shown, each with its source; numbers that no source records are refused. Tulu, its neighbour, is given beside each for comparison.</div>
</div>
""", unsafe_allow_html=True)

language_nav("Koraga", "converter")


def rows_html(rows):
    return "".join(
        f'<div class="conv-result-row">'
        f'<span class="conv-result-sublabel">{label}</span>'
        f'<span class="conv-result-subvalue">{value}</span>'
        f"</div>"
        for label, value in rows
    )


def note_html(label, text):
    return (f'<div class="ko-note"><div class="ko-note-label">{label}</div>'
            f"<p>{text}</p></div>")


def error_html(msg):
    return f'<div class="conv-error-card"><p class="conv-error-text">{msg}</p></div>'


def form_html(form, mal, cite):
    ml = f'<span class="ko-ml">{mal}</span>' if mal else ""
    return f'<span class="ko-main">{form}</span>{ml} <span class="ko-muted">· {cite}</span>'


def tulu_html(n):
    """Tulu for comparison, or '' where the Tulu converter has no form."""
    try:
        kn, rom, src = Tulu.number_to_tulu(n), Tulu.tulu_romanised(n), Tulu.source_note(n)
    except (ValueError, TypeError):
        return ""
    return (f'<div class="ko-compare"><div class="ko-compare-label">Tulu, for comparison — not Koraga</div>'
            f'<span class="ko-kn">{kn}</span> <em>{rom}</em> '
            f'<span class="ko-muted">· {src}</span></div>')


def result_rows(n):
    rows = [(SOURCES[key][0], form_html(form, mal, cite)) for key, form, mal, cite in forms(n)]
    missing = missing_sources(n)
    if missing:
        rows.append(("Not recorded by", ", ".join(missing)))
    return rows


NOTES = {
    1: ("Mudu unji",
        "Bhat compares Mudu <em>unji</em> with Tulu <em>oñji</em> (1971, p. 90). Onti and Tappu "
        "have <em>onji</em>."),
    7: ("Seven in the dialects",
        "Bhat cites Kannada <em>e:ḷu</em> beside Onti <em>e:lɨ</em>, Tappu <em>e:rɨ</em> "
        "(p. 92) and Mudu <em>yo:ḷu</em> (p. 112)."),
    2: ("Three dialects, three words",
        "Onti <em>raḍḍɨ</em> is the same as Tulu <em>raḍḍɨ</em>, which Bhat cites beside it "
        "(p. 113), and Tappu <em>naḍḍɨ</em> is cross-referred to it. Mudu has <em>eyḍɨ</em>. "
        "Bhat (p. 2) explains that all Onti speakers are bilingual in Tulu and all Mudu speakers "
        "in Kannada, and that each dialect has followed its neighbour's sound changes and "
        "borrowed its words."),
    8: ("Three spellings in one handbook",
        "The Kerala handbook's Table 7 writes 8 as <em>enme</em> in Latin letters but എൺമ "
        "(<em>eṇma</em>) in Malayalam, and as <em>enma</em>, എൻമ, in 8,000 (pp. 107–108). Its "
        "word list has <em>eṇumma</em> (p. 166)."),
    11: ("Tappu p becomes h",
         "Bhat lists Tappu <em>hattonji</em> 11 and <em>hadra:ḍɨ</em> 12 beside Tulu "
         "<em>pattonji</em> and <em>padra:ḍɨ</em> (p. 42): in Tappu an initial <em>p</em> has "
         "become <em>h</em>, a change he notes also in the Kannada dialects."),
    12: ("Twelve in the dialects",
         "Bhat compares Tappu <em>hadra:ḍɨ</em> with Tulu <em>padra:ḍɨ</em> and Mudu "
         "<em>hanneyḍɨ</em> with Kannada <em>hanneraḍu</em> (p. 115). Sharma's Korra Koraga "
         "<em>pattɨrəɖɖɨ</em> is built from ten and two. The Kerala word list's "
         "<em>patRāḍu</em> is written പത്രാണ്ടു in Malayalam."),
    15: ("A row set aside",
         "The Kerala word list prints <em>patnāji</em> (or <em>patineni</em>) as 'fifteen' and "
         "<em>patinainu</em> as 'sixteen' (p. 167), though <em>āji</em> is six and <em>ainu</em> "
         "five. The two rows look swapped, so the converter uses neither."),
    16: ("A row set aside",
         "The Kerala word list prints <em>patinainu</em> as 'sixteen' and <em>patnāji</em> (or "
         "<em>patineni</em>) as 'fifteen' (p. 167), though <em>ainu</em> is five and <em>āji</em> "
         "six. The two rows look swapped, so the converter uses neither."),
    17: ("One word set aside",
         "The Kerala word list's row for 'seventeen' reads <em>patinenma/patinēḷu</em> (p. 167). "
         "Its Malayalam has only പതിനേളു, and <em>patinenma</em> is the list's word for 18, so "
         "only <em>patinēḷu</em> is shown."),
    13: ("As written",
         "Sharma writes <em>patti-</em> here where his other teens have <em>pattɨ-</em>; the "
         "form is shown as given."),
    18: ("pad- in 18 and 19",
         "Sharma's 18 and 19 begin with <em>pad-</em>, his 11 to 17 with <em>patt-</em>."),
    19: ("pad- in 18 and 19",
         "Sharma's 18 and 19 begin with <em>pad-</em>, his 11 to 17 with <em>patt-</em>."),
    50: ("Fifty to sixty",
         "In Bhat's Onti story a crowd is <em>onji ayva ajippa jana</em>, which he translates "
         "'some fifty to sixty people' (p. 58)."),
    60: ("Fifty to sixty",
         "In Bhat's Onti story a crowd is <em>onji ayva ajippa jana</em>, which he translates "
         "'some fifty to sixty people' (p. 58)."),
    90: ("Ninety with c-",
         "Sharma's <em>conpa</em> and the Kerala word list's <em>conuppa</em>, also written "
         "<em>soṇuppa</em>, begin with <em>c</em>; Brigel's Tulu has <em>soṇpa</em>."),
    300: ("The hundreds",
          "Only the Kerala word list records the hundreds from 200 to 900, each as a unit before "
          "<em>nūdu</em> (pp. 168–169), as in Tulu. No source shows how a hundred joins a smaller "
          "number, so 301 is refused."),
    500: ("Two spellings",
          "The word list has <em>aīṇudu</em> (p. 168). The handbook's examples of vowels have "
          "<em>aiņûdu</em> (p. 53), whose Malayalam spelling ഐനൂഡു (<em>ainūḍu</em>) marks a "
          "different consonant as retroflex."),
    1000: ("Thousand",
           "Sharma (1990) gives <em>caːwra</em>. The Kerala word list gives <em>cāiRam</em>, "
           "<em>onjisāiRam</em> or <em>sāviRa</em>, and its Table 7 gives <em>saavira</em>, the "
           "word D'Souza (2019) records for Tulu today. Brigel's Tulu of 1872 has <em>sāra</em>."),
}

SPELLING_NOTE = """
<div class="ko-spelling-note">
    <div class="ko-spelling-note-label">About the spellings: recorded forms only</div>
    <p>Koraga has no writing system or digits of its own. Each source spells it its own way:
    Sharma (1990) in IPA, Bhat (1971) in his romanisation, and the Kerala handbook (KIRTADS 2019)
    in Latin letters and Malayalam script. Every form is shown as printed. Only numbers a source
    records are given; none is built by pattern.</p>
</div>"""

EMPTY = '<div class="conv-empty-state"><p>Enter a value on the left to see the result.</p></div>'

arabic_input = ""
ko_input = ""

left_col, right_col = st.columns([1, 1], gap="large")

with right_col:
    st.markdown('<div class="conv-section-label conv-direction-label">Conversion Direction</div>',
                unsafe_allow_html=True)
    direction = st.radio(
        "Direction", ["Arabic → Koraga", "Koraga → Arabic"],
        horizontal=True, label_visibility="collapsed", key="ko_direction",
    )
    st.markdown(SPELLING_NOTE, unsafe_allow_html=True)

with left_col:
    st.markdown('<div class="conv-section-label">Preset Examples</div>', unsafe_allow_html=True)
    if direction == "Arabic → Koraga":
        presets = [1, 2, 7, 8, 12, 16, 20, 90, 300, 500, 1000, LAKH]
        st.markdown('<p class="conv-presets-sublabel">Click a value to load it</p>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, num in enumerate(presets):
            if cols[i % 4].button(grouped(num), key=f"p_a_{i}", use_container_width=True):
                st.session_state["ko_arabic_input"] = str(num)

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a number</div>
    <div class="conv-input-hint">Any whole number. Only the 45 numbers recorded in the sources are given: 1 to 20, the tens, the hundreds, 1,000, 4,000 to 10,000, and 1,00,000.</div>
</div>""", unsafe_allow_html=True)
        arabic_input = st.text_input(
            "Enter a number", key="ko_arabic_input",
            placeholder="e.g. 7", label_visibility="collapsed",
        )
    else:
        presets = ["oñji", "eyḍɨ", "yo:ḷu", "hattonji", "irwa", "cāiRam", "ഏളു", "lacca"]
        st.markdown('<p class="conv-presets-sublabel">Click a form to load it</p>', unsafe_allow_html=True)
        cols = st.columns(2)
        for i, form in enumerate(presets):
            if cols[i % 2].button(form, key=f"p_b_{i}", use_container_width=True):
                st.session_state["ko_word_input"] = form

        st.markdown('<div class="conv-section-label">Convert</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="conv-input-card">
    <div class="conv-input-title">Enter a Koraga numeral</div>
    <div class="conv-input-hint">As any source prints it: IPA (<em>eːlɨ</em>), Bhat's spelling (<em>yo:ḷu</em>), Latin letters (<em>eelu</em>) or Malayalam (ഏളു). Accents and length marks are optional.</div>
</div>""", unsafe_allow_html=True)
        ko_input = st.text_input(
            "Enter a Koraga numeral", key="ko_word_input",
            placeholder="e.g. eyḍɨ", label_visibility="collapsed",
        )

with right_col:
    if direction == "Arabic → Koraga":
        if arabic_input:
            n = None
            try:
                raw = arabic_input.strip().replace(",", "").replace(" ", "")
                negative = raw.startswith("-")
                digits = raw[1:] if negative else raw
                if not digits.isdecimal():
                    raise ValueError("Please enter a whole number.")
                # past any range the converter covers; avoids Python's limit on very long integers
                n = int(digits) if len(digits.lstrip("0")) <= 18 else 10 ** 18
                n = -n if negative else n
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">'
                    f'Koraga forms recorded for {grouped(n)}</div>'
                    f"{rows_html(result_rows(n))}</div>",
                    unsafe_allow_html=True,
                )
                if n in NOTES:
                    st.markdown(note_html(*NOTES[n]), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
            if n is not None and n > 0:
                st.markdown(tulu_html(n), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)
    else:
        if ko_input:
            try:
                readings = koraga_lookup(ko_input)
                n = readings[0][0]
                matched = "".join(f"<span class='ko-alt'>{label}</span>" for _, label in readings)
                matched_labels = {label.split(" · ")[0] for _, label in readings}
                others = "".join(
                    f"<span class='ko-alt'>{form_html(form, mal, cite)} "
                    f"<span class='ko-muted'>({SOURCES[key][0]})</span></span>"
                    for key, form, mal, cite in forms(n) if SOURCES[key][0] not in matched_labels
                )
                rows = [
                    ("Arabic numeral", f'<span class="ko-big">{grouped(n)}</span>'),
                    ("Recorded by", matched),
                ]
                if others:
                    rows.append(("Other sources", others))
                st.markdown(
                    f'<div class="conv-result-card"><div class="conv-result-label">Arabic numeral</div>'
                    f"{rows_html(rows)}</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(tulu_html(n), unsafe_allow_html=True)
            except ValueError as exc:
                st.markdown(error_html(exc), unsafe_allow_html=True)
        else:
            st.markdown(EMPTY, unsafe_allow_html=True)

    st.markdown("""
<div class="conv-caption">
Koraga forms as printed in D. N. S. Bhat's <em>The Koraga Language</em> (1971) for the Onti, Tappu
and Mudu dialects; in S. R. Sharma's list of Korra Koraga (1990) in Chan's <em>Numeral Systems of the
World's Languages</em>; and in KIRTADS's <em>Pasaru</em> handbook (2019) for the Koraga of Kerala,
in its Table 7 and its word list.
Tulu from J. Brigel's <em>A Grammar of the Tulu Language</em> (1872). Algorithm by Yi Zou.
</div>
""", unsafe_allow_html=True)

footer_nav("Koraga", "converter")
