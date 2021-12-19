import json
from functools import reduce
from itertools import product
from math import ceil, floor

import utils


class Number():
    def __init__(self, raw, level=0, parent=None, root=None):

        if isinstance(raw, str):
            raw = json.loads(raw)

        self.__level = level
        self.__parent = parent
        self.__root = self if root is None else root
        if root is None:
            self.__exploded = False
            self.__splut = False

        left, right = raw
        self.left = Number(left, level + 1, self, self.__root) if isinstance(left, list) else left
        self.right = Number(right, level + 1, self, self.__root) if isinstance(right, list) else right

    def __add__(self, other):
        a = Number([self.listify(), other.listify()])
        b = a.listify().copy()
        a.reduce()
        while a.listify() != b:
            b = a.listify().copy()
            a.reduce()
        return a

    def __repr__(self):
        return f'{self.listify()}'

    def __str__(self):
        return f'{self.listify()}'

    def __getitem__(self, item):
        if item == 0:
            return self.left
        elif item == 1:
            return self.right
        else:
            raise NotImplementedError('Number must be indexed with either 0 for its left side or 1 for its right side.')

    def __setitem__(self, key, value):
        if key == 0:
            setattr(self, 'left', value)
        elif key == 1:
            setattr(self, 'right', value)
        else:
            raise NotImplementedError('Number must be indexed with either 0 for its left side or 1 for its right side.')

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= 1:
            ret = self[self.n]
            self.n += 1
            return ret
        else:
            raise StopIteration

    def listify(self):
        left = self.left if isinstance(self.left, int) else self.left.listify()
        right = self.right if isinstance(self.right, int) else self.right.listify()
        return [left, right]

    def magnitude(self):
        if isinstance(self.left, Number):
            self.left = self.left.magnitude() * 3
        else:
            self.left *= 3
        if isinstance(self.right, Number):
            self.right = self.right.magnitude() * 2
        else:
            self.right *= 2
        return self.left + self.right

    def reduce(self):
        self.__reduce_by_exploding()
        if self.__root.__exploded:
            self.__root.__exploded = False
            return
        self.__reduce_by_splitting()
        if self.__root.__splut:
            self.__root.__splut = False
        return

    def __reduce_by_exploding(self):
        if self.__root.__exploded:
            return
        else:
            if self.__level == 4:
                self.__explode()
                self.__root.__exploded = True
            else:
                for child in self:
                    if isinstance(child, Number):
                        child.__reduce_by_exploding()
                    if self.__root.__exploded:
                        break

    def __reduce_by_splitting(self):
        if self.__root.__splut:
            return
        else:
            for side, child in enumerate(self):
                if isinstance(child, int) and child >= 10:
                    self.__split(side)
                    self.__root.__splut = True
                    break
                elif isinstance(child, Number):
                    child.__reduce_by_splitting()
                    if self.__root.__splut:
                        break

    def __split(self, side):
        self[side] = Number([floor(self[side] / 2), ceil(self[side] / 2)],
                            level=self.__level + 1,
                            parent=self,
                            root=self.__root)

    def __explode(self):
        left_done, right_done = False, False

        if isinstance(self.__parent.left, int):
            self.__parent.left += self.left
            left_done = True
        elif isinstance(self.__parent.left, Number) and self.__parent.left != self:
            left_done = self.__add_to_sibling(self.__parent, 0)

        if isinstance(self.__parent.right, int):
            self.__parent.right += self.right
            right_done = True
        elif isinstance(self.__parent.right, Number) and self.__parent.right != self:
            right_done = self.__add_to_sibling(self.__parent, 1)

        if not left_done:
            self.__add_to_cousin(0)

        if not right_done:
            self.__add_to_cousin(1)

        if self.__parent.left == self:
            self.__parent.left = 0
        else:
            self.__parent.right = 0

    def __add_to_cousin(self, side):
        parent = self.__parent
        while parent.__parent is not None:
            if isinstance(parent.__parent[side], int):
                parent.__parent[side] += self[side]
                break
            if isinstance(parent.__parent[side], Number) and parent.__parent[side] != parent:
                done = self.__add_to_sibling(parent.__parent, side)
                if done:
                    break
            parent = parent.__parent

    def __add_to_sibling(self, parent, side):
        other = 1 if side == 0 else 0
        neighbor = parent[side]
        while isinstance(neighbor[other], Number):
            neighbor = neighbor[other]
        if isinstance(neighbor[other], int):
            neighbor[other] += self[side]
            return True
        return False


if __name__ == '__main__':
    timer = utils.Timer()

    # Part 1
    """
    timer.start()
    data = [Number(line) for line in utils.read_str_lines()]
    S = reduce(lambda a, b: a + b, data)
    print(S.magnitude())
    timer.stop()  # 450.62ms
    """

    # Part 2
    # """
    timer.start()
    data = [Number(line) for line in utils.read_str_lines()]
    maximum = 0
    for i, j in product(range(len(data)), repeat=2):
        S = data[i] + data[j]
        mag = S.magnitude()
        maximum = mag if mag > maximum else maximum
    print(maximum)
    timer.stop()  # 5748.92ms
    # """
