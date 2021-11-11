from two_d.vector2 import Vector2


class Point2:
    def __init__(self, x, y, w=1):
        if isinstance(x, float) and isinstance(y, float) and isinstance(w, int):
            self.x = x
            self.y = y
            self.w = w

    def __add__(self, other):
        if isinstance(other, Vector2) or isinstance(other, Point2):
            return Point2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2) or isinstance(other, Point2):
            return Point2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, float):
            return Point2(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __eq__(self, other_point):
        if isinstance(other_point, Point2):
            return self.x == other_point.x and self.y == other_point.y
        return NotImplemented

    def __ne__(self, other_point):
        if isinstance(other_point, Point2):
            return self.x != other_point.x or self.y != other_point.y
        return NotImplemented

    def __le__(self, other_point):
        if isinstance(other_point, Point2):
            return self.x <= other_point.x and self.y <= other_point.y
        return NotImplemented

    def __ge__(self, other_point):
        if isinstance(other_point, Point2):
            return self.x >= other_point.x and self.y >= other_point.y
        return NotImplemented

    def to_vector(self):
        return Vector2(self.x, self.y)

    def distance_to(self, other_point):
        if isinstance(other_point, Point2):
            return (self - other_point).to_vector().length()
