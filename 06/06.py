import utils


def evolve(days, fishies):
    for _ in range(days):
        fishies[7] += fishies[0]
        fishies = {day: amount for day, amount in zip(list(fishies.keys()), list(fishies.values())[1:] + [fishies[0]])}
    return sum(fishies.values())


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()[0].split(',')
    fishies = {day: data.count(f'{day}') for day in range(9)}
    print(evolve(80, fishies))
    timer.stop()  # 0.24ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()[0].split(',')
    fishies = {day: data.count(f'{day}') for day in range(9)}
    print(evolve(256, fishies))
    timer.stop()  # 0.41ms
    # """
