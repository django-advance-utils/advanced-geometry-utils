import math


class Vector2:
    def __init__(self, x=0, y=0, w=0):
        self.x = x
        self.y = y
        self.w = w

    def __add__(self, other):
        if isinstance(self, Vector2) and isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(self, Vector2) and isinstance(other, float):
            return Vector2(self.x + other, self.y + other)
        elif isinstance(self, float) and isinstance(other, Vector2):
            return Vector2(self + other.x, self + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(self, Vector2) and isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(self, Vector2) and isinstance(other, float):
            return Vector2(self.x - other, self.y - other)
        elif isinstance(self, float) and isinstance(other, Vector2):
            return Vector2(other.x - self, other.y - self)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(self, Vector2) and isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        elif isinstance(self, Vector2) and isinstance(other, float):
            return Vector2(self.x * other, self.y * other)
        elif isinstance(self, float) and isinstance(other, Vector2):
            return Vector2(self * other.x, self * other.y)
        else:
            return NotImplemented

    def __div__(self, other):
        if isinstance(self, Vector2) and isinstance(other, float):
            return Vector2(self.x / other, self.y / other)
        elif isinstance(self, float) and isinstance(other, Vector2):
            return Vector2(other.x / self, other.y / self)
        else:
            return NotImplemented

    def __eq__(self, other):
        return bool(self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return bool(self.x != other.x or self.y != other.y)

    def normalise(self):
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def reverse(self):
        return Vector2(self.x * -1, self.y * -1)

    def length(self):
        return float(math.sqrt(self * self))

    def dot(self, other):
        return float(self.x * other.x + self.y * other.y)

    def cross(self, other):
        return Vector2(self.x * other.y - self.y * other.x, self.y * other.x - other.x * self.y)
