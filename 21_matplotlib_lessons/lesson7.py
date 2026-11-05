import matplotlib.pyplot as plt

x = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
y = [30, 35, 38, 50, 65, 70, 80]

colors = [
    "#FF3B30",
    "#FF9500",
    "#FFD60A",
    "#39E75F",
    "#00D4FF",
    "#A020F0",
    "#FF00A8"
]

plt.plot(x, y, color="black", linewidth=1.5)

plt.scatter(
    x, y,
    c=colors,
    edgecolors="black",
    s=100
)

# Display percentage values above each point
for i in range(len(x)):
    plt.text(
        x[i], y[i] + 2,
        f"{y[i]}%",
        ha="center",
        fontsize=10
    )

plt.title("Global Warming")
plt.xlabel("Year")
plt.ylabel("Percent (%)")

plt.grid(True, linestyle="--", alpha=0.4)
plt.show()