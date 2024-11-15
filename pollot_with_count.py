import matplotlib.pyplot as plt


def read_from_file():
    data = []
    with open("../cm_1/spline.txt", "r") as file:

        lines = file.readlines()
        i = 0
        while i < len(lines):
            N = int(lines[i].strip())  # Считываем количество точек
            i += 1

            points = []
            for _ in range(N):
                x, y = map(float, lines[i].strip().split())
                points.append((x, y))
                i += 1

            data.append(points)

    return data


plt.figure(figsize=(10, 10))
data = read_from_file()

for index, points in enumerate(data):  # индексация
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.plot(x_values, y_values, )
    plt.plot(x_values, y_values, label=f'Graph {index + 1}')  # для задания 1

plt.title('Многочлены Лагранжа степени 1-15')

plt.xlabel('X')
plt.ylabel('Y')


plt.axhline(0, color='black', linewidth=0.001, ls='-')
plt.axvline(0, color='black', linewidth=0.001, ls='-')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.legend()
plt.show()
