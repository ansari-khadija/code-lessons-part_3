import matplotlib.pyplot as plt
import numpy as np

products = ["Shoes", "Shirts", "Jeans", "Bags"]

sales_women = [100, 170, 130, 190]
sales_men = [130, 110, 140, 80]

fig, ax = plt.subplots(figsize=(9, 5))

# Calculate total sales
totals = [
    women + men
    for women, men in zip(sales_women, sales_men)
]

# Women bars
bars1 = ax.bar(
    products,
    sales_women,
    label="Women",
    color="#FAA2CB"
)

# Men bars
bars2 = ax.bar(
    products,
    sales_men,
    bottom=sales_women,
    label="Men",
    color="#7AA9FF"
)

# Display women's values
ax.bar_label(
    bars1,
    label_type="center",
    color="black"
)

# Display men's values
ax.bar_label(
    bars2,
    label_type="center",
    color="black"
)

# Display total values above stacked bars
ax.bar_label(
    bars2,
    labels=totals,
    label_type="edge",
    padding=5
)

ax.set_title("Fashion Product Sales")
ax.set_xlabel("Products")
ax.set_ylabel("Sales")

ax.legend()
plt.tight_layout()
plt.show()