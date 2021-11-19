from three_d.point3 import Point3, is_point3
from three_d.vector3 import Vector3, is_vector3


class AxisAlignedBox3:
    def __init__(self, minimum=Point3(0.0, 0.0, 0.0), maximum=Point3(0.0, 0.0, 0.0)):
        if is_point3(minimum) and is_point3(maximum):
            self.min = minimum
            self.max = maximum
        else:
            raise TypeError("AxisAlignedBox3 arguments must be objects of Point3")

    def include(self, other):
        if is_point3(other):
            self.max.x = max(self.max.x, other.x)
            self.min.x = min(self.min.x, other.x)
            self.max.y = max(self.max.y, other.y)
            self.min.y = min(self.min.y, other.y)
            self.max.z = max(self.max.z, other.z)
            self.min.z = min(self.min.z, other.z)
        elif is_box3(other):
            self.include(other.min)
            self.include(other.max)
        else:
            raise TypeError("Inclusion must be with an object of Point3 or AxisAlignedBox3")

    def __contains__(self, item):
        if is_point3(item):
            return self.min <= item <= self.max
        if isinstance(item, AxisAlignedBox3):
            return self.__contains__(item.min) and self.__contains__(item.max)
        raise TypeError("Variable must be an object of Point2 or AxisAlignedBox2")

    def intersects(self, item):
        if is_box3(item):
            return item.min >= self.min and item.max <= self.max
        raise TypeError("Intersection must be with an object of AxisAlignedBox2")

    def size(self):
        return (self.max - self.min).to_vector()

    def offset(self, offset_vector):
        if is_vector3(offset_vector):
            return self + offset_vector
        raise TypeError("Offset must be with an object of Vector3")

    def centre(self):
        return ((self.min + self.max).to_vector())/2.0

    def __add__(self, vector):
        if is_vector3(vector):
            return AxisAlignedBox3(self.min + vector, self.max + vector)
        raise TypeError("Addition must be with an object of Vector3")

    def __eq__(self, box):
        if is_box3(box):
            return self.max == box.max and self.min == box.min

    def __ne__(self, box):
        if is_box3(box):
            return self.max != box.max or self.min != box.min
        raise TypeError("Comparison must be with an object of AxisAlignedBox3")

    def empty(self):
        return self.size() == Vector3(0.0, 0.0, 0.0)


def is_box3(input_variable):
    return isinstance(input_variable, AxisAlignedBox3)
