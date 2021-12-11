import numpy as np

import utils


def perform_step(data):
    data = np.pad(data, (1, 1), mode='constant', constant_values=-9999)
    kernel = np.ones((3, 3), dtype=data.dtype)
    data += 1
    has_to_flash = set(zip(*np.where(data > 9)))
    already_flashed = set()
    while len(has_to_flash) > 0:
        this_round = has_to_flash.copy()
        for h, w in this_round:
            if (h, w) not in already_flashed:
                data[h - 1:h + 2, w - 1:w + 2] += kernel
                already_flashed.add((h, w))
                has_to_flash = set(zip(*np.where(data > 9)))
        has_to_flash = has_to_flash.difference(already_flashed)
    data[data > 9] = 0
    return data[1:-1, 1:-1]


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = np.array([[int(elem) for elem in line] for line in utils.read_str_lines()])
    total = 0
    for _ in range(100):
        data = perform_step(data)
        total += np.sum(data == 0)
    print(total)
    timer.stop()  # 72.86ms
    """

    # Part 2
    # """
    timer.start()
    data = np.array([[int(elem) for elem in line] for line in utils.read_str_lines()])
    step = 1
    while True:
        data = perform_step(data)
        if not np.any(data):
            break
        step += 1
    print(step)
    timer.stop()  # 230.62ms
    # """
