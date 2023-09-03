import matplotlib.pyplot as plt

# График квадратов
squares = [i ** 2 for i in range(100)]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()

