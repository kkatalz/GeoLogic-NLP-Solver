import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def draw_triangle(given, to_solve, triangle_name, results, side_length=5):
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

    # Create figure with adjusted size and bottom margin
    plt.figure(figsize=(4, 5))

    # Create main axes for triangle with adjusted position - increased bottom position to 0.45
    ax = plt.axes([0.1, 0.45, 0.8, 0.5])

    # Plot triangle
    ax.plot(
        [vertices[triangle_name[0]][0], vertices[triangle_name[1]][0],
            vertices[triangle_name[2]][0], vertices[triangle_name[0]][0]],
        [vertices[triangle_name[0]][1], vertices[triangle_name[1]][1],
            vertices[triangle_name[2]][1], vertices[triangle_name[0]][1]],
        color='blue', linestyle='-', marker='o'
    )

    # Annotate vertices
    for label, (x, y) in vertices.items():
        ax.text(x, y, label, fontsize=12, ha='center', va='bottom')

    def draw_angle_arc(center, start_angle, end_angle, radius, text, offset):
        arc = patches.Arc(center, radius, radius, angle=0,
                          theta1=start_angle, theta2=end_angle, color="blue", lw=1.5)
        ax.add_patch(arc)
        ax.text(center[0] + offset[0], center[1] + offset[1],
                text, fontsize=10, color='blue', ha='center')

    # Angles for A, B, and C
    draw_angle_arc(vertices[triangle_name[0]], 0, 60,
                   1, "60°", (-0.4, 0.4))  # Angle at A
    draw_angle_arc(vertices[triangle_name[1]], 120, 180,
                   1, "60°", (0.4, 0.4))  # Angle at B
    draw_angle_arc(vertices[triangle_name[2]], 240,
                   300, 1, "60°", (0, 0.4))  # Angle at C

   # Depict specific lines if required
    if any("середній лінія" in task for task in to_solve):
        midpoint_ac = ((vertices[triangle_name[0]][0] + vertices[triangle_name[2]][0]) / 2,
                       (vertices[triangle_name[0]][1] + vertices[triangle_name[2]][1]) / 2)
        midpoint_bc = ((vertices[triangle_name[1]][0] + vertices[triangle_name[2]][0]) / 2,
                       (vertices[triangle_name[1]][1] + vertices[triangle_name[2]][1]) / 2)

        ax.plot(
            [midpoint_ac[0], midpoint_bc[0]],
            [midpoint_ac[1], midpoint_bc[1]],
            color='orange', linestyle='--'
        )

        # Annotate points L and K
        for task in to_solve:
            if "середній лінія" in task:
                parts = task.split()
                if len(parts) > 2:
                    ax.text(midpoint_ac[0], midpoint_ac[1] - 0.2, parts[2][0].upper(),
                            fontsize=12, ha='center', color='purple')
                    ax.text(midpoint_bc[0], midpoint_bc[1] - 0.2, parts[2][1].upper(),
                            fontsize=12, ha='center', color='purple')

        # Add '?' over the line
        mid_x = (midpoint_ac[0] + midpoint_bc[0]) / 2
        mid_y = (midpoint_ac[1] + midpoint_bc[1]) / 2
        ax.text(mid_x, mid_y + 0.2, '?', fontsize=12,
                color='red', ha='center')

    # Turn off axes
    ax.axis('off')

    # Add details below the plot without a box
    given_text = f"Дано:\nТрикутник - {triangle_name}\n Усі кути:60" + \
        "\n".join([f"{k}: {v}" for k, v in given.items()])

    to_solve_text = f"\n\nЗнайти:\n" + \
        "\n".join(to_solve)

    answer_text = f"\n\nРезультат:\n" + \
        "\n".join(results)

    # Moved text closer to triangle by increasing y position from 0.15 to 0.25
    plt.figtext(0.3, 0.25, given_text + to_solve_text + answer_text,
                wrap=True,
                horizontalalignment='left',
                verticalalignment='center',
                fontsize=10)

    plt.show()


def draw_line(point1, point2, color='blue'):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, color=color, linestyle='-', marker='o')


def draw_perpendicular(name, base_line, color='red'):
    base_p1, base_p2 = base_line
    lower_point, high_point = name[0], name[1]

    h_x = (base_p1[0] + base_p2[0]) / 2
    h_y = base_p1[1]
    h_point = (h_x, h_y)

    base_length = np.sqrt(
        (base_p2[0] - base_p1[0])**2 + (base_p2[1] - base_p1[1])**2)

    c_point = (h_x, h_y + base_length / 2)

    plt.plot([h_point[0], c_point[0]], [h_point[1], c_point[1]],
             color=color, linestyle='-', marker='o')

    plt.scatter(h_point[0], h_point[1], color='orange', label=high_point)
    plt.scatter(c_point[0], c_point[1], color='purple', label=lower_point)

    plt.text(h_point[0], h_point[1] - 0.1, high_point,
             fontsize=12, ha='center', va='top')
    plt.text(c_point[0], c_point[1], lower_point,
             fontsize=12, ha='left', va='bottom')
