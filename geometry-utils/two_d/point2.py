from two_d.vector2 import Vector2


class Point2:
    def __init__(self, x, y, w=1):
        self.x = x
        self.y = y
        self.w = w

    def __add__(self, other):
        if isinstance(other, Vector2) or isinstance(other, Point2):
            return Point2(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2) or isinstance(other, Point2):
            return Point2(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, float):
            return Point2(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point2):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if isinstance(other, Point2):
            return self.x != other.x or self.y != other.y

    def to_vector(self):
        return Vector2(self.x, self.y)

    def distance_to(self, point):
        if isinstance(point, Point2):
            return (self - point).to_vector().length()
