"""Build a one-page cover letter PDF, in the CV's style, from a variant's COVER_LETTER.

    cd cv && CV_MODULE=variants.<slug> python3 build_cover_letter.py ../out
"""

import asyncio

from build_cv import C, OUT, build_pdf, e, link

L = C.COVER_LETTER
STEM = C.FILE_STEM.replace("_CV_", "_Cover_Letter_")


def build_html() -> str:
    contact = " · ".join(e(x) for x in C.CONTACT[:-1]) + " · " + link(C.CONTACT[-1], f"mailto:{C.CONTACT[-1]}")
    links_line = " · ".join(link(t, u) for t, u in C.LINKS)
    to = "<br>".join(e(x) for x in L["to"])
    body = "".join(f"<p>{e(p)}</p>" for p in L["paragraphs"])
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{e(C.NAME)} — Cover Letter</title>
<style>
  @page {{ size: A4; margin: 16mm 18mm; }}
  body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: 11pt; line-height: 1.42;
         color: #111; margin: 0; }}
  a {{ color: #111; text-decoration: none; white-space: nowrap; }}
  h1 {{ font-size: 21pt; margin: 0; letter-spacing: .2px; }}
  .title {{ font-size: 11.5pt; font-weight: bold; color: #1f3a68; margin: 1px 0 3px; }}
  .contact {{ font-size: 9.6pt; }}
  .rule {{ border-bottom: 1px solid #1f3a68; margin: 8px 0 16px; }}
  .date {{ margin-bottom: 12px; }}
  .to {{ margin-bottom: 14px; }}
  p {{ margin: 0 0 10px; }}
  .sign {{ margin-top: 16px; }}
</style></head>
<body>
<h1>{e(C.NAME)}</h1>
<div class="title">{e(C.TITLE)}</div>
<div class="contact">{contact}</div>
<div class="contact">{links_line}</div>
<div class="rule"></div>
<div class="date">{e(L["date"])}</div>
<div class="to">{to}</div>
<p>{e(L["greeting"])}</p>
{body}
<div class="sign">{e(L.get("closing", "Sincerely,"))}<br><b>{e(C.NAME)}</b></div>
</body></html>"""


if __name__ == "__main__":
    html_path = OUT / f"{STEM}.html"
    html_path.write_text(build_html(), encoding="utf-8")
    asyncio.run(build_pdf(html_path, OUT / f"{STEM}.pdf"))
    print("built", f"{STEM}.pdf")
