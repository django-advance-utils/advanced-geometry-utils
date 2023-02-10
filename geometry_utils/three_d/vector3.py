import math
import geometry_utils.two_d.vector2

from geometry_utils.maths_utility import is_int_or_float, are_ints_or_floats, floats_are_close, radians_to_degrees, \
    EPSILON


class Vector3:
    """
    A class to create a 3D vector

    Attributes:
    ___________
    x: int/float
        the x-coordinate of the vector
    y: int/float
        the y-coordinate of the vector
    z: int/float
        the z-coordinate of the vector
    w: int/float
        the w-coordinate of the vector
        w=0 leave the vector unchanged when multiplied by a translation matrix

    Methods:
    ________
    __str__(): string
        Returns the attributes of the 3D vector in string format
    __add__(Vector3): Vector3
        Returns the addition of the vector with another 3D vector
    __sub__(Vector3): Vector3
        Returns the subtraction of another 3D vector from the vector
    __mul__(int/float): Vector3
        Returns the multiplication of the vector with an int or float scalar
    __div__(int/float): Vector3
        Returns the division of the vector by an int or float scalar
    __eq__(Vector3): bool
        Returns the equality comparison of the vector with another 3D vector
    __ne__(Vector3): bool
        Returns the inequality comparison of the vector with another 3D vector
    equal(Vector3, float): bool
        Returns the equality comparison of the vector with another 3D vector with specified tolerance level
    normalised(): Vector3
        Returns the normal of the vector
    normalise(): Vector3
        Converts the 3D vector into a normal of itself
    length(): int/float
        Returns the pythagorean length of the vector
    square_length(): int/float
        Returns the square of the pythagorean length of the vector
    dot(Vector3): int/float
        Returns the dot product of vector with another 3D vector
    cross(Vector3): Vector3
        Returns the cross product of vector with another 3D vector
    get_perpendicular(): Vector3, Vector3
        Returns the two possible perpendicular 3D vectors of the vector
    invert(): Vector2
        Converts the 2D vector into an inverse of itself
    inverted(): Vector2
        Returns the inverse of the vector
    angle_to(Vector3, bool): float
        Returns the angle of the vector to another vector in radians or degrees
    signed_angle_to(Vector3, bool): float
        Returns the signed angle of the vector to another vector in radians or degrees
    angle_to_x_axis(bool): float
        Returns the angle of the vector the x-axis in radians or degrees
    from_comma_string(str): Vector3
        Returns a 3D vector from a string input
    to_vector2(): Vector2
        Returns a 3D vector from the 2D vector with a z coordinate value of 0.0
    accuracy_fix(): Vector3
        Converts the 3D vector coordinates with very low values to 0.0
    """
    def __init__(self, x=0.0, y=0.0, z=0.0, w=0):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
        else:
            raise TypeError("Vector3 argument must be an int or float")

    def __str__(self):
        """
        Prints the attributes of the 3D vector

        :return: the string of the vector
        :rtype: str
        """
        return ("Vector3(x:" + str("{:.2f}".format(self.x)) +
                ", y:" + str("{:.2f}".format(self.y)) +
                ", z:" + str("{:.2f}".format(self.z)) + ")")

    def __add__(self, other_vector):
        """
        Calculates the addition of 3D vector with another 3D vector

        :param   other_vector: the addition 3D vector
        :type    other_vector: Vector3
        :return: the resulting added vector
        :rtype:  Vector3
        :raises: TypeError: wrong argument type
        """
        if is_vector3(other_vector):
            return Vector3(self.x + other_vector.x, self.y + other_vector.y, self.z + other_vector.z)
        raise TypeError("Addition of a Vector3 object must be with an object of Vector3")

    def __sub__(self, other_vector):
        """
        Calculates the subtraction of another 3D vector from the vector

        :param   other_vector: the subtraction 3D vector
        :type    other_vector: Vector3
        :return: the resulting subtracted vector
        :rtype:  Vector3
        :raises: TypeError: wrong argument type
        """
        if is_vector3(other_vector):
            return Vector3(self.x - other_vector.x, self.y - other_vector.y, self.z - other_vector.z)
        raise TypeError("Subtraction of a Vector3 object must be with an object of Vector3")

    def __mul__(self, scalar):
        """
        Calculates the multiplication of self with a scalar.

        :param  scalar: the multiplication scalar
        :type   scalar: int/float
        :return:the resulting multiplied vector
        :rtype: Vector3
        :raises:TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
        raise TypeError("Multiplication of a Vector3 object must be by a scalar of type int or float")

    def __div__(self, scalar):
        """
        Calculates the division of self with a scalar.

        :param  scalar: the division scalar
        :type   scalar: int/float
        :return:the resulting divided vector
        :rtype: Vector3
        :raises:TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)
        raise TypeError("Division of a Vector3 object must be by a scalar of type int or float")

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other_vector):
        """
        Compares the equality of the vector and another 3D vector.

        :param  other_vector: the other 3D vector
        :type   other_vector: Vector3
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector3(other_vector):
            return (floats_are_close(self.x, other_vector.x) and
                    floats_are_close(self.y, other_vector.y) and
                    floats_are_close(self.z, other_vector.z))
        raise TypeError("Comparison must be with another object of Vector3")

    def __ne__(self, other_vector):
        """
        Compares the inequality of the vector and another 3D vector.

        :param  other_vector: the other 3D vector
        :type   other_vector: Vector3
        :return:the vector inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector3(other_vector):
            return (not floats_are_close(self.x, other_vector.x) or
                    not floats_are_close(self.y, other_vector.y) or
                    not floats_are_close(self.y, other_vector.y))
        raise TypeError("Comparison must be with another object of Vector3")

    @classmethod
    def from_point3(cls, point):
        """
        Constructs and returns a Vector3 from a point3

        :param  cls: Vector3 class
        :type   cls: Vector3 class
        :param  point: Point3 object
        :type   point: Point3
        :return: Vector3 object
        :rtype: Vector3
        :raises:TypeError: Wrong argument type
        """
        try:
            return cls(point.x, point.y, point.z)
        except AttributeError:
            raise TypeError("from_point3 must be passed a Point3")

    def equal(self, other_vector, tol=0.01):
        """
        Compares the equality of the vector and another 3D vector with tolerance input

        :param  other_vector: the other 3D vector
        :param  tol: equality tolerance
        :type   other_vector: Vector2
        :type   tol: float
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        return abs(self.x - other_vector.x) <= tol and abs(self.y - other_vector.y) <= tol and abs(self.z - other_vector.z) <= tol

    def normalised(self):
        """
        Calculates the normal vector of the vector

        :return: the normal vector
        :rtype: Vector3
        """
        vector_length = self.length()
        if floats_are_close(vector_length, 0.0):
            return self
        return self / vector_length

    def normalise(self):
        """
        Normalises the vector

        """
        vector_length = self.length()
        if floats_are_close(vector_length, 0.0):
            return self
        self.x /= vector_length
        self.y /= vector_length
        self.z /= vector_length
        return self

    def length(self):
        """
        Calculates the pythagorean length of the vector.

        :return: length
        :rtype: int/float
        """
        return math.sqrt(self.square_length())

    def square_length(self):
        """
        Caclulates the square of the pythagorean length of the vector

        :return: the squared vector length
        :rtype: int/float
        """
        return self.dot(self)

    def dot(self, other_vector):
        """
        Calculates the dot product of self and other vector.

        :param other_vector: the other vector
        :type other_vector: Vector3
        :return: the dot product.
        :rtype: float
        :raises:TypeError: Wrong argument type
        """
        if is_vector3(other_vector):
            return float((self.x * other_vector.x) + (self.y * other_vector.y) + (self.z * other_vector.z))
        raise TypeError("Dot product must be with another object of Vector3")

    def cross(self, other_vector):
        """
        Calculates the cross product of self and other vector.

        :param other_vector: the other vector
        :type other_vector: Vector3
        :return: the cross product.
        :rtype: Vector3
        :raises:TypeError: Wrong argument type
        """
        if is_vector3(other_vector):
            return Vector3(self.y * other_vector.z - self.z * other_vector.y,
                           self.z * other_vector.x - self.x * other_vector.z,
                           self.x * other_vector.y - self.y * other_vector.x)
        raise TypeError("Cross product must be with another object of Vector3")

    def get_perpendicular(self, vector_1, vector_2):
        """
        Calculates the two possible 3D vectors perpendicular to the vector

        :return: the perpendicular vector
        :rtype: Vector3
        """
        if self == Vector3():
            return vector_1, vector_2
        x_abs = abs(self.x)
        y_abs = abs(self.y)
        z_abs = abs(self.z)

        cross_vector = Vector3(1.0, 0.0, 0.0)
        if y_abs < x_abs:
            cross_vector.x = 0.0
            cross_vector.y = 1.0
            cross_vector.z = 0.0
        if z_abs < y_abs:
            cross_vector.x = 0.0
            cross_vector.y = 0.0
            cross_vector.z = 1.0

        vector_1 = self.cross(cross_vector).normalised()
        vector_2 = self.cross(vector_1).normalised()

        return vector_1, vector_2

    def invert(self):
        """
        Converts the 3D vector into an inverse of itself

        """
        self.x *= -1
        self.y *= -1
        self.z *= -1
        return self

    def inverted(self):
        """
       Calculates the 3D vector inverse to the vector

       :return:the inverse vector
       :rtype: Vector3
       """
        return Vector3(-self.x, -self.y, -self.z)

    @classmethod
    def from_comma_string(cls, string):
        """
        Creates a Vector3 object from a string

        :param string: String containing the 3D point coordinates
        :return: a Vector3 object
        """
        v = string.split(',')
        return cls(float(v[0]), float(v[1]), float(v[2]))

    def angle_to(self, other_vector, rad=False):
        """
        Calculates the angle of the vector to another 3D vector

        :param other_vector: the other 3D vector
        :param rad: if the result should be calculated in radians
        :rtype: float
        :return: the angle between the vectors
        """
        if is_vector3(other_vector):
            self_unit_vector = self.normalised()
            other_unit_vector = other_vector.normalised()

            dot_product = self_unit_vector.dot(other_unit_vector)
            if floats_are_close(dot_product, 1.0):
                return 0.0

            angle = math.acos(dot_product)
            if not rad:
                angle = radians_to_degrees(angle)
            return angle

    def signed_angle_to(self, other_vector):
        """
        Calculates the signed angle of the vector to another 3D vector

        :param other_vector: the other 3D vector
        :rtype: float
        :return: the signed angle between the vectors
        """
        return self.to_vector2().signed_angle_to(other_vector.to_vector2())

    def to_vector2(self):
        """
        Creates a 2D vector of the 3D vector discarding the coordinate value

        :return: the 3D vector
        """
        vector_2d = geometry_utils.two_d.vector2.Vector2(self.x, self.y, self.w)
        return vector_2d

    def accuracy_fix(self):
        """
        Converts the 3D vector coordinates with very low values to 0.0

        """
        if -EPSILON < self.x < EPSILON:
            self.x = 0.0
        if -EPSILON < self.y < EPSILON:
            self.y = 0.0
        if -EPSILON < self.z < EPSILON:
            self.z = 0.0
        return self


def is_vector3(input_variable):
    """
    Checks if the input variable is an object of Vector3

    :param input_variable: the input variable to be checked
    :return: bool
    """
    return isinstance(input_variable, Vector3)
