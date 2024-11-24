import matplotlib.pyplot as plt
import numpy as np


def draw_triangle(given, to_solve, triangle_name=None, side_length=10):
    # Determine triangle vertices based on name or default to ABC
    if triangle_name is None:
        triangle_name = 'ABC'
    else:
        triangle_name = triangle_name.upper()

    height = (np.sqrt(3) / 2) * side_length
    vertices = {
        triangle_name[0]: (0, 0),
        triangle_name[1]: (side_length, 0),
        triangle_name[2]: (side_length / 2, height)
    }

    # Plot triangle
    plt.figure(figsize=(8, 8))
    plt.plot(
        [vertices[triangle_name[0]][0], vertices[triangle_name[1]][0],
            vertices[triangle_name[2]][0], vertices[triangle_name[0]][0]],
        [vertices[triangle_name[0]][1], vertices[triangle_name[1]][1],
            vertices[triangle_name[2]][1], vertices[triangle_name[0]][1]],
        color='blue', linestyle='-', marker='o'
    )

    # Annotate vertices
    for label, (x, y) in vertices.items():
        plt.text(x, y, label, fontsize=12, ha='center', va='bottom')

    # Depict specific lines if required
    if any("середній лінія" in task for task in to_solve):
        midpoint_ac = ((vertices[triangle_name[0]][0] + vertices[triangle_name[2]][0]) / 2,
                       (vertices[triangle_name[0]][1] + vertices[triangle_name[2]][1]) / 2)
        midpoint_bc = ((vertices[triangle_name[1]][0] + vertices[triangle_name[2]][0]) / 2,
                       (vertices[triangle_name[1]][1] + vertices[triangle_name[2]][1]) / 2)

        plt.plot(
            [midpoint_ac[0], midpoint_bc[0]],
            [midpoint_ac[1], midpoint_bc[1]],
            color='orange', linestyle='--'
        )

        # Annotate points L and K using keys
        for task in to_solve:
            if "середній лінія" in task:
                parts = task.split()
                if len(parts) > 2:  # Ensure valid task structure
                    plt.text(midpoint_ac[0], midpoint_ac[1] - 0.1, parts[2][0].upper(),
                             fontsize=12, ha='center', color='purple')
                    plt.text(midpoint_bc[0], midpoint_bc[1] - 0.1, parts[2][1].upper(),
                             fontsize=12, ha='center', color='purple')

        # Add '?' over the line
        mid_x = (midpoint_ac[0] + midpoint_bc[0]) / 2
        mid_y = (midpoint_ac[1] + midpoint_bc[1]) / 2
        plt.text(mid_x, mid_y + 0.2, '?', fontsize=14,
                 color='red', ha='center')

    # Add title
    plt.title('Triangle Visualization')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # Add details below the plot
    # Add details below the plot
    given_text = f"Given: {', '.join([f'{k}: {v}' for k, v in given.items()])}"
    to_solve_text = f"To Solve: {', '.join(to_solve)}"
    plt.figtext(0.5, -0.05, given_text, wrap=True,
                horizontalalignment='center', fontsize=12, color='green')
    plt.figtext(0.5, -0.1, to_solve_text, wrap=True,
                horizontalalignment='center', fontsize=12, color='red')

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
