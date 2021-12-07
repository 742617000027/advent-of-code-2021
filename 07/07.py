import numpy as np

import utils


def tri(n):
    return n * (n + 1) / 2


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = np.array(utils.read_int_sequence())
    print(int(np.sum(np.abs(data - np.floor(np.median(data))))))
    timer.stop()  # 0.67ms
    """

    # Part 2
    # """
    timer.start()
    data = np.array(utils.read_int_sequence())
    target = np.mean(data)
    a, b = np.sum(tri(np.abs(data - np.floor(target)))), \
           np.sum(tri(np.abs(data - np.ceil(target))))
    print(int(np.min([a, b])))
    timer.stop()  # 1.21ms
    # """
