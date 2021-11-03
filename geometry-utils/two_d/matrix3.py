import math

from two_d.vector2 import Vector2


class Matrix3:
    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        else:
            if len(vals) == 3 and len(vals[0]) == 3 and isinstance(vals, list):
                self.vals = vals

    def make_translation(self, other):
        if isinstance(other, Vector2):
            self.set_identity()
            self.vals[0][2] = other.x
            self.vals[1][2] = other.y

    def set_identity(self):
        self.vals = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    def make_rotation(self, other):
        if isinstance(other, float):
            self.set_identity()
            self.vals[0][0] = math.cos(other)
            self.vals[0][1] = -math.sin(other)
            self.vals[1][0] = math.sin(other)
            self.vals[1][1] = math.cos(other)

    def __mul__(self, other):
        result = Matrix3()

        if isinstance(other, Matrix3):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]

        return result
