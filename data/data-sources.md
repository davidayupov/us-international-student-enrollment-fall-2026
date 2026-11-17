# Data sources and provenance

All figures in the manuscript are traceable to the sources below. Values in `data/*.csv` were transcribed by hand from these documents. Rights in the underlying data belong to IIE, NAFSA and the other publishers named here; the package licence does not override them, and any reuse should carry the attribution given below.

Data current as of **November 17, 2026**. On that date a second verification pass was made against primary documents: the two court orders of September 14 and November 16, 2026, the IIE Fall 2026 Snapshot key-findings PDF (read in full), and the Open Doors 2026 press release. Items previously marked [secondary] that were closed by that pass are marked **[checked]** below, with the document that closed them.

Two status markers are used throughout. **They record what the author of this note did, not an independent audit.** Each one should be re-derived by whoever submits the paper:

- **[checked]** — the figure was read in the document cited, by the author of this note.
- **[secondary]** — the figure comes from reporting or from a summary document rather than from the instrument itself.

Where a marker and the text disagree, the text is right and the marker is stale.

## `data/iie_fall_2026_snapshot.csv` and `data/reasons_for_decline.csv`

IIE, *Fall 2026 Snapshot on International Student Enrollment: Key Findings* (November 2026). https://opendoorsdata.org/wp-content/uploads/2026/11/IIE_Fall-Snapshot_2026_Key-Findings_2026.pdf

Every figure in this section comes from this one PDF, which was read in full on November 17, 2026.

- Survey of **809 institutions**, conducted by IIE with ten partner higher-education associations; academic year 2026/27; a subset of the nearly 3,000 institutions surveyed for Open Doors. **[checked]**
- Year-over-year changes as reported (rounded by IIE): total including OPT −9%; new enrollments −15%; undergraduate −3%; graduate −15%; OPT −6%. **[checked]**
- Reasons for decline (Table 4, Figure 2): visa process 88%, travel restrictions 70%, students enrolling in other countries 60%, costs 45%. Base is institutions reporting a decline in new enrollments; multiple answers allowed, so shares do not sum to 100%. **[checked]**
- The size of the base (n) is not reported in the key-findings document. The manuscript says so in the Figure 2 note and does not describe the base as "809 institutions". **[checked — the document was read in full and contains no n for this base]**
- Section 5 also uses: 95% (students likely to consider other countries if OPT were limited), 81% (recruitment a priority), 91% / 99% (STEM priority), and the recruitment-target country lists (undergraduate: Vietnam, India, Brazil; graduate: India, Vietnam, Nepal). **[checked]** The text cites them to the key-findings document.
- The key-findings document reports change by level — undergraduate, graduate, OPT — and contains no breakdown by program length or degree type. Section 8 rests on this absence. **[checked]**

## `data/open_doors_totals.csv`

| Academic year | Total | Change | Source |
|---|---|---|---|
| 2022/23 | 1,057,018 | +12% | Open Doors 2023 |
| 2023/24 | 1,126,690 | +7% | Open Doors 2024 |
| 2024/25 | 1,177,766 | +5% | Open Doors 2025 (*Fast Facts*) |
| 2025/26 | 1,146,163 | −2.7% | Open Doors 2026 press release (IIE), 16.11.2026 |

