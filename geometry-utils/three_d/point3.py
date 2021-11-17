from maths_utility import is_float, is_int
from three_d.vector3 import Vector3, is_vector3


class Point3:
    def __init__(self, x, y, z, w=1):
        if is_float(x) and is_float(y) and is_float(z) and is_int(w):
            self.x = x
            self.y = y
            self.z = z
            self.w = w

    def __add__(self, other):
        if is_point3(other) or is_vector3(other):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if is_point3(other) or is_vector3(other):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __mul__(self, other):
        if is_float(other):
            return Point3(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __eq__(self, other):
        if is_point3(other):
            return bool(self.x == other.x and self.y == other.y and self.z == other.z)
        return NotImplemented

    def __ne__(self, other):
        if is_point3(other):
            return bool(self.x != other.x or self.y != other.y or self.z != other.z)
        return NotImplemented

    def __le__(self, other_point):
        if is_point3(other_point):
            return self.x <= other_point.x and self.y <= other_point.y and self.z <= other_point.z
        return NotImplemented

    def __ge__(self, other_point):
        if is_point3(other_point):
            return self.x >= other_point.x and self.y >= other_point.y and self.z >= other_point.z
        return NotImplemented

    def to_vector(self):
        return Vector3(self.x, self.y, self.z)

    def distance_to(self, point):
        if is_point3(point):
            return (self - point).to_vector().length()


def is_point3(input_variable):
    return isinstance(input_variable, Point3)
