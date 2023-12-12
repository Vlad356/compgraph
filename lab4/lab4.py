import numpy as np
import matplotlib.pyplot as plt

# Зчитуємо датасет з файлу
dataset = np.loadtxt('E:\output.txt')

# Додаємо координату z = 100
dataset = np.hstack([dataset, np.ones((dataset.shape[0], 1)) * 100])

# Встановлюємо точку сходження
h_x, h_y = 540, 960

# Знаходимо матрицю центральної проекції P
P = np.array([[1, 0, -h_x / h_y],
              [0, 1, -h_y / h_y],
              [0, 0, 0]])

# Здійснюємо центральну проекцію
projected_dataset = np.dot(dataset, P.T)

# Встановлюємо розміри вікна
plt.figure(figsize=(9.6, 5.4))

# Відображаємо проектований датасет
plt.scatter(projected_dataset[:, 0], projected_dataset[:, 1], c='red')

# Виводимо результати у файл графічного формату
plt.savefig('E:\output_image_projected.png')

# Показуємо графік
plt.show()
