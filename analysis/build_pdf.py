"""
Build the camera-ready PDF and DOCX versions of the paper.

Pipeline:
  Markdown (paper/policy-research-paper.md)
    -> pandoc -> standalone HTML (with academic CSS)
    -> WeasyPrint -> paper/policy-research-paper.pdf
  Markdown -> pandoc -> paper/policy-research-paper.docx

Usage:  python3 analysis/build_pdf.py
Requires: pandoc, weasyprint (pip install weasyprint)
"""

import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPER = ROOT / "paper" / "policy-research-paper.md"
CSS = ROOT / "analysis" / "paper.css"
HTML = ROOT / "paper" / "_paper_build.html"
PDF = ROOT / "paper" / "policy-research-paper.pdf"
DOCX = ROOT / "paper" / "policy-research-paper.docx"

TITLE = ("From Growth to Decline: Policy Uncertainty and International "
         "Student Enrollment in U.S. Higher Education")

CSS_TEXT = """
@page {
  size: A4;
  margin: 22mm 20mm 24mm 20mm;
  @bottom-center {
    content: counter(page) " / " counter(pages);
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt;
    color: #8a8f98;
  }
}
body {
  font-family: 'DejaVu Serif', Georgia, serif;
  font-size: 10pt;
  line-height: 1.52;
  color: #1c1f24;
  text-align: justify;
  hyphens: auto;
}
h1 {
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 17pt;
  line-height: 1.25;
  color: #1f3b73;
  text-align: left;
  margin: 0 0 6pt 0;
  padding-bottom: 8pt;
  border-bottom: 2.2pt solid #1f3b73;
}
h2 {
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 13pt;
  color: #1f3b73;
  margin: 18pt 0 6pt 0;
  text-align: left;
  page-break-after: avoid;
}
h3 {
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 11pt;
  color: #2a2f36;
  margin: 14pt 0 5pt 0;
  text-align: left;
  page-break-after: avoid;
}
p { margin: 0 0 8pt 0; }
a { color: #1f3b73; text-decoration: none; word-break: break-word; }
#title-block-header { display: none; }
figure { margin: 12pt 0 14pt 0; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; }
figcaption {
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 8.5pt;
  color: #555a61;
  text-align: left;
  line-height: 1.35;
  margin-top: 4pt;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 10pt 0 12pt 0;
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 8.6pt;
  page-break-inside: avoid;
}
th {
  background: #1f3b73;
  color: #ffffff;
  text-align: left;
  padding: 5pt 7pt;
  font-weight: bold;
}
td {
  border-bottom: 0.6pt solid #d5d9df;
  padding: 4.5pt 7pt;
  vertical-align: top;
}
tr:nth-child(even) td { background: #f4f6f9; }
blockquote {
  margin: 10pt 0;
  padding: 8pt 12pt;
  background: #f4f6f9;
  border-left: 2.5pt solid #1f3b73;
  font-size: 9.5pt;
}
code {
  font-family: 'DejaVu Sans Mono', monospace;
  font-size: 8.5pt;
  background: #f0f2f5;
  padding: 0 2pt;
}
hr { border: none; border-top: 0.75pt solid #c9ced6; margin: 14pt 0; }
#TOC {
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 9pt;
  background: #f4f6f9;
  padding: 10pt 14pt;
  margin: 0 0 14pt 0;
  page-break-after: always;
}
#TOC ul { list-style: none; padding-left: 12pt; margin: 2pt 0; }
#TOC > ul { padding-left: 0; }
#TOC li { margin: 1.5pt 0; }
#TOC a { color: #1c1f24; }
strong { color: #14213d; }
"""

def run(cmd, **kw):
    print("+", " ".join(str(c) for c in cmd))
    r = subprocess.run([str(c) for c in cmd], check=False, **kw)
    if r.returncode != 0:
        sys.exit(f"FAILED ({r.returncode}): {cmd}")

def main():
    CSS.write_text(CSS_TEXT, encoding="utf-8")
    paper_dir = ROOT / "paper"

    # Markdown -> HTML (run from paper/ so ../figures/... resolves)
    run(["pandoc", "policy-research-paper.md", "--from", "markdown+pipe_tables",
         "--to", "html5", "--standalone",
         "--toc", "--toc-depth", "2",
         "--metadata", f"title={TITLE}",
         "-o", "_paper_build.html"],
        cwd=paper_dir)

    # HTML -> PDF (WeasyPrint; base_url resolves ../figures from paper/)
    from weasyprint import HTML as WHTML, CSS as WCSS
    WHTML(filename=str(HTML)).write_pdf(
        str(PDF), stylesheets=[WCSS(string=CSS_TEXT, base_url=str(paper_dir))])
    print("PDF written:", PDF)

    # Markdown -> DOCX (run from paper/ so figures embed)
    run(["pandoc", "policy-research-paper.md", "--from", "markdown+pipe_tables",
         "--to", "docx", "--toc", "--toc-depth", "2",
         "-o", "policy-research-paper.docx"],
        cwd=paper_dir)
    print("DOCX written:", DOCX)

    HTML.unlink(missing_ok=True)  # temp file
    print("Done.")

if __name__ == "__main__":
    main()
