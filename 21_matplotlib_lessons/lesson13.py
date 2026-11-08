import matplotlib.pyplot as plt
import numpy as np

products = ["Mobile", "Laptop", "Tablet", "Watch"]

sales_online = np.array([200, 300, 150, 100])
sales_offline = np.array([100, 200, 250, 150])

fig, ax = plt.subplots(figsize=(9, 5))

# Calculate total sales
totals = sales_online + sales_offline

# Calculate percentages
online_percent = sales_online / totals * 100
offline_percent = sales_offline / totals * 100

# Online bars
bars1 = ax.bar(
    products,
    online_percent,
    label="Online",
    color="#FBE6FF"
)

# Offline bars
bars2 = ax.bar(
    products,
    offline_percent,
    bottom=online_percent,
    label="Offline",
    color="#CCD2F5"
)

# Display online percentages
ax.bar_label(
    bars1,
    labels=[f"{v:.1f}%" for v in online_percent],
    label_type="center"
)

# Display offline percentages
ax.bar_label(
    bars2,
    labels=[f"{v:.1f}%" for v in offline_percent],
    label_type="center"
)

ax.set_title("Percentage Stacked Bar Chart")
ax.set_xlabel("Products")
ax.set_ylabel("Sales Percentage")

ax.set_ylim(0, 110)

ax.legend()

plt.tight_layout()
plt.show()