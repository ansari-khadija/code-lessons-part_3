import matplotlib.pyplot as plt

products = ["Watches", "Jackets", "Sneakers", "Sunglasses"]
sales = [280, 350, 240, 180]

colors = ["#B8C0FF", "#C8E7F5", "#D8B4E2", "#A8D5BA"]

# Separate slices
explode = [0, 0.1, 0, 0]

fig, ax = plt.subplots(figsize=(9, 7))

wedges, texts, autotexts = ax.pie(
    sales,

    # Display product names
    labels=products,

    # Custom colours
    colors=colors,

    # Display percentages
    autopct="%1.1f%%",

    # Separate slices
    explode=explode,

    # Rotate pie chart
    startangle=90,

    # Add shadow
    shadow=True,

    # Percentage text customization
    pctdistance=0.7,

    # Label distance
    labeldistance=1.15,

    # Border between slices
    wedgeprops={
        "edgecolor": "black",
        "linewidth": 0.5
    },

    # Text customization
    textprops={
        "fontsize": 12,
        "fontweight": "bold",
        "color": "black"
    },

    # Counterclockwise direction
    counterclock=True,

    # Radius of pie chart
    radius=1
)

# Customize percentage text separately
for autotext in autotexts:
    autotext.set_color("black")
    autotext.set_fontsize(11)
    autotext.set_fontweight("bold")

# Add title
ax.set_title(
    "Fashion Sales Distribution",
    fontsize=16,
    fontweight="bold"
)

# Add legend
ax.legend(
    wedges,
    products,
    title="Products",
    loc="upper right",
    bbox_to_anchor=(1.3, 1)
)

# Keep pie circular
ax.axis("equal")

plt.tight_layout()
plt.show()