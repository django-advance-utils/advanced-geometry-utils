from math import cos, sin

from maths_utility import is_list, is_float
from two_d.vector2 import is_vector2


class Matrix3:
    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        if is_list(vals) and len(vals) == 3 and len(vals[0]) == 3:
            self.vals = vals

    def set_identity(self):
        self.vals = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    def __mul__(self, other):
        if is_matrix3(other):
            result = Matrix3()
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result

    def __eq__(self, other):
        return [[True if i == j else False for i in self.vals] for j in other.vals]

    @classmethod
    def make_translation(cls, vector):
        if is_vector2(vector):
            mat = cls
            mat.vals = [[1.0, 0.0, vector.x],
                        [0.0, 1.0, vector.y],
                        [0.0, 0.0, 1.0]]

            return mat

    @classmethod
    def make_rotation(cls, theta):
        if is_float(theta):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[cos_theta, -sin_theta, 0.0],
                        [sin_theta,  cos_theta, 0.0],
                        [0.0,        0.0,       1.0]]

            return mat


def is_matrix3(input_variable):
    return isinstance(input_variable, Matrix3)
