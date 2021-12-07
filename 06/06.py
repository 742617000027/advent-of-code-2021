import utils


def evolve(days, fishies):
    for _ in range(days):
        fishies[7] += fishies[0]
        fishies = {
            day: amount
            for day, amount
            in zip(list(fishies.keys()),
                   list(fishies.values())[1:] + [fishies[0]])
        }
    return sum(fishies.values())


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_int_sequence()
    fishies = {day: data.count(day) for day in range(9)}
    print(evolve(80, fishies))
    timer.stop()  # 0.24ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_int_sequence()
    fishies = {day: data.count(day) for day in range(9)}
    print(evolve(256, fishies))
    timer.stop()  # 0.41ms
    # """
