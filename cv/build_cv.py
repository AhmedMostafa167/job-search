"""Build the CV as an ATS-friendly PDF (HTML -> Chromium) and DOCX from cv_content.py."""

import asyncio
import html
import importlib
import os
import sys
from pathlib import Path

# CV_MODULE selects a per-job variant (e.g. variants.arabic_ai); default is the base CV.
C = importlib.import_module(os.environ.get("CV_MODULE", "cv_content"))
STEM = getattr(C, "FILE_STEM", "Ahmed_Dorra_CV")

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
OUT.mkdir(parents=True, exist_ok=True)
e = html.escape


# ---------------------------------------------------------------- HTML / PDF
def link(text, url):
    return f'<a href="{e(url)}">{e(text)}</a>'


def build_html() -> str:
    contact = " · ".join(e(x) for x in C.CONTACT[:-1]) + " · " + link(C.CONTACT[-1], f"mailto:{C.CONTACT[-1]}")
    links_line = " · ".join(link(t, u) for t, u in C.LINKS)
    skills = "".join(f"<li><b>{e(k)}:</b> {e(v)}</li>" for k, v in C.SKILLS)

    projects = []
    for p in C.PROJECTS:
        links = " · ".join(link(t, u) for t, u in p["links"])
        bullets = "".join(f"<li>{e(b)}</li>" for b in p["bullets"])
        projects.append(
            f'<div class="item"><div class="row"><span><b>{e(p["name"])}</b> — {e(p["tagline"])}</span>'
            f'<span class="right">{links}</span></div>'
            f'<div class="stack">{e(p["stack"])}</div><ul>{bullets}</ul></div>'
        )

    exp = []
    for x in C.EXPERIENCE:
        bullets = "".join(f"<li>{e(b)}</li>" for b in x["bullets"])
        exp.append(
            f'<div class="item"><div class="row"><span><b>{e(x["role"])}</b> — {e(x["org"])}</span>'
            f'<span class="right">{e(x["dates"])}</span></div>{f"<ul>{bullets}</ul>" if bullets else ""}</div>'
        )

    pubs = "".join(
        f'<li><b>{e(p["title"])}</b> — {e(p["venue"])} ({e(p["date"])}) · {link(*p["link"])}</li>'
        for p in C.PUBLICATIONS
    )

    edu = []
    for x in C.EDUCATION:
        edu.append(
            f'<div class="item"><div class="row"><span><b>{e(x["degree"])}</b> — {e(x["org"])}</span>'
            f'<span class="right">{e(x["dates"])}</span></div><div class="detail">{e(x["detail"])}</div></div>'
        )

    training = "".join(f"<li>{e(t)}</li>" for t in C.TRAINING)

    def section(title, items):
        """Heading and first item stay on the same page; the rest may flow."""
        items = items if isinstance(items, list) else [items]
        return f'<div class="keep"><h2>{e(title)}</h2>{items[0]}</div>{"".join(items[1:])}'

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{e(C.NAME)} — CV</title>
<style>
  @page {{ size: A4; margin: 13mm 14mm; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: 10.4pt; line-height: 1.32;
         color: #111; margin: 0; }}
  a {{ color: #111; text-decoration: none; white-space: nowrap; }}
  h1 {{ font-size: 21pt; margin: 0; letter-spacing: .2px; }}
  .title {{ font-size: 11.5pt; font-weight: bold; color: #1f3a68; margin: 1px 0 3px; }}
  .contact {{ font-size: 9.6pt; }}
  h2 {{ font-size: 11pt; text-transform: uppercase; letter-spacing: .6px; color: #1f3a68;
        border-bottom: 1px solid #1f3a68; margin: 9px 0 4px; padding-bottom: 1px; }}
  p {{ margin: 0; }}
  ul {{ margin: 1px 0 0 0; padding-left: 15px; }}
  li {{ margin: 0 0 1.5px 0; }}
  ul.plain {{ padding-left: 15px; }}
  .item, .keep {{ margin-bottom: 5px; break-inside: avoid; }}
  .keep > .item {{ margin-bottom: 0; }}
  .row {{ display: flex; justify-content: space-between; gap: 10px; }}
  .right {{ white-space: nowrap; font-size: 9.6pt; }}
  .stack {{ font-size: 9.4pt; font-style: italic; color: #333; }}
  .detail {{ font-size: 10pt; }}
  .cols {{ columns: 2; column-gap: 18px; }}
</style></head>
<body>
<h1>{e(C.NAME)}</h1>
<div class="title">{e(C.TITLE)}</div>
<div class="contact">{contact}</div>
<div class="contact">{links_line}</div>

{section("Summary", f"<p>{e(C.SUMMARY)}</p>")}
{section("Skills", f'<ul class="plain">{skills}</ul>')}
{section("Projects", projects)}
{section("Experience", exp)}
{section("Publications", f'<ul class="plain">{pubs}</ul><p class="detail">ORCID: {link(*C.ORCID)}</p>')}
{section("Education", edu)}
{section("Training", f'<ul class="plain">{training}</ul>')}
{section("Languages", f"<p>{e(C.LANGUAGES)}</p>")}
</body></html>"""


async def build_pdf(html_path: Path, pdf_path: Path):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        exe = "/opt/pw-browsers/chromium"
        browser = await p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
        page = await browser.new_page()
        await page.goto(html_path.resolve().as_uri())
        await page.pdf(path=str(pdf_path), format="A4", print_background=True, prefer_css_page_size=True)
        await browser.close()


# ---------------------------------------------------------------- DOCX
def build_docx(path: Path):
    from docx import Document
    from docx.enum.text import WD_TAB_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.opc.constants import RELATIONSHIP_TYPE as RT
    from docx.oxml.ns import qn
    from docx.shared import Mm, Pt, RGBColor

    NAVY = RGBColor(0x1F, 0x3A, 0x68)
    doc = Document()
    sec = doc.sections[0]
    sec.page_height, sec.page_width = Mm(297), Mm(210)
    sec.top_margin = sec.bottom_margin = Mm(13)
    sec.left_margin = sec.right_margin = Mm(14)
    right_tab = sec.page_width - sec.left_margin - sec.right_margin

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.08

    def para(text="", bold=False, size=None, color=None, italic=False, after=0, before=0):
        p = doc.add_paragraph()
        if text:
            r = p.add_run(text)
            r.bold, r.italic = bold, italic
            if size:
                r.font.size = Pt(size)
            if color:
                r.font.color.rgb = color
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.space_before = Pt(before)
        return p

    def hyperlink(p, text, url, size=None):
        h = OxmlElement("w:hyperlink")
        h.set(qn("r:id"), p.part.relate_to(url, RT.HYPERLINK, is_external=True))
        r, rPr, t = OxmlElement("w:r"), OxmlElement("w:rPr"), OxmlElement("w:t")
        if size:
            sz = OxmlElement("w:sz")
            sz.set(qn("w:val"), str(int(size * 2)))
            rPr.append(sz)
        t.text = text
        t.set(qn("xml:space"), "preserve")
        r.append(rPr)
        r.append(t)
        h.append(r)
        p._p.append(h)

    def links(p, pairs, size=None, sep=" · "):
        for i, (text, url) in enumerate(pairs):
            if i:
                rr = p.add_run(sep)
                if size:
                    rr.font.size = Pt(size)
            hyperlink(p, text, url, size)

    def heading(text):
        p = para(text.upper(), bold=True, size=11, color=NAVY, before=8, after=3)
        p.paragraph_format.keep_with_next = True
        pPr = p._p.get_or_add_pPr()
        bdr = OxmlElement("w:pBdr")
        bottom = OxmlElement("w:bottom")
        for k, v in (("w:val", "single"), ("w:sz", "6"), ("w:space", "1"), ("w:color", "1F3A68")):
            bottom.set(qn(k), v)
        bdr.append(bottom)
        pPr.append(bdr)

    def row(left_bold, left_rest, right=None, right_links=None):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.tab_stops.add_tab_stop(right_tab, WD_TAB_ALIGNMENT.RIGHT)
        p.paragraph_format.space_before = Pt(3)
        r = p.add_run(left_bold)
        r.bold = True
        if left_rest:
            p.add_run(f" — {left_rest}")
        if right:
            rr = p.add_run(f"\t{right}")
            rr.font.size = Pt(9.5)
        if right_links:
            p.add_run("\t")
            links(p, right_links, size=9.5)
        return p

    def bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(1)
        if bold_prefix:
            p.add_run(bold_prefix).bold = True
        p.add_run(text)

    para(C.NAME, bold=True, size=21)
    para(C.TITLE, bold=True, size=11.5, color=NAVY, after=2)
    para(" · ".join(C.CONTACT), size=9.5)
    links(para(after=2), C.LINKS, size=9.5)

    heading("Summary")
    para(C.SUMMARY)

    heading("Skills")
    for k, v in C.SKILLS:
        bullet(v, bold_prefix=f"{k}: ")

    heading("Projects")
    for p in C.PROJECTS:
        row(p["name"], p["tagline"], right_links=p["links"])
        para(p["stack"], italic=True, size=9.5).paragraph_format.keep_with_next = True
        for b in p["bullets"]:
            bullet(b)

    heading("Experience")
    for x in C.EXPERIENCE:
        row(x["role"], x["org"], x["dates"])
        for b in x["bullets"]:
            bullet(b)

    heading("Publications")
    for p in C.PUBLICATIONS:
        bullet(f" — {p['venue']} ({p['date']}) · {p['link'][0]}", bold_prefix=p["title"])
    links(para("ORCID: ", size=10), [C.ORCID], size=10)

    heading("Education")
    for x in C.EDUCATION:
        row(x["degree"], x["org"], x["dates"])
        para(x["detail"], size=10)

    heading("Training")
    for t in C.TRAINING:
        bullet(t)

    heading("Languages")
    para(C.LANGUAGES)

    doc.core_properties.author = C.NAME
    doc.core_properties.title = f"{C.NAME} — CV"
    doc.save(path)


if __name__ == "__main__":
    html_path = OUT / f"{STEM}.html"
    html_path.write_text(build_html(), encoding="utf-8")
    asyncio.run(build_pdf(html_path, OUT / f"{STEM}.pdf"))
    build_docx(OUT / f"{STEM}.docx")
    print("built", *sorted(p.name for p in OUT.iterdir()))
