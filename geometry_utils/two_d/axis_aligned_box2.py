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
    def __init__(self, minimum=Point2(0.0, 0.0), maximum=Point2(0.0, 0.0)):
        if is_point2(minimum) and is_point2(maximum):
            self.min = minimum
            self.max = maximum
        else:
            raise TypeError("AxisAlignedBox2 arguments must be objects of Point2")

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
            self.max.x = max(self.max.x, other.x)
            self.min.x = min(self.min.x, other.x)
            self.max.y = max(self.max.y, other.y)
            self.min.y = min(self.min.y, other.y)
        elif is_box2(other):
            self.include(other.min)
            self.include(other.max)
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
            return self.__contains__(item.min) and self.__contains__(item.max)
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
        return Vector2((self.min.x + self.max.x) * 0.5, (self.min.y + self.max.y) * 0.5)

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

    def empty(self):
        """
        Checks if self is empty

        :return:the emptiness of the box
        :rtype: bool
        """
        return self.size() == Vector2(0.0, 0.0)


def is_box2(input_variable):
    return isinstance(input_variable, AxisAlignedBox2)
