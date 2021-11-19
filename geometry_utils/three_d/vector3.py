from math import sqrt

from maths_utility import is_float, are_ints_or_floats


class Vector3:
    def __init__(self, x=0, y=0, z=0, w=0):
        if are_ints_or_floats([x, y, z, w]):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
        else:
            raise TypeError("Vector3 argument must be an int or float")

    def __add__(self, other):
        if is_vector3(other):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Addition must be with an object of Vector3")

    def __sub__(self, other):
        if is_vector3(other):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Subtraction must be with an object of Vector3")

    def __mul__(self, other):
        if is_float(other):
            return Vector3(self.x * other, self.y * other, self.z * other)
        raise TypeError("Multiplication must be done by a float")

    def __div__(self, other):
        if is_float(other):
            return Vector3(self.x / other, self.y / other, self.z / other)
        raise TypeError("Division must be done by a float")

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other):
        if is_vector3(other):
            return bool(self.x == other.x and self.y == other.y and self.z == other.z)
        raise TypeError("Comparison must be with another object of Vector3")

    def __ne__(self, other):
        if is_vector3(other):
            return bool(self.x != other.x or self.y != other.y or self.z != other.z)
        raise TypeError("Comparison must be with another object of Vector3")

    def reverse(self):
        return Vector3(self.x * -1, self.y * -1, self.z * -1)

    def normalise(self):
        """
        Derives the normal of the vector

        :return: .         """
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def length(self):
        """
        Calculates the length of the vector.

        :rtype: float
        :return: length
        """
        return float(sqrt(self.dot(self)))

    def dot(self, other):
        """
        Calculates the dot product of self and other vector.

        :param other: the other vector
        :type other: Vector3
        :rtype: float
        :return: the dot product.
        """
        if is_vector3(other):
            return float(self.x * other.x + self.y * other.y + self.z * other.z)
        raise TypeError("Dot product must be with another object of Vector3")

    def cross(self, other):
        """
        Calculates the cross product of self and other vector.

        :param other: the other vector
        :type other: Vector3
        :rtype: Vector3
        :return: the cross product.
        """
        if is_vector3(other):
            return Vector3(self.y * other.z - self.z * other.y,
                           self.z * other.x - self.x * other.z,
                           self.x * other.y - self.y * other.x)
        raise TypeError("Cross product must be with another object of Vector3")


def is_vector3(input_variable):
    return isinstance(input_variable, Vector3)
