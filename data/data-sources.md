# Data sources and provenance

All figures in the manuscript are traceable to the sources below. Values in `data/*.csv` were transcribed by hand from these documents. Rights in the underlying data belong to IIE, NAFSA and the other publishers named here; the package licence does not override them, and any reuse should carry the attribution given below.

Data current as of **November 17, 2026**.

Two status markers are used throughout. **They record what the author of this note did, not an independent audit.** Each one should be re-derived by whoever submits the paper:

- **[checked]** — the figure was read in the document cited, by the author of this note.
- **[secondary]** — the figure comes from reporting or from a summary document rather than from the instrument itself.

Where a marker and the text disagree, the text is right and the marker is stale.

## `data/iie_fall_2026_snapshot.csv` and `data/reasons_for_decline.csv`

IIE, *Fall 2026 Snapshot on International Student Enrollment: Key Findings* (November 2026). https://opendoorsdata.org/wp-content/uploads/2026/11/IIE_Fall-Snapshot_2026_Key-Findings_2026.pdf

Every figure in this section comes from this one PDF. The distinction drawn below is not between documents but between which parts of it were re-read carefully: the headline changes were, the institutional-response shares were not.

- Survey of **809 institutions**, conducted by IIE with ten partner higher-education associations; academic year 2026/27; a subset of the nearly 3,000 institutions surveyed for Open Doors. **[checked]**
- Year-over-year changes as reported (rounded by IIE): total including OPT −9%; new enrollments −15%; undergraduate −3%; graduate −15%; OPT −6%. **[checked]**
- Reasons for decline (Table 4, Figure 2): visa process 88%, travel restrictions 70%, students enrolling in other countries 60%, costs 45%. Base is institutions reporting a decline in new enrollments; multiple answers allowed, so shares do not sum to 100%. **[secondary — same PDF, not re-read line by line]**
- The size of the base (n) is not reported in the document used here. The manuscript says so in the Figure 2 note and does not describe the base as "809 institutions".
- Section 5 also uses: 95% (students likely to consider other countries if OPT were limited), 81% (recruitment a priority), 91% / 99% (STEM priority), and the recruitment-target country lists. **[secondary — same PDF, not re-read line by line]** The text flags them as coming from the summary.

## `data/open_doors_totals.csv`

| Academic year | Total | Change | Source |
|---|---|---|---|
| 2022/23 | 1,057,018 | +12% | Open Doors 2023 |
| 2023/24 | 1,126,690 | +7% | Open Doors 2024 |
| 2024/25 | 1,177,766 | +5% | Open Doors 2025 (*Fast Facts*) |
| 2025/26 | 1,146,163 | −2.7% | Open Doors 2026, reported by Higher Ed Dive, 16.11.2026 |

- The series shows **three** consecutive years of growth (2022/23–2024/25), not four. **[checked]**
- The 2023/24 change is +7% in the paper (the rounded figure IIE publishes) and 6.6% in the CSV (the precise value). Neither is an error; do not mix them.
- The 2025/26 total comes from Open Doors 2026 as reported by Higher Ed Dive. **[secondary]** Check against the Open Doors 2026 release before submission.
- **The −17% new-enrollment fall in 2025/26** is from the IIE Fall 2025 Snapshot. A question was raised in review whether the correct figure is −17% or −18%, and it has not been resolved. The manuscript therefore describes the fall as "double-digit", gives 17% as the figure in the Fall 2025 Snapshot, and says the two have not been reconciled. **[secondary]**
- **The "approximately 6% of total U.S. higher education enrollment"** claim has been removed from Section 1. It could not be matched to a specific year: the source previously seen gave 6% for 2023/24, not 2024/25.

## `data/nafsa_economic_impact.csv`

| Academic year | Students | US$ bn | Jobs | Status |
|---|---|---|---|---|
| 2023/24 | 1,126,690 | 43.8 | 378,175 | NAFSA/JB International estimate |
| 2024/25 | 1,177,766 | 42.9 | 355,736 | NAFSA/JB International estimate |
| 2025/26 | 1,146,163 | 39.9 | 309,409 | NAFSA/JB International estimate |
| 2026/27 | 1,053,668 | 37.5 | 278,208 | NAFSA projection from the IIE Fall 2026 Snapshot |

- 2025/26 and 2024/25: NAFSA/JB International release of November 16, 2026. **[checked]** https://www.nafsa.org/about/about-nafsa/international-students-contributed-399-billion-us-economy-2025-2026-fall-2026
- 2023/24 and the 2026/27 projection: NAFSA, *Fall 2026 International Student Enrollment Snapshot and Economic Impact Overview.* **[checked]** https://www.nafsa.org/sites/default/files/media/document/Fall%202026%20International%20Student%20Enrollment%20Snapshot%20Economic%20Impact%20Overview%20FINAL_0.pdf
- Methodology: NAFSA, *The economic value of international student enrollment: Methodology* (2025) — one job per three international students. **[secondary — the 2025 methodology document was not read; the multiplier is taken from the 2022 version and from the 2026 releases that restate it]** It is an input assumption of the model, not an estimated parameter, and Section 6.1 says so. Verify by reading the 2025 document.
- The student totals include OPT participants; NAFSA states that its dollar and job estimates do not count students on OPT. Figure 3's note says the panels are therefore not ratios of one another.
- Scenario arithmetic in Section 6.2: the American Immigration Council range of $72–145bn over a decade is roughly $7–15bn a year, i.e. two to five times the $3.0bn annual measured decline. The manuscript no longer says "an order of magnitude".
- NAFSA is a plaintiff in the fixed-period litigation. Disclosed in the abstract, Section 4.2, Section 6.1, Section 9 and the Figure 3 note.

