from math import sqrt, cos, sin

from maths_utility import are_ints_or_floats, is_int_or_float


class Vector2:
    """
    A class to create a 2D vector

    Attributes:
    ___________
    x: int or float
        the x-coordinate of the vector
    y: int or float
        the y-coordinate of the vector
    w: int or float
        the w-coordinate of the vector
        w=0 leave the vector unchanged when multiplied by a translation matrix

    Methods:
    ________
    __add__(other_vector): Vector2
        Returns the addition of the vector with another 2D vector
    __sub__(other_Vector): Vector2
        Returns the subtraction of another 2D vector from the vector
    __mul__(scalar): Vector2
        Returns the multiplication of the vector with an int or float scalar
    __div__(scalar): Vector2
        Returns the division of the vector by an int or float scalar
    __eq__(Vector2): bool
        Returns the equality comparison of the vector with another 2D vector
    __ne__(Vector2): bool
        Returns the inequality comparison of the vector with another 2D vector
    reverse(): Vector2
        Returns the reverse of the vector
    normalise(): Vector2
        Returns the normal of the vector
    length(): int or float
        Returns the pythagorean length of the vector
    dot(Vector2): int or float
        Returns the dot product of vector with another 2D vector
    cross(Vector2): Vector2
        Returns the cross product of vector with another 2D vector
    get_perpendicular(): Vector2
        Returns the perpendicular of the vector
    invert(): Vector2
        Returns the inverse of the vector
    rotate(origin, theta): Vector2
        Returns the rotation of the vector at angle theta with respect to 2D vector origin
    """
    def __init__(self, x=0, y=0, w=0):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.w = w
        else:
            raise TypeError("Arguments must be ints or floats")

    def __add__(self, other_vector):
        """
        Calculates the addition of self with other vector

        :param  other_vector: the other vector
        :type   other_vector: Vector2
        :return:the resulting added vector
        :rtype: Vector2
        :raises:TypeError: wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x + other_vector.x, self.y + other_vector.y)
        raise TypeError("Addition must be with an object of Vector2")

    def __sub__(self, other_vector):
        """
        Calculates the subtraction of other vector from self

        :param  other_vector: the other vector
        :type   other_vector: Vector2
        :return:the resulting subtracted vector
        :rtype: Vector2
        :raises:TypeError: wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x - other_vector.x, self.y - other_vector.y)
        raise TypeError("Subtraction must be with an object of Vector2")

    def __mul__(self, scalar):
        """
        Calculates the multiplication of self with a scalar.

        :param  scalar: the multiplication scalar
        :type   scalar: int/float
        :return:the resulting multiplied vector
        :rtype: Vector2
        :raises:TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector2(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication must be by a scalar of type int or float")

    def __div__(self, scalar):
        """
        Calculates the division of self with a scalar.

        :param  scalar: the division scalar
        :type   scalar: int/float
        :return:the resulting divided vector
        :rtype: Vector2
        :raises:TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector2(self.x / scalar, self.y / scalar)
        raise TypeError("Division must be by a scalar of type int or float")

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other_vector):
        """
        Compares the equality of self and other vector.

        :param  other_vector: the other vector
        :type   other_vector: Vector2
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return self.x == other_vector.x and self.y == other_vector.y
        raise TypeError("Comparison must be with another object of Vector2")

    def __ne__(self, other_vector):
        """
        Compares the inequality of self and other vector.

        :param  other_vector: the other vector
        :type   other_vector: Vector2
        :return:the vector inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return self.x != other_vector.x or self.y != other_vector.y
        raise TypeError("Comparison must be with another object of Vector2")

    def reverse(self):
        """
        Calculates the reverse vector of the vector

        :return: the reverse vector
        :rtype: Vector2
        """
        return Vector2(-self.x, -self.y)

    def normalise(self):
        """
        Calculates the normal vector of the vector

        :return: the normal vector
        :rtype: Vector2
        """
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def length(self):
        """
        Calculates the pythagorean length of the vector

        :return: the vector length
        :rtype: int or float
        """
        return sqrt(self.dot(self))

    def dot(self, other_vector):
        """
        Calculates the dot product of self and other vector.

        :param:  other_vector: the other vector
        :type:   other_vector: Vector2
        :return:the dot product
        :rtype: float
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return self.x * other_vector.x + self.y * other_vector.y
        raise TypeError("Dot product must be with another object of Vector2")

    def cross(self, other_vector):
        """
        Calculates the cross product of self and other vector.

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
        Calculates the vector perpendicular to self

        :return: the perpendicular vector
        :rtype: Vector2
        """
        return Vector2(-self.y, self.x)

    def invert(self):
        """
        Calculates the inverse vector to self

        :return:the inverse vector
        :rtype: Vector2
        """
        return Vector2(-self.x, -self.y)

    def rotate(self, origin, theta):
        """
        Calculates the vector rotation of self

        :param: origin: the origin vector of rotation
                theta:  the angle of rotation
        :type:  origin: Vector2
                theta:  Float or Int
        :return:the cross product
        :rtype: Vector2
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(origin) and is_int_or_float(theta):
            cos_theta = cos(theta)
            sin_theta = sin(theta)

            self_origin_difference = self - origin
            result = Vector2()

            result.x = (self_origin_difference.x * cos_theta) - (self_origin_difference.y * sin_theta)
            result.y = (self_origin_difference.x * sin_theta) + (self_origin_difference.y * cos_theta)

            return result + origin

        if not is_vector2(origin):
            raise TypeError("Origin of rotation must be an object of Vector2")
        if not is_int_or_float(theta):
            raise TypeError("Angle of rotation must be a float or int")


def is_vector2(input_variable):
    return isinstance(input_variable, Vector2)
