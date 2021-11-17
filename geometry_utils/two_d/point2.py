from maths_utility import is_float, is_int
from two_d.vector2 import Vector2, is_vector2


class Point2:
    def __init__(self, x, y, w=1):
        if is_float(x) and is_float(y) and is_int(w):
            self.x = x
            self.y = y
            self.w = w

    def __add__(self, other):
        if is_vector2(other) or is_point2(other):
            return Point2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if is_vector2(other) or is_point2(other):
            return Point2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if is_float(scalar):
            return Point2(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __eq__(self, other_point):
        if is_point2(other_point):
            return self.x == other_point.x and self.y == other_point.y
        return NotImplemented

    def __ne__(self, other_point):
        if is_point2(other_point):
            return self.x != other_point.x or self.y != other_point.y
        return NotImplemented

    def __le__(self, other_point):
        if is_point2(other_point):
            return self.x <= other_point.x and self.y <= other_point.y
        return NotImplemented

    def __ge__(self, other_point):
        if is_point2(other_point):
            return self.x >= other_point.x and self.y >= other_point.y
        return NotImplemented

    def to_vector(self):
        return Vector2(self.x, self.y)

    def distance_to(self, other_point):
        if is_point2(other_point):
            return (self - other_point).to_vector().length()


def is_point2(input_variable):
    return isinstance(input_variable, Point2)
