from time import process_time

import numpy as np

import utils

if __name__ == '__main__':
    # Part 1
    """
    tic = process_time()
    data = utils.read_int_sequence()
    N = len([x for i, x in enumerate(data[1:]) if x > data[i]])
    print(N)
    toc = process_time()
    print(f'fininshed in {1000 * (toc - tic):.2f}ms') # 2.08ms
    """

    # Part 2
    tic = process_time()
    data = utils.read_int_sequence()
    conv = np.convolve(np.array(data), np.ones(3), mode='valid')
    N = len([x for i, x in enumerate(conv[1:]) if x > conv[i]])
    print(N)
    toc = process_time()
    print(f'fininshed in {1000 * (toc - tic):.2f}ms')  # 2.08ms
