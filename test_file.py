import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 - 2 * x * np.cos(x)

x_values = np.linspace(0, 2, 100)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = 1 - 2x * cos(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # линия y=0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # линия x=0
plt.title('График функции f(x) = 1 - 2x * cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

# Устанавливаем пределы по осям
plt.ylim(-5, 5)
plt.xlim(-3, 3)

# Устанавливаем шаг делений на осях
plt.xticks(np.arange(-3, 4, 0.5))  # Шаг по оси x
plt.yticks(np.arange(-5, 6, 1))     # Шаг по оси y

plt.show()