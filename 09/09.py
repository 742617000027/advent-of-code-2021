import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

import utils


class Conv(nn.Module):
    def __init__(self):
        super(Conv, self).__init__()
        self.in_conv = nn.Conv2d(in_channels=1,
                                 out_channels=4,
                                 kernel_size=(3, 3),
                                 bias=False)
        self.out_conv = nn.Conv2d(in_channels=4,
                                  out_channels=1,
                                  kernel_size=(1, 1),
                                  bias=False)
        self.init_weights()

    def forward(self, data):
        x = F.pad(data, (1, 1, 1, 1), mode='constant', value=10.)
        x = self.in_conv(x)
        x = torch.sign(x)
        x = self.out_conv(x)
        return x == -4

    def init_weights(self):
        self.in_conv.weight[..., :] = 0
        self.in_conv.weight[..., 1, 1] = 1
        for i, (h, w) in enumerate([(0, 1), (1, 2), (2, 1), (1, 0)]):
            self.in_conv.weight[i, :, h, w] = -1
        self.out_conv.weight[..., :] = 1


def floodfill(point, data):
    h, w = data.shape
    y, x = point
    if data[y, x] != 0 or data[y, x] == 1:
        return
    else:
        data[y, x] = 1
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= y + dy <= h - 1 and 0 <= x + dx <= w:
                floodfill((y + dy, x + dx), data)


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = torch.tensor([[float(elem) for elem in line] for line in utils.read_str_lines()])[None, None, :, :]
    conv = Conv()
    with torch.no_grad():
        lows = conv(data)
    risk = torch.sum(lows * (data + 1))
    print(risk.item())
    timer.stop()  # 5.50ms
    """

    # Part 2
    # """
    timer.start()
    data = torch.tensor([[float(elem) for elem in line] for line in utils.read_str_lines()])[None, None, :, :]
    conv = Conv()
    with torch.no_grad():
        lows = conv(data)
    data = F.pad(data, (1, 1, 1, 1), value=9.).squeeze().numpy()
    lows = F.pad(lows, (1, 1, 1, 1)).squeeze().numpy()
    data[data != 9] = 0
    data[data == 9] = -1
    sizes = []
    for low in zip(*np.where(lows)):
        before = np.sum(data)
        floodfill(low, data)
        sizes.append(np.abs(np.sum(data) - before))
    print(int(np.prod(sorted(sizes)[-3:])))
    timer.stop()  # 104.53ms
    # """
