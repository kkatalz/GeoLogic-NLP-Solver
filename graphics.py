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

    def draw_side_label(point1, point2, value, align='center'):
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2

    # Adjust alignment and position based on alignment parameter
        if align == 'left':
            ax.text(mid_x - 0.2, mid_y + 0.2, value, fontsize=10,
                    color='blue', ha='right')  # Left alignment
        elif align == 'right':
            ax.text(mid_x + 0.2, mid_y + 0.2, value, fontsize=10,
                    color='blue', ha='left')   # Right alignment
        else:
            ax.text(mid_x, mid_y + 0.2, value, fontsize=10, color='blue',
                    ha='center')       # Center alignment (default)


    # fmt: off

    # Add side length based on 'Сторона'
    if 'Сторона' in given:
        side_info = given['Сторона']
        if side_info.isdigit() or side_info.replace('.', '', 1).isdigit():  # Default case
            draw_side_label(vertices[triangle_name[0]], vertices[triangle_name[2]], f"{side_info.strip('.')}", align='left')
        else:  # Specific side case (e.g., "Сторона AB")
            parts = side_info.split()
            if len(parts) == 2 and parts[1] in ['AB', 'BC', 'AC']:
                if parts[1] == 'AB':
                    draw_side_label(vertices[triangle_name[0]], vertices[triangle_name[1]], f"{parts[0].strip('.')}")
                elif parts[1] == 'BC':
                    draw_side_label(vertices[triangle_name[1]], vertices[triangle_name[2]], f"{parts[0].strip('.')}")
                elif parts[1] == 'AC':
                    draw_side_label(vertices[triangle_name[0]], vertices[triangle_name[2]], f"{parts[0].strip('.')}")

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

    if any("середній лінія" in task.lower() for task in to_solve):
        # Calculate midpoints of two sides
        midpoint_bm = ((vertices[triangle_name[1]][0] + vertices[triangle_name[2]][0]) / 2,
                      (vertices[triangle_name[1]][1] + vertices[triangle_name[2]][1]) / 2)
        midpoint_nm = ((vertices[triangle_name[2]][0] + vertices[triangle_name[0]][0]) / 2,
                      (vertices[triangle_name[2]][1] + vertices[triangle_name[0]][1]) / 2)

        # Draw the middle line
        ax.plot(
            [midpoint_bm[0], midpoint_nm[0]],
            [midpoint_bm[1], midpoint_nm[1]],
            color='orange', linestyle='--'
        )

        # Annotate points L and K
        for task in to_solve:
            if "середній лінія" in task.lower():
                # Extract L and K from the task text
                if "lk" in task.lower():
                    ax.text(midpoint_bm[0], midpoint_bm[1] - 0.2, "L",
                           fontsize=12, ha='center', color='purple')
                    ax.text(midpoint_nm[0], midpoint_nm[1] - 0.2, "K",
                           fontsize=12, ha='center', color='purple')

        # Add '?' over the line
        mid_x = (midpoint_bm[0] + midpoint_nm[0]) / 2
        mid_y = (midpoint_bm[1] + midpoint_nm[1]) / 2
        ax.text(mid_x, mid_y + 0.2, '?', fontsize=12,
                color='red', ha='center')

    elif any("середній лінія" in key.lower() for key in given.keys()):
    # Find the key in 'given' that contains the middle line information
        middle_line_key = next(key for key in given.keys() if "середній лінія" in key.lower())

        # Extract the points for the middle line, e.g., "MN" from "Середня лінія MN"
        points_label = [word for word in middle_line_key.split() if len(word) == 2 and word.isalpha()][0]
        start_point_label, end_point_label = points_label[0], points_label[1]

        # Calculate midpoints of two sides
        midpoint_start = ((vertices[triangle_name[1]][0] + vertices[triangle_name[2]][0]) / 2,
                          (vertices[triangle_name[1]][1] + vertices[triangle_name[2]][1]) / 2)
        midpoint_end = ((vertices[triangle_name[2]][0] + vertices[triangle_name[0]][0]) / 2,
                        (vertices[triangle_name[2]][1] + vertices[triangle_name[0]][1]) / 2)

        # Draw the middle line
        ax.plot(
            [midpoint_start[0], midpoint_end[0]],
            [midpoint_start[1], midpoint_end[1]],
            color='orange', linestyle='--'
        )

        # Annotate the points
        ax.text(midpoint_start[0], midpoint_start[1] - 0.2, start_point_label,
                fontsize=12, ha='center', color='purple')
        ax.text(midpoint_end[0], midpoint_end[1] - 0.2, end_point_label,
                fontsize=12, ha='center', color='purple')

        # Add the given length of the middle line as a label
        middle_line_length = given[middle_line_key]
        mid_x = (midpoint_start[0] + midpoint_end[0]) / 2
        mid_y = (midpoint_start[1] + midpoint_end[1]) / 2
        ax.text(mid_x, mid_y + 0.2, f"{middle_line_length}", fontsize=12, color='red', ha='center')

    if any("висот" in task.lower() for task in to_solve):
        # Draw height (perpendicular) from vertex C to side AB
        midpoint = ((vertices[triangle_name[0]][0] + vertices[triangle_name[1]][0]) / 2,
                    (vertices[triangle_name[0]][1] + vertices[triangle_name[1]][1]) / 2)

        draw_perpendicular(ax, vertices[triangle_name[2]], midpoint, triangle_name[2], 'H')

    elif any("висот" in key.lower() for key in given.keys()):
    # Find the key in 'given' that contains the height information
        height_key = next(key for key in given.keys() if "висот" in key.lower())

        # Extract the height label, e.g., "bk" from the key "Висота bk"
        height_label = [word for word in height_key.split() if len(word) == 2 and word.isalpha()][0].lower()
        top_point_label = height_label[0].upper()  # First letter of the height label (e.g., "b" -> "B")
        bottom_point_label = height_label[1].upper()  # Second letter of the height label (e.g., "k" -> "K")

        # Dynamically calculate midpoint if bottom point is not a vertex (e.g., "K")
        if bottom_point_label == "K":  # Place K at the midpoint of AC
            midpoint = ((vertices[triangle_name[0]][0] + vertices[triangle_name[2]][0]) / 2,
                        (vertices[triangle_name[0]][1] + vertices[triangle_name[2]][1]) / 2)
            draw_perpendicular(ax, vertices[top_point_label], midpoint, top_point_label, bottom_point_label,
                               height_value=given[height_key])
        else:
            # If bottom_point_label is a vertex, use its coordinates directly
            draw_perpendicular(ax, vertices[top_point_label], vertices[bottom_point_label], top_point_label,
                               bottom_point_label, height_value=given[height_key])

    if any("вписаний коло" in task.lower() for task in to_solve):
        draw_inscribed_circle(ax, vertices, triangle_name)

    elif any("описаний коло" in task.lower() for task in to_solve):
        draw_circumscribed_circle(ax, vertices, triangle_name)

    # Turn off axes
    ax.axis('off')

    # Add details below the plot without a box
    given_text = f"Дано:\nТрикутник - {triangle_name}\n Усі кути:60\n" + \
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


