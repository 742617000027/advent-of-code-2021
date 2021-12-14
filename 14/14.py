from collections import defaultdict

import utils


def parse_data(data):
    template = data[0]
    insertions = dict()
    for elem in data[2:]:
        pair, insertion = elem.split(' -> ')
        insertions[pair] = (pair[0] + insertion, insertion + pair[1])
    return template, insertions


def solve(template, insertions, steps):
    pairs = defaultdict(lambda: int())
    for i in range(len(template) - 1):
        pairs[template[i:i + 2]] += 1
    for _ in range(steps):
        temp_pairs = pairs.copy()
        for pair in pairs:
            a, b = insertions[pair]
            temp_pairs[a] += pairs[pair]
            temp_pairs[b] += pairs[pair]
            temp_pairs[pair] -= pairs[pair]
        pairs = temp_pairs
    counter = defaultdict(lambda: int())
    for pair, value in pairs.items():
        counter[pair[0]] += value
    counter[template[-1]] += 1
    return (max(counter.values()) - min(counter.values()))


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    template, insertions = parse_data(data)
    print(solve(template, insertions, 10))
    timer.stop()  # 0.65ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_lines()
    template, insertions = parse_data(data)
    print(solve(template, insertions, 40))
    timer.stop()  # 1.40ms
    # """
