import math

from geometry_utils.maths_utility import is_list, is_int_or_float, radians_to_degrees, degrees_to_radians, is_float
from geometry_utils.three_d.vector3 import Vector3, is_vector3
from geometry_utils.three_d.point3 import Point3, is_point3


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

    def __str__(self):
        return ("Matrix4(vals:\n\t\t\t" + str(self.vals[0]) + "\n\t\t\t" + str(self.vals[1]) + "\n\t\t\t" +
                str(self.vals[2]) + "\n\t\t\t" + str(self.vals[3]) + ")")

    def set_identity(self):
        """
        Converts the matrix to an identity matrix

        :return: the identity matrix
        :rtype:  Matrix4
        """
        self.vals = [[1 if i == j else 0.0 for i in range(4)] for j in range(4)]

    def zeros(self):
        self.vals = [[0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0]]

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
            result.zeros()
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result

        if is_vector3(other) or is_point3(other):
            if is_vector3(other):
                result = Vector3()
            else:
                result = Point3()
            result.x = (self.vals[0][0] * other.x + self.vals[0][1] * other.y +
                        self.vals[0][2] * other.z + self.vals[0][3] * other.w)
            result.y = (self.vals[1][0] * other.x + self.vals[1][1] * other.y +
                        self.vals[1][2] * other.z + self.vals[1][3] * other.w)
            result.z = (self.vals[2][0] * other.x + self.vals[2][1] * other.y +
                        self.vals[2][2] * other.z + self.vals[2][3] * other.w)
            result.w = (self.vals[3][0] * other.x + self.vals[3][1] * other.y +
                        self.vals[3][2] * other.z + self.vals[3][3] * other.w)
            result.accuracy_fix()
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
        # if is_matrix4(other):
        for row in range(4):
            for column in range(4):
                if self.vals[row][column] != other.vals[row][column]:
                    return False
        return True
        # raise TypeError("Comparison must be with another object of Matrix4")

    @classmethod
    def translation(cls, vector):
        """
        Creates a translation matrix using the 3D vector

        :param   vector: the translation vector
        :type    vector: Vector3
        :return: translation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_vector3(vector):
            mat = cls()
            mat.vals = [[1.0, 0.0, 0.0, vector.x],
                        [0.0, 1.0, 0.0, vector.y],
                        [0.0, 0.0, 1.0, vector.z],
                        [0.0, 0.0, 0.0, 1.0]]

            return mat
        raise TypeError("Translation must be with an object of Vector3")

    @classmethod
    def x_rotation(cls, theta, rad=False):
        """
        Creates an x-axis rotation matrix using an angle

        :param   rad: rotation angle in Degrees, unless rad = True
        :param   theta: the angle of rotation
        :type    theta: int/float
        :return: x-axis rotation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_float(theta):
            mat = cls()
            if rad is False:
                theta = degrees_to_radians(theta)

            cos_theta = math.cos(theta)
            sin_theta = math.sin(theta)
            negative_sin_theta = 0.0 if (-sin_theta == -0.0) else -sin_theta

            mat.vals = [[1.0, 0.0, 0.0, 0.0],
                        [0.0, cos_theta, negative_sin_theta, 0.0],
                        [0.0, sin_theta, cos_theta, 0.0],
                        [0.0, 0.0, 0.0, 1.0]]

            return mat
        raise TypeError("X rotation must be with an int or float")

    @classmethod
    def y_rotation(cls, theta, rad=False):
        """
        Creates a y-axis rotation matrix using an angle

        :param   theta: the angle of rotation
        :type    theta: int/float
        :return: y-axis rotation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_int_or_float(theta):
            mat = cls()
            if rad is False:
                theta = degrees_to_radians(theta)
            cos_theta = math.cos(theta)
            sin_theta = math.sin(theta)
            negative_sin_theta = 0.0 if (-sin_theta == -0.0) else -sin_theta
            mat.vals = [[cos_theta, 0.0, negative_sin_theta, 0.0],
                        [0.0, 1.0, 0.0, 0.0],
                        [sin_theta, 0.0, cos_theta, 0.0],
                        [0.0, 0.0, 0.0, 1.0]]

            return mat
        raise TypeError("Y rotation must be with an int or float")

    @classmethod
    def z_rotation(cls, theta, rad=False):
        """
        Creates a z-axis rotation matrix using an angle

        :param   theta: the angle of rotation
        :type    theta: int/float
        :return: z-axis rotation matrix
        :rtype:  Matrix4
        :raises: TypeError: Wrong argument type
        """
        if is_int_or_float(theta):
            mat = cls()
            if rad is False:
                theta = degrees_to_radians(theta)
            cos_theta = math.cos(theta)
            sin_theta = math.sin(theta)
            negative_sin_theta = 0.0 if (-sin_theta == -0.0) else -sin_theta
            mat.vals = [[cos_theta, negative_sin_theta, 0.0, 0.0],
                        [sin_theta, cos_theta, 0.0, 0.0],
                        [0.0, 0.0, 1.0, 0.0],
                        [0.0, 0.0, 0.0, 1.0]]

            return mat
        raise TypeError("Z rotation must be with an int or float")

    @classmethod
    def x_reflection(cls):
        """
        Creates a x-axis reflection matrix

        :return: x-axis reflection matrix
        :rtype:  Matrix4
        """
        mat = cls()
        mat.vals = [[-1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]]

        return mat

    @classmethod
    def basis_change(cls, base_x, base_y, base_z, new_x, new_y, new_z):
        matrix = Matrix4()

        matrix.vals[0][0] = new_x.dot(base_x)
        matrix.vals[0][1] = new_x.dot(base_y)
        matrix.vals[0][2] = new_x.dot(base_z)
        matrix.vals[0][3] = 0.0

        matrix.vals[1][0] = new_y.dot(base_x)
        matrix.vals[1][1] = new_y.dot(base_y)
        matrix.vals[1][2] = new_y.dot(base_z)
        matrix.vals[1][3] = 0.0

        matrix.vals[2][0] = new_z.dot(base_x)
        matrix.vals[2][1] = new_z.dot(base_y)
        matrix.vals[2][2] = new_z.dot(base_z)
        matrix.vals[2][3] = 0.0

        matrix.vals[3][0] = 0.0
        matrix.vals[3][1] = 0.0
        matrix.vals[3][2] = 0.0
        matrix.vals[3][3] = 1.0

        return matrix

    # def to_matrix3(self):
    #     matrix_3d = geometry_utils.two_d.matrix3.Matrix3([
    #         self.vals[0][0], self
    #     ])



def is_matrix4(input_variable):
    return isinstance(input_variable, Matrix4)
