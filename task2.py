import numpy as np
import matplotlib.pyplot as plt

random_x = np.random.rand(100)  # массив из 5 случайных чисел
random_y = np.random.rand(100)

plt.scatter(random_x, random_y)
plt.title("Scattering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()