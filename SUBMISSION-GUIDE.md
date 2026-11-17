# Submission Guide

This document maps the paper to realistic publication venues and provides a cover-letter template.

## Before submitting

1. **Fill in the author block** in `paper/policy-research-paper.md` (name, affiliation, email, ORCID).
2. **Convert the paper** to the target venue's template. Most venues accept a Markdown/Word manuscript at initial submission; the bibliography in `paper/references.bib` imports cleanly into Zotero, Mendeley, and LaTeX (BibTeX) workflows.
3. **Regenerate figures** at the venue's required resolution: edit `analysis/make_figures.py` (`figure.dpi`) and rerun.
4. **Verify links** — court and regulatory statuses cited here are current as of November 17, 2026. Update Section 4 if new rulings issue (especially the CPT preliminary-injunction decision, which was under advisement as of writing, and any appeal of the November 16 vacatur).

## Venue shortlist

### Peer-reviewed journals (strong fit)

| Venue | Why it fits | Notes |
|---|---|---|
| **Journal of Studies in International Education** (Sage) | The flagship journal for exactly this topic; publishes policy analyses of enrollment trends | Refereed; expect 3–6 months |
| **Journal of International Students** | Fast-turnaround, open-access-friendly, publishes data-driven policy briefs | Strong fit for time-sensitive analysis |
| **International Migration** / **Migration Studies** (Oxford) | The policy-uncertainty framing fits their economics-of-migration angle | Reframe abstract toward migration economics |
| **Policy Futures in Education** | Accepts timely policy commentary with evidence | Faster than flagship journals |
| **Higher Education Quarterly** | UK-based, but covers international recruitment and finance | Emphasize the economic section |

### Working-paper / preprint routes (fast, strengthens the record)

- **SSRN** (International Education, Immigration Law, or Higher Education eJournals) — post as a working paper same-day; DOI issued.
- **OSF preprints** — free, DOI, versioned.
- **EdArXiv** — education-focused preprint server.

### Practitioner outlets (fast publication, wide readership)

- **University World News** / **The PIE News** — accept well-sourced analytical op-eds based on the paper.
- **NAFSA Trends & Insights** — perspective pieces from researchers.
- **Inside Higher Ed / Chronicle of Higher Education** — op-ed submissions.

### Suggested strategy

Post the SSRN preprint first (protects the timestamp and makes the work citable), then submit to the Journal of Studies in International Education or the Journal of International Students. Publish the LinkedIn summary (see `LINKEDIN-POST.md`) simultaneously — practitioner reach and academic citation are complements, not substitutes.

## Cover-letter template

> Dear Editors,
>
> I am pleased to submit my manuscript, "From Growth to Decline: Policy Uncertainty and International Student Enrollment in U.S. Higher Education — Evidence from the Fall 2026 IIE Snapshot," for consideration as a research article in [Journal].
>
> The paper provides, to my knowledge, the first integrated analysis of the fall 2026 enrollment data released by the Institute of International Education (a 9% total decline and 15% decline in new enrollments across 809 institutions) alongside the four federal regulatory developments that shaped the 2025–2026 environment for F-1 students: the SEVIS record terminations, the fixed-period-of-admission rule (vacated by a federal court on November 16, 2026), the proposed $70,000 OPT fee, and the contested narrowing of Curricular Practical Training.
>
> The contribution is threefold. First, a precise descriptive reading of the newest enrollment evidence with explicit attention to what each indicator measures. Second, a careful classification of each policy measure by its actual legal status — final, enjoined, vacated, or proposed — which public discussion routinely conflates. Third, an analytical framework (lifecycle-spanning policy uncertainty) that integrates enrollment data, institutional attributions, and economic projections while being explicit about the inferential limits of each evidence type.
>
> The analysis is fully reproducible: all datasets and figure-generation code are publicly archived at [repository URL].
>
> The manuscript is not under consideration elsewhere, and I have no conflicts of interest to disclose.
>
> Sincerely,
> [Name], [Affiliation]

## Reviewer-anticipation notes

Likely reviewer questions and where the paper already addresses them:

- *"Is this just advocacy?"* — Sections 4 and 7.2 explicitly separate court outcomes of record from party self-reports, and classify measures by legal status without endorsing any side.
- *"Survey of 809 institutions isn't national data."* — Section 2 and 7.2, point 2.
- *"Where's the causal identification?"* — Section 7.2 lists the four identification obstacles and Section 8 proposes the data linkage (applications → offers → enrollment → visa outcomes) that would support causal claims.
- *"Why should we care about one year's snapshot?"* — Sections 3.2 (intake falling faster than stock implies compounding) and 6 (quantified economic stakes).
