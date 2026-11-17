"""
Build the manuscript deliverables from paper/policy-research-paper.md.

  python analysis/build.py

Writes, into paper/:
  policy-research-paper.docx  - Word version (fonts: Times New Roman / Cambria, A4)
  policy-research-paper.pdf   - PDF version (DejaVu fonts, registered from assets/fonts)

Run it from anywhere; paths are derived from this file's location.

The Markdown used in ARTICLE.md is a small subset: "## " and "### " headings,
blank-line-separated paragraphs, pipe tables with a header row, "![..](path)"
images, "\\newpage", and inline **bold**, *italic* and `code`.
"""
import pathlib
import re
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent  # repository root
MD = (ROOT / "paper" / "policy-research-paper.md").read_text(encoding="utf-8").replace("../figures/", "figures/")

TITLE_BLOCK_PARAS = 3          # author / affiliation / date lines before Abstract


# --------------------------------------------------------------- parsing
def parse(md):
    """Return a list of blocks: (kind, payload)."""
    blocks = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.strip() == r"\newpage":
            blocks.append(("pagebreak", None))
            i += 1
            continue
        if line.startswith("### "):
            blocks.append(("h3", line[4:].strip()))
            i += 1
            continue
        if line.startswith("## "):
            blocks.append(("h2", line[3:].strip()))
            i += 1
            continue
        if line.startswith("# "):
            blocks.append(("h1", line[2:].strip()))
            i += 1
            continue
        m = re.match(r"!\[(.*?)\]\((.*?)\)", line.strip())
        if m:
            blocks.append(("image", (m.group(2), m.group(1))))
            i += 1
            continue
        if line.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                raw = lines[i].strip().strip("|")
                cells = [c.strip() for c in raw.split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows))
            continue
        # paragraph: consume until blank line or a block starter
        buf = [line.strip()]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            if (not nxt.strip() or nxt.lstrip().startswith("|")
                    or nxt.startswith("#") or nxt.strip() == r"\newpage"
                    or nxt.lstrip().startswith("![")):
                break
            buf.append(nxt.strip())
            i += 1
        blocks.append(("p", " ".join(buf)))
    return blocks


BLOCKS = parse(MD)

# The three lines after the title are the author block.
title = None
author_block = []
rest = []
seen_title = False
for kind, payload in BLOCKS:
    if kind == "h1" and not seen_title:
        title = payload
        seen_title = True
        continue
    if seen_title and kind == "p" and len(author_block) < TITLE_BLOCK_PARAS:
        author_block.append(payload)
        continue
    rest.append((kind, payload))
BLOCKS = rest


