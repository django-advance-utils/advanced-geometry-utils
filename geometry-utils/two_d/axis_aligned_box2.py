from two_d.point2 import Point2
from two_d.vector2 import Vector2


class AxisAlignedBox2:
    def __init__(self, minimum, maximum):
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
            return self.min.x <= item.x <= self.max.x and self.min.y <= item.y <= self.max.y

        if isinstance(item, AxisAlignedBox2):
            return self.__contains__(item.min) and self.__contains__(item.max)

    def intersects(self, item):
        if isinstance(item, AxisAlignedBox2):
            return item.min.x >= self.min.x and item.max.x <= self.max.x and \
                   item.min.y >= self.min.y and item.max.y <= self.max.y

    def size(self):
        return Vector2(self.max.x - self.min.x, self.max.y - self.min.y)

    def offset(self, offset_vector):
        if isinstance(offset_vector, Vector2):
            new_box = AxisAlignedBox2(self.min + offset_vector, self.max + offset_vector)
            return new_box

    def centre(self):
        return Vector2((self.min.x + self.max.x) / 2.0, (self.min.y + self.max.y) / 2.0)

    def __eq__(self, box):
        if isinstance(box, AxisAlignedBox2):
            return self.max == box.max and self.max == box.max

    def __ne__(self, box):
        if isinstance(box, AxisAlignedBox2):
            return self.max != box.max or self.max != box.max

    def empty(self):
        return self.size() == Vector2(0.0, 0.0)
