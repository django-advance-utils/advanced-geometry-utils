from maths_utility import is_int_or_float, are_ints_or_floats
from two_d.vector2 import Vector2, is_vector2


class Point2:
    """
    A class to create a 2D point

    Attributes:
    ___________
    x: int or float
        the x-coordinate of the point
    y: int or float
        the y-coordinate of the point
    w: int or float
        the w-coordinate of the vector
        w=1 allows the point to be translated when multiplied by a translation matrix

    Methods:
    ________
    __add__(Point2): Point2
        Returns the addition of the point with another 2D point or a 2D vector
    __sub__(Point2): Point2
        Returns the subtraction of another 2D point or a 2D vector from the point
    __mul__(int or float  ): Point2
        Returns the multiplication of the point with an int or float scalar
    __eq__(Point2): bool
        Returns the equality comparison of the point with another 2D point
    __ne__(Point2): bool
        Returns the inequality comparison of the vector with another 2D point
    __le__(Point2): bool
        Returns the less than or equal to comparison of the point with another 2D point
    __ge__(Point2): bool
        Returns the greater than or equal to comparison of the point with another 2D point
    to_vector(): Vector2
        Returns the vector of the point
    distance_to(other_point): float
        Returns the pythagorean length of the difference between the point and another 2D point
    """
    def __init__(self, x=0, y=0, w=1):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.w = w
        else:
            raise TypeError("Point2 argument must be an int or float")

    def __add__(self, other):
        """
        Calculates the addition of self with other vector

        :param  other: the other point or vector
        :type   other: Point2/Vector2
        :return:the resulting added point
        :rtype: Point2
        :raises:TypeError: wrong argument type
        """
        if is_vector2(other) or is_point2(other):
            return Point2(self.x + other.x, self.y + other.y)
        raise TypeError("Addition must be done with an object of Vector2 or Point2")

    def __sub__(self, other):
        """
        Calculates the subtraction of other vector from self

        :param  other: the other point or vector
        :type   other: Point2/Vector2
        :return:the resulting subtracted vector
        :rtype: Point2
        :raises:TypeError: wrong argument type
        """
        if is_vector2(other) or is_point2(other):
            return Point2(self.x - other.x, self.y - other.y)
        raise TypeError("Subtraction must be done with an object of Vector2 or Point2")

    def __mul__(self, scalar):
        """
        Calculates the multiplication of self with a scalar.

        :param  scalar: the multiplication scalar
        :type   scalar: int/float
        :return:the resulting multiplied point
        :rtype: Point2
        :raises:TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Point2(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication must be done by a float")

    def __eq__(self, other_point):
        """
        Compares the equality of self and other point.

        :param  other_point: the other vector
        :type   other_point: Point2
        :return:the point equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x == other_point.x and self.y == other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def __ne__(self, other_point):
        """
        Compares the inequality of self with another vector.

        :param  other_point: the other vector
        :type   other_point: Point2
        :return:the point inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x != other_point.x or self.y != other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def __le__(self, other_point):
        """
        Tests if self is less than or equal to the other vector.

        :param  other_point: the other point
        :type   other_point: Point2
        :return:the vector less than or equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x <= other_point.x and self.y <= other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def __ge__(self, other_point):
        """
        Tests if self is greater than or equal to the other vector.

        :param  other_point: the other point
        :type   other_point: Point2
        :return:the vector less than or equal to comparison
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x >= other_point.x and self.y >= other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def to_vector(self):
        """
        Converts the point to a vector

        :return:the vector representation of the point
        :rtype: Vector2
        """
        return Vector2(self.x, self.y)

    def distance_to(self, other_point):
        """
        Calculates the pythagorean distance of the difference of the point to another point

        :param  other_point: the other point
        :type   other_point: Point2
        :return:length of the point subtractions
        :rtype: float
        :raises:TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return (self - other_point).to_vector().length()
        raise TypeError("Argument must be an object of Point2")


def is_point2(input_variable):
    return isinstance(input_variable, Point2)
