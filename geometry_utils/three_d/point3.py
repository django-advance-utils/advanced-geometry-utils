import geometry_utils.two_d.point2

from geometry_utils.maths_utility import are_ints_or_floats, floats_are_close, EPSILON
from geometry_utils.three_d.vector3 import Vector3, is_vector3


class Point3:
    """
    A class to create a 3D point

    Attributes:
    ___________
    x: int or float
        the x-coordinate of the point
    y: int or float
        the y-coordinate of the point
    z: int or float
        the z-coordinate of the point
    w: int or float
        the w-coordinate of the vector
        w=1 allows the point to be translated when multiplied by a translation matrix

    Methods:
    ________
    __str__(): string
        Returns the attributes of the 3D point in string format
    __add__(Vector3): Point3
        Returns the addition of the point with another 3D point or a 3D vector
    __sub__(Vector3/Point3): Point3/Vector3
        Returns the subtraction of another 3D point or a 3D vector from the point
    __eq__(Point3): bool
        Returns the equality comparison of the point with another 3D point
    __ne__(Point3): bool
        Returns the inequality comparison of the vector with another 3D point
    __le__(Point3): bool
        Returns the less than or equal to comparison of the point with another 3D point
    __ge__(Point3): bool
        Returns the greater than or equal to comparison of the point with another 3D point
    __lt__(Point3): bool
        Returns the less than comparison of the point with another 3D point
    __gt__(Point3): bool
        Returns the greater than comparison of the point with another 3D point
    equal(Point3, float): bool
        Returns the equality comparison of the vector with another 3D point with specified tolerance
    to_vector(): Vector2
        Returns the vector representation of the point
    distance_to(other_point): int/float
        Returns the pythagorean length of the difference between the point and another 3D point
    mirror_x(): Point3
        Mirrors the 3D point about the x axis
    mirror_y(): Point3
        Mirrors the 3D point about the y axis
    mirror_z(): Point3
        Mirrors the 3D point about the z axis
    mirror_origin(): Point3
        Mirrors the 3D point about the origin
    mirrored_origin(): Point3
        Returns the 3D point mirrored about the origin
    from_comma_string(str): Point3
        Returns a 3D point from a string input
    to_point2(): Point2
        Returns a 2D point from the 3D point discarding z coordinate value
    accuracy_fix(): Point3
        Converts the 3D point coordinates with very low values to 0.0
    """

    def __init__(self, x=0.0, y=0.0, z=0.0, w=1):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
            self.name = ''
        else:
            raise TypeError("Point3 argument must be an int or float")

    def __str__(self):
        """
        Prints the attributes of the 3D point

        :return: the string of the point
        :rtype: str
        """
        return ("Point3(x:" + str("{:.2f}".format(self.x)) +
                ", y:" + str("{:.2f}".format(self.y)) +
                ", z:" + str("{:.2f}".format(self.z)) + ")")

    def __add__(self, vector):
        """
        Translates point by the 3D vector value

        :param   vector: the translation 3D vector
        :type    vector: Vector3
        :return: the resulting translated point
        :rtype:  Point3
        :raises: TypeError: wrong argument type
        """
        if is_vector3(vector):
            return Point3(self.x + vector.x, self.y + vector.y, self.z + vector.z)
        raise TypeError("Addition must be done with an object of Vector3")

    def __sub__(self, other):
        """
        Translates point by the inverse of the 3D vector or derives the 3D vector difference with another 3D point

        :param   other: the other 3D point or 3D vector
        :type    other: Vector3/Point3
        :return: the resulting translated point or vector difference
        :rtype:  Point3/Vector3
        :raises: TypeError: wrong argument type
        """
        if is_vector3(other):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        if is_point3(other):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Subtraction must be done with an object of Vector3 or Point3")

    def __eq__(self, other_point):
        """
        Compares the equality of self and other 3D point.

        :param   other_point: the other vector
        :type    other_point: Point3
        :return: the point equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return (floats_are_close(self.x, other_point.x) and
                    floats_are_close(self.y, other_point.y) and
                    floats_are_close(self.z, other_point.z))
        raise TypeError("Comparison must be done with another object of Point3")

    def __ne__(self, other_point):
        """
        Compares the inequality of self with another 3D point

        :param   other_point: the other vector
        :type    other_point: Point3
        :return: the point inequality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return (not floats_are_close(self.x, other_point.x) or
                    not floats_are_close(self.y, other_point.y) or
                    not floats_are_close(self.z, other_point.z))
        raise TypeError("Comparison must be done with another object of Point3")

    def __le__(self, other_point):
        """
        Compares if the point is less than or equal to another 3D point in a 3D space

        :param   other_point: the other point
        :type    other_point: Point3
        :return: the vector less than or equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return self.x <= other_point.x and self.y <= other_point.y and self.z <= other_point.z
        raise TypeError("Comparison must be done with another object of Point3")

    def __ge__(self, other_point):
        """
        Compares if the point is greater than or equal to another 3D point in a 3D space

        :param   other_point: the other point
        :type    other_point: Point3
        :return: the vector less than or equal to comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return self.x >= other_point.x and self.y >= other_point.y and self.z >= other_point.z
        raise TypeError("Comparison must be done with another object of Point3")

    def __lt__(self, other_point):
        """
        Compares if the point is less than another 3D point in a 3D space

        :param   other_point: the other 3D point
        :type    other_point: Point3
        :return: the point greater than or equal to comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return self.x < other_point.x and self.y < other_point.y and self.z < other_point.z
        raise TypeError("Comparison must be done with another object of Point3")

    def __gt__(self, other_point):
        """
        Compares if the point is greater than another 3D point in a 3D space

        :param   other_point: the other 3D point
        :type    other_point: Point3
        :return: the point greater than or equal to comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return self.x > other_point.x and self.y > other_point.y and self.z > other_point.z
        raise TypeError("Comparison must be done with another object of Point3")

    def to_vector3(self):
        """
        Converts the point to a vector

        :return: the vector representation of the point
        :rtype:  Vector3
        """
        return Vector3(self.x, self.y, self.z)

    def distance_to(self, other_point):
        """
        Calculates the pythagorean distance of the difference of the point to another point

        :param   other_point: the other point
        :type    other_point: Point3
        :return: length of the point subtractions
        :rtype:  int/float
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return (self - other_point).length()
        raise TypeError("Argument must be an object of Point3")

    @classmethod
    def from_comma_string(cls, string):
        """
        Creates a Point3 object from a string

        :param string: String containing the 3D point coordinates
        :return: a Point3 object
        """
        v = string.split(',')
        return cls(float(v[0]), float(v[1]), float(v[2]))

    def mirror_x(self):
        """
        Mirrors the 3D point about the x axis

        """
        self.y = -self.y
        self.z = -self.z
        return self

    def mirror_y(self):
        """
        Mirrors the 3D point about the y axis

        """
        self.x = -self.x
        self.z = -self.z
        return self

    def mirror_z(self):
        """
        Mirrors the 3D point about the z axis

        """
        self.x = -self.x
        self.y = -self.y
        return self

    def mirror_origin(self):
        """
        Mirrors the 3D point about the origin

        """
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        return self

    def mirrored_origin(self):
        """
        Returns the 3D point mirrored about the origin

        :return: Point3
        """
        return Point3(-self.x, -self.y, -self.z)

    def to_point2(self):
        """
        Converts the 3D point to a 2D point

        :return: a Point2 object
        """
        point_2d = geometry_utils.two_d.point2.Point2(self.x, self.y, self.w)
        point_2d.name = self.name
        return point_2d

    def accuracy_fix(self):
        """
        Converts the 3D point coordinates with very low values to 0.0

        """
        if -EPSILON < self.x < EPSILON:
            self.x = 0.0
        if -EPSILON < self.y < EPSILON:
            self.y = 0.0
        if -EPSILON < self.z < EPSILON:
            self.z = 0.0
        return self


def is_point3(input_variable):
    """
    Checks if the input variable is an object of Point3

    :param input_variable: the input variable to be checked
    :return: bool
    """
    return isinstance(input_variable, Point3)
