import matplotlib.pyplot as plt

def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            points.append((x, y))
    return points

def plot_points(points):
    x, y = zip(*points)
    plt.scatter(x, y)
    plt.xlim(0, 960)
    plt.ylim(0, 540)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Points')
    plt.savefig('E:\output.png')  # Зберігає зображення у форматі PNG
    plt.show()

if __name__ == "__main__":
    dataset_path = 'E:\DS5.txt'
    points = read_dataset(dataset_path)
    plot_points(points)
