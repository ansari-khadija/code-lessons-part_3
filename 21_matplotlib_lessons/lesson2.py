import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = ["TATA","MAHINDRA","MARUTI","HONDA","HYUNDAI"]
y = [60 ,45, 30, 25, 33]

ax.bar(x, y)

ax.set_title("Shares Graph")
ax.set_xlabel("Companies")
ax.set_ylabel("Shares Percent")

plt.show()
