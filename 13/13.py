import matplotlib.pyplot as plt
import numpy as np

import utils


def parse_data(data):
    points, folds = [], []
    W, H = 0, 0
    for line in data:
        if ',' in line:
            w, h = [int(elem) for elem in line.split(',')]
            W, H = w if w > W else W, h if h > H else H
            points.append((h, w))
        elif 'fold' in line:
            folds.append((0 if 'y' in line else 1, int(line.split('=')[1])))
    grid = np.zeros((H + 1, W + 1))
    grid[tuple(zip(*points))] = 1
    return grid, folds


def fold_grid(fold, grid):
    axis, z = fold
    return np.sign(grid[:z, :] + np.flipud(grid[z + 1:, :]) if axis == 0 \
                       else grid[:, :z] + np.fliplr(grid[:, z + 1:]))


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    grid, folds = parse_data(data)
    grid = fold_grid(folds[0], grid)
    print(np.sum(grid))
    timer.stop()  # 32.68ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_lines()
    grid, folds = parse_data(data)
    for fold in folds:
        grid = fold_grid(fold, grid)
    plt.imshow(grid)
    plt.show()
    timer.stop()  # 244.18ms
    # """
