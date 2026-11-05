import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Art"]
students = [60, 70, 90, 88, 55]

colors = [
    "#A7A8E6",
    "#5452BD",
    "#313280",
    "#202152",
    "#3425B8"
]

# Create one figure with two plotting areas
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Vertical chart
ax[0].bar(
    subjects, students,
    color=colors,
    width=0.5,
    edgecolor="black",
    linewidth=1.5
)

ax[0].set_title("Vertical Bar Chart")
ax[0].set_xlabel("Subjects")
ax[0].set_ylabel("Students")

# Horizontal chart
ax[1].barh(
    subjects, students,
    color=colors,
    height=0.5,
    edgecolor="black",
    linewidth=1.5
)

ax[1].set_title("Horizontal Bar Chart")
ax[1].set_xlabel("Students")
ax[1].set_ylabel("Subjects")

plt.tight_layout()
plt.show()