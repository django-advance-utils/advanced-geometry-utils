import copy
import geometry_utils.two_d.axis_aligned_box2
import geometry_utils.three_d.edge3

from geometry_utils.three_d.point3 import Point3, is_point3
from geometry_utils.three_d.vector3 import Vector3, is_vector3


class AxisAlignedBox3:
    """
    A class to create a 3D box

    Attributes:
    ___________
    min: Point3
        the minimum point in the 3D box
    max: Point3
        the maximum point in the 3D box

    Methods:
    ________
    include(Point3):
        Includes the 3D point in the 3D box
    __contains__(AxisAlignedBox3 or Point3): bool
        Tests if the 3D box contains another 3D box or 3D point
    intersect(AxisAlignedBox3): bool
        Tests if the 3D box intersects another 3D box
    size(): Vector3
        Returns the 3D vector of the 3D box
    offset(Vector3): AxisAlignedBox3
        Returns the 3D box offset by the 3D vector
    centre(): Vector3
        Returns the 3D vector of the centre of the 3D box
    __add__(Vector3): AxisAlignedBox3
        Returns the addition of the 3D box with a 3D vector
    __eq__(AxisAlignedBox3): bool
        Returns the equality comparison of the 3D box with another 3D box
    __ne__(AxisAlignedBox3): bool
        Returns the inequality comparison of the 3D box with another 3D box
    empty(Point3): bool
        Tests if the 3D box is empty
    """

    def __init__(self, minimum=None, maximum=None):
        if (is_point3(minimum) and is_point3(maximum)) or (minimum is None and maximum is None):
            self.min = minimum
            self.max = maximum
        else:
            raise TypeError("AxisAlignedBox3 arguments must be objects of Point3")

    def __str__(self):
        return "AxisAlignedBox3(min:" + str(self.min) + ", max:" + str(self.max) + ")"

    def include(self, other):
        if is_point3(other):
            if not self.is_valid():
                self.min = copy.deepcopy(other)
                self.max = copy.deepcopy(other)
            else:
                self.max.x = max(self.max.x, other.x)
                self.min.x = min(self.min.x, other.x)
                self.max.y = max(self.max.y, other.y)
                self.min.y = min(self.min.y, other.y)
                self.max.z = max(self.max.z, other.z)
                self.min.z = min(self.min.z, other.z)

        elif is_box3(other):
            if not self.is_valid():
                self.min = copy.deepcopy(other.min)
                self.max = copy.deepcopy(other.max)
            else:
                self.include(other.min)
                self.include(other.max)

        elif geometry_utils.three_d.edge3.is_edge3(other):
            if not self.is_valid():
                self.min = Point3(other.minimum_x(), other.minimum_y(), other.minimum_z())
                self.max = Point3(other.maximum_x(), other.maximum_y(), other.maximum_z())
            else:
                self.include(other.p1)
                self.include(other.p2)

        else:
            raise TypeError("Inclusion must be with an object of Point3 or AxisAlignedBox3")

    def __contains__(self, item):
        """
        Test the 3D point or 3D box is in self

        :param  item: the other 3D point or 3D box
        :type   item: Point3/AxisAlignedBox3
        :return:the item inclusion
        :rtype: bool
        :raises:TypeError: wrong argument type
        """
        if is_point3(item):
            return self.min <= item <= self.max
        if is_box3(item):
            return item.min in self and item.max in self
        raise TypeError("Variable must be an object of Point3 or AxisAlignedBox3")

    def intersects(self, item):
        """
        Test self intersects the other 3D box

        :param  item: the other 3D box
        :type   item: AxisAlignedBox3
        :return:the item intersection
        :rtype: bool
        :raises:TypeError: wrong argument type
        """
        if is_box3(item):
            return item.min >= self.min and item.max <= self.max
        raise TypeError("Intersection must be with an object of AxisAlignedBox3")

    def size(self):
        """
        Calculates the 3D vector size of self

        :return:the 3D box size
        :rtype: Vector3
        """
        return self.max - self.min

    def offset(self, offset_vector):
        """
        Offsets self by 3D vector

        :param  offset_vector: the other 3D vector
        :type   offset_vector: Vector3
        :return:the offset box
        :rtype: AxisAlignedBox3
        :raises:TypeError: wrong argument type
        """
        if is_vector3(offset_vector):
            return self + offset_vector
        raise TypeError("Offset must be with an object of Vector3")

    def centre(self):
        """
        Calculates the centre of self

        :return:the box centre
        :rtype: Vector3
        """
        return Point3((self.min.x + self.max.x) * 0.5, (self.min.y + self.max.y) * 0.5, (self.min.z + self.max.z) * 0.5)

    def __add__(self, vector):
        """
        Calculates the addition of self with a vector

        :param  vector: the addition vector
        :type   vector: Vector3
        :return:the resulting added box
        :rtype: AxisAlignedBox3
        :raises:TypeError: wrong argument type
        """
        if is_vector3(vector):
            return AxisAlignedBox3(self.min + vector, self.max + vector)
        raise TypeError("Addition must be with an object of Vector3")

    def __eq__(self, box):
        """
        Compares the equality of self and other box

        :param  box: the other 3D box
        :type   box: AxisAlignedBox3
        :return:the box equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_box3(box):
            return self.max == box.max and self.min == box.min
        raise TypeError("Comparison must be with an object of AxisAlignedBox3")

    def __ne__(self, box):
        """
        Compares the inequality of self with another vector.

        :param  box: the other 3D box
        :type   box: AxisAlignedBox3
        :return:the box inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_box3(box):
            return self.max != box.max or self.min != box.min
        raise TypeError("Comparison must be with an object of AxisAlignedBox3")

    def is_empty(self):
        """
        Checks if self is empty

        :return:the emptiness of the box
        :rtype: bool
        """
        if not self.is_valid():
            return True
        return self.size() == Vector3(0.0, 0.0, 0.0)

    def is_valid(self):
        return self.min is not None and self.max is not None

    def to_axis_aligned_box2(self):
        if self.is_valid():
            box_2d = geometry_utils.two_d.axis_aligned_box2.AxisAlignedBox2(self.min.to_point2(), self.max.to_point2())
        else:
            box_2d = geometry_utils.two_d.axis_aligned_box2.AxisAlignedBox2()
        return box_2d


def is_box3(input_variable):
    return isinstance(input_variable, AxisAlignedBox3)
