from collections import Counter

import utils


def evolve(days, fishies):
    for _ in range(days):
        fishies[7] += fishies[0]
        fishies = {day: amount for day, amount in zip(list(fishies.keys()), list(fishies.values())[1:] + [fishies[0]])}
    return sum(list(fishies.values()))


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()
    counts = Counter([int(fish) for fish in data[0].split(',')])
    fishies = {day: counts[day] for day in range(9)}
    print(evolve(80, fishies))
    timer.stop()  # 0.24ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()
    counts = Counter([int(fish) for fish in data[0].split(',')])
    fishies = {day: counts[day] for day in range(9)}
    print(evolve(256, fishies))
    timer.stop()  # 0.41ms
    # """
