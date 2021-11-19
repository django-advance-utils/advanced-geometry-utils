import inspect
from math import cos, sin

from maths_utility import is_list, is_float
from three_d.vector3 import is_vector3


class Matrix4:
    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        elif is_list(vals) and len(vals) == 4 and len(vals[0]) == 4:
            self.vals = vals
        else:
            if not is_list(vals):
                raise TypeError("Matrix4 argument must be a list")
            if not len(vals) == 4 or not len(vals[0]) == 4:
                raise AttributeError("Input Matrix must be 4 x 4")

    def set_identity(self):
        self.vals = [[1.0 if i == j else 0.0 for i in range(4)] for j in range(4)]

    def __mul__(self, other):
        if is_matrix4(other):
            result = Matrix4()
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result
        raise TypeError("Multiplication must be done with an object of Matrix4")

    def __eq__(self, other):
        if is_matrix4(other) or inspect.isclass(other):  # revisit
            return [[True if i == j else False for i in self.vals] for j in other.vals]
        raise TypeError("Comparison must be with another object of Matrix4")

    @classmethod
    def make_translation(cls, vector):
        if is_vector3(vector):
            mat = cls
            mat.vals = [[1.0, 0.0, 0.0, vector.x],
                        [0.0, 1.0, 0.0, vector.y],
                        [0.0, 0.0, 1.0, vector.z],
                        [0.0, 0.0, 0.0, 1.0]]

            return mat
        raise TypeError("Translation must be with an object of Vector3")

    @classmethod
    def make_x_rotation(cls, theta):
        if is_float(theta):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[1.0,  0.0,       0.0,       0.0],
                        [0.0,  cos_theta, sin_theta, 0.0],
                        [0.0, -sin_theta, cos_theta, 0.0],
                        [0.0,  0.0,       0.0,       1.0]]

            return mat
        raise TypeError("X rotation must be with a float")

    @classmethod
    def make_y_rotation(cls, theta):
        if is_float(theta):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[cos_theta, 0.0, -sin_theta, 0.0],
                        [0.0,       1.0,  0.0,       0.0],
                        [sin_theta, 0.0,  cos_theta, 0.0],
                        [0.0,       0.0,  0.0,       1.0]]

            return mat
        raise TypeError("Y rotation must be with a float")

    @classmethod
    def make_z_rotation(cls, theta):
        if is_float(theta):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[cos_theta, -sin_theta, 0.0, 0.0],
                        [sin_theta,  cos_theta, 0.0, 0.0],
                        [0.0,        0.0,       1.0, 0.0],
                        [0.0,        0.0,       0.0, 1.0]]

            return mat
        raise TypeError("Z rotation must be with a float")


def is_matrix4(input_variable):
    return isinstance(input_variable, Matrix4)
