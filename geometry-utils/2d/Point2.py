from Vector2 import Vector2


class Point2:
    def __init__(self, x, y, w=1):
        self.x = x
        self.y = y
        self.w = w

    def __add__(self, other):
        if isinstance(self, Point2) and isinstance(other, Point2):
            return Point2(self.x + other.x, self.y + other.y)
        elif isinstance(self, Point2) and isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(self, Vector2) and isinstance(other, Point2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(self, Point2) and isinstance(other, Point2):
            return Point2(self.x - other.x, self.y - other.y)
        elif isinstance(self, Point2) and isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(self, Vector2) and isinstance(other, Point2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __eq__(self, other):
        return bool(self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return bool(self.x != other.x or self.y != other.y)
