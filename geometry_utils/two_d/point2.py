from maths_utility import is_float, are_ints_or_floats
from two_d.vector2 import Vector2, is_vector2


class Point2:
    def __init__(self, x=0, y=0, w=1):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.w = w
        else:
            raise TypeError("Point2 argument must be an int or float")

    def __add__(self, other):
        if is_vector2(other) or is_point2(other):
            return Point2(self.x + other.x, self.y + other.y)
        raise TypeError("Addition must be done with an object of Vector2 or Point2")

    def __sub__(self, other):
        if is_vector2(other) or is_point2(other):
            return Point2(self.x - other.x, self.y - other.y)
        raise TypeError("Subtraction must be done with an object of Vector2 or Point2")

    def __mul__(self, scalar):
        if is_float(scalar):
            return Point2(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication must be done by a float")

    def __eq__(self, other_point):
        if is_point2(other_point):
            return self.x == other_point.x and self.y == other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def __ne__(self, other_point):
        if is_point2(other_point):
            return self.x != other_point.x or self.y != other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def __le__(self, other_point):
        if is_point2(other_point):
            return self.x <= other_point.x and self.y <= other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def __ge__(self, other_point):
        if is_point2(other_point):
            return self.x >= other_point.x and self.y >= other_point.y
        raise TypeError("Comparison must be done with another object of Point2")

    def to_vector(self):
        return Vector2(self.x, self.y)

    def distance_to(self, other_point):
        if is_point2(other_point):
            return (self - other_point).to_vector().length()
        raise TypeError("Argument must be an object of Point2")


def is_point2(input_variable):
    return isinstance(input_variable, Point2)
