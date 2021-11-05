from math import cos, sin

from two_d.vector2 import Vector2


class Matrix3:
    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        else:
            if len(vals) == 3 and len(vals[0]) == 3 and isinstance(vals, list):
                self.vals = vals

    def set_identity(self):
        self.vals = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    def __mul__(self, other):
        result = Matrix3()

        if isinstance(other, Matrix3):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]

        return result

    def __eq__(self, other):
        return [[True if i == j else False for i in self.vals] for j in other.vals]

    @classmethod
    def make_translation(cls, other):
        mat = cls
        if isinstance(other, Vector2):
            mat.vals = [[1.0, 0.0, other.x],
                        [0.0, 1.0, other.y],
                        [0.0, 0.0, 1.0]]

            return mat

    @classmethod
    def make_rotation(cls, theta):
        mat = cls
        if isinstance(theta, float):
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[cos_theta, -sin_theta, 0.0],
                        [sin_theta,  cos_theta, 0.0],
                        [0.0,        0.0,       1.0]]
