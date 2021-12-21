import numpy as np

import utils


def parse_input(data):
    iea = data[0]
    img = np.array([[0 if char == '.' else 1 for char in row] for row in data[2:]])
    return iea, img


def enhance(iea, img, step):
    constant = 0 if iea[0] == '.' else (step % 2 if iea[-1] == '.' else 1)
    enhanced = np.pad(np.zeros_like(img), 1)
    img = np.pad(img, 2, constant_values=constant)
    for i in range(img.shape[0] - 2):
        for j in range(img.shape[1] - 2):
            patch = img[i:i + 3, j:j + 3].flatten()
            idx = int(''.join([f'{bit}' for bit in patch]), base=2)
            if iea[idx] == '#': enhanced[i, j] = 1
    return enhanced


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    iea, img = parse_input(data)
    for step in range(2):
        img = enhance(iea, img, step)
    print(np.sum(img))
    timer.stop()  # 98.67ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_lines()
    iea, img = parse_input(data)
    for step in range(50):
        img = enhance(iea, img, step)
    print(np.sum(img))
    timer.stop()  # 4693.17ms
    # """
