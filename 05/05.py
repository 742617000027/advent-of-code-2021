import numpy as np

import utils


def parse_lines(data, mode='HV'):
    assert mode in ['HV', 'all'], 'Mode must be one of `HV` or `all`.'
    lines = [[tuple(int(x) for x in elem.split(',')) for elem in line.split(' -> ')] for line in data]
    max_x, max_y = max([line[i][0] for line in lines for i in range(2)]), \
                   max([line[i][1] for line in lines for i in range(2)])
    diagram = np.zeros((max_y + 1, max_x + 1))
    for line in lines:
        [(x1, y1), (x2, y2)] = line
        flip = False
        x1, x2, flip = (x2, x1, not flip) if x2 - x1 < 0 else (x1, x2, flip)
        y1, y2, flip = (y2, y1, not flip) if y2 - y1 < 0 else (y1, y2, flip)
        if (x1 == x2 or y1 == y2):
            diagram[y1:y2 + 1, x1:x2 + 1] += 1
        elif mode == 'all':
            diagram[y1:y2 + 1, x1:x2 + 1] += np.eye(x2 - x1 + 1)[::-1 if flip else 1]

    return diagram


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()
    diagram = parse_lines(data)
    print(np.sum(diagram >= 2))
    timer.stop()  # 24.13ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()
    diagram = parse_lines(data, 'all')
    print(np.sum(diagram >= 2))
    timer.stop()  # 472.86ms
    # """
