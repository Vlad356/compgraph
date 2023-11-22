import numpy as np
import matplotlib.pyplot as plt

def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [list(map(int, line.split())) for line in lines]
    return np.array(points)

def affine_transformation(points, rotation_angle):
    rotation_angle_rad = np.radians(rotation_angle)
    rotation_matrix = np.array([[np.cos(rotation_angle_rad), -np.sin(rotation_angle_rad)],
                                [np.sin(rotation_angle_rad), np.cos(rotation_angle_rad)]])
    transformed_points = np.dot(points - np.array([480, 480]), rotation_matrix.T) + np.array([480, 480])
    return transformed_points

def plot_points(points, color='blue'):
    plt.scatter(points[:, 0], points[:, 1], color=color)
    plt.xlim(0, 960)
    plt.ylim(0, 960)

def save_plot(file_path):
    plt.savefig(file_path)
    plt.show()

def main():
    dataset_file = 'E:\DS5.txt'  
    output_file = 'E:\output.png'  

    points = read_dataset(dataset_file)
    n = 5
    rotation_angle = 10 * (n + 1)  # Розрахунок кута згідно з вказаними умовами
    transformed_points = affine_transformation(points, rotation_angle)

    plt.figure(figsize=(9.6, 9.6))
    plot_points(transformed_points)

    save_plot(output_file)

if __name__ == "__main__":
    main()
