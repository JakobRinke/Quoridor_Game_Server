import math


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def switched(self):
        return Vector(self.y, self.x)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Wall:
    def __init__(self, position_block1_start: Vector, position_block1_end, position_block2_start, position_block2_end):
        self.pbs1 = position_block1_start
        self.pbe1 = position_block1_end
        self.pbs2 = position_block2_start
        self.pbe2 = position_block2_end

    def blocks(self, pos1: Vector, pos2: Vector):
        return pos1 == self.pbs1 and pos2 == self.pbe1 or \
            pos2 == self.pbs1 and pos1 == self.pbe1 or \
            pos1 == self.pbs2 and pos2 == self.pbe2 or \
            pos2 == self.pbs2 and pos1 == self.pbe2
