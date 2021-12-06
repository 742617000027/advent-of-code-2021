import utils


def evolve(N, fishies):
    for i in range(N):
        spawning = fishies[0]
        fishies[7] += spawning
        fishies = {day: amount for day, amount in zip(list(fishies.keys()), list(fishies.values())[1:])}
        fishies[9] = spawning
    return sum(list(fishies.values())[:-1])


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()
    fishies = {days: 0 for days in range(10)}
    for fish in  [int(fish) for fish in data[0].split(',')]:
        fishies[fish] += 1
    print(evolve(80, fishies))
    timer.stop()  # 0.69ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()
    fishies = {days: 0 for days in range(10)}
    for fish in [int(fish) for fish in data[0].split(',')]:
        fishies[fish] += 1
    print(evolve(256, fishies))
    timer.stop()  # 0.41ms
    # """
