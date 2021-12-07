import numpy as np

import utils

if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_int_lines()
    N = len([x for i, x in enumerate(data[1:]) if x > data[i]])
    print(N)
    timer.stop()
    """

    # Part 2
    timer.start()
    data = utils.read_int_lines()
    conv = np.convolve(np.array(data), np.ones(3), mode='valid')
    N = len([x for i, x in enumerate(conv[1:]) if x > conv[i]])
    print(N)
    timer.stop()
