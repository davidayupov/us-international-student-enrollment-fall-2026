"""
Figure generation for "From Growth to Decline".

All values and category labels are read from the CSV files in DATA_DIR, so the
figures change if the data change. Annotations are positioned relative to the
data, not at fixed absolute coordinates.

  fig1 - year-over-year changes; y ticks every 5 points; colour intensity
         encodes the size of the decline.
  fig2 - horizontal bars ordered by share; wrapped note; n is not reported
         in the source material used.
  fig3 - three single-scale panels (no dual axis); the projection is a dashed
         segment ending in an open marker; no panel starts at zero, stated in
         the note.

Usage:  python make_figures.py
Reads data/ and writes figures/ at the repository root (the parent of
analysis/), so it runs the same whatever the working directory.
"""
import csv
import pathlib
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter, MultipleLocator

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Bundled fonts keep the output identical across machines. The lookup tries the
# package layout first and then a flat layout, so the script works whether it
# sits in the package root or in a subdirectory.
FONT_CANDIDATES = [ROOT / "assets" / "fonts"]
FONT_DIR = next((d for d in FONT_CANDIDATES if d.is_dir()), None)
if FONT_DIR is None:
    import warnings
    warnings.warn(
        "assets/fonts not found next to the script or one level up; figures "
        "will use the system default font and may differ between machines."
    )
else:
    for f in FONT_DIR.glob("DejaVu*.ttf"):
        font_manager.fontManager.addfont(str(f))

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.titlesize": 11, "axes.titleweight": "bold", "axes.labelsize": 9,
    "figure.dpi": 300, "savefig.dpi": 300,
})
NAVY, RED, MID, GRAY, MUTED, INK = "#1f3b73", "#b3372f", "#c96a4f", "#9aa0a8", "#5f646c", "#2b2f36"
MINUS = "−"


def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def signed(v, nd=0):
    s = f"{abs(v):.{nd}f}"
    return (MINUS + s) if v < 0 else s


def note(fig, text, width, x=0.008, y=0.008, size=7.5):
    fig.text(x, y, textwrap.fill(text, width), ha="left", va="bottom",
             fontsize=size, color=MUTED, linespacing=1.45)


# ---------------------------------------------------------------- Figure 1
rows = read_csv("iie_fall_2026_snapshot.csv")
SHORT = {
    "Total international students (incl. OPT)": "Total\n(incl. OPT)",
    "New international student enrollments": "New\nenrollments",
    "Undergraduate students": "Undergraduate",
    "Graduate students": "Graduate",
    "Optional Practical Training (OPT) participants": "OPT\nparticipants",
}
labels = [SHORT.get(r["category"], r["category"]) for r in rows]
values = [float(r["change_pct_2026_27"]) for r in rows]


def colour(v):
    d = -v                                    # size of the decline
    return NAVY if d <= 5 else (MID if d < 10 else RED)


fig, ax = plt.subplots(figsize=(7.2, 4.1))
bars = ax.bar(labels, values, color=[colour(v) for v in values], width=0.58,
              edgecolor="white", linewidth=0.6, zorder=2)
for b, v in zip(bars, values):
    ax.annotate(signed(v) + "%", (b.get_x() + b.get_width() / 2, v),
                xytext=(0, -5), textcoords="offset points",
                ha="center", va="top", fontsize=10.5, fontweight="bold", color=INK)
ax.set_ylim(min(values) - 3.5, 1.5)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: signed(y)))
ax.set_ylabel("Year-over-year change (%)")
ax.axhline(0, color="#333333", linewidth=0.9, zorder=3)
ax.grid(axis="y", linestyle=":", linewidth=0.6, color=GRAY, alpha=0.55, zorder=0)
ax.set_axisbelow(True)
ax.tick_params(axis="x", length=0, pad=6)
ax.set_title("International student enrollment change, fall 2026\n"
             "809 responding institutions, 2026/27 academic year (IIE Fall 2026 Snapshot)",
             fontsize=10.5)
note(fig, "Colour marks the size of the decline: dark blue = 5% or less; orange = more than 5% "
          "and less than 10%; red = 10% or more. All five are year-over-year changes among the 809 "
          "responding institutions, as reported (rounded) by IIE.", 104)
fig.tight_layout(rect=(0, 0.115, 1, 1))
fig.savefig(OUT / "fig1_enrollment_changes.png", bbox_inches="tight", facecolor="white")
plt.close(fig)

# ---------------------------------------------------------------- Figure 2
rows = sorted(read_csv("reasons_for_decline.csv"),
              key=lambda r: float(r["share_of_institutions_pct"]))
labels = [r["factor"] for r in rows]
values = [float(r["share_of_institutions_pct"]) for r in rows]