def draw_perpendicular(ax, top_point, bottom_point, top_label, bottom_label, color='red', height_value=None):
    ax.plot([top_point[0], bottom_point[0]], [top_point[1], bottom_point[1]],
            color=color, linestyle='--', marker='')

    # Add a right angle symbol higher along the perpendicular
    right_angle_size = 0.2
    angle_vertex = (
        bottom_point[0],  # Keep x-coordinate of the base
        bottom_point[1] + (top_point[1] - bottom_point[1]) * 0.05  # Move y-coordinate higher
    )
    dx = right_angle_size  
    dy = right_angle_size * (1 if top_point[0] > bottom_point[0] else -1)

    ax.plot([angle_vertex[0], angle_vertex[0] + dx, angle_vertex[0] + dx],
            [angle_vertex[1], angle_vertex[1], angle_vertex[1] + dy],
            color=color, linewidth=1)

    # Label the points
    ax.text(bottom_point[0], bottom_point[1] - 0.2, bottom_label,
            fontsize=12, ha='center', va='top', color=color)

    # Add '?' near the middle of the perpendicular line
    mid_x = (top_point[0] + bottom_point[0]) / 2
    mid_y = (top_point[1] + bottom_point[1]) / 2
    if height_value:
        ax.text(mid_x + 0.2, mid_y, f"{height_value}", fontsize=12, color='red', ha='left')
    else:
        ax.text(mid_x + 0.2, mid_y, '?', fontsize=12, color='red', ha='left', va='center')

def draw_inscribed_circle(ax, vertices, triangle_name):
    """Draws the inscribed circle of the triangle using its vertices."""
    A = vertices[triangle_name[0]]
    B = vertices[triangle_name[1]]
    C = vertices[triangle_name[2]]

    # Calculate side lengths
    a = np.linalg.norm(np.array(B) - np.array(C))
    b = np.linalg.norm(np.array(A) - np.array(C))
    c = np.linalg.norm(np.array(A) - np.array(B))
    perimeter = a + b + c

    # Incenter coordinates
    incenter_x = (a * A[0] + b * B[0] + c * C[0]) / perimeter
    incenter_y = (a * A[1] + b * B[1] + c * C[1]) / perimeter

    # Radius of the inscribed circle
    area = 0.5 * abs(
        A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])
    )
    radius = area / (0.5 * perimeter)

    # Draw the inscribed circle
    circle = patches.Circle((incenter_x, incenter_y), radius, edgecolor='green', fill=False, linewidth=1.5, linestyle='--')
    ax.add_patch(circle)

    # Annotate the incenter
    ax.text(incenter_x, incenter_y, 'r', fontsize=12, ha='center', va='center', color='green')


def draw_circumscribed_circle(ax, vertices, triangle_name):
    """Draws the circumscribed circle of the triangle using its vertices."""
    A = vertices[triangle_name[0]]
    B = vertices[triangle_name[1]]
    C = vertices[triangle_name[2]]

    # Calculate the circumcenter (intersection of perpendicular bisectors)
    D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    ux = ((A[0]**2 + A[1]**2) * (B[1] - C[1]) +
          (B[0]**2 + B[1]**2) * (C[1] - A[1]) +
          (C[0]**2 + C[1]**2) * (A[1] - B[1])) / D
    uy = ((A[0]**2 + A[1]**2) * (C[0] - B[0]) +
          (B[0]**2 + B[1]**2) * (A[0] - C[0]) +
          (C[0]**2 + C[1]**2) * (B[0] - A[0])) / D

    # Radius of the circumscribed circle
    radius = np.linalg.norm(np.array([ux, uy]) - np.array(A))

    # Draw the circumscribed circle
    circle = patches.Circle((ux, uy), radius, edgecolor='blue', fill=False, linewidth=1.5, linestyle='--')
    ax.add_patch(circle)

    # Annotate the circumcenter
    ax.text(ux, uy, 'O', fontsize=12, ha='center', va='center', color='blue')