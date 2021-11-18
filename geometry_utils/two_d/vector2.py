from math import sqrt, cos, sin

from maths_utility import is_float, is_int, are_ints_or_floats, is_int_or_float


class Vector2:
    def __init__(self, x, y, w=0):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.w = w
        else:
            raise TypeError("Vector2 argument must be an int or float")

    def __add__(self, other_vector):
        if is_vector2(other_vector):
            return Vector2(self.x + other_vector.x, self.y + other_vector.y)
        raise TypeError("Addition must be with an object of Vector2")

    def __sub__(self, other_vector):
        if is_vector2(other_vector):
            return Vector2(self.x - other_vector.x, self.y - other_vector.y)
        raise TypeError("Subtraction must be with an object of Vector2")

    def __mul__(self, scalar):
        if is_float(scalar):
            return Vector2(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication must be by a scalar")

    def __div__(self, scalar):
        if is_float(scalar):
            return Vector2(self.x / scalar, self.y / scalar)
        raise TypeError("Division must be by a scalar")

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other):
        if is_vector2(other):
            return self.x == other.x and self.y == other.y
        raise TypeError("Comparison must be with another object of Vector2")

    def __ne__(self, other):
        if is_vector2(other):
            return self.x != other.x or self.y != other.y
        raise TypeError("Comparison must be with another object of Vector2")

    def reverse(self):
        return Vector2(-self.x, -self.y)

    def normalise(self):
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def length(self):
        return float(sqrt(self.dot(self)))

    def dot(self, other_vector):
        if is_vector2(other_vector):
            return float(self.x * other_vector.x + self.y * other_vector.y)
        raise TypeError("Dot product must be with another object of Vector2")

    def cross(self, other):
        if is_vector2(other):
            return Vector2(self.x * other.y - self.y * other.x, self.y * other.x - self.x * other.y)
        raise TypeError("Cross product must be with another object of Vector2")

    def get_perpendicular(self):
        return Vector2(-self.y, self.x)

    def invert(self):
        return Vector2(-self.x, -self.y)

    def rotate(self, origin, theta):
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
