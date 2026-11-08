import matplotlib.pyplot as plt

products = ["Watches", "Jackets", "Sneakers", "Sunglasses"]
sales = [320, 250, 290, 180]

colors = ["#12372A", "#436850", "#ADBC9F", "#FBFADA"]

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(
    products,
    sales,
    color=colors
)

# Add annotation with arrow
ax.annotate(
    "Highest Sales!",
    xy=("Watches", 320),
    xytext=("Watches", 350),
    arrowprops=dict(
        arrowstyle="->",
        color="red",
        lw=2
    ),
    fontsize=12,
    color="red",
    fontweight="bold",
    ha="center"
)

ax.set_title("Product Sales Report")
ax.set_xlabel("Products")
ax.set_ylabel("Sales")

ax.set_ylim(0, 400)

plt.tight_layout()
plt.show()