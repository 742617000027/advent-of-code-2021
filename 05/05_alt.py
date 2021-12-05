from collections import defaultdict
from itertools import cycle

import utils


def parse_lines(data, mode='HV'):
    assert mode in ['HV', 'all'], 'Mode must be one of `HV` or `all`.'
    diagram = defaultdict(lambda: defaultdict(lambda: 0))

    for x, y, hv in [point for elem in [
        list(zip(cycle(X) if len(X) == 1 else X, cycle(Y) if len(Y) == 1 else Y, cycle([len(X) == 1 or len(Y) == 1])))
        for X, Y in [[list(range(z1, z2 + (1 if z2 >= z1 else -1), 1 if z2 >= z1 else -1)) for z1, z2 in
                      zip(*[tuple(int(x) for x in elem.split(',')) for elem in line.split(' -> ')])] for line in data]]
                     for point in elem]:
        if hv or mode == 'all': diagram[x][y] += 1
    return diagram


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()
    diagram = parse_lines(data)
    print(sum(val >= 2 for elem in diagram.values() for val in elem.values()))
    timer.stop()  # 59.03ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()
    diagram = parse_lines(data, 'all')
    print(sum(val >= 2 for elem in diagram.values() for val in elem.values()))
    timer.stop()  # 99.90ms
    # """
