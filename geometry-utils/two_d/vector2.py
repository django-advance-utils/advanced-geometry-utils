import math


class Vector2:
    def __init__(self, x, y, w=0):
        self.x = x
        self.y = y
        self.w = w

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, float):
            return Vector2(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __div__(self, other):
        if isinstance(other, float):
            return Vector2(self.x / other, self.y / other)
        else:
            return NotImplemented

    # division in Python 3x = division in Python 2x
    __truediv__ = __div__

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if isinstance(other, Vector2):
            return self.x != other.x or self.y != other.y

    def normalise(self):
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def reverse(self):
        return Vector2(-self.x, -self.y)

    def length(self):
        return float(math.sqrt(self.dot(self)))

    def dot(self, other):
        if isinstance(other, Vector2):
            return float(self.x * other.x + self.y * other.y)
        else:
            return NotImplemented

    def cross(self, other):
        return Vector2(self.x * other.y - self.y * other.x, self.y * other.x - self.x * other.y)
