import matplotlib.pyplot as plt
import numpy as np

def draw_pythagoras_tree(ax, x, y, side, angle, level):
    if level == 0:
        return

    x1 = x + side * np.cos(angle)
    y1 = y + side * np.sin(angle)
    x2 = x1 - side * np.sin(angle) * np.tan(np.pi / 4)
    y2 = y1 + side * np.cos(angle) * np.tan(np.pi / 4)

    ax.plot([x, x1], [y, y1], color='brown')
    ax.plot([x1, x2], [y1, y2], color='brown')
    ax.plot([x2, x + side * np.cos(angle - np.pi / 2)], [y2, y], color='brown')
    ax.plot([x + side * np.cos(angle - np.pi / 2), x], [y, y], color='brown')

    draw_pythagoras_tree(ax, x1, y1, side / np.sqrt(2), angle - np.pi / 4, level - 1)
    draw_pythagoras_tree(ax, x2, y2, side / np.sqrt(2), angle + np.pi / 4, level - 1)

fig, ax = plt.subplots()
draw_pythagoras_tree(ax, 0, 0, 1, np.pi / 2, 5)
ax.set_aspect('equal')
plt.show()
