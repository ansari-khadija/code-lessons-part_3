import matplotlib.pyplot as plt

x = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
y = [30, 35, 38, 50, 65, 70, 80]


plt.plot(
    x, y,
    color="#EC1B1B",
    linestyle="-",
    marker="o",
    linewidth=2,
    markersize=8,
    markerfacecolor="#000000",
    markeredgecolor="#000000",
    markeredgewidth=0.5
)

plt.title("AI use Yearly Data")
plt.xlabel("Year")
plt.ylabel("AI Usage")

plt.grid(True, linestyle="--", alpha=0.4)

plt.show()