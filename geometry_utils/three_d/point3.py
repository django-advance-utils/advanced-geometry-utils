from geometry_utils.maths_utility import are_ints_or_floats, floats_are_close
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
    to_vector(): Vector2
        Returns the vector representation of the point
    distance_to(other_point): int/float
        Returns the pythagorean length of the difference between the point and another 3D point
    """

    def __init__(self, x=0, y=0, z=0, w=1):
        if are_ints_or_floats([x, y, z, w]):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
        else:
            raise TypeError("Point3 argument must be an int or float")

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
        Compares the equality of self and other point.

        :param   other_point: the other vector
        :type    other_point: Point3
        :return: the point equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return floats_are_close(self.x, other_point.x) and \
                   floats_are_close(self.y, other_point.y) and \
                   floats_are_close(self.z, other_point.z)
        raise TypeError("Comparison must be done with another object of Point3")

    def __ne__(self, other_point):
        """
        Compares the inequality of self with another vector.

        :param   other_point: the other vector
        :type    other_point: Point3
        :return: the point inequality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return not floats_are_close(self.x, other_point.x) or \
                   not floats_are_close(self.y, other_point.y) or \
                   not floats_are_close(self.z, other_point.z)
        raise TypeError("Comparison must be done with another object of Point3")

    def __le__(self, other_point):
        """
        Tests if self is less than or equal to the other vector.

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
        Tests if self is greater than or equal to the other vector.

        :param   other_point: the other point
        :type    other_point: Point3
        :return: the vector less than or equal to comparison
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_point3(other_point):
            return self.x >= other_point.x and self.y >= other_point.y and self.z >= other_point.z
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


def is_point3(input_variable):
    return isinstance(input_variable, Point3)