## Legal and regulatory documents

| Item | Status | Where |
|---|---|---|
| Fixed-period final rule, 17.07.2026 | **[checked]** publishing date and rule title | https://studyinthestates.dhs.gov/2026/07/dhs-publishes-final-rule-establishing-a-fixed-time-period-of-admission-and-an-extension-of ; FAQ: https://studyinthestates.dhs.gov/final-rule-establishing-a-fixed-time-period-of-admission-and-an-extension-of-stay-procedure-faq |
| Four-year cap, extension procedure | **[checked]** | same |
| Grace period cut from 60 to 30 days | **[secondary]** | agency FAQ as summarised; not re-read line by line |
| September 14, 2026 order, §705, "no rational connection" | **[secondary]** | BAL Immigration News |
| November 16, 2026 order, statutory ground, less burdensome alternatives, quotations | **[secondary — the order itself was not obtained]** | Kreighbaum, Bloomberg Law |
| Appeal not taken | **[unverified]** | The manuscript says the author is not aware of an appeal and that it has not been checked against the docket. Do not upgrade this to a positive statement without checking PACER. |
| "Duration of status remains in force" | **[inference]** | The manuscript states only that the rule was set aside before it took effect, and avoids "nationwide". |
| OPT fee NPRM, 91 FR 64566, 08.10.2026, $70,000 / $30,000 | **[checked]** | Federal Register |
| Comment period closed 09.11.2026 | **[secondary]** | not confirmed on regulations.gov |
| Comment count 3,473 | **[unverified — removed from the text]** | |
| Opponents: AAU, NAFSA, Chamber, EPI | **[secondary]** comment letters cited, but the Chamber entry has a title mismatch — its page is headed "$70,000/$100,000" while the rule sets $70,000/$30,000; the reference now carries a neutral title and a note | |
| Opponents: ACE, AAMC, Columbia, EIG | **[secondary]** | named in reporting, not cited to filings; the text says so and the argument does not rest on them |
| CPT broadcast messages 2608-01 / 2608-02, Aug 12 and 24 | **[secondary]** | AAU and NAFSA resource pages |
| "More than 35 years" of the prior CPT interpretation | **[secondary]** | AAU/NAFSA characterisation |
| CPT litigation, 1:26-cv-14520; hearing 06.11.2026 | **[secondary]** | AAU, NAFSA, Bloomberg Law |
| SEVIS terminations: ~5,000 students, 3,000+ visa revocations, 65+ suits | **[secondary]** | American Immigration Council; Inside Higher Ed |
| "Termination authority not judicially foreclosed" | **[removed as a legal conclusion]** | replaced by a statement about what the account relied on does and does not establish |

Two cases, not one: **1:26-cv-13799** is the fixed-period rule; **1:26-cv-14520** is the CPT broadcast messages.

## What to verify before submission

Ranked by how much a referee is likely to care.

1. **The November 16 order** (PACER, docket 1:26-cv-13799). Confirm the statutory holding, replace the three quotations, check whether an appeal has been filed, and update Section 4.2 and Section 9. If the statutory ground turns out to be a remark inside the arbitrary-and-capricious analysis rather than an independent holding, change "on statutory grounds" in the abstract, Table 3 and Section 9.
2. **The Open Doors 2026 total** of 1,146,163 and −2.7%, currently via Higher Ed Dive.
3. **The 17% / 18% question** for new enrollments in 2025/26. If one of the two is right, replace the hedging sentence in Section 3.2 with the correct figure.
4. **Snapshot summary statistics**: 88/70/60/45, 95, 81, 91, 99 and the country lists. All are in the same key-findings PDF as the headline changes; ten minutes with the document closes them, and they can then be re-marked as checked.
5. **Whether the Snapshot or any IIE product reports enrollment by program length** (or by doctoral versus master's versus non-degree). Section 8 rests on the claim that the public release does not, and on the consequence that the program-length comparison must be requested from institutions. If IIE does publish such a breakdown, §8 needs a sentence saying where.
6. **Comment period close date** (09.11) and **CPT hearing date** (06.11).
7. **Grace period 60 → 30 days** in the final rule.
8. **NAFSA methodology, 2025 version** — read it for the OPT treatment and the job multiplier rather than relying on the 2022 version.
9. **The Chamber letter title** — the page heading says $70,000/$100,000 while the rule sets $30,000 for a subsequent recommendation. Decide whether to cite the page as titled or use the neutral title now in the reference list.

## Caveats that travel with the data

- The Snapshot is a preliminary institutional survey, not a final national count. No weights, response history or confidence intervals are published in the key-findings document.
- The Snapshot reports change by level — undergraduate, graduate, OPT — and does not separate doctoral and research master's study from one-year master's and non-degree study. Section 8 depends on this: the program-length comparison it describes cannot be built from the public series and has to be requested.
- NAFSA's 2026/27 figures are projections by an organisation that is a party to one of the cases discussed, and its estimates have been revised between releases.
- Claims by party organisations about the harm of a rule are self-reports and are treated as such.
