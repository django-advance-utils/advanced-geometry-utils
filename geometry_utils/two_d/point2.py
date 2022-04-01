import geometry_utils.three_d.point3

from geometry_utils.maths_utility import are_ints_or_floats, floats_are_close, EPSILON
from geometry_utils.two_d.vector2 import Vector2, is_vector2


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
    __str__(): string
        Returns the attributes of the 2D point in string format
    __add__(Vector2): Point2
        Returns the addition of the point with a 2D vector
    __sub__(Vector2/Point2): Point2/Vector2
        Returns the subtraction of another 2D point or a 2D vector from the point
    __eq__(Point2): bool
        Returns the equality comparison of the point with another 2D point
    __ne__(Point2): bool
        Returns the inequality comparison of the vector with another 2D point
    __le__(Point2): bool
        Returns the less than or equal to comparison of the point with another 2D point
    __ge__(Point2): bool
        Returns the greater than or equal to comparison of the point with another 2D point
    __lt__(Point2): bool
        Returns the less than comparison of the point with another 2D point
    __gt__(Point2): bool
        Returns the greater than comparison of the point with another 2D point
    equal(Point2, float): bool
        Returns the equality comparison of the vector with another 2D point with specified tolerance
    to_vector(): Vector2
        Returns the vector representation of the point
    distance_to(other_point): float
        Returns the pythagorean length of the difference between the point and another 2D point
    mirror_y(): Point2
        Mirrors the 2D point about the y axis
    mirror_x(): Point2
        Mirrors the 2D point about the x axis
    mirror_origin(): Point2
        Mirrors the 2D point about the origin
    from_comma_string(str): Point2
        Returns a 2D point from a string input
    to_point3(): Point3
        Returns a 3D point from the 2D point with a z coordinate value of 0.0
    accuracy_fix(): Vector2
        Converts the 2D point coordinates with very low values to 0.0
    """

    def __init__(self, x=0.0, y=0.0, w=1):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.w = w
            self.name = ''
        else:
            raise TypeError("Point2 argument must be an int or float")

    def __str__(self):
        """
        Prints the attributes of the 2D point

        :return: the string of the point
        :rtype: str
        """
        return "Point2(x:" + str("{:.2f}".format(self.x)) + ", y:" + str("{:.2f}".format(self.y)) + ")"

    def __add__(self, vector):
        """
        Translates point by the 2D vector value

        :param   vector: the translation 2D vector
        :type    vector: Vector2
        :return: the resulting translated point
        :rtype:  Point2
        :raises: TypeError: wrong argument type
        """
        if is_vector2(vector):
            return Point2(self.x + vector.x, self.y + vector.y)
        raise TypeError("Addition of a Point2 object must be done with an object of Vector2")

    def __sub__(self, other):
        """
        Translates point by the inverse of the 2D vector or derives the 2D vector difference with another 2D point

        :param   other: the other 2D point or 2D vector
        :type    other: Vector2/Point2
        :return: the resulting translated point or vector difference
        :rtype:  Point2/Vector2
        :raises: TypeError: wrong argument type
        """
        if is_vector2(other):
            return Point2(self.x - other.x, self.y - other.y)
        if is_point2(other):
            return Vector2(self.x - other.x, self.y - other.y)
        raise TypeError("Subtraction of a Point2 object must be done with an object of Vector2 or Point2")

    def __eq__(self, other_point):
        """
        Compares the equality of the point and another 2D point

        :param   other_point: the other 2D point
        :type    other_point: Point2
        :return: the point equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return floats_are_close(self.x, other_point.x) and floats_are_close(self.y, other_point.y)
        raise TypeError("Equality comparison of a Point2 object must be done with another object of Point2")

    def __ne__(self, other_point):
        """
        Compares the inequality of the point with another 2D point

        :param   other_point: the other 2D point
        :type    other_point: Point2
        :return: the point inequality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return not floats_are_close(self.x, other_point.x) or not floats_are_close(self.y, other_point.y)
        raise TypeError("Inequality comparison of a Point2 object must be done with another object of Point2")

    def __le__(self, other_point):
        """
        Compares if the point is less than or equal to another 2D point in a 2D space

        :param   other_point: the other 2D point
        :type    other_point: Point2
        :return: the point less than or equality comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x <= other_point.x and self.y <= other_point.y
        raise TypeError("Less than or equal to comparison of a Point2 object must be done with another object of "
                        "Point2")

    def __ge__(self, other_point):
        """
        Compares if the point is greater than or equal to another 2D point in a 2D space

        :param   other_point: the other 2D point
        :type    other_point: Point2
        :return: the point greater than or equal to comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x >= other_point.x and self.y >= other_point.y
        raise TypeError("Greater than or equal to comparison of a Point2 object must be done with another object of "
                        "Point2")

    def __lt__(self, other_point):
        """
        Compares if the point is less than another 2D point in a 2D space

        :param   other_point: the other 2D point
        :type    other_point: Point2
        :return: the point greater than or equal to comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x < other_point.x and self.y < other_point.y
        raise TypeError("Less than comparison of a Point2 object must be done with another object of Point2")

    def __gt__(self, other_point):
        """
        Compares if the point is greater than another 2D point in a 2D space

        :param   other_point: the other 2D point
        :type    other_point: Point2
        :return: the point greater than or equal to comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return self.x > other_point.x and self.y > other_point.y
        raise TypeError("Greater than comparison must be done with another object of Point2")

    def equal(self, other_point, tol=0.01):
        """
        Compares the equality of the vector and another 2D point with tolerance input

        :param  other_point: the other 2D point
        :param  tol: equality tolerance
        :type   other_point: Point2
        :type   tol: float
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return abs(self.x - other_point.x) <= tol and abs(self.y - other_point.y) <= tol
        raise TypeError("Equality comparison must be done with another object of Point2")

    def to_vector2(self):
        """
        Converts the point to a vector

        :return: the vector representation of the point
        :rtype:  Vector2
        """
        return Vector2(self.x, self.y)

    def distance_to(self, other_point):
        """
        Calculates the pythagorean distance of the difference of the point to another point

        :param   other_point: the other point
        :type    other_point: Point2
        :return: length of the point subtractions
        :rtype:  int/float
        :raises: TypeError: Wrong argument type
        """
        if is_point2(other_point):
            return (self - other_point).length()
        raise TypeError("Argument must be an object of Point2")

    def mirror_y(self):
        """
        Mirrors the 2D point about the y axis

        """
        self.x = -self.x
        return self

    def mirror_x(self):
        """
        Mirrors the 2D point about the x axis

        """
        self.y = -self.y
        return self

    def mirror_origin(self):
        """
        Mirrors the 2D point about the origin

        """
        self.x = -self.x
        self.y = -self.y
        return self

    @classmethod
    def from_comma_string(cls, string):
        """
        Creates a Point2 object from a string

        :param string: String containing the 2D point coordinates
        :return: a Point2 object
        """
        v = string.split(',')
        return cls(float(v[0]), float(v[1]))

    def to_point3(self):
        """
        Converts the 2D point to a 3D point

        :return: a Point3 object
        :rtype: Point3
        """
        point_3d = geometry_utils.three_d.point3.Point3(self.x, self.y, 0.0, self.w)
        point_3d.name = self.name
        return point_3d

    def accuracy_fix(self):
        """
        Converts the 2D point coordinates with very low values to 0.0

        """
        if -EPSILON < self.x < EPSILON:
            self.x = 0.0
        if -EPSILON < self.y < EPSILON:
            self.y = 0.0
        return self


def is_point2(input_variable):
    """
    Checks if the input variable is an object of Point2

    :param input_variable: the input variable to be checked
    :return: bool
    """
    return isinstance(input_variable, Point2)
