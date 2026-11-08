import matplotlib.pyplot as plt

products = ["coats", "boots", "hoodies", "scarfs"]
sales = [240, 200, 350, 190]
colors = ["#263238", "#536B72", "#A8C3C8", "#F1EDE5"]

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(
    products,
    sales,
    color=colors
)

# Add custom text
ax.text(
    1,
    380,
    "Highest Sales!",
    fontsize=15,
    color="#000000",
    fontweight="bold",
    backgroundcolor="#EEEEEE",
    rotation=0
)

ax.set_xlabel("Products")
ax.set_ylabel("Sales")

plt.tight_layout()
plt.show()