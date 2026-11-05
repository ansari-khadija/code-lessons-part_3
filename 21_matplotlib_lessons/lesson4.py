# Formatting in matplotlib
import matplotlib.pyplot as plt

x =["2020","2021","2022","2023","2024","2025","2026"]
y = [60 ,45, 30, 25, 33, 40,70]

# Method one to give color for all bars
# plt.bar(x, y,color="#E8C7FD",width=0.5)

# Method two to give color in each bars
colors = [
    "#CDA7E6",
    "#9252BD",
    "#613180",
    "#3D2052",
    "#7F25B8",
    "#A77AC5",
    "#E8D5F2"
]
plt.bar(x, y,color=colors,width=0.5,edgecolor="#000000",linewidth=1.5)

plt.title("Modest Fashion Trends Yearly Data")
plt.xlabel("Year")
plt.ylabel("Fashion Trends")

plt.show()