fig, ax = plt.subplots(figsize=(7.4, 3.8))
bars = ax.barh(labels, values, color=NAVY, height=0.52)
for b, v in zip(bars, values):
    ax.annotate(f"{v:.0f}%", (v, b.get_y() + b.get_height() / 2), xytext=(5, 0),
                textcoords="offset points", va="center", fontsize=10.5,
                fontweight="bold", color=INK)
ax.set_xlim(0, 100)
ax.set_xlabel("Share of institutions citing the factor (%)")
ax.set_title("Contributing factors cited by institutions reporting declines\n"
             "in new international student enrollments (IIE Fall 2026 Snapshot)", fontsize=10.5)
ax.grid(axis="x", linestyle=":", linewidth=0.6, color=GRAY, alpha=0.55)
ax.set_axisbelow(True)
ax.tick_params(axis="y", length=0)
note(fig, "Base: institutions that reported a decline in new international enrollments. Institutions "
          "could cite more than one factor, so shares do not sum to 100%. The shares are institutional "
          "attributions, not estimated effect sizes. The size of the base (n) is not reported in the "
          "source material used here.", 100)
fig.tight_layout(rect=(0, 0.155, 1, 1))
fig.savefig(OUT / "fig2_reasons_for_decline.png", bbox_inches="tight", facecolor="white")
plt.close(fig)

# ---------------------------------------------------------------- Figure 3
rows = read_csv("nafsa_economic_impact.csv")
years = [r["academic_year"].replace("-", "/") for r in rows]
students = [int(r["total_international_students"]) for r in rows]
dollars = [float(r["dollars_contributed_bn"]) for r in rows]
jobs = [int(r["jobs_supported"]) for r in rows]
x = list(range(len(years)))

panels = [
    ("International students in the U.S.", "Students (millions)",
     [v / 1e6 for v in students], lambda v: f"{v:.3f}", lambda v, _: f"{v:.2f}", "o"),
    ("Economic contribution", "U.S. dollars (billions)",
     dollars, lambda v: f"${v:.1f}B", lambda v, _: f"{v:.0f}", "s"),
    ("Jobs supported", "Jobs (thousands)",
     [v / 1e3 for v in jobs], lambda v: f"{v:.0f}k", lambda v, _: f"{v:.0f}", "^"),
]
fig, axes = plt.subplots(1, 3, figsize=(10.2, 3.9))
for ax, (title, ylabel, s, lab, tick, mk) in zip(axes, panels):
    ax.plot(x[:-1], s[:-1], marker=mk, color=NAVY, linewidth=2.0, markersize=5.5,
            label="Actual", zorder=3)
    ax.plot(x[-2:], s[-2:], linestyle=(0, (4, 2)), color=RED, linewidth=2.0,
            label="Projection", zorder=3)
    ax.plot([x[-1]], [s[-1]], marker=mk, markersize=7.5, markerfacecolor="white",
            markeredgecolor=RED, markeredgewidth=1.8, linestyle="none", zorder=4)
    ax.set_title(title, fontsize=10, pad=8)
    ax.set_ylabel(ylabel)
    ax.set_xlim(-0.25, len(x) - 0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(years, rotation=35, ha="right", fontsize=8)
    ax.grid(axis="y", linestyle=":", linewidth=0.6, color=GRAY, alpha=0.55)
    ax.set_axisbelow(True)
    ax.yaxis.set_major_formatter(FuncFormatter(tick))
    lo, hi = min(s), max(s)
    span = max(hi - lo, abs(hi) * 0.04)
    ax.set_ylim(lo - span * 0.75, hi + span * 0.65)
    ax.annotate(lab(s[-1]), (x[-1], s[-1]), xytext=(-3, -12), textcoords="offset points",
                ha="center", va="top", fontsize=8.5, color=RED, fontweight="bold")
axes[0].legend(frameon=False, fontsize=7.5, loc="lower left")
fig.suptitle("Economic footprint of international students in the U.S. "
             "(NAFSA / JB International, November 2026)", fontsize=11, fontweight="bold", y=0.99)
note(fig, "Dashed segments and open markers are NAFSA's projection for 2026/27, based on the IIE Fall "
          "2026 Snapshot; earlier years are NAFSA/JB International estimates. Each panel has its own "
          "vertical scale and none starts at zero. NAFSA states that its dollar and job estimates do not "
          "count students on OPT, whereas the student totals shown include them, so the panels are not "
          "ratios of one another. NAFSA is a plaintiff in the fixed-period litigation discussed in the "
          "paper.", 172, size=7)
fig.subplots_adjust(left=0.065, right=0.985, top=0.84, bottom=0.285, wspace=0.40)
fig.savefig(OUT / "fig3_economic_impact.png", bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"figures written to {OUT}")
