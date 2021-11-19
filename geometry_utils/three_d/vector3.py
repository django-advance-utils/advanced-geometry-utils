from math import sqrt

from maths_utility import is_int_or_float, are_ints_or_floats


class Vector3:
    """
    A class to create a 3D vector

    Attributes:
    ___________
    x: int or float
        the x-coordinate of the vector
    y: int or float
        the y-coordinate of the vector
    z: int or float
        the z-coordinate of the vector
    w: int or float
        the w-coordinate of the vector
        w=0 leave the vector unchanged when multiplied by a translation matrix

    Methods:
    ________
    __add__(other_vector): Vector3
        Returns the addition of the vector with another 3D vector
    __sub__(other_Vector): Vector3
        Returns the subtraction of another 3D vector from the vector
    __mul__(scalar): Vector3
        Returns the multiplication of the vector with an int or float scalar
    __div__(scalar): Vector3
        Returns the division of the vector by an int or float scalar
    __eq__(Vector2): bool
        Returns the equality comparison of the vector with another 3D vector
    __ne__(Vector2): bool
        Returns the inequality comparison of the vector with another 3D vector
    reverse(): Vector3
        Returns the reverse of the vector
    normalise(): Vector3
        Returns the normal of the vector
    length(): int or float
        Returns the pythagorean length of the vector
    dot(Vector3): int or float
        Returns the dot product of vector with another 3D vector
    cross(Vector3): Vector3
        Returns the cross product of vector with another 3D vector
    """
    def __init__(self, x=0, y=0, z=0, w=0):
        if are_ints_or_floats([x, y, z, w]):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
        else:
            raise TypeError("Vector3 argument must be an int or float")

    def __add__(self, other_vector):
        """
        Calculates the addition of self with other vector

        :param  other_vector: the other vector
        :type   other_vector: Vector3
        :return:the resulting added vector
        :rtype: Vector3
        :raises:TypeError: wrong argument type
        """
        if is_vector3(other_vector):
            return Vector3(self.x + other_vector.x, self.y + other_vector.y, self.z + other_vector.z)
        raise TypeError("Addition must be with an object of Vector3")

    def __sub__(self, other_vector):
        """
        Calculates the subtraction of other vector from self

        :param  other_vector: the other vector
        :type   other_vector: Vector3
        :return:the resulting subtracted vector
        :rtype: Vector3
        :raises:TypeError: wrong argument type
        """
        if is_vector3(other_vector):
            return Vector3(self.x - other_vector.x, self.y - other_vector.y, self.z - other_vector.z)
        raise TypeError("Subtraction must be with an object of Vector3")

    def __mul__(self, scalar):
        """
        Calculates the multiplication of self with a scalar.

        :param  scalar: the multiplication scalar
        :type   scalar: int or float
        :return:the resulting multiplied vector
        :rtype: Vector3
        :raises:TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
        raise TypeError("Multiplication must be done by a float")

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
        raise TypeError("Division must be done by a float")

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other_vector):
        """
        Compares the equality of self and other vector.

        :param  other_vector: the other vector
        :type   other_vector: Vector3
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector3(other_vector):
            return self.x == other_vector.x and self.y == other_vector.y and self.z == other_vector.z
        raise TypeError("Comparison must be with another object of Vector3")

    def __ne__(self, other_vector):
        """
        Compares the inequality of self and other vector.

        :param  other_vector: the other vector
        :type   other_vector: Vector3
        :return:the vector inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector3(other_vector):
            return self.x != other_vector.x or self.y != other_vector.y or self.z != other_vector.z
        raise TypeError("Comparison must be with another object of Vector3")

    def reverse(self):
        """
        Calculates the reverse vector of the vector

        :return: the reverse vector
        :rtype: Vector3
        """
        return Vector3(self.x * -1, self.y * -1, self.z * -1)

    def normalise(self):
        """
        Calculates the normal vector of the vector

        :return: the normal vector
        :rtype: Vector3
        """
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def length(self):
        """
        Calculates the pythagorean length of the vector.

        :return: length
        :rtype: float
        """
        return sqrt(self.dot(self))

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
            return self.x * other_vector.x + self.y * other_vector.y + self.z * other_vector.z
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


def is_vector3(input_variable):
    return isinstance(input_variable, Vector3)
