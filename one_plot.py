import matplotlib.pyplot as plt

def read_from_file():
    data = []
    with open("../cm_lab2/test.txt", "r") as file:
    #with open("../cm_1/data.txt", "r") as file:
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

plt.figure(figsize=(10, 10))

plt.title('Oshibka Priblizheniya splines')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black', linewidth=1, ls='-')
plt.axvline(0, color='black', linewidth=1, ls='-')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.plot(x_values, y_values, label=f'Graph')

plt.legend()
plt.show()