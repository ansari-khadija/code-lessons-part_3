import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

subjects = ["Maths", "Science", "English", "History"]
students = ["Student A", "Student B", "Student C", "Student D"]

marks = np.array([
    [85, 72, 90, 78],
    [65, 88, 75, 92],
    [95, 80, 84, 70],
    [70, 65, 82, 90]
])

fig, ax = plt.subplots(figsize=(9, 6))

# Define Soft Royal Gradient
soft_royal_hex = [
    "#2C3E50",
    "#9B8CB3",
    "#F9F6F0",
    "#D4AF37"
]

soft_royal_cmap = LinearSegmentedColormap.from_list(
    "soft_royal", soft_royal_hex
)

# Create heatmap
im = ax.imshow(
    marks,
    cmap=soft_royal_cmap,
    aspect="auto",
    vmin=60,
    vmax=100
)

# Add cell borders
ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
ax.grid(which="minor", color="black", linewidth=1.5)
ax.tick_params(which="minor", bottom=False, left=False)

# Add values inside cells
for i in range(len(students)):
    for j in range(len(subjects)):

        text_color = "black" if marks[i, j] >= 80 else "white"

        ax.text(
            j, i, marks[i, j],
            ha="center",
            va="center",
            color=text_color,
            fontsize=12,
            fontweight="bold"
        )

# Set labels
ax.set_xticks(range(len(subjects)))
ax.set_xticklabels(subjects)

ax.set_yticks(range(len(students)))
ax.set_yticklabels(students)

# Add color bar
plt.colorbar(im, ax=ax, label="Marks")

# Set title
ax.set_title(
    "Student Marks Heatmap",
    fontsize=14,
    pad=15
)

plt.tight_layout()
plt.show()