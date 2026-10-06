"""Shared plotting style for every notebook in the project.

One seaborn theme, one categorical palette (fixed slot order, validated for
colour-vision deficiency), one sequential blue ramp, and a save helper that
writes 300-dpi PNGs to images/.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = PROJECT_ROOT / "images"
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

# Categorical slots - always assigned in this order, never cycled.
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100",
    "#e87ba4", "#008300", "#4a3aa7", "#e34948",
)
PALETTE = [BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED]

# Fixed colour per room type so the same entity has the same colour everywhere.
ROOM_COLORS = {
    "Entire home/apt": BLUE,
    "Private room": ORANGE,
    "Hotel room": AQUA,
    "Shared room": YELLOW,
}

# Neutral ink and surfaces.
SURFACE = "#fcfcfb"
TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID = "#e4e3df"
NEUTRAL = "#a3a29c"

# Sequential (magnitude) and diverging (polarity) colormaps.
SEQ_BLUE = LinearSegmentedColormap.from_list(
    "seq_blue",
    ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"],
)
DIVERGING = LinearSegmentedColormap.from_list(
    "div_red_blue", ["#e34948", "#f0efec", "#2a78d6"]
)


def set_style():
    """Apply the project-wide seaborn/matplotlib theme."""
    sns.set_theme(style="whitegrid", palette=PALETTE, font_scale=1.0)
    mpl.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "figure.dpi": 110,
        "axes.edgecolor": GRID,
        "axes.labelcolor": TEXT_SECONDARY,
        "axes.titlecolor": TEXT_PRIMARY,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlepad": 12,
        "axes.labelsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "xtick.color": TEXT_SECONDARY,
        "ytick.color": TEXT_SECONDARY,
        "text.color": TEXT_PRIMARY,
        "legend.frameon": False,
        "lines.linewidth": 2,
    })


def euro(x, _pos=None):
    """Tick formatter for euro amounts."""
    return f"€{x:,.0f}"


def save_fig(fig, name):
    """Save a figure to images/<name>.png at 300 dpi."""
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    path = IMAGES_DIR / f"{name}.png"
    fig.savefig(path, dpi=300, bbox_inches="tight")
    return path
