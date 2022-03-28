import copy
import geometry_utils.three_d.axis_aligned_box3
import geometry_utils.two_d.edge2

from geometry_utils.two_d.point2 import Point2, is_point2
from geometry_utils.two_d.vector2 import Vector2, is_vector2


class AxisAlignedBox2:
    """
    A class to create a 2D box

    Attributes:
    ___________
    min: Point2
        the minimum point in the 2D box
    max: Point2
        the maximum point in the 2D box

    Methods:
    ________
    include(Point2):
        Includes the 2D point in the 2D box
    __contains__(AxisAlignedBox2 or Point2): bool
        Tests if the 2D box contains another 2D box or 2D point
    intersect(AxisAlignedBox2): bool
        Tests if the 2D box intersects another 2D box
    size(): Vector2
        Returns the 2D vector of the 2D box
    offset(Vector2): AxisAlignedBox2
        Returns the 2D box offset by the 2D vector
    centre(): Vector2
        Returns the 2D vector of the centre of the 2D box
    __add__(Vector2): AxisAlignedBox2
        Returns the addition of the 2D box with a 2D vector
    __eq__(AxisAlignedBox2): bool
        Returns the equality comparison of the 2D box with another 2D box
    __ne__(AxisAlignedBox2): bool
        Returns the inequality comparison of the 2D box with another 2D box
    empty(Point2): bool
        Tests if the 2D box is empty
    """
    def __init__(self, minimum=None, maximum=None):
        if (is_point2(minimum) and is_point2(maximum)) or (minimum is None and maximum is None):
            self.min = minimum
            self.max = maximum
        else:
            raise TypeError("AxisAlignedBox2 must be objects of type Point2")

    def __str__(self):
        return "AxisAlignedBox2(min:" + str(self.min) + ", max:" + str(self.max) + ")"

    def include(self, other):
        """
        Includes the 2D point or 2D box in self

        :param  other: the other 2D box or 2D point
        :type   other: AxisAlignedBox2/Point2
        :return:the resulting included box
        :rtype: AxisAlignedBox2
        :raises:TypeError: wrong argument type
        """
        if is_point2(other):
            if not self.is_valid():
                self.min = copy.deepcopy(other)
                self.max = copy.deepcopy(other)
            else:
                self.max.x = max(self.max.x, other.x)
                self.min.x = min(self.min.x, other.x)
                self.max.y = max(self.max.y, other.y)
                self.min.y = min(self.min.y, other.y)

        elif is_box2(other):
            if not self.is_valid():
                self.min = copy.deepcopy(other.min)
                self.max = copy.deepcopy(other.max)
            else:
                self.include(other.min)
                self.include(other.max)

        elif geometry_utils.two_d.edge2.is_edge2(other):
            if not self.is_valid():
                self.min = Point2(other.minimum_x(), other.minimum_y())
                self.max = Point2(other.maximum_x(), other.maximum_y())
            else:
                self.include(other.p1)
                self.include(other.p2)
        else:
            raise TypeError("Inclusion must be with an object of Point2 or AxisAlignedBox2")

    def __contains__(self, item):
        """
        Test the 2D point or 2D box is in self

        :param  item: the other 2D point or 2D box
        :type   item: Point2/AxisAlignedBox2
        :return:the item inclusion
        :rtype: bool
        :raises:TypeError: wrong argument type
        """
        if is_point2(item):
            return self.min <= item <= self.max
        if is_box2(item):
            return item.min in self and item.max in self
        raise TypeError("Variable must be an object of Point2 or AxisAlignedBox2")

    def intersects(self, item):
        """
        Test self intersects the other 2D box

        :param  item: the other 2D box
        :type   item: AxisAlignedBox2
        :return:the item intersection
        :rtype: bool
        :raises:TypeError: wrong argument type
        """
        if is_box2(item):
            return item.min >= self.min and item.max <= self.max
        raise TypeError("Intersection must be with an object of AxisAlignedBox2")

    def size(self):
        """
        Calculates the 2D vector size of self

        :return:the 2D box size
        :rtype: Vector2
        """
        return self.max - self.min

    def offset(self, offset_vector):
        """
        Offsets self by 2D vector

        :param  offset_vector: the other 2D vector
        :type   offset_vector: Vector2
        :return:the offset box
        :rtype: AxisAlignedBox2
        :raises:TypeError: wrong argument type
        """
        if is_vector2(offset_vector):
            return self + offset_vector
        raise TypeError("Offset must be with an object of Vector2")

    def centre(self):
        """
        Calculates the centre of self

        :return:the box centre
        :rtype: Vector2
        """
        return Point2((self.min.x + self.max.x) * 0.5, (self.min.y + self.max.y) * 0.5)

    def __add__(self, vector):
        """
        Calculates the addition of self with a vector

        :param  vector: the addition vector
        :type   vector: Vector2
        :return:the resulting added box
        :rtype: AxisAlignedBox2
        :raises:TypeError: wrong argument type
        """
        if is_vector2(vector):
            return AxisAlignedBox2(self.min + vector, self.max + vector)
        raise TypeError("Addition must be with an object of Vector2")

    def __eq__(self, box):
        """
        Compares the equality of self and other box

        :param  box: the other 2D box
        :type   box: AxisAlignedBox2
        :return:the box equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_box2(box):
            return self.max == box.max and self.max == box.max
        raise TypeError("Comparison must be with an object of AxisAlignedBox2")

    def __ne__(self, box):
        """
        Compares the inequality of self with another vector.

        :param  box: the other 2D box
        :type   box: AxisAlignedBox2
        :return:the box inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_box2(box):
            return self.max != box.max or self.max != box.max
        raise TypeError("Comparison must be with an object of AxisAlignedBox2")

    def is_empty(self):
        """
        Checks if self is empty

        :return:the emptiness of the box
        :rtype: bool
        """
        if not self.is_valid():
            return True
        return self.size() == Vector2(0.0, 0.0)

    def is_valid(self):
        return self.min is not None and self.max is not None

    def to_axis_aligned_box3(self):
        if self.is_valid():
            box_3d = geometry_utils.three_d.axis_aligned_box3.AxisAlignedBox3(self.min.to_point3(),
                                                                              self.max.to_point3())
        else:
            box_3d = geometry_utils.three_d.axis_aligned_box3.AxisAlignedBox3()
        return box_3d


def is_box2(input_variable):
    return isinstance(input_variable, AxisAlignedBox2)
