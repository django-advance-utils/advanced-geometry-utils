from math import cos, sin

from three_d.vector3 import Vector3


class Matrix4:
    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()

        else:
            if len(vals) == 4 and len(vals[0]) == 4 and isinstance(vals, list):
                self.vals = vals

    def set_identity(self):
        self.vals = [[1.0 if i == j else 0.0 for i in range(4)] for j in range(4)]

    def make_translation(self, other):
        if isinstance(other, Vector3):
            self.set_identity()
            self.vals[0][3] = other.x
            self.vals[1][3] = other.y
            self.vals[2][3] = other.z

    def make_x_rotation(self, theta):
        if isinstance(theta, float):
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            self.set_identity()
            self.vals[1][1] = cos_theta
            self.vals[1][2] = sin_theta
            self.vals[2][1] = -sin_theta
            self.vals[2][2] = cos_theta

    def make_y_rotation(self, theta):
        if isinstance(theta, float):
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            self.set_identity()
            self.vals[0][0] = cos_theta
            self.vals[0][2] = -sin_theta
            self.vals[2][0] = sin_theta
            self.vals[2][2] = cos_theta

    def make_z_rotation(self, theta):
        if isinstance(theta, float):
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            self.set_identity()
            self.vals[0][0] = cos_theta
            self.vals[0][1] = -sin_theta
            self.vals[1][0] = sin_theta
            self.vals[1][1] = cos_theta

    def __mul__(self, other):
        result = Matrix4()

        if isinstance(other, Matrix4):
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]

        return result

