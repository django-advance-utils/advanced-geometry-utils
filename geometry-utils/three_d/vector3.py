from math import sqrt

from maths_utility import is_float, is_int


class Vector3:
    def __init__(self, x, y, z, w=0):
        if is_float(x) and is_float(y) and is_float(z) and is_int(w):
            self.x = x
            self.y = y
            self.z = z
            self.w = w

    def __add__(self, other):
        if is_vector3(other):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if is_vector3(other):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __mul__(self, other):
        if is_float(other):
            return Vector3(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __div__(self, other):
        if is_float(other):
            return Vector3(self.x / other, self.y / other, self.z / other)
        return NotImplemented

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other):
        if is_vector3(other):
            return bool(self.x == other.x and self.y == other.y and self.z == other.z)

    def __ne__(self, other):
        if is_vector3(other):
            return bool(self.x != other.x or self.y != other.y or self.z != other.z)

    def reverse(self):
        return Vector3(self.x * -1, self.y * -1, self.z * -1)

    def normalise(self):
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def length(self):
        return float(sqrt(self.dot(self)))

    def dot(self, other):
        if is_vector3(other):
            return float(self.x * other.x + self.y * other.y + self.z * other.z)

    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)


def is_vector3(input_variable):
    return isinstance(input_variable, Vector3)
