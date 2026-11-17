"""
Reproduce all figures for the paper
"From Growth to Decline: Policy Uncertainty and International Student
Enrollment in U.S. Higher Education" (Fall 2026).

Data sources: IIE Fall 2026 Snapshot, Open Doors, NAFSA/JB International
(see ../data/data-sources.md for full provenance and URLs).

Usage:  python3 analysis/make_figures.py
Output: figures/*.png
"""

import csv
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIGS = ROOT / "figures"
FIGS.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "figure.dpi": 200,
})

NAVY = "#1f3b73"
RED = "#b3372f"
GRAY = "#8a8f98"


def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------- Figure 1
# Enrollment change by category, Fall 2026 Snapshot
rows = read_csv("iie_fall_2026_snapshot.csv")
labels = ["Total\n(incl. OPT)", "New\nenrollments", "Undergraduate", "Graduate", "OPT\nparticipants"]
values = [float(r["change_pct_2026_27"]) for r in rows]

fig, ax = plt.subplots(figsize=(8.6, 4.6))
colors = [RED if v <= -10 else "#c96a4f" if v < -5 else NAVY for v in values]
bars = ax.bar(labels, values, color=colors, width=0.62)
for b, v in zip(bars, values):
    ax.text(b.get_x() + b.get_width() / 2, v - 0.7, f"{v:.0f}%",
            ha="center", va="top", fontsize=11, fontweight="bold",
            color="#333333")
ax.set_ylim(-17.5, 1.5)
ax.set_ylabel("Year-over-year change (%)")
ax.axhline(0, color="#333333", linewidth=0.8)
ax.set_title("International Student Enrollment Change, U.S. Institutions, Fall 2026\n"
             "(IIE Fall 2026 Snapshot, 809 institutions, 2026/27 academic year)",
             fontsize=11)
plt.tight_layout()
plt.savefig(FIGS / "fig1_enrollment_changes.png", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- Figure 2
# Factors cited by institutions reporting declines in new enrollments
rows = read_csv("reasons_for_decline.csv")
labels = [r["factor"] for r in rows][::-1]
values = [float(r["share_of_institutions_pct"]) for r in rows][::-1]

fig, ax = plt.subplots(figsize=(8.2, 4.2))
bars = ax.barh(labels, values, color=NAVY, height=0.55)
for b, v in zip(bars, values):
    ax.text(v + 1.2, b.get_y() + b.get_height() / 2, f"{v:.0f}%",
            va="center", fontsize=11, fontweight="bold", color="#333333")
ax.set_xlim(0, 100)
ax.set_xlabel("Share of institutions citing factor (%)")
ax.set_title("Contributing Factors Cited by Institutions Reporting Declines\n"
             "in New International Student Enrollments (IIE Fall 2026 Snapshot)",
             fontsize=11)
ax.grid(axis="x", linestyle=":", linewidth=0.6, color=GRAY, alpha=0.6)
plt.tight_layout()
plt.savefig(FIGS / "fig2_reasons_for_decline.png", bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- Figure 3
# Economic contribution trend with 2026/27 projection
rows = read_csv("nafsa_economic_impact.csv")
years = [r["academic_year"] for r in rows]
students = [int(r["total_international_students"]) for r in rows]
dollars = [float(r["dollars_contributed_bn"]) for r in rows]
jobs = [int(r["jobs_supported"]) for r in rows]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))

ax = axes[0]
ax.plot(years, students, marker="o", color=NAVY, linewidth=2.2, markersize=6)
ax.plot(years[-1], students[-1], marker="o", color=RED, markersize=8)
ax.set_title("International students in the U.S.", fontsize=11)
ax.set_ylabel("Students (incl. OPT)")
ax.grid(axis="y", linestyle=":", linewidth=0.6, color=GRAY, alpha=0.6)
ax.annotate("2026/27:\nprojection", xy=(3, students[-1]),
            xytext=(2.05, students[-1] - 62000), fontsize=9, color=RED,
            arrowprops=dict(arrowstyle="->", color=RED, lw=1))
ax.tick_params(axis="x", rotation=20)

ax = axes[1]
ax.plot(years, dollars, marker="s", color=NAVY, linewidth=2.2, markersize=6,
        label="Economic contribution ($bn)")
ax.plot(years[-1], dollars[-1], marker="s", color=RED, markersize=8)
ax.set_title("Economic contribution and jobs supported", fontsize=11)
ax.set_ylabel("U.S. dollars (billions)")
ax.grid(axis="y", linestyle=":", linewidth=0.6, color=GRAY, alpha=0.6)
ax2 = ax.twinx()
ax2.plot(years, [j / 1000 for j in jobs], marker="^", color=GRAY,
         linewidth=1.8, markersize=6, label="Jobs supported (thousands)")
ax2.set_ylabel("Jobs supported (thousands)", color=GRAY)
ax2.tick_params(axis="y", colors=GRAY)
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(GRAY)
ax.annotate("2026/27:\nprojection", xy=(3, dollars[-1]),
            xytext=(1.9, dollars[-1] - 2.6), fontsize=9, color=RED,
            arrowprops=dict(arrowstyle="->", color=RED, lw=1))
ax.tick_params(axis="x", rotation=20)

fig.suptitle("Economic Footprint of International Students in the U.S.\n"
             "(NAFSA / JB International, November 2026)", fontsize=12,
             fontweight="bold")
plt.tight_layout()
plt.savefig(FIGS / "fig3_economic_impact.png", bbox_inches="tight")
plt.close(fig)

print("Figures written to", FIGS)
for p in sorted(FIGS.glob("*.png")):
    print(" -", p.name)
