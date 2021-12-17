from math import prod

import utils


class Version():
    def __init__(self, version):
        self.own = version
        self.aggregate = version


class Packet():
    def __init__(self, binary):
        v, t, b = self.unpack(binary)
        self.version = Version(v)
        self.type = t
        self.body = b
        self.contents = [] if self.type != 4 else None
        self.length = None
        self.value = None
        self.parse_literal() if self.type == 4 else self.parse_operator()

    def __len__(self):
        return self.length

    def unpack(self, binary):
        return int(binary[:3], base=2), int(binary[3:6], base=2), binary[6:]

    def parse_literal(self):
        literal = ''
        for i in range(0, len(self.body), 5):
            literal += self.body[i + 1:i + 5]
            if self.body[i] == '0':
                self.length = 6 + len(self.body[:i + 5])
                self.value = int(literal, base=2)
                break

    def parse_operator(self):
        length_type, self.body = self.body[0], self.body[1:]
        length = 15 if length_type == '0' else 11
        limit, self.body = int(self.body[:length], base=2), self.body[length:]
        self.length = 6 + 1 + length
        bits_parsed, packets_parsed = 0, 0
        while (bits_parsed if length_type == '0' else packets_parsed) < limit:
            subpacket = Packet(self.body[bits_parsed:])
            self.version.aggregate += subpacket.version.aggregate
            bits_parsed += len(subpacket)
            packets_parsed += 1
            self.contents.append(subpacket)
        self.length += bits_parsed
        self.value = self.evaluate()

    def evaluate(self):
        if self.type == 4:
            return self.value
        local = [child.evaluate() for child in self.contents]
        match self.type:
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


def hex2bin(data):
    return ''.join([bin(int(elem, base=16)).replace("0b", "").zfill(4) for elem in data])


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = hex2bin(utils.read_str_lines()[0])
    packet = Packet(data)
    print(packet.version.aggregate)
    timer.stop()  # 2.32ms
    """

    # Part 2
    # """
    timer.start()
    data = hex2bin(utils.read_str_lines()[0])
    packet = Packet(data)
    print(packet.value)  # 2.18ms
    timer.stop()
    # """
