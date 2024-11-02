import matplotlib.pyplot as plt


def read_from_file():
    data = []
    #with open("../cm_1/data.txt", "r") as file:
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

plt.title('Многочлены Лагранжа степени 1-15')  # Задание 1?
# plt.title('Многочлен Лагранжа в нулях Чебышева') #Задание 2?
# plt.title('Сравнение двух графиков многочленов Лагранжа при равномерной и неравномерной сетках.')
# plt.title('Многочлен Ньютона и Лагранжа') #Задание 2?

plt.xlabel('X')
plt.ylabel('Y')
# q = 0.5
# w = 0.15
# plt.xlim(-q, q)
# plt.ylim(-w, w)

plt.axhline(0, color='black', linewidth=0.001, ls='-')
plt.axvline(0, color='black', linewidth=0.001, ls='-')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.legend()  # Задание 1
# plt.legend(['Неравномерная', 'Равномерная'])  # Задание 2
# plt.legend(['Ньютон', 'Лагранж']) #Задание 3

plt.show()
