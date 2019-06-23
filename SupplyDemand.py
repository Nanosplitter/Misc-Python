import matplotlib.pyplot as plt 

x = [30, 24, 15, 7, 5, 3, 1]
y = [0, 1, 2, 3, 4, 5, 6]

x1 = [0, 7, 11, 15, 16]
y1 = [0.5, 2, 3, 4, 5]
plt.plot(x1, y1, label="Supply")
plt.plot(x, y, label="Demand")
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.title("Supply Demand Curve")
plt.show()
