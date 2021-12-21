import numpy as np

import utils

TRANSFORMS = [(0, 0, 0), (0, 0, 90), (0, 0, 180), (0, 0, 270), (0, 90, 0), (0, 90, 90),
              (0, 90, 180), (0, 90, 270), (0, 180, 0), (0, 180, 90), (0, 180, 180), (0, 180, 270),
              (0, 270, 0), (0, 270, 90), (0, 270, 180), (0, 270, 270), (90, 0, 0), (90, 0, 90),
              (90, 0, 180), (90, 0, 270), (90, 180, 0), (90, 180, 90), (90, 180, 180), (90, 180, 270)]


def preprocess(data):
    scanners, scanner = [], []
    for line in data:
        if ',' in line:
            x, y, z = [int(elem) for elem in line.split(',')]
            scanner.append([x, y, z])
        if line == '':
            scanner = np.array(scanner)
            scanners.append(scanner)
            scanner = []
    scanners.append(np.array(scanner))

    return scanners


def rot(mat, transform):
    sin = {0: 0, 90: 1, 180: 0, 270: -1}
    cos = {0: 1, 90: 0, 180: -1, 270: 0}
    alpha, beta, gamma = transform
    rotmat = np.array([[cos[alpha] * cos[beta],
                        cos[alpha] * sin[beta] * sin[gamma] - sin[alpha] * cos[gamma],
                        cos[alpha] * sin[beta] * cos[gamma] + sin[alpha] * sin[gamma]],
                       [sin[alpha] * cos[beta],
                        sin[alpha] * sin[beta] * sin[gamma] + cos[alpha] * cos[gamma],
                        sin[alpha] * sin[beta] * cos[gamma] - cos[alpha] * sin[gamma]],
                       [-sin[beta],
                        cos[beta] * sin[gamma],
                        cos[beta] * cos[gamma]]])
    return np.matmul(rotmat, mat.T).T


def setlify(mat):
    return {tuple(vec) for vec in mat}


def distance(scanner, mode='first'):
    assert mode in ['first', 'all'], 'Mode must be one of either `first` or `all`.'
    if mode == 'first':
        return scanner - scanner[0], scanner[0]
    else:
        up = []
        for beacon in scanner:
            up.append((scanner - beacon, beacon))
        return up


def align(scanners):
    ref_distances = distance(scanners[0], 'all')
    scanner_pos = {
        0: np.zeros(3)
    }
    aligned = {0}
    while True:
        if len(aligned) == len(scanners):
            break
        for i, dud_scanner in enumerate(scanners):
            if i in aligned:
                continue
            done = False
            for dud_transform in TRANSFORMS:
                dud_rotation = rot(dud_scanner, dud_transform)
                dud_distances = distance(dud_rotation, 'all')
                for ref_u, ref_p in ref_distances:
                    for dud_u, dud_p in dud_distances:
                        intersection = setlify(ref_u).intersection(setlify(dud_u))
                        if len(intersection) >= 12:
                            print(f'{len(aligned)}/{len(scanners) - 1} | Scanner {i} aligned!')
                            aligned.add(i)
                            done = True
                            scanner_pos[i] = ref_p - dud_p
                            new = np.array([beacon for beacon in dud_u if tuple(beacon) not in setlify(ref_u)])
                            assembled = np.concatenate([ref_u, new]) + ref_p
                            ref_distances = distance(assembled, 'all')
                            break
                    if done:
                        break
                if done:
                    break
            if done:
                break
    global_u, global_p = ref_distances[0]
    return global_u + global_p, scanner_pos


def manhatten(scanner_positions):
    distances = np.zeros((len(scanner_positions), len(scanner_positions)))
    for i, val_i in scanner_positions.items():
        for j, val_j in scanner_positions.items():
            distances[i, j] = np.sum(np.abs(val_i - val_j))
    return distances.astype(int)


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = utils.read_str_lines()
    scanners = preprocess(data)
    beacons, scanner_positions = align(scanners)
    timer.stop()  # 4925529.38ms
    """

    # Part 2
    # """
    data = utils.read_str_lines()
    scanners = preprocess(data)
    beacons, scanner_positions = align(scanners)
    distances = manhatten(scanner_positions)
    print(np.max(distances))
    timer.stop()  # 5178738.21ms
    # """
