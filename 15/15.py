import networkx as nx
import numpy as np

import utils


def build(data):
    H = len(data)
    W = len(data[0])
    G = nx.DiGraph()
    for h in range(H):
        for w in range(W):
            for dh, dw in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= h + dh < H and 0 <= w + dw < W:
                    G.add_edge((h, w), (h + dh, w + dw), weight=data[h + dh][w + dw])
    return G


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = np.array([[int(elem) for elem in line] for line in utils.read_str_lines()])
    G = build(data)
    path = nx.shortest_path(G, (0, 0), (len(data) - 1, len(data[0]) - 1), 'weight')
    H, W = zip(*path[1:])
    print(sum(data[H, W]))
    timer.stop()  # 139.12ms
    """

    # Part 2
    # """
    timer.start()
    data = np.array([[int(elem) for elem in line] for line in utils.read_str_lines()])
    for axis in range(2):
        data = np.concatenate([data] + [((data + rep) % 9) + 1 for rep in range(4)], axis=axis)
    G = build(data)
    path = nx.shortest_path(G, (0, 0), (len(data) - 1, len(data[0]) - 1), 'weight')
    H, W = zip(*path[1:])
    print(sum(data[H, W]))
    timer.stop()  # 7474.97ms
    # """
