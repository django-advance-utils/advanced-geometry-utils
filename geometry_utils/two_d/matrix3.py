from math import cos, sin

from geometry_utils.maths_utility import is_list, is_int_or_float, are_ints_or_floats, is_float, degrees_to_radians
from geometry_utils.two_d.point2 import is_point2, Point2
from geometry_utils.two_d.vector2 import Vector2, is_vector2


class Matrix3:
    """
    A class to create a 3 x 3 matrix

    Attributes:
    ___________
    vals:   int/float
            the elements of the matrix

    Methods:
    ________
    set_identity(): Matrix3
        Returns a 3 x 3 identity matrix
    __mul__(Matrix3/Vector2): Matrix3/Vector2
        Returns the multiplication of the matrix with another 3 x 3 matrix or 2D vector
    __eq__(Matrix3): bool
        Returns the equality comparison of the matrix with another 3 x 3 matrix
    make_translation(Vector2): Matrix3
        Creates a 3 x 3 translation matrix
    make_rotation(int/float): Matrix3
        Creates a 3 x 3 rotation matrix
    """

    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        elif is_list(vals) and len(vals) == 3 and len(vals[0]) == 3 and are_ints_or_floats(vals[0]) and \
                are_ints_or_floats(vals[0]) and are_ints_or_floats(vals[0]):
            self.vals = vals
        else:
            if not is_list(vals):
                raise TypeError("Matrix3 argument must be a list")
            if not len(vals) == 3 or not len(vals[0]) == 3:
                raise AttributeError("Input Matrix must be 3 x 3")
            if not are_ints_or_floats(vals[0]) or are_ints_or_floats(vals[0]) or are_ints_or_floats(vals[0]):
                raise TypeError("Matrix3 argument list must contain int or float")

    def __str__(self):
        return ("Matrix3(vals:" + str(self.vals[0]) + "\n\t\t\t" + str(self.vals[1]) + "\n\t\t\t" +
                str(self.vals[2]) + ")")

    def set_identity(self):
        """
        Converts the matrix to an identity matrix

        :return: the identity matrix
        :rtype:  Matrix3
        """
        self.vals = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    def __mul__(self, other):
        """
        Calculates the multiplication of the matrix with another 3 x 3 matrix or a 2D vector

        :param   other: the right hand side 3 x 3 matrix or 2D vector
        :type    other: Matrix3/Vector2
        :return: the resulting multiplied matrix or vector
        :rtype:  Matrix3/Vector2
        :raises: TypeError: wrong argument type
        """
        if is_int_or_float(other):
            result = Matrix3()
            for row in range(3):
                for column in range(3):
                    result.vals[row][column] = self.vals[row][column] * other
            return result

        if is_matrix3(other):
            result = Matrix3()
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result

        if is_vector2(other) or is_point2(other):
            if is_vector2(other):
                result = Vector2()
            else:
                result = Point2()
            result.x = self.vals[0][0] * other.x + self.vals[0][1] * other.y + self.vals[0][2] * other.w
            result.y = self.vals[1][0] * other.x + self.vals[1][1] * other.y + self.vals[1][2] * other.w
            result.w = self.vals[2][0] * other.x + self.vals[2][1] * other.y + self.vals[2][2] * other.w
            result.accuracy_fix()
            return result

        raise TypeError("Multiplication must be done with another 3 x 3 matrix, a 2D vector, a 2D point or a scalar")

    def __eq__(self, other):
        """
        Compares the equality of self and other 3 x 3 matrix.

        :param   other: the other matrix
        :type    other: Matrix3
        :return: the point equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_matrix3(other):
            return [[True if i == j else False for i in self.vals] for j in other.vals]
        raise TypeError("Comparison must be with another object of Matrix3")

    @classmethod
    def translation(cls, vector):
        """
        Creates a translation matrix using the 2D vector

        :param   vector: the translation vector
        :type    vector: Vector2
        :return: translation matrix
        :rtype:  Matrix3
        :raises: TypeError: Wrong argument type
        """
        if is_vector2(vector):
            mat = cls()
            mat.vals = [[1.0, 0.0, vector.x],
                        [0.0, 1.0, vector.y],
                        [0.0, 0.0, 1.0]]
            return mat
        raise TypeError("Translation must be with an object of Vector2")

    @classmethod
    def rotation(cls, theta, rad=False):
        """
        Creates a rotation matrix using an angle

        :param   theta: the angle of rotation
        :type    theta: int/float
        :return: rotation matrix
        :rtype:  Matrix3
        :raises: TypeError: Wrong argument type
        """

        if is_float(theta):
            mat = cls()
            if rad is False:
                theta = degrees_to_radians(theta)
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            negative_sin_theta = 0.0 if (-sin_theta == -0.0) else -sin_theta
            mat.vals = [[cos_theta, negative_sin_theta, 0.0],
                        [sin_theta, cos_theta, 0.0],
                        [0.0, 0.0, 1.0]]
            return mat
        raise TypeError("Rotation must be with a float")


def is_matrix3(input_variable):
    return isinstance(input_variable, Matrix3)
