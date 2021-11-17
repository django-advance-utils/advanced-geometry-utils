from two_d.point2 import Point2, is_point2
from two_d.vector2 import Vector2, is_vector2


class AxisAlignedBox2:
    def __init__(self, minimum=Point2(0.0, 0.0), maximum=Point2(0.0, 0.0)):
        if is_point2(minimum) and is_point2(maximum):
            self.min = minimum
            self.max = maximum

    def include(self, other):
        if is_point2(other):
            self.max.x = max(self.max.x, other.x)
            self.min.x = min(self.min.x, other.x)
            self.max.y = max(self.max.y, other.y)
            self.min.y = min(self.min.y, other.y)

        if is_box2(other):
            self.include(other.min)
            self.include(other.max)

    def __contains__(self, item):
        if is_point2(item):
            return self.min <= item <= self.max

        if is_box2(item):
            return self.__contains__(item.min) and self.__contains__(item.max)

    def intersects(self, item):
        if is_box2(item):
            return item.min >= self.min and item.max <= self.max

    def size(self):
        return (self.max - self.min).to_vector()

    def offset(self, offset_vector):
        if is_vector2(offset_vector):
            return self + offset_vector

    def centre(self):
        return ((self.min + self.max).to_vector())/2.0

    def __add__(self, vector):
        if is_vector2(vector):
            return AxisAlignedBox2(self.min + vector, self.max + vector)
        return NotImplemented

    def __eq__(self, box):
        if is_box2(box):
            return self.max == box.max and self.max == box.max

    def __ne__(self, box):
        if is_box2(box):
            return self.max != box.max or self.max != box.max

    def empty(self):
        return self.size() == Vector2(0.0, 0.0)


def is_box2(input_variable):
    return isinstance(input_variable, AxisAlignedBox2)
