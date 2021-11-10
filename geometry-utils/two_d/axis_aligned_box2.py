from two_d.point2 import Point2
from two_d.vector2 import Vector2


class AxisAlignedBox2:
    def __init__(self, minimum=Point2(0.0, 0.0), maximum=Point2(0.0, 0.0)):
        if isinstance(minimum, Point2) and isinstance(maximum, Point2):
            self.min = minimum
            self.max = maximum

    def include(self, other):
        if isinstance(other, Point2):
            self.max.x = max(self.max.x, other.x)
            self.min.x = min(self.min.x, other.x)
            self.max.y = max(self.max.y, other.y)
            self.min.y = min(self.min.y, other.y)

        if isinstance(other, AxisAlignedBox2):
            self.include(other.min)
            self.include(other.max)

    def __contains__(self, item):
        if isinstance(item, Point2):
            return self.min <= item <= self.max

        if isinstance(item, AxisAlignedBox2):
            return self.__contains__(item.min) and self.__contains__(item.max)

    def intersects(self, item):
        if isinstance(item, AxisAlignedBox2):
            return item.min >= self.min and item.max <= self.max

    def size(self):
        return (self.max - self.min).to_vector()

    def offset(self, offset_vector):
        if isinstance(offset_vector, Vector2):
            return self + offset_vector

    def centre(self):
        return ((self.min + self.max).to_vector())/2.0

    def __add__(self, vector):
        if isinstance(vector, Vector2):
            return AxisAlignedBox2(self.min + vector, self.max + vector)
        return NotImplemented

    def __eq__(self, box):
        if isinstance(box, AxisAlignedBox2):
            return self.max == box.max and self.max == box.max

    def __ne__(self, box):
        if isinstance(box, AxisAlignedBox2):
            return self.max != box.max or self.max != box.max

    def empty(self):
        return self.size() == Vector2(0.0, 0.0)
