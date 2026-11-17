# From Growth to Decline: International Student Enrollment and Regulatory Risk in U.S. Higher Education

**A descriptive account of the Fall 2026 IIE Snapshot and the 2025–2026 federal regulatory landscape for F-1 students**

*Data current as of November 17, 2026*

---

## What this repository contains

A complete, reproducible policy research package analyzing the decline of international student enrollment in U.S. higher education and its regulatory context:

| Path | Contents |
|---|---|
| [`paper/policy-research-paper.md`](paper/policy-research-paper.md) | Full research paper (abstract, JEL codes, 9 sections, 29 references, embedded figures) |
| [`paper/policy-research-paper.pdf`](paper/policy-research-paper.pdf) | Camera-ready PDF (17 pages) |
| [`paper/policy-research-paper.docx`](paper/policy-research-paper.docx) | Word version for journal submission portals |
| [`paper/references.bib`](paper/references.bib) | BibTeX bibliography for journal submission workflows |
| [`data/`](data/) | Machine-readable datasets (CSV) with full provenance |
| [`data/data-sources.md`](data/data-sources.md) | Provenance of every figure in the paper, with per-item verification status |
| [`analysis/make_figures.py`](analysis/make_figures.py) | One-command reproduction of all figures |
| [`analysis/build.py`](analysis/build.py) | One-command rebuild of the PDF and DOCX from the Markdown source (pure Python: reportlab + python-docx) |
| [`figures/`](figures/) | Publication-ready charts (PNG, 300 dpi) |
| [`assets/fonts/`](assets/fonts/) | Bundled DejaVu fonts, so figures reproduce identically on any machine |
| [`SUBMISSION-GUIDE.md`](SUBMISSION-GUIDE.md) | Target journals, working-paper venues, and anticipated referee objections |
| [`COVER-LETTER.md`](COVER-LETTER.md) | Cover letter template for submission |
| [`REVIEWER-RESPONSES.md`](REVIEWER-RESPONSES.md) | Answers to likely reviewer questions, with pointers into the paper |
| [`LINKEDIN-POST.md`](LINKEDIN-POST.md) | Ready-to-publish summary post |

## Key findings

**Enrollment (IIE Fall 2026 Snapshot, 809 institutions, 2026/27 academic year):**

- Total international students (incl. OPT): **−9%**
- New international student enrollments: **−15%**
- Graduate students: **−15%** (vs. −3% undergraduate)
- OPT participants: **−6%**

This follows a 2.7% decline in 2025/26 (1,177,766 → 1,146,163 students), reversing three consecutive years of growth (2022/23–2024/25) that peaked at a record 1,177,766 students in 2024/25. Intake is falling about 1.7 times as fast as the total stock, so the aggregate is likely to keep falling unless intake recovers.

**Attribution (institutions reporting new-enrollment declines):** visa application process 88%, travel restrictions 70%, students enrolling in other countries 60%, costs 45%. These are institutional attributions, not estimated effect shares.

**Policy landscape as of November 17, 2026:**

| Measure | Status |
|---|---|
| 2025 SEVIS terminations (~5,000 F-1 students) | Largely reversed after 65+ lawsuits; limits of the termination power not settled |
| Fixed 4-year admission periods (final rule, Jul 17, 2026) | **Vacated** by D. Mass. (Nov 16, 2026) as arbitrary and capricious and contrary to statutory authority; government's appeal of the September injunction pending in the First Circuit |
| OPT fees ($70,000 / $30,000 per student) | Proposed rule only (91 FR 64566); comments closed Nov 9, 2026 |
| CPT narrowing (SEVP Broadcast Messages, Aug 2026) | **In effect**; preliminary-injunction hearing held Nov 6, 2026 |

**Economic footprint (NAFSA / JB International):** $39.9 billion contributed and 309,409 U.S. jobs supported in 2025/26 (down from $42.9B / 355,736 jobs in 2024/25); 2026/27 projection: $37.5 billion and 278,208 jobs. NAFSA is also a plaintiff in the fixed-period litigation; the paper treats its estimates as the work of an interested source and flags the projections as such.

## Central argument

The paper does not estimate the effect of any measure on enrollment. It documents the decline, reports what institutions attribute it to, and argues that the observed pattern — intake falling faster than the total, attribution to visa processing and travel, reported diversion to other destinations — is *consistent with* a response to regulatory risk: within eighteen months, every stage of the international student pathway (entry, retention, in-study work, post-graduation work) faced an adverse regulatory development. Sections 7 and 8 state explicitly what the survey cannot establish and what linked data (admissions funnels, a fixed institution panel, cross-destination comparison) causal identification would require.

## Reproducing the figures

```bash
pip install matplotlib
python3 analysis/make_figures.py
```

All three figures regenerate into `figures/` from the CSVs in `data/`, using the fonts bundled in `assets/fonts/`, so the output is identical across machines.

## Rebuilding the PDF / DOCX

```bash
pip install reportlab python-docx
python3 analysis/build.py
```

Rebuilds `paper/policy-research-paper.pdf` (typeset from the Markdown source with embedded figures and academic styling) and `paper/policy-research-paper.docx`.

## Data provenance

Every figure traces to a named primary or secondary source — IIE survey publications, Federal Register notices, DHS/SEVP documents, court records, and NAFSA economic analyses. [`data/data-sources.md`](data/data-sources.md) records, for each item, whether it was checked against the primary document, comes from secondary reporting, or remains unverified.

## Suggested citation

```bibtex
@techreport{ayupov2026decline,
  author      = {David Ayupov},
  title       = {From Growth to Decline: International Student Enrollment and Regulatory Risk in U.S. Higher Education},
  year        = {2026},
  month       = nov,
  url         = {https://github.com/davidayupov/us-international-student-enrollment-fall-2026}
}
```

## License

Text and figures: [CC BY 4.0](LICENSE). Code: MIT (see [`analysis/`](analysis/make_figures.py) header). Rights in the underlying data remain with IIE, NAFSA and the other publishers named in [`data/data-sources.md`](data/data-sources.md).

## AI disclosure

Generative AI tools were used to assist with collecting and organising source material, drafting and editing text, and writing the figure-generation code. The author reviewed all content, checked the cited sources where they could be accessed, and takes responsibility for the analysis and for any errors it contains. See the Declarations section of the paper.
