from geometry_utils.maths_utility import floats_are_close, is_float, is_int_or_float, DOUBLE_EPSILON
from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.point3 import Point3, is_point3


class Edge3:
    """
    A class to create a 3D edge

    Attributes:
    ___________
    p1: Point3
        initial 3D point of the edge
    via:Point3
        a 3D point along the edge
    p2: Point3
        final 3D point of the edge
    radius: int/float
        the radius of the edge
    clockwise: bool
        check if the edge direction is clockwise
    large:
        check if the edge is large
    arc_centre:
        the calculated centre of the edge

    Methods:
    ________
    calculate_arc_centre(): Point3
        returns the calculated centre of the edge
    is_arc(): bool
        returns True if the edge is an arc
    point_parametric(int/float): Point2
        returns the point along the edge from 0 = p1 to 1 = p2
    parametric_point(Point2): int/float
        returns the number along the edge from p1 = 0 to p2 = 1
    get_tangent(): int/float
        returns the tangent of the edge
    get_sweep(): int/float
        returns the sweep of the edge
    get_edge_bounds(): AxisAlignedBox3
        returns the bounds of the edge in 2D points
    """

    def __init__(self,
                 p1=Point3(0.0, 0.0, 0.0),
                 p2=Point3(0.0, 0.0, 0.0),
                 via=Point3(0.0, 0.0, 0.0),
                 radius=0.0,
                 clockwise=False,
                 large=False):
        if is_point3(p1) and is_point3(p2) and is_point3(via) and is_float(radius):
            self.p1 = p1
            self.p2 = p2
            self.via = via
            self.radius = radius
            self.clockwise = clockwise
            self.large = large
            self.centre = self.calculate_centre()
        else:
            if not is_point3(p1) or not is_point3(p2) or not is_point3(via):
                raise TypeError("First, second and third arguments must be objects of Point2")
            if not is_int_or_float(radius):
                raise TypeError("Fourth argument must be an int or float")

    def __str__(self):
        return ("Edge3(p1:" + str(self.p1) + ", p2:" + str(self.p2) + ", via:" + str(self.via) +
                ", centre:" + str(self.centre) + ", radius:" + str(self.radius) + ", clockwise:" + str(self.clockwise) +
                ", large:" + str(self.large) + ")")

    def __eq__(self, other_edge):
        """
        Compares the equality of the edge and another 3D edge

        :param   other_edge: the other 3D point
        :type    other_edge: Edge3
        :return: the edge equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_edge3(other_edge):
            equality = (self.p1 == other_edge.p1 and self.p2 == other_edge.p2 and self.via == self.via and
                        self.radius == other_edge.radius and self.large == other_edge.large and
                        self.centre == other_edge.centre and self.clockwise == other_edge.clockwise)
            return equality
        raise TypeError("Comparison must be with another object of Edge3")

    def calculate_centre(self):
        """
        Calculates the centre of the arc

        :return:the 3D point of the arc centre
        :rtype: Point3
        """
        if floats_are_close(self.radius, 0.0):
            return Point3((self.p1.x + self.p2.x) * 0.5, (self.p1.y + self.p2.y) * 0.5, (self.p1.z + self.p2.z) * 0.5)

    def is_arc(self):
        """
        Tests if the edge is an arc

        :return:if the edge is an arc
        :rtype: bool
        """
        return self.radius > DOUBLE_EPSILON

    def midpoint(self):
        return self.point_parametric(0.5)

    def point_parametric(self, s):
        """
        Calculates the point on the edge from 0 to 1

        :param  s: the number between 0 and 1 along the edge
        :type   s: int/float
        :return:the resulting point along the edge
        :rtype: Point3
        :raises:TypeError: wrong argument type
        """

        if is_int_or_float(s):
            if self.p1 == self.p2:
                return self.p1

            tangent = self.get_tangent()  # vector
            p1_p2_distance = self.p1.distance_to(self.p2)  # vector
            vector = tangent * (s * p1_p2_distance)  # vector
            return self.p1 + vector  # point

        else:
            raise TypeError("Point parametric must be with an int or float")

    def parametric_point(self, point):
        """
        Calculates the number on the edge from p1 to p2

        :param  point: the 3D point between along the edge
        :type   point: Point3
        :return:the resulting number along the edge
        :rtype: int/float
        :raises:TypeError: wrong argument type
        """
        if is_point3(point):
            tangent = self.get_tangent()  # vector
            point_p1_difference = (point - self.p1)  # vector
            distance = tangent.dot(point_p1_difference)
            return distance / self.p1.distance_to(self.p2)
        raise TypeError("Argument must be an object of Point3")

    def get_tangent(self):
        """
        Calculates the tangent of the edge

        :return:the resulting tangent of the edge
        :rtype: int/float
        """
        p1_vector = self.p1.to_vector3()
        p2_vector = self.p2.to_vector3()
        return (p2_vector - p1_vector).normalised()

    def get_edge_bounds(self):
        """
        Creates a 3D AxisAlignedBox of the edge

        :return:the resulting 3D box of the edge
        :rtype: AxisAlignedBox3
        """
        bounds = AxisAlignedBox3()
        bounds.include(self.p1)
        bounds.include(self.p2)
        return bounds

    def is_circle(self):
        return self.is_arc() and self.p1 == self.p2


def is_edge3(input_variable):
    return isinstance(input_variable, Edge3)
