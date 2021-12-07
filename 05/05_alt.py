from collections import defaultdict
from itertools import cycle

import utils


def parse_lines(data, mode='HV'):
    assert mode in ['HV', 'all'], 'Mode must be one of `HV` or `all`.'
    diagram = defaultdict(lambda: defaultdict(lambda: 0))
    for line in data:
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        X, Y = list(range(x1, x2 + (1 if x2 >= x1 else -1), 1 if x2 >= x1 else -1)), \
               list(range(y1, y2 + (1 if y2 >= y1 else -1), 1 if y2 >= y1 else -1))
        for x, y in zip(cycle(X) if len(X) == 1 else X, cycle(Y) if len(Y) == 1 else Y):
            if x1 == x2 or y1 == y2 or mode == 'all':
                diagram[x][y] += 1

    return diagram


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    diagram = parse_lines(data)
    print(sum(val >= 2 for elem in diagram.values() for val in elem.values()))
    timer.stop()  # 59.03ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_lines()
    diagram = parse_lines(data, 'all')
    print(sum(val >= 2 for elem in diagram.values() for val in elem.values()))
    timer.stop()  # 99.90ms
    # """
