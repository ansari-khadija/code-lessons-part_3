import matplotlib.pyplot as plt
import numpy as np

# Dataset
products = ["Shoes", "Shirts", "Jeans", "Bags"]

sales_women = [100, 170, 130, 190]
sales_men = [130, 110, 140, 80]

# Create grouped bars
x = np.arange(len(products))
width = 0.35

# Women bars
bars1 = plt.bar(
    x - width/2,
    sales_women,
    width,
    label="Women",
    color="#FAA2CB",
    edgecolor="#C94381",
    linewidth=1.5
)

# Men bars
bars2 = plt.bar(
    x + width/2,
    sales_men,
    width,
    label="Men",
    color="#7AA9FF",
    edgecolor="#446EBD",
    linewidth=1.5
)

plt.xticks(x, products)

plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

# Add values without creating new bars
plt.bar_label(bars1, padding=3)
plt.bar_label(bars2, padding=3)

plt.legend()
plt.tight_layout()
plt.show()