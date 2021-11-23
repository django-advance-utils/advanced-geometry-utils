import inspect
from math import cos, sin

from maths_utility import is_list, is_int_or_float
from two_d.vector2 import is_vector2


class Matrix3:
    """
    A class to create a 3 x 3 matrix

    Attributes:
    ___________
    vals:   int or float
            the elements of the matrix

    Methods:
    ________
    set_identity(): Matrix3
        Returns a 3 x 3 identity matrix
    __mul__(Matrix3): Matrix3
        Returns the multiplication of the matrix with another 3 x 3 matrix
    __eq__(Matrix3): bool
        Returns the equality comparison of the matrix with another 3 x 3 matrix
    make_translation(Vector2): Matrix3
        Creates a 3 x 3 translation matrix
    make_rotation(int or float): Matrix3
        Creates a 3 x 3 rotation matrix
    """
    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        elif is_list(vals) and len(vals) == 3 and len(vals[0]) == 3:
            self.vals = vals
        else:
            if not is_list(vals):
                raise TypeError("Matrix3 argument must be a list")
            if not len(vals) == 3 or not len(vals[0]) == 3:
                raise AttributeError("Input Matrix must be 3 x 3")

    def set_identity(self):
        """
        Converts the matrix to an identity matrix

        :return:the identity matrix
        :rtype: Matrix3
        """
        self.vals = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    def __mul__(self, other):
        """
        Calculates the matrix multiplication of self with another 3 x 3 matrix

        :param  other: the right hand side matrix
        :type   other: Matrix3
        :return:the resulting multiplied matrix
        :rtype: Matrix3
        :raises:TypeError: wrong argument type
        """
        if is_matrix3(other):
            result = Matrix3()
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result
        raise TypeError("Multiplication must be done with an object of Matrix3")

    def __eq__(self, other):
        """
        Compares the equality of self and other 3 x 3 matrix.

        :param  other: the other matrix
        :type   other: Matrix3
        :return:the point equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_matrix3(other) or inspect.isclass(other):  # revisit
            return [[True if i == j else False for i in self.vals] for j in other.vals]
        raise TypeError("Comparison must be with another object of Matrix3")

    @classmethod
    def make_translation(cls, vector):
        """
        Creates a translation matrix using the 2D vector

        :param  vector: the translation vector
        :type   vector: Vector2
        :return:translation matrix
        :rtype: Matrix3
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(vector):
            mat = cls
            mat.vals = [[1.0, 0.0, vector.x],
                        [0.0, 1.0, vector.y],
                        [0.0, 0.0, 1.0]]

            return mat
        raise TypeError("Translation must be with an object of Vector2")

    @classmethod
    def make_rotation(cls, theta):
        """
        Creates a rotation matrix using an angle

        :param  theta: the angle of rotation
        :type   theta: int/float
        :return:rotation matrix
        :rtype: Matrix3
        :raises:TypeError: Wrong argument type
        """

        if is_int_or_float(theta):
            mat = cls
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            mat.vals = [[cos_theta, -sin_theta, 0.0],
                        [sin_theta,  cos_theta, 0.0],
                        [0.0,        0.0,       1.0]]

            return mat
        raise TypeError("Rotation must be with an int or float")


def is_matrix3(input_variable):
    return isinstance(input_variable, Matrix3)
