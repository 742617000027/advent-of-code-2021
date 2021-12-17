from math import prod

import utils


def hex2bin(data):
    return ''.join([bin(int(elem, base=16)).replace("0b", "").zfill(4) for elem in data])


def unpack(binary):
    version = int(binary[:3], base=2)
    type_id = int(binary[3:6], base=2)
    body = binary[6:]
    return version, type_id, body


def evaluate(packet):
    if packet['typeId'] == 4:
        return packet['value']
    local = [evaluate(child) for child in packet['contents']]
    match packet['typeId']:
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


def parse_literal(packet, body):
    literal = ''
    for i in range(0, len(body), 5):
        literal += body[i + 1:i + 5]
        if body[i] == '0':
            packet['len'] = 6 + len(body[:i + 5])
            packet['value'] = int(literal, base=2)
            break


def parse_operator(packet, body):
    length_type, body = body[0], body[1:]
    length = 15 if length_type == '0' else 11
    limit, body = int(body[:length], base=2), body[length:]
    packet['len'] = 6 + 1 + length
    packet['contents'] = []
    bits_parsed, packets_parsed = 0, 0
    while (bits_parsed if length_type == '0' else packets_parsed) < limit:
        subpacket = dict()
        interpreter(body[bits_parsed:], subpacket)
        packet['version']['aggregate'] += subpacket['version']['aggregate']
        bits_parsed += subpacket['len']
        packets_parsed += 1
        packet['contents'].append(subpacket)
    packet['len'] += bits_parsed
    packet['value'] = evaluate(packet)


def interpreter(binary, packet):
    version, type_id, body = unpack(binary)
    packet['version'] = {
        'self': version,
        'aggregate': version
    }
    packet['typeId'] = type_id
    if type_id == 4:
        parse_literal(packet, body)
    else:
        parse_operator(packet, body)


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = hex2bin(utils.read_str_lines()[0])
    packet = dict()
    interpreter(data, packet)
    print(packet['version']['aggregate'])
    timer.stop()  # 1.78ms
    """

    # Part 2
    # """
    timer.start()
    data = hex2bin(utils.read_str_lines()[0])
    packet = dict()
    interpreter(data, packet)
    print(packet['value'])  # 1.93ms
    timer.stop()
    # """
