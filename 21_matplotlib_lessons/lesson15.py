import matplotlib.pyplot as plt

Subjects = ["Cosmology", "Geology", "Zoology", "Botany"]
Students = [200, 350, 240, 180]

colors = ["#5146A5", "#A77B55", "#83A66B", "#65B99A"]

# Calculate total students
total = sum(Students)

fig, ax = plt.subplots(figsize=(9, 7))

wedges, texts, autotexts = ax.pie(
    Students,
    labels=Subjects,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    pctdistance=0.75,
    labeldistance=1.15,
    wedgeprops={
        "width": 0.4,
        "edgecolor": "white",
        "linewidth": 1
    },
    textprops={
        "fontsize": 11,
        "fontweight": "bold"
    }
)

# Customize percentage text
for autotext in autotexts:
    autotext.set_color("black")
    autotext.set_fontsize(11)
    autotext.set_fontweight("bold")

# Add title
ax.set_title(
    "Student Distribution by Subject",
    fontsize=16,
    fontweight="bold"
)

# Add legend
ax.legend(
    wedges,
    Subjects,
    title="Subjects",
    loc="upper right",
    bbox_to_anchor=(1.3, 1)
)

# Add text inside donut hole
ax.text(
    0,
    0,
    f"Total Students\n{total}",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold",
    color="#333333"
)

ax.axis("equal")

plt.tight_layout()
plt.show()