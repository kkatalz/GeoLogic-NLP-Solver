import matplotlib.pyplot as plt
import numpy as np


def draw_triangle(given, to_solve, side_length=10):
    # Calculate vertices of the equilateral triangle
    height = (np.sqrt(3) / 2) * side_length
    vertices = {
        'A': (0, 0),
        'B': (side_length, 0),
        'C': (side_length / 2, height)
    }

    # Plot triangle
    plt.figure(figsize=(8, 8))
    plt.plot(
        [vertices['A'][0], vertices['B'][0], vertices['C'][0], vertices['A'][0]],
        [vertices['A'][1], vertices['B'][1], vertices['C'][1], vertices['A'][1]],
        color='blue', linestyle='-', marker='o', label='Triangle'
    )

    # Annotate vertices
    for label, (x, y) in vertices.items():
        plt.text(x, y, label, fontsize=12, ha='center', va='bottom')

    # Add given elements
    for key, value in given.items():
        plt.text(
            vertices['C'][0], vertices['C'][1] + 1.5, f"{key}: {value}",
            fontsize=10, color='green', ha='center'
        )

    # Add unknowns to solve
    for key in to_solve:
        plt.text(
            vertices['C'][0], vertices['C'][1] - 1.5, f"{key}: ?",
            fontsize=10, color='red', ha='center'
        )

    # Add legend
    plt.legend(['Triangle', 'Given', 'To Solve'], loc='upper right')
    plt.title('Triangle Visualization')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()


def draw_line(point1, point2, color='blue'):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, color=color, linestyle='-', marker='o')


def draw_perpendicular(name, base_line, color='red'):
    base_p1, base_p2 = base_line
    lower_point, high_point = name[0], name[1]

    h_x = (base_p1[0] + base_p2[0]) / 2  # Midpoint of the base line
    h_y = base_p1[1]
    h_point = (h_x, h_y)

    base_length = np.sqrt(
        (base_p2[0] - base_p1[0])**2 + (base_p2[1] - base_p1[1])**2)

    # Set point C above H, with length of CH equal to half of the base line length
    c_point = (h_x, h_y + base_length / 2)

    # Draw the perpendicular segment CH
    plt.plot([h_point[0], c_point[0]], [h_point[1], c_point[1]],
             color=color, linestyle='-', marker='o')

    # Plot points C and H with labels for legend
    plt.scatter(h_point[0], h_point[1], color='orange', label=high_point)
    plt.scatter(c_point[0], c_point[1], color='purple', label=lower_point)

    # Position labels
    plt.text(h_point[0], h_point[1] - 0.1, high_point,
             fontsize=12, ha='center', va='top')
    plt.text(c_point[0], c_point[1], lower_point,
             fontsize=12, ha='left', va='bottom')
