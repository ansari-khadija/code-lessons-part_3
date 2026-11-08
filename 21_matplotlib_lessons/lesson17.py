import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_2024 = [200, 250, 230, 300, 350, 400]
sales_2025 = [180, 220, 280, 270, 380, 450]
sales_2026 = [150, 200, 250, 320, 360, 420]

fig, ax = plt.subplots(figsize=(10, 6))

# First line
ax.plot(
    months,
    sales_2024,
    color="#7AA9FF",
    marker="o",
    linewidth=2,
    label="2024"
)

# Second line
ax.plot(
    months,
    sales_2025,
    color="#FAA2CB",
    marker="s",
    linewidth=2,
    label="2025"
)

# Third line
ax.plot(
    months,
    sales_2026,
    color="#83A66B",
    marker="^",
    linewidth=2,
    label="2026"
)

# Title and labels
ax.set_title("Monthly Sales Comparison", fontsize=16)
ax.set_xlabel("Months")
ax.set_ylabel("Sales")

# Grid
ax.grid(
    True,
    linestyle="--",
    alpha=0.4
)

# Legend
ax.legend(title="Years")

plt.tight_layout()
plt.show()