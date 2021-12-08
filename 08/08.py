import utils


def rest(a, b):
    return len(''.join([letter for letter in a if letter not in b]))


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = [segment for line in utils.read_str_lines() for segment in line.split(' | ')[1].split()]
    print(sum([len(elem) in [2, 3, 4, 7] for elem in data]))
    timer.stop()  # 0.88ms
    # """

    # Part 2
    # """
    timer.start()
    unique_patterns = []
    output_values = []

    for line in utils.read_str_lines():
        patterns, values = line.split(' | ')
        unique_patterns.append([''.join(sorted(pattern)) for pattern in patterns.split()])
        output_values.append([''.join(sorted(value)) for value in values.split()])

    total = 0
    for patterns, values in zip(unique_patterns, output_values):
        lens = [len(pattern) for pattern in patterns]
        solution = {
            1: patterns[lens.index(2)],
            4: patterns[lens.index(4)],
            7: patterns[lens.index(3)],
            8: 'abcdefg'
        }

        for pattern in patterns:

            match (rest(pattern, solution[4]), rest(pattern, solution[7]), len(pattern)):
                case (2, 2, 5):
                    solution[3] = pattern
                case (2, 3, 5):
                    solution[5] = pattern
                case (2, 3, 6):
                    solution[9] = pattern
                case (3, 3, 5):
                    solution[2] = pattern
                case (3, 3, 6):
                    solution[0] = pattern
                case (3, 4, 6):
                    solution[6] = pattern

        reverse_solution = {pattern: f'{digit}' for digit, pattern in solution.items()}
        total += int(''.join([reverse_solution[value] for value in values]))

    print(total)
    timer.stop()  # 4.52ms
    # """
