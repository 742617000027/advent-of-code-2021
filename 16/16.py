from math import prod

import utils


def hex2bin(data):
    ret = ''
    for hexa in data:
        ret += bin(int(hexa, base=16)).replace("0b", "").zfill(4)
    return ret


def parse_packet(binary):
    version = int(binary[:3], base=2)
    type_id = int(binary[3:6], base=2)
    body = binary[6:]
    return version, type_id, body


def parse_subpacket(bits, body, bits_parsed, packets_parsed):
    bits['contents'].append(dict())
    interpreter(body[bits_parsed:], bits['contents'][-1])
    bits_parsed += bits['contents'][-1]['len']
    packets_parsed += 1
    return bits_parsed, packets_parsed


def interpreter(binary, bits):
    version, type_id, body = parse_packet(binary)
    bits['version'] = version
    bits['typeId'] = type_id

    if type_id == 4:
        literal = ''
        for i in range(0, len(body), 5):
            literal += body[i + 1:i + 5]
            if body[i] == '0':
                bits['type'] = 'literal'
                bits['binary'] = binary[:i + 11]
                bits['len'] = len(binary[:i + 11])
                bits['contents'] = int(literal, base=2)
                break
    else:
        length_type, body = body[0], body[1:]
        length = 15 if length_type == '0' else 11
        N, body = int(body[:length], base=2), body[length:]
        bits['type'] = 'operator'
        bits['binary'] = binary
        bits['len'] = 6 + 1 + length
        bits['contents'] = []
        bits_parsed = 0
        packets_parsed = 0
        while (bits_parsed if length_type == '0' else packets_parsed) < N:
            bits_parsed, packets_parsed = parse_subpacket(bits, body, bits_parsed, packets_parsed)
        bits['len'] += bits_parsed


def total_version(bits):
    global total
    total += bits['version']
    if isinstance(bits['contents'], list):
        for child in bits['contents']:
            total_version(child)


def evaluate(bits):
    if bits['typeId'] == 4:
        return bits['contents']
    local = [evaluate(child) for child in bits['contents']]
    match bits['typeId']:
        case 0:
            return sum(local)
        case 1:
            return prod(local)
        case 2:
            return min(local)
        case 3:
            return max(local)
        case 5:
            return (local[0] > local[1]) * 1
        case 6:
            return (local[0] < local[1]) * 1
        case 7:
            return (local[0] == local[1]) * 1


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = hex2bin(utils.read_str_lines()[0])
    BITS = dict()
    interpreter(data, BITS)
    total = 0
    total_version(BITS)
    print(total)
    timer.stop()  # 1.31ms
    """

    # Part 2
    # """
    timer.start()
    data = hex2bin(utils.read_str_lines()[0])
    BITS = dict()
    interpreter(data, BITS)
    total = evaluate(BITS)
    print(total)  # 1.78ms
    timer.stop()
    # """
