import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x ** 3) * ((1 - x ** 2) ** 0.5)

def read_from_file():
    data = []
    with open("../cm_lab2/Monte-carlo-500points.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            x, y = line.split()
            data.append((float(x), float(y)))
    return data

data = read_from_file()

if not data:
    print("No data to plot.")
else:
    x_values = [point[0] for point in data]
    y_values = [point[1] for point in data]

    plt.figure(figsize=(10, 10))

    plt.title('Monte Carlo graph')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', linewidth=1, ls='-')
    plt.axvline(0, color='black', linewidth=1, ls='-')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    for x, y in zip(x_values, y_values):
        if y > f(x):
            plt.scatter(x, y, color='red')
        else:
            plt.scatter(x, y, color='green')

    x_range = np.linspace(min(x_values), max(x_values), 100)  # Create a range of x values
    plt.plot(x_range, [f(x) for x in x_range], color='blue', label='f(x)', linewidth=2)

    plt.legend()
    plt.show()