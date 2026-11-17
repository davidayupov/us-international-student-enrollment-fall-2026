# From Growth to Decline: Policy Uncertainty and International Student Enrollment in U.S. Higher Education

**An evidence-based policy research study of the Fall 2026 IIE Snapshot and the 2025–2026 federal regulatory landscape for F-1 students**

*Data current as of November 17, 2026*

---

## What this repository contains

A complete, reproducible policy research package analyzing the sharp decline of international student enrollment in U.S. higher education and its regulatory context:

| Path | Contents |
|---|---|
| [`paper/policy-research-paper.md`](paper/policy-research-paper.md) | Full research paper (abstract, JEL codes, 8 sections, 26 primary references, embedded figures) |
| [`paper/policy-research-paper.pdf`](paper/policy-research-paper.pdf) | Camera-ready PDF (20 pages, typeset with academic styling) |
| [`paper/policy-research-paper.docx`](paper/policy-research-paper.docx) | Word version for journal submission portals |
| [`paper/references.bib`](paper/references.bib) | BibTeX bibliography for journal submission workflows |
| [`data/`](data/) | Machine-readable datasets (CSV) with full provenance |
| [`analysis/make_figures.py`](analysis/make_figures.py) | One-command reproduction of all figures |
| [`analysis/build_pdf.py`](analysis/build_pdf.py) | One-command rebuild of the PDF and DOCX from the Markdown source |
| [`figures/`](figures/) | Publication-ready charts (PNG, 200 dpi) |
| [`SUBMISSION-GUIDE.md`](SUBMISSION-GUIDE.md) | Target journals, working-paper venues, and a cover-letter template |
| [`LINKEDIN-POST.md`](LINKEDIN-POST.md) | Ready-to-publish LinkedIn summary post |

## Key findings

**Enrollment (IIE Fall 2026 Snapshot, 809 institutions, 2026/27 academic year):**

- Total international students (incl. OPT): **−9%**
- New international student enrollments: **−15%**
- Graduate students: **−15%** (vs. −3% undergraduate)
- OPT participants: **−6%**

This follows a 2.7% decline in 2025/26 (1,177,766 → 1,146,163 students), reversing four consecutive years of growth that peaked at a record 1,177,766 students in 2024/25.

**Attribution (institutions reporting new-enrollment declines):** visa application process 88%, travel restrictions 70%, students enrolling in other countries 60%, costs 45%.

**Policy landscape as of November 17, 2026:**

| Measure | Status |
|---|---|
| 2025 SEVIS terminations (~5,000 F-1 students) | Largely reversed after 65+ lawsuits; authority contested |
| Fixed 4-year admission periods (final rule, Jul 17, 2026) | **Vacated** by D. Mass. (Nov 16, 2026) as arbitrary and capricious |
| OPT fees ($70,000 / $30,000 per student) | Proposed rule only (91 FR 64566); comments closed Nov 9, 2026 |
| CPT narrowing (SEVP Broadcast Messages, Aug 2026) | **In effect**; preliminary injunction heard Nov 6, 2026 |

**Economic footprint (NAFSA / JB International):** $39.9 billion contributed and 309,409 U.S. jobs supported in 2025/26 (down from $42.9B / 355,736 jobs in 2024/25); 2026/27 projection: $37.5 billion and 278,208 jobs.

## Central argument

The decline is best understood not as a revealed preference against U.S. education but as a rational response to **lifecycle-spanning policy uncertainty**: within eighteen months, every stage of the international student pathway — entry (visas), retention (SEVIS, fixed admission periods), in-study work (CPT), and post-graduation work (OPT) — was hit by an adverse regulatory development. Intake is falling ~1.5x faster than the stock, which mechanically implies deeper aggregate declines in future years absent reversal.

## Reproducing the figures

```bash
pip install matplotlib
python3 analysis/make_figures.py
```

All three figures regenerate into `figures/` from the CSVs in `data/`. No other dependencies.

## Rebuilding the PDF / DOCX

```bash
pip install weasyprint   # plus a local pandoc installation
python3 analysis/build_pdf.py
```

Rebuilds `paper/policy-research-paper.pdf` (typeset from the Markdown source with embedded figures, table of contents, and academic styling) and `paper/policy-research-paper.docx`.

## Data provenance

Every figure traces to a primary source — IIE survey publications, Federal Register notices, DHS/SEVP documents, court records, and NAFSA economic analyses. Full source list with URLs: [`data/data-sources.md`](data/data-sources.md).

## Suggested citation

```bibtex
@techreport{ayupov2026decline,
  author      = {David Ayupov},
  title       = {From Growth to Decline: Policy Uncertainty and International Student Enrollment in U.S. Higher Education},
  year        = {2026},
  month       = nov,
  url         = {https://github.com/davidayupov/us-international-student-enrollment-fall-2026}
}
```

## License

Text and figures: [CC BY 4.0](LICENSE). Code: MIT (see [`analysis/`](analysis/make_figures.py) header).
