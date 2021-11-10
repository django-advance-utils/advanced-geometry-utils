from math import sqrt


class Vector2:
    def __init__(self, x, y, w=0):
        if isinstance(x, float) and isinstance(y, float) and isinstance(w, int):
            self.x = x
            self.y = y
            self.w = w

    def __add__(self, other_vector):
        if isinstance(other_vector, Vector2):
            return Vector2(self.x + other_vector.x, self.y + other_vector.y)
        return NotImplemented

    def __sub__(self, other_vector):
        if isinstance(other_vector, Vector2):
            return Vector2(self.x - other_vector.x, self.y - other_vector.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, float):
            return Vector2(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __div__(self, scalar):
        if isinstance(scalar, float):
            return Vector2(self.x / scalar, self.y / scalar)
        return NotImplemented

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if isinstance(other, Vector2):
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
        if isinstance(other_vector, Vector2):
            return float(self.x * other_vector.x + self.y * other_vector.y)

    def cross(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.y - self.y * other.x, self.y * other.x - self.x * other.y)
