import math
import geometry_utils.three_d.vector3

from geometry_utils.maths_utility import is_int_or_float, are_ints_or_floats, floats_are_close, radians_to_degrees


class Vector2:
    """
    A class to create a 2D vector

    Attributes:
    ___________
    x: int/float
        the x-coordinate of the vector
    y: int/float
        the y-coordinate of the vector
    w: int/float
        the w-coordinate of the vector
        w=0 leave the vector unchanged when multiplied by a translation matrix

    Methods:
    ________
    __add__(Vector2): Vector2
        Returns the addition of the vector with another 2D vector
    __sub__(Vector2): Vector2
        Returns the subtraction of another 2D vector from the vector
    __mul__(int/float): Vector2
        Returns the multiplication of the vector with an int or float scalar
    __div__(int/float): Vector2
        Returns the division of the vector by an int or float scalar
    __eq__(Vector2): bool
        Returns the equality comparison of the vector with another 2D vector
    __ne__(Vector2): bool
        Returns the inequality comparison of the vector with another 2D vector
    reverse(): Vector2
        Returns the reverse of the vector
    normalise(): Vector2
        Returns the normal of the vector
    length(): int/float
        Returns the pythagorean length of the vector
    dot(Vector2): int/float
        Returns the dot product of vector with another 2D vector
    cross(Vector2): Vector2
        Returns the cross product of vector with another 2D vector
    get_perpendicular(): Vector2
        Returns the perpendicular of the vector
    invert(): Vector2
        Returns the inverse of the vector
    rotate(Vector2, int/float): Vector2
        Returns the rotation of the vector at angle theta with respect to 2D vector origin
    """
    def __init__(self, x=0.0, y=0.0, w=0):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.w = w
        else:
            raise TypeError("Vector2 argument must be an int or float")

    def __str__(self):
        return "Vector2(x:" + str("{:.2f}".format(self.x)) + ", y:" + str("{:.2f}".format(self.y)) + ")"

    def __add__(self, other_vector):
        """
        Calculates the addition of vector with another 2D vector

        :param   other_vector: the addition 2D vector
        :type    other_vector: Vector2
        :return: the resulting added vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x + other_vector.x, self.y + other_vector.y)
        raise TypeError("Addition must be with an object of Vector2")

    def __sub__(self, other_vector):
        """
        Calculates the subtraction of another 2D vector from the vector

        :param   other_vector: the subtraction 2D vector
        :type    other_vector: Vector2
        :return: the resulting subtracted vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x - other_vector.x, self.y - other_vector.y)
        raise TypeError("Subtraction must be with an object of Vector2")

    def __mul__(self, scalar):
        """
        Calculates the multiplication of the vector with a scalar of type int or float

        :param   scalar: the multiplication scalar
        :type    scalar: int/float
        :return: the resulting multiplied vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector2(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication must be by a scalar of type int or float")

    def __div__(self, scalar):
        """
        Calculates the division of the vector by a scalar of type int or float

        :param   scalar: the division scalar
        :type    scalar: int/float
        :return: the resulting divided vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector2(self.x / scalar, self.y / scalar)
        raise TypeError("Division must be by a scalar of type int or float")

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other_vector):
        """
        Compares the equality of the vector and another 2D vector

        :param  other_vector: the other 2D vector
        :type   other_vector: Vector2
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return floats_are_close(self.x, other_vector.x) and floats_are_close(self.y, other_vector.y)
        raise TypeError("Comparison must be with another object of Vector2")

    def __ne__(self, other_vector):
        """
        Compares the inequality of the vector and another 2D vector

        :param  other_vector: the other 2D vector
        :type   other_vector: Vector2
        :return:the vector inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return (not floats_are_close(self.x, other_vector.x)) or (not floats_are_close(self.y, other_vector.y))
        raise TypeError("Comparison must be with another object of Vector2")

    def normalised(self):
        """
        Calculates the normal vector of the vector

        :return: the normal vector
        :rtype: Vector2
        """
        vector_length = self.length()
        if floats_are_close(vector_length, 0.0):
            return self
        return self / vector_length

    def normalise(self):
        vector_length = self.length()
        if floats_are_close(vector_length, 0.0):
            return self
        self.x /= vector_length
        self.y /= vector_length
        return self

    def length(self):
        """
        Calculates the pythagorean length of the vector

        :return: the vector length
        :rtype: int/float
        """
        return math.sqrt(self.square_length())

    def square_length(self):
        return self.dot(self)

    def dot(self, other_vector):
        """
        Calculates the dot product of self and another 2D vector

        :param:  other_vector: the other vector
        :type:   other_vector: Vector2
        :return:the dot product
        :rtype: float
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return (self.x * other_vector.x) + (self.y * other_vector.y)
        raise TypeError("Dot product must be with another object of Vector2")

    def cross(self, other_vector):
        """
        Calculates the cross product of the vector and another 2D vector

        :param  other_vector: the other vector
        :type   other_vector: Vector2
        :return:the cross product
        :rtype: Vector2
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x * other_vector.y - self.y * other_vector.x,
                           self.y * other_vector.x - self.x * other_vector.y)
        raise TypeError("Cross product must be with another object of Vector2")

    def get_perpendicular(self):
        """
        Calculates the 2D vector perpendicular to the vector

        :return: the perpendicular vector
        :rtype: Vector2
        """
        return Vector2(-self.y, self.x)

    def invert(self):
        """
        Calculates the 2D vector inverse to the vector

        :return:the inverse vector
        :rtype: Vector2
        """
        self.x *= -1
        self.y *= -1
        return self

    def inverted(self):
        return Vector2(-self.x, -self.y)

    def rotate(self, origin, theta):
        """
        Calculates the vector rotation of self

        :param: origin: the origin vector of rotation
                theta:  the angle of rotation
        :type:  origin: Vector2
                theta:  int/float
        :return:the cross product
        :rtype: Vector2
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(origin) and is_int_or_float(theta):
            cos_theta = math.cos(theta)
            sin_theta = math.sin(theta)

            self_origin_difference = self - origin
            result = Vector2()

            result.x = (self_origin_difference.x * cos_theta) - (self_origin_difference.y * sin_theta)
            result.y = (self_origin_difference.x * sin_theta) + (self_origin_difference.y * cos_theta)

            return result + origin

        if not is_vector2(origin):
            raise TypeError("Origin of rotation must be an object of Vector2")
        if not is_int_or_float(theta):
            raise TypeError("Angle of rotation must be a float or int")

    def angle_to(self, other_vector):
        if is_vector2(other_vector):
            self_unit_vector = self.normalised()
            other_unit_vector = other_vector.normalised()

            dot_product = self_unit_vector.dot(other_unit_vector)
            if floats_are_close(dot_product, 1.0):
                return 0.0

            angle = math.acos(dot_product)
            angle = radians_to_degrees(angle)
            return angle

    def signed_angle_to(self, other_vector, rad=False):
        if is_vector2(other_vector):
            angle = self.angle_to_x_axis(rad) - other_vector.angle_to_x_axis(rad)
            return angle

    def angle_to_x_axis(self, rad=False):
        angle = math.atan2(self.y, self.x)
        if not rad:
            angle = radians_to_degrees(angle)
        return angle

    @classmethod
    def from_comma_string(cls, string):
        v = string.split(',')
        return cls(float(v[0]), float(v[1]))

    def to_vector3(self):
        vector_3d = geometry_utils.three_d.vector3.Vector3(self.x, self.y, 0.0, self.w)
        return vector_3d


def is_vector2(input_variable):
    return isinstance(input_variable, Vector2)
