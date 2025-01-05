import numpy as np
import matplotlib.pyplot as plt

# Створення даних
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Побудова графіка
plt.plot(x, y)
plt.title("Графік синусоїди")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()
plt.savefig("sine_wave.png")  # Збереження графіка
plt.show()
