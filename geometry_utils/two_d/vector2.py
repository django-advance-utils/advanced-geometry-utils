from math import sqrt, cos, sin

from maths_utility import is_float, is_int


class Vector2:
    def __init__(self, x=0.0, y=0.0, w=0):
        if is_float(x) and is_float(y) and is_int(w):
            self.x = x
            self.y = y
            self.w = w

    def __add__(self, other_vector):
        if is_vector2(other_vector):
            return Vector2(self.x + other_vector.x, self.y + other_vector.y)
        return NotImplemented

    def __sub__(self, other_vector):
        if is_vector2(other_vector):
            return Vector2(self.x - other_vector.x, self.y - other_vector.y)
        return NotImplemented

    def __mul__(self, scalar):
        if is_float(scalar):
            return Vector2(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __div__(self, scalar):
        if is_float(scalar):
            return Vector2(self.x / scalar, self.y / scalar)
        return NotImplemented

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other):
        if is_vector2(other):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if is_vector2(other):
            return self.x != other.x or self.y != other.y

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

    def cross(self, other):
        if is_vector2(other):
            return Vector2(self.x * other.y - self.y * other.x, self.y * other.x - self.x * other.y)

    def get_perpendicular(self):
        return Vector2(-self.y, self.x)

    def invert(self):
        return Vector2(-self.x, -self.y)

    def rotate(self, origin, theta):
        if is_vector2(origin) and is_float(theta):
            cos_theta = cos(theta)
            sin_theta = sin(theta)

            self_origin_difference = self - origin
            result = Vector2()

            result.x = (self_origin_difference.x * cos_theta) - (self_origin_difference.y * sin_theta)
            result.y = (self_origin_difference.x * sin_theta) + (self_origin_difference.y * cos_theta)

            return result + origin


def is_vector2(input_variable):
    return isinstance(input_variable, Vector2)