- The series shows **three** consecutive years of growth (2022/23–2024/25), not four. **[checked]**
- The 2023/24 change is +7% in the paper (the rounded figure IIE publishes) and 6.6% in the CSV (the precise value). Neither is an error; do not mix them.
- The 2025/26 total and change come from the Open Doors 2026 press release. The release rounds the fall to "3 percent"; the precise change from 1,177,766 to 1,146,163 is −2.7%, which is what the paper and the CSV use. **[checked]** https://opendoorsdata.org/wp-content/uploads/2026/11/Open-Doors-Data-Press-Release_2026.pdf
- **The new-enrollment fall in 2025/26** is 17% as first reported in the IIE Fall 2025 Snapshot and 18% (to 228,123) in the final Open Doors 2026 count. The manuscript now gives both, attributing each to its source; the discrepancy is an early-estimate versus final-count difference, not an unresolved conflict. **[checked]**
- Other Open Doors 2026 figures verified in the same press release and available if a referee asks: graduate enrollment 423,078 (−13%, driven by master's −22% and doctoral +3%); undergraduate 356,165 (−0.3%); OPT 335,785 (+14% in 2025/26). **[checked]**
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
| Grace period cut from 60 to 30 days | **[checked]** | the September 14 opinion describes the "reduction from a 60 to 30-day departure period" |
| September 14, 2026 order, §705, "no rational connection" | **[checked]** | opinion read in full; exact wording is "DHS failed to show that there is a rational connection between the Final Rule and its purported objectives of preventing fraud and furthering national security"; relief was nationwide; vacatur denied without prejudice. https://www.presidentsalliance.org/wp-content/uploads/2026/09/9.14.26-opinion-in-DS-case.pdf |
| November 16, 2026 order, vacatur, statutory ground, less burdensome alternatives, quotations | **[checked]** | order obtained and read in full; rule VACATED under APA §706 as "arbitrary, capricious, an abuse of discretion, and otherwise not in accordance with law"; independent statutory ground under 8 U.S.C. § 1101(a)(15)(F) ("contrary to statutory authority, as well as arbitrary and capricious, and may be vacated on that basis as well"); all quotations in Section 4.2 verified verbatim. https://www.presidentsalliance.org/wp-content/uploads/2026/11/2026-11-16-District-Judge-dckt-73_0.pdf |
| Appeal status | **[checked as of 17.11.2026]** | the government appealed the September 14 injunction to the First Circuit on 30.09.2026 (No. 26-2112) and moved on 03.11.2026 to hold the appeal in abeyance; the November 16 order states the appeal "remains pending as of this writing" and that it did not divest the district court of jurisdiction. No appeal of the November 16 judgment appears on the public record as of 17.11.2026; the docket itself was not independently checked on PACER. |
| "Duration of status remains in force" | **[inference]** | The rule was vacated before its effective date, so the prior framework was never replaced. The manuscript states only this and does not use "nationwide". |
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

Ranked by how much a referee is likely to care. Items 1–5 were closed by the verification pass of November 17, 2026 (see the markers above); they are listed here with their resolution so the history is visible.

1. **The November 16 order** — resolved. The order was obtained and read in full; the statutory holding is express and independent ("contrary to statutory authority, as well as arbitrary and capricious, and may be vacated on that basis as well"); all quotations in Section 4.2 are from the order itself; the abstract, Table 3 and Section 9 were updated accordingly.
2. **The Open Doors 2026 total** — resolved. 1,146,163 and −2.7% confirmed against the IIE press release of November 16, 2026 (which rounds the fall to 3 percent).
3. **The 17% / 18% question** — resolved. 17% is the Fall 2025 Snapshot estimate; 18% (to 228,123) is the final Open Doors 2026 count. The manuscript gives both with sources.
4. **Snapshot summary statistics** — resolved. 88/70/60/45, 95, 81, 91, 99 and the country lists verified against the key-findings PDF.
5. **Program-length breakdown** — resolved. The key-findings PDF, read in full, contains no breakdown by program length or degree type; Section 8's claim stands.
6. **Comment period close date** (09.11) and **CPT hearing date** (06.11). Still from secondary sources; both are plausible but unconfirmed against regulations.gov and the CPT docket.
7. **NAFSA methodology, 2025 version** — read it for the OPT treatment and the job multiplier rather than relying on the 2022 version.
8. **The Chamber letter title** — the page heading says $70,000/$100,000 while the rule sets $30,000 for a subsequent recommendation. Decide whether to cite the page as titled or use the neutral title now in the reference list.
9. **PACER docket check** — the appeal status above is taken from the November 16 order and contemporaneous reporting, not from an independent docket search. If the paper is submitted after further weeks pass, re-check whether the November 16 judgment has been appealed.

## Caveats that travel with the data

- The Snapshot is a preliminary institutional survey, not a final national count. No weights, response history or confidence intervals are published in the key-findings document.
- The Snapshot reports change by level — undergraduate, graduate, OPT — and, read in full, contains no breakdown by program length or degree type. Section 8 depends on this: the program-length comparison it describes cannot be built from the public series and has to be requested.
- NAFSA's 2026/27 figures are projections by an organisation that is a party to one of the cases discussed, and its estimates have been revised between releases.
- Claims by party organisations about the harm of a rule are self-reports and are treated as such.
