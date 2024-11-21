import matplotlib.pyplot as plt

def read_from_file():
    data = []
    with open("../cm_lab3/first_ex.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            x, y = line.split()
            data.append((float(x), float(y)))
    return data

data = read_from_file()

x_values = []
y_values = []

for point in data:
    x_values.append(point[0])
    y_values.append(point[1])

# Заданные точки
x_points = [0., 0.4, 0.8, 1.2, 1.6, 2.]
y_points = [31., 0.78825, 0.66407, 0.84878, 1.3389, 3.1099]

plt.figure(figsize=(10, 10))

plt.title('График интерполирующей функции и исходных данных для задачи №2.')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black', linewidth=1, ls='-')
plt.axvline(0, color='black', linewidth=1, ls='-')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.plot(x_values, y_values, label='Интерполирующая функция')

plt.scatter(x_points, y_points, color='red', label='Исходные точки', zorder=5)

plt.legend()
plt.show()