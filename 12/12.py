import utils


def build(data):
    G = dict()
    for line in data:
        a, b = line.split('-')
        if a in G:
            G[a].append(b)
        else:
            G[a] = [b]
        if b in G:
            G[b].append(a)
        else:
            G[b] = [a]
    return G


def prune(G):
    dead_ends = set()
    while True:
        H = G.copy()
        for cave in G:
            if len(G[cave]) == 1 and G[cave][0].islower():
                dead_ends.add(cave)
                del H[cave]
        if G == H:
            break
        else:
            G = H
    for cave in G:
        G[cave] = [neighbor for neighbor in sorted(G[cave]) if neighbor not in dead_ends]
    return G


def traverse(G, current_cave, current_path=None, can_revisit=False):
    if current_path == None:
        current_path = []
    current_path.append(current_cave)
    for neighbor in G[current_cave]:
        if neighbor != 'start' and (neighbor.isupper() or (can_revisit or neighbor not in current_path)):
            if neighbor == 'end':
                PATHS.append(current_path + [neighbor])
            else:
                traverse(G,
                         neighbor,
                         current_path=current_path.copy(),
                         can_revisit=can_revisit and not (neighbor.islower() and neighbor in current_path))


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    G = prune(build(data))
    PATHS = []
    traverse(G, 'start')
    print(len(PATHS))
    timer.stop()  # 50.94ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_lines()
    G = build(data)
    PATHS = []
    traverse(G, 'start', can_revisit=True)
    print(len(PATHS))
    timer.stop()  # 610.58ms
    # """
