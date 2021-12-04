import numpy as np

import utils


def parse_boards(data):
    boards = []
    this_board = []
    for line in data:
        if line == '':
            boards.append(np.array(this_board))
            this_board = []
        else:
            this_board.append([int(elem) + 1 for elem in line.split()])
    boards.append(np.array(this_board))
    return boards


def bingo(numbers, boards, mode='first'):
    assert mode in ['first', 'last'], 'Mode must be one of `first` or `last`.'
    winning_boards = set()
    for i, number in enumerate(numbers):
        for j, board in enumerate(boards):
            board[board == number] *= -1
            if i >= 4:
                v = np.all(np.sign(board) == -1, axis=0)
                h = np.all(np.sign(board) == -1, axis=1)
                if np.any(h) or np.any(v):
                    winning_boards.add(j)
                    if mode == 'first' or (mode == 'last' and len(winning_boards) == len(boards)):
                        return (np.sum(board[np.sign(board) == 1] - 1)) * (number - 1)


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_sequence()
    numbers = [int(elem) + 1 for elem in data[0].split(',')]
    boards = parse_boards(data[2:])
    score= bingo(numbers, boards)
    print(score)
    timer.stop()  # 171.68ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_sequence()
    numbers = [int(elem) + 1 for elem in data[0].split(',')]
    boards = parse_boards(data[2:])
    score = bingo(numbers, boards, 'last')
    print(score)
    timer.stop()  # 340.16ms
    # """
