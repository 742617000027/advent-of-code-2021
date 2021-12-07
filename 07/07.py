import numpy as np

import utils


def tri(n):
    return n * (n + 1) / 2


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()[0].split(',')
    fuel = np.array([int(x) for x in data])
    print(int(np.sum(np.abs(fuel - np.floor(np.median(fuel))))))
    timer.stop()  # 0.67ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()[0].split(',')
    fuel = np.array([int(x) for x in data])
    target = np.mean(fuel)
    a, b = np.sum(tri(np.abs(fuel - np.floor(target)))), \
           np.sum(tri(np.abs(fuel - np.ceil(target))))
    print(int(np.min([a, b])))
    timer.stop()  # 1.21ms
    # """
