# Submission guide

Status of every legal statement in the manuscript: **November 17, 2026**. Anything dated later changes Section 4, Table 3 and Section 9.

## Before you submit, in this order

1. **Verify the flagged items** in `data-sources.md`, "What to verify before submission". Item 1 (the November 16 order) is the one a referee is most likely to check, because the abstract now says the court rested on statutory grounds.
2. **Author block and metadata.** The first page carries name and affiliation. Add email and ORCID in the journal's own form rather than in the PDF, so the published file does not carry contact details you would rather keep private.
3. **Journal-specific formatting.** Word counts, reference style, and any required structure. The manuscript is deliberately conservative: A4, Times New Roman / Cambria in the DOCX, numbered sections, author–date citations, no endnotes.
4. **AI-use form.** Many publishers now require a separate declaration beyond the paragraph in "Declarations". Check the policy before uploading, and keep the wording consistent with it.
5. **Rebuild if you change the text.** Edit `ARTICLE.md`, then run `python build.py` and `python make_figures.py`.

## Realistic route

The paper is a descriptive policy analysis: one survey wave, no causal identification, source base weighted toward agency documents, court reporting and sector organisations. In that form it is unlikely to clear peer review at a general-interest journal. The sequence that works:

1. **Working paper with a DOI** — SSRN, OSF Preprints or EdArXiv. This fixes priority and gives you a citable version. Post it before any social-media announcement.
2. **Sector outlets** — University World News, The PIE News, Inside Higher Ed, NAFSA's Trends & Insights. These take analytically framed pieces built on an underlying report, and they reach the audience that actually uses the numbers.
3. **Peer-reviewed journal**, after adding literature and, ideally, a second data point. A research note or policy brief is a more credible target than a full article.

## Journals, by fit

| Journal | Fit | What it would need |
|---|---|---|
| Journal of Studies in International Education (Sage) | Strongest topical fit | Literature review and a theoretical frame; engagement with the student-mobility scholarship |
| Journal of International Students (open access) | Good fit for a research note | Tighter scope; note the article-processing charge |
| International Migration (Wiley / IOM) | Migration-economics framing | Strengthen Section 6; treat the economic mechanism formally |
| Migration Studies (Oxford) | Migration-studies framing | Different publisher and audience; do not merge with the row above |
| Higher Education Quarterly | Finance and international recruitment | Expand the economic section, add institutional-finance data |
| Policy Futures in Education | Policy commentary | Check whether it takes non-empirical policy pieces |

Review times are not stated here because they could not be verified. Check each journal's own page.

## Anticipated referees' objections, and where the manuscript answers them

- **"This is advocacy."** Section 4 separates court outcomes from party self-reports, and the NAFSA conflict is disclosed four times: abstract, 4.2, 6.1, 9.
- **"809 institutions is not national data."** Section 2, Section 7.2 and obstacle two in Section 8.
- **"Where is the causal identification?"** Section 7.2 states the limits and Section 8 names the data and the two designs. The paper claims consistency, never an effect.
- **"Why one snapshot?"** Section 3.2 (intake falling faster than the stock) and Section 8's timing obstacle.
- **"The November ruling changes your story."** Section 7.1 states explicitly what the reading does *not* predict — that intake recovers in full once a rule is struck down, and an appeal is still possible — and Section 8 lists the segment-level data a program-length comparison would need, while stating that neither a differential nor a uniform recovery would settle the question.
- **"Where is your literature?"** Section 7.1 now cites Dixit and Pindyck (1994), Bloom (2009) and Gulen and Ion (2016) for irreversible investment under uncertainty. That is a thin frame, not a literature review, and the guide above says so: a sector outlet or a research note is a more realistic first target than a general-interest journal.
- **"Why call it regulatory risk rather than policy uncertainty?"** Because uncertainty is not measured here; what the data can support is a reading about perceived risk, and the title no longer claims more.
- **"Several numbers in §5 and §4 are not in your data files."** Correct: they come from the Snapshot summary or from reporting. Section 2 names the categories; `data-sources.md` marks each one with the author's own verification status, which you should re-check yourself rather than take on trust.

## Files to upload

- `manuscript.pdf` (review copy) and `manuscript.docx` (if the portal wants an editable file)
- `figures/fig1_enrollment_changes.png`, `fig2_reasons_for_decline.png`, `fig3_economic_impact.png` at 300 dpi
- `data/*.csv`, `make_figures.py`, `data-sources.md` as supplementary material, if the journal accepts a data package
- `submission/cover-letter.md`, filled in

## Do not upload

Anything containing chat transcripts, draft versions with placeholder text, or the strings "release v1.0.0" and repository links that do not resolve. If the repository release does not exist yet, leave the repository out of the cover letter entirely — the manuscript no longer promises one.
