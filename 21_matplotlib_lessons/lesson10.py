import matplotlib.pyplot as plt

products = ["Shoes", "Shirts", "Jeans", "Bags"]
sales = [230, 280, 270, 270]


colors = [
    "#110981",
    "#2F31CA",
    "#6572EE",
    "#D8CFFF"
]

# Sort sales in descending order
sorted_data = sorted(
    zip(sales, products),
    reverse=True
)

sorted_sales, sorted_products = zip(*sorted_data)

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(
    sorted_products,
    sorted_sales,
    color=colors
)

# Display values
ax.bar_label(bars, padding=5)

ax.set_title("Products Sales - Descending Order")
ax.set_xlabel("Products")
ax.set_ylabel("Sales")

plt.tight_layout()
plt.show()