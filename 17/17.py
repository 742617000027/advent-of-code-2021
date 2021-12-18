import utils

if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = {
        elem.split('=')[0]: {
            'min': int(elem.split('=')[1].split('..')[0]),
            'max': int(elem.split('=')[1].split('..')[1])
        }
        for elem
        in utils.read_str_lines()[0].replace('target area: ', '').split(', ')
    }
    print(sum(range(abs(data['y']['min']))))
    timer.stop()  # 0.08ms
    """

    # Part 2
    # """
    timer.start()
    data = {
        elem.split('=')[0]: {
            'min': int(elem.split('=')[1].split('..')[0]),
            'max': int(elem.split('=')[1].split('..')[1])
        }
        for elem
        in utils.read_str_lines()[0].replace('target area: ', '').split(', ')
    }
    max_steps = 2 * abs(data['y']['min']) + 2
    x0_min = 0
    while sum(range(x0_min + 1)) < data['x']['min']:
        x0_min += 1
    x0_max = abs(data['x']['max'])
    y0_min = data['y']['min']
    y0_max = abs(data['y']['min']) - 1
    solutions = set()
    for steps in range(1, max_steps + 1):
        for x0 in range(x0_min, x0_max + 1):
            x_end_pos = x0 * (steps if steps <= x0 else x0) - sum(range((steps if steps <= x0 else x0)))
            if not data['x']['min'] <= x_end_pos <= data['x']['max']:
                continue
            for y0 in range(y0_min, y0_max + 1):
                y_end_pos = y0 * steps - sum(range(steps))
                if data['x']['min'] <= x_end_pos <= data['x']['max'] \
                        and data['y']['min'] <= y_end_pos <= data['y']['max']:
                    solutions.add((x0, y0))
    print(len(solutions))
    timer.stop()  # 118.45ms
    # """
