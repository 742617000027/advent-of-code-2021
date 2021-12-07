import utils


def mcv(data):
    n_lines = len(data)
    n_bits = len(data[0])
    return [sorted(line[i] for line in data)[n_lines // 2] for i in range(n_bits)]


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    flip = {'0': '1', '1': '0'}
    n_lines = len(data)
    n_bits = len(data[0])
    gamma = int(''.join(mcv(data)), 2)
    epsilon = int(''.join(flip[elem] for elem in f'{gamma:b}'), 2)
    print(gamma * epsilon)
    timer.stop()  # 0.09ms
    """

    # Part 2
    # """
    timer.start()
    data = utils.read_str_lines()
    n_bits = len(data[0])

    oxygen = data.copy()
    co2 = data.copy()

    for i in range(n_bits):

        if len(oxygen) == len(co2) == 1:
            break

        if len(oxygen) > 1:
            mcv_oxygen = mcv(oxygen)
            oxygen = [line for line in oxygen if line[i] == mcv_oxygen[i]]

        if len(co2) > 1:
            mcv_co2 = mcv(co2)
            co2 = [line for line in co2 if line[i] != mcv_co2[i]]

    oxygen = int(oxygen[0], 2)
    co2 = int(co2[0], 2)
    print(oxygen * co2)
    timer.stop()  # 4.93ms
    # """
