from math import cos, sin

from three_d.vector3 import Vector3


class Matrix4:
    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        if isinstance(vals, list) and len(vals) == 4 and len(vals[0]) == 4:
            self.vals = vals

    def set_identity(self):
        self.vals = [[1.0 if i == j else 0.0 for i in range(4)] for j in range(4)]

    def __mul__(self, other):
        if isinstance(other, Matrix4):
            result = Matrix4()
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result

    def __eq__(self, other):
        return [[True if i == j else False for i in self.vals] for j in other.vals]

    @classmethod
    def make_translation(cls, vector):
        if isinstance(vector, Vector3):
            mat = cls
            mat.vals = [[1.0, 0.0, 0.0, vector.x],
                        [0.0, 1.0, 0.0, vector.y],
                        [0.0, 0.0, 1.0, vector.z],
                        [0.0, 0.0, 0.0, 1.0]]

            return mat

    @classmethod
    def make_x_rotation(cls, theta):
        if isinstance(theta, float):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[1.0,  0.0,       0.0,       0.0],
                        [0.0,  cos_theta, sin_theta, 0.0],
                        [0.0, -sin_theta, cos_theta, 0.0],
                        [0.0,  0.0,       0.0,       1.0]]

            return mat

    @classmethod
    def make_y_rotation(cls, theta):
        if isinstance(theta, float):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[cos_theta, 0.0, -sin_theta, 0.0],
                        [0.0,       1.0,  0.0,       0.0],
                        [sin_theta, 0.0,  cos_theta, 0.0],
                        [0.0,       0.0,  0.0,       1.0]]

            return mat

    @classmethod
    def make_z_rotation(cls, theta):
        if isinstance(theta, float):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[cos_theta, -sin_theta, 0.0, 0.0],
                        [sin_theta,  cos_theta, 0.0, 0.0],
                        [0.0,        0.0,       1.0, 0.0],
                        [0.0,        0.0,       0.0, 1.0]]

            return mat