# ----------------------------------------------------------- inline markup
def segments(text):
    """Split text into (style, chunk) pairs; style in {'', 'b', 'i', 'code'}."""
    out = []
    pattern = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`)")
    for part in pattern.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            out.append(("b", part[2:-2]))
        elif part.startswith("*") and part.endswith("*"):
            out.append(("i", part[1:-1]))
        elif part.startswith("`") and part.endswith("`"):
            out.append(("code", part[1:-1]))
        else:
            out.append(("", part))
    return out


def plain(text):
    return "".join(c for _, c in segments(text))


def column_widths(rows, avail):
    """Allocate table column widths from content.

    Each column gets a share of the available width proportional to its longest
    cell, but never less than the width of its longest single word (so words are
    not split) and never more than the width its content can use.
    """
    from reportlab.pdfbase import pdfmetrics

    ncols = max(len(r) for r in rows)
    size = 8.6
    pad = 9.0                      # left+right padding and a little slack
    longest = [0.0] * ncols        # widest word per column
    typical = [0.0] * ncols        # longest full cell per column
    for row in rows:
        for ci in range(ncols):
            cell = plain(row[ci]) if ci < len(row) else ""
            if not cell:
                continue
            longest[ci] = max(longest[ci], max(
                pdfmetrics.stringWidth(w, "Serif", size) for w in cell.split()))
            typical[ci] = max(typical[ci], pdfmetrics.stringWidth(cell, "Serif", size))

    mins = [w + pad for w in longest]
    wants = [min(w + pad, avail) for w in typical]
    widths = list(wants)
    # shrink proportionally if too wide; grow the last columns if too narrow
    for _ in range(40):
        total = sum(widths)
        if abs(total - avail) < 1.0:
            break
        if total > avail:
            excess = total - avail
            reducible = [max(0.0, w - mn) for w, mn in zip(widths, mins)]
            pool = sum(reducible)
            if pool <= 0:
                break
            widths = [w - excess * r / pool for w, r in zip(widths, reducible)]
        else:
            deficit = avail - total
            slack = [max(0.0, want - w) + 1.0 for w, want in zip(widths, wants)]
            pool = sum(slack)
            widths = [w + deficit * s / pool for w, s in zip(widths, slack)]
    scale = avail / sum(widths) if sum(widths) > avail else 1.0
    return [w * scale for w in widths]


# ------------------------------------------------------------------- DOCX
def build_docx(path):
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor

    BODY_FONT, HEAD_FONT = "Times New Roman", "Cambria"
    INK = RGBColor(0x1A, 0x1A, 0x1A)
    MUTED = RGBColor(0x55, 0x5A, 0x62)

    doc = Document()
    for s in doc.sections:
        s.page_height, s.page_width = Cm(29.7), Cm(21.0)
        s.top_margin = s.bottom_margin = Cm(2.5)
        s.left_margin = s.right_margin = Cm(2.5)

    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(11)
    normal.font.color.rgb = INK
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    pf = normal.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(6)
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = 1.3
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    def set_font(run, name=BODY_FONT, size=11, bold=False, italic=False, color=INK):
        run.font.name = name
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color
        run._element.rPr.rFonts.set(qn("w:eastAsia"), name)

    # Real Word styles for headings, so the navigation pane, the outline level and
    # any style-based reformatting by an editor keep working. Run-level formatting
    # is applied on top, so the appearance does not depend on the style defaults.
    for st_name, st_size in (("Heading 1", 17), ("Heading 2", 13), ("Heading 3", 11.5)):
        st = doc.styles[st_name]
        st.font.name = HEAD_FONT
        st.font.size = Pt(st_size)
        st.font.bold = True
        st.font.color.rgb = INK
        st.font.italic = False
        rpr = st.element.get_or_add_rPr()
        rpr.rFonts.set(qn("w:eastAsia"), HEAD_FONT)
        st.paragraph_format.keep_with_next = True
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        st.paragraph_format.space_before = Pt(0)
        st.paragraph_format.space_after = Pt(6)

    def add_runs(par, text, size=11, base_bold=False, color=INK, font=BODY_FONT):
        for style, chunk in segments(text):
            run = par.add_run(chunk)
            set_font(run, name=font, size=size,
                     bold=base_bold or style == "b",
                     italic=style == "i",
                     color=color)
            if style == "code":
                run.font.name = "Consolas"
                run.font.size = Pt(size - 0.5)
        return par

    def para(text, size=11, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
             space_before=0, space_after=6, color=INK, indent=None, font=BODY_FONT):
        p = doc.add_paragraph()
        p.paragraph_format.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        if indent is not None:
            p.paragraph_format.left_indent = Cm(indent)
            p.paragraph_format.first_line_indent = Cm(-indent)
        add_runs(p, text, size=size, base_bold=bold, color=color, font=font)
        return p

    def rule(par, edge="bottom", size=6, color="999999"):
        pPr = par._p.get_or_add_pPr()
        borders = pPr.find(qn("w:pBdr"))
        if borders is None:
            borders = OxmlElement("w:pBdr")
            pPr.append(borders)
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(size))
        el.set(qn("w:space"), "4")
        el.set(qn("w:color"), color)
        borders.append(el)

    # ---- title block
    p = doc.add_paragraph(style="Heading 1")
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(10)
    p.paragraph_format.line_spacing = 1.12
    add_runs(p, title, size=17, base_bold=True, font=HEAD_FONT)

    name, affil, date = (author_block + ["", "", ""])[:3]
    p = para(name, size=11.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=1)
    p = para(affil, size=10, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=1, color=MUTED)
    p = para(date, size=10, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=10, color=MUTED)
    rule(p, "bottom", 8, "BBBBBB")

    in_refs = False
    caption_next = False
    for kind, payload in BLOCKS:
        if kind == "pagebreak":
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            continue
        if kind == "h1":
            continue
        if kind == "h2":
            in_refs = payload.strip().lower().startswith("reference")
            size = 10.5 if in_refs else 13
            p = doc.add_paragraph(style="Heading 2")
            p.paragraph_format.space_before = Pt(2 if in_refs else 14)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_runs(p, payload, size=size, base_bold=True, font=HEAD_FONT)
            if not in_refs:
                rule(p, "bottom", 4, "CCCCCC")
            continue
        if kind == "h3":
            p = doc.add_paragraph(style="Heading 3")
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_runs(p, payload, size=11.5, base_bold=True, font=HEAD_FONT)
            continue
        if kind == "image":
            src, _alt = payload
            p = doc.add_paragraph()
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            p.add_run().add_picture(str(ROOT / src), width=Cm(15.4))
            continue
        if kind == "table":
            rows = payload
            ncols = max(len(r) for r in rows)
            tbl = doc.add_table(rows=len(rows), cols=ncols)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl.autofit = True
            for ri, row in enumerate(rows):
                for ci in range(ncols):
                    cell = tbl.cell(ri, ci)
                    cell.text = ""
                    cp = cell.paragraphs[0]
                    cp.paragraph_format.space_before = Pt(3)
                    cp.paragraph_format.space_after = Pt(3)
                    cp.paragraph_format.line_spacing = 1.05
                    cp.paragraph_format.alignment = (
                        WD_ALIGN_PARAGRAPH.LEFT if ci == 0 else WD_ALIGN_PARAGRAPH.LEFT)
                    txt = row[ci] if ci < len(row) else ""
                    add_runs(cp, txt, size=9.5, base_bold=(ri == 0))
                    if ri == 0:
                        rule(cp, "bottom", 6, "666666")
                        for r in cp.runs:
                            r.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
                    elif ri == len(rows) - 1:
                        rule(cp, "bottom", 6, "666666")
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            continue
        # paragraphs
        text = payload
        is_caption = text.startswith("*Figure") or text.startswith("*Table")
        if in_refs:
            para(text, size=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=5, indent=0.8)
            continue
        if is_caption:
            para(text, size=9, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=10, color=MUTED)
            continue
        if text.startswith("*Data current"):
            para(text, size=9, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=4, color=MUTED)
            continue
        if text.startswith("*Keywords") or text.startswith("**Keywords"):
            para(text, size=10, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=3)
            continue
        if text.startswith("**JEL"):
            para(text, size=10, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=10)
            continue
        para(text)

    # footer page numbers
    footer = doc.sections[0].footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = fp.add_run()
    set_font(run, size=9, color=MUTED)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run._element.addnext(fld)

    doc.core_properties.title = plain(title)
    doc.core_properties.author = "David Ayupov"
    doc.core_properties.subject = ("International student enrollment, fall 2026, "
                                   "and U.S. federal regulatory developments")
    doc.core_properties.keywords = ("international students; F-1 visas; OPT; SEVIS; "
                                    "regulatory risk; student mobility")
    doc.save(str(path))


# -------------------------------------------------------------------- PDF
def build_pdf(path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, Frame, Image, PageTemplate,
                                    Paragraph, Spacer, Table, TableStyle, KeepTogether)

    fd = ROOT / "assets" / "fonts"
    pdfmetrics.registerFont(TTFont("Serif", str(fd / "DejaVuSerif.ttf")))
    pdfmetrics.registerFont(TTFont("Serif-Bold", str(fd / "DejaVuSerif-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Serif-Italic", str(fd / "DejaVuSerif-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("Serif-BoldItalic", str(fd / "DejaVuSerif-BoldItalic.ttf")))
    pdfmetrics.registerFont(TTFont("Sans", str(fd / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("Sans-Bold", str(fd / "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold",
                                  italic="Serif-Italic", boldItalic="Serif-BoldItalic")

    INK = colors.HexColor("#14171A")
    MUTED = colors.HexColor("#555A62")
    RULE = colors.HexColor("#BBBBBB")

    def style(name, **kw):
        base = dict(fontName="Serif", fontSize=10.2, leading=15.4, textColor=INK,
                    alignment=TA_JUSTIFY, spaceAfter=7)
        base.update(kw)
        return ParagraphStyle(name, **base)

    S = {
        "body": style("body"),
        "title": style("title", fontName="Sans-Bold", fontSize=16.5, leading=21,
                       alignment=TA_LEFT, spaceAfter=10),
        "author": style("author", fontName="Sans-Bold", fontSize=11, leading=15,
                        alignment=TA_LEFT, spaceAfter=2),
        "affil": style("affil", fontSize=9.5, leading=13, alignment=TA_LEFT,
                       spaceAfter=1, textColor=MUTED),
        "h2": style("h2", fontName="Sans-Bold", fontSize=12.5, leading=16,
                    alignment=TA_LEFT, spaceBefore=15, spaceAfter=6),
        "h3": style("h3", fontName="Sans-Bold", fontSize=10.8, leading=14.5,
                    alignment=TA_LEFT, spaceBefore=11, spaceAfter=4),
        "caption": style("caption", fontSize=8.6, leading=12.4, alignment=TA_LEFT,
                         spaceAfter=11, textColor=MUTED),
        "ref": style("ref", fontSize=8.8, leading=12.2, alignment=TA_LEFT,
                     spaceAfter=5, leftIndent=22, firstLineIndent=-22),
        "cell": style("cell", fontSize=8.6, leading=11.6, alignment=TA_LEFT, spaceAfter=0),
        "cellh": style("cellh", fontName="Sans-Bold", fontSize=8.6, leading=11.6,
                       alignment=TA_LEFT, spaceAfter=0, textColor=INK),
    }

    def md_inline(text):
        out = []
        for st, chunk in segments(text):
            esc = (chunk.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            if st == "b":
                out.append(f"<b>{esc}</b>")
            elif st == "i":
                out.append(f"<i>{esc}</i>")
            elif st == "code":
                out.append(f'<font name="Sans" size="9">{esc}</font>')
            else:
                out.append(esc)
        return "".join(out)

    frame = Frame(2.4 * cm, 2.2 * cm, A4[0] - 4.8 * cm, A4[1] - 4.4 * cm,
                  id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    def on_page(canvas, doc_):
        canvas.saveState()
        canvas.setFont("Sans", 8)
        canvas.setFillColor(MUTED)
        canvas.drawCentredString(A4[0] / 2, 1.35 * cm, str(canvas.getPageNumber()))
        canvas.restoreState()

    docu = BaseDocTemplate(str(path), pagesize=A4,
                           leftMargin=2.4 * cm, rightMargin=2.4 * cm,
                           topMargin=2.2 * cm, bottomMargin=2.2 * cm,
                           title=plain(title), author="David Ayupov",
                           subject="International student enrollment, fall 2026, and "
                                   "U.S. federal regulatory developments")
    docu.addPageTemplates([PageTemplate(id="std", frames=[frame], onPage=on_page)])

    story = [Paragraph(md_inline(title), S["title"])]
    if author_block:
        story.append(Paragraph(md_inline(author_block[0]), S["author"]))
    for line in author_block[1:]:
        story.append(Paragraph(md_inline(line), S["affil"]))
    story.append(Spacer(1, 6))

    avail = A4[0] - 4.8 * cm
    in_refs = False
    for kind, payload in BLOCKS:
        if kind == "pagebreak":
            from reportlab.platypus import PageBreak
            story.append(PageBreak())
            continue
        if kind == "h1":
            continue
        if kind == "h2":
            in_refs = payload.strip().lower().startswith("reference")
            story.append(Paragraph(md_inline(payload), S["h2"]))
            continue
        if kind == "h3":
            story.append(Paragraph(md_inline(payload), S["h3"]))
            continue
        if kind == "image":
            src, _alt = payload
            from reportlab.lib.utils import ImageReader
            iw, ih = ImageReader(str(ROOT / src)).getSize()
            w = avail
            story.append(Spacer(1, 8))
            story.append(Image(str(ROOT / src), width=w, height=w * ih / iw))
            continue
        if kind == "table":
            rows = payload
            ncols = max(len(r) for r in rows)
            data = []
            for ri, row in enumerate(rows):
                data.append([Paragraph(md_inline(row[ci] if ci < len(row) else ""),
                                       S["cellh"] if ri == 0 else S["cell"])
                             for ci in range(ncols)])
            widths = column_widths(rows, avail)
            t = Table(data, colWidths=widths, hAlign="LEFT", repeatRows=1)
            t.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("LINEBELOW", (0, 0), (-1, 0), 0.7, colors.HexColor("#666666")),
                ("LINEBELOW", (0, -1), (-1, -1), 0.7, colors.HexColor("#666666")),
            ]))
            caption = None
            if len(story) > 2 and isinstance(story[-1], Paragraph) \
                    and story[-1].style.name == "caption":
                caption = story.pop()
            story.append(Spacer(1, 4))
            # A short table keeps its caption and never breaks across pages. A
            # table too tall to fit comfortably on a page is allowed to break,
            # with its header row repeated, rather than leaving a half-empty page.
            _, t_height = t.wrap(avail, 10000)
            if t_height < (A4[1] - 6.5 * cm) * 0.75:
                story.append(KeepTogether([caption, t] if caption else [t]))
            else:
                if caption:
                    story.append(caption)
                story.append(t)
            story.append(Spacer(1, 9))
            continue
        text = payload
        if in_refs:
            # Put each URL on its own line: reportlab splits overlong words
            # at arbitrary characters, which can cut "https://" in half when
            # a URL begins near the end of a text line. Starting every URL
            # at the left indent keeps the protocol intact and the break,
            # when one is still needed, falls inside the path.
            markup = md_inline(text)
            for proto in ("https://", "http://"):
                markup = markup.replace(" " + proto, "<br/>" + proto)
            # Keep each entry whole: a URL tail stranded at the top of the
            # next page is worse than the white space this can leave.
            story.append(KeepTogether([Paragraph(markup, S["ref"])]))
        elif text.startswith("*Figure") or text.startswith("*Table") or text.startswith("*Data current"):
            story.append(Paragraph(md_inline(text), S["caption"]))
        elif text.startswith("**Keywords") or text.startswith("**JEL"):
            story.append(Paragraph(md_inline(text),
                                   style("kw", fontSize=9.2, leading=13, spaceAfter=4)))
        else:
            story.append(Paragraph(md_inline(text), S["body"]))

    docu.build(story)


if __name__ == "__main__":
    build_docx(ROOT / "paper" / "policy-research-paper.docx")
    print("docx ok")
    build_pdf(ROOT / "paper" / "policy-research-paper.pdf")
    print("pdf ok")
