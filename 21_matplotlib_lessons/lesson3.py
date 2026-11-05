
import matplotlib.pyplot as plt

x = ["TATA","MAHINDRA","MARUTI","HONDA","HYUNDAI"]
y = [60 ,45, 30, 25, 33]

fig, ax = plt.subplots(1, 2)

# First graph
ax[0].plot(x, y)
ax[0].set_title("Shares Graph")
ax[0].set_xlabel("Companies")
ax[0].set_ylabel("Shares Percent")

# Second graph
ax[1].bar(x, y)
ax[1].set_title("Shares Graph")
ax[1].set_xlabel("Companies")
ax[1].set_ylabel("Shares Percent")

plt.show()