def read_int_sequence(file='input'):
    with open(file, 'r') as fp:
        sequence = [int(n) for n in fp.read().splitlines()]
    return sequence


def read_str_sequence(file='input'):
    with open(file, 'r') as fp:
        sequence = fp.read().splitlines()
    return sequence
