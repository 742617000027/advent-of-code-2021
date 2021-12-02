import utils

if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()
    cmds = [(elem.split(' ')[0], int(elem.split(' ')[1])) for elem in data]

    depth = horizontal = 0

    for cmd in cmds:
        match cmd:
            case ('forward', mag):
                horizontal += mag
            case ('down', mag):
                depth += mag
            case('up', mag):
                depth -= mag

    print(depth * horizontal)
    timer.stop()  # 2.74ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()
    cmds = [(elem.split(' ')[0], int(elem.split(' ')[1])) for elem in data]

    depth = horizontal = aim = 0

    for cmd in cmds:
        match cmd:
            case ('forward', mag):
                horizontal += mag
                depth += aim * mag
            case ('down', mag):
                aim += mag
            case ('up', mag):
                aim -= mag

    print(depth * horizontal)
    timer.stop()  # 2.84ms
    # """
