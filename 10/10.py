import utils

if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    score = 0
    for line in data:
        close_next = []
        for ch in line:
            if ch in pairs:
                close_next.append(pairs[ch])
            else:
                if ch == close_next[-1]:
                    close_next = close_next[:-1]
                else:
                    score += points[ch]
                    break
    print(score)
    timer.stop()  # 1.36ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_lines()
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    scores = []
    for line in data:
        close_next = []
        corrupt = False
        for ch in line:
            if ch in pairs:
                close_next.append(pairs[ch])
            else:
                if ch == close_next[-1]:
                    close_next = close_next[:-1]
                else:
                    corrupt = True
                    break
        if corrupt:
            continue
        close_next = reversed(close_next)
        scores.append(0)
        for ch in close_next:
            scores[-1] *= 5
            scores[-1] += points[ch]
    print(sorted(scores)[len(scores) // 2])
    timer.stop()  # 1.42ms
    # """
