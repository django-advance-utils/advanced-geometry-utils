from math import cos, sin

from geometry_utils.maths_utility import is_list, is_int_or_float
from geometry_utils.three_d.vector3 import Vector3, is_vector3


class Matrix4:
    """
    A class to create a 4 x 4 matrix

    Attributes:
    ___________
    vals:   int/float
            the elements of the matrix

    Methods:
    ________
    set_identity(): Matrix4
        Returns a 4 x 4 identity matrix
    __mul__(Matrix4/Vector3): Matrix4/Vector3
        Returns the multiplication of the matrix with another 4 x 4 matrix or 3D vector
    __eq__(Matrix4): bool
        Returns the equality comparison of the matrix with another 4 x 4 matrix
    make_translation(Vector2): Matrix4
        Creates a 4 x 4 translation matrix
    make_x_rotation(int/float): Matrix4
        Creates a 4 x 4 rotation matrix around x-axis
    make_y_rotation(int/float): Matrix4
        Creates a 4 x 4 rotation matrix around y-axis
    make_z_rotation(int/float): Matrix4
        Creates a 4 x 4 rotation matrix around z-axis
    """

    def __init__(self, vals=None):
        if vals is None:
            self.set_identity()
        elif is_list(vals) and len(vals) == 4 and len(vals[0]) == 4 and is_int_or_float(vals[0][0]):
            self.vals = vals
        else:
            if not is_list(vals):
                raise TypeError("Matrix4 argument must be a list")
            if not len(vals) == 4 or not len(vals[0]) == 4:
                raise AttributeError("Input Matrix must be 4 x 4")
            if not is_int_or_float(vals[0][0]):
                raise TypeError("Matrix4 argument list must contain int or float")

    def set_identity(self):
        """
        Converts the matrix to an identity matrix

        :return: the identity matrix
        :rtype:  Matrix4
        """
        self.vals = [[1 if i == j else 0.0 for i in range(4)] for j in range(4)]

    def __mul__(self, other):
        """
        Calculates the multiplication of the matrix with another 4 x 4 matrix or a 3D vector

        :param   other: the right hand side 4 x 4 matrix or 3D vector
        :type    other: Matrix4/Vector3
        :return: the resulting multiplied matrix or vector
        :rtype:  Matrix4/Vector3
        :raises: TypeError: wrong argument type
        """
        if is_matrix4(other):
            result = Matrix4()
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result

        if is_vector3(other):
            result = Vector3()
            result.x = (self.vals[0][0] * other.x + self.vals[0][1] * other.y +
                        self.vals[0][2] * other.z + self.vals[0][3] * other.w)
            result.y = (self.vals[1][0] * other.x + self.vals[1][1] * other.y +
                        self.vals[1][2] * other.z + self.vals[1][3] * other.w)
            result.z = (self.vals[2][0] * other.x + self.vals[2][1] * other.y +
                        self.vals[2][2] * other.z + self.vals[2][3] * other.w)
            result.w = (self.vals[3][0] * other.x + self.vals[3][1] * other.y +
                        self.vals[3][2] * other.z + self.vals[3][3] * other.w)

            return result
        raise TypeError("Multiplication must be done with a 4 x 4 matrix or 3D vector")

    def __eq__(self, other):
        """
        Compares the equality of self and other 4 x 4 matrix.

        :param   other: the other matrix
        :type    other: Matrix4
        :return: the point equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_matrix4(other):
            return [[True if i == j else False for i in self.vals] for j in other.vals]
        raise TypeError("Comparison must be with another object of Matrix4")

    def make_translation(self, vector):
        """
        Creates a translation matrix using the 3D vector

        :param   vector: the translation vector
        :type    vector: Vector3
        :return: translation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_vector3(vector):
            self.vals = [[1.0, 0.0, 0.0, vector.x],
                         [0.0, 1.0, 0.0, vector.y],
                         [0.0, 0.0, 1.0, vector.z],
                         [0.0, 0.0, 0.0, 1.0]]

            return self
        raise TypeError("Translation must be with an object of Vector3")

    def make_x_rotation(self, theta):
        """
        Creates an x-axis rotation matrix using an angle

        :param   theta: the angle of rotation
        :type    theta: int/float
        :return: x-axis rotation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_int_or_float(theta):
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            self.vals = [[1.0, 0.0, 0.0, 0.0],
                         [0.0, cos_theta, sin_theta, 0.0],
                         [0.0, -sin_theta, cos_theta, 0.0],
                         [0.0, 0.0, 0.0, 1.0]]

            return self
        raise TypeError("X rotation must be with an int or float")

    def make_y_rotation(self, theta):
        """
        Creates a y-axis rotation matrix using an angle

        :param   theta: the angle of rotation
        :type    theta: int/float
        :return: y-axis rotation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_int_or_float(theta):
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            self.vals = [[cos_theta, 0.0, -sin_theta, 0.0],
                         [0.0, 1.0, 0.0, 0.0],
                         [sin_theta, 0.0, cos_theta, 0.0],
                         [0.0, 0.0, 0.0, 1.0]]

            return self
        raise TypeError("Y rotation must be with an int or float")

    def make_z_rotation(self, theta):
        """
        Creates a z-axis rotation matrix using an angle

        :param   theta: the angle of rotation
        :type    theta: int/float
        :return: z-axis rotation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_int_or_float(theta):
            cos_theta = cos(theta)
            sin_theta = sin(theta)
            self.vals = [[cos_theta, -sin_theta, 0.0, 0.0],
                         [sin_theta, cos_theta, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0],
                         [0.0, 0.0, 0.0, 1.0]]

            return self
        raise TypeError("Z rotation must be with an int or float")


def is_matrix4(input_variable):
    return isinstance(input_variable, Matrix4)
