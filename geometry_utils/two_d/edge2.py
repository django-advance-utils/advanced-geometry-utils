import copy
from math import atan2, acos, fabs, sin, cos, pi

from geometry_utils.maths_utility import floats_are_close, DOUBLE_EPSILON, PI, TWO_PI, is_list, is_int_or_float, CIRCLE_FACTORS, CIRCLE_DIVISIONS
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.ellipse import Ellipse
from geometry_utils.two_d.intersection import Intersection
from geometry_utils.two_d.point2 import Point2, is_point2
from geometry_utils.two_d.vector2 import is_vector2


class Edge2:
    """
    A class to create a 2D edge

    Attributes:
    ___________
    p1: Point2
        initial 2D point of the edge
    p2: Point2
        final 2D point of the edge
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
    calculate_arc_centre(): Point2
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
    get_edge_bounds(): AxisAlignedBox2
        returns the bounds of the edge in 2D points
    intersect(Edge2, list):
        returns an intersection of the edge with another edge and appends the list of intersections
    """

    def __init__(self,
                 p1=Point2(0.0, 0.0),
                 p2=Point2(0.0, 0.0),
                 radius=0.0,
                 clockwise=False,
                 large=False):
        if is_point2(p1) and is_point2(p2) and is_int_or_float(radius):
            self.p1 = p1
            self.p2 = p2
            self.radius = radius
            self.clockwise = clockwise
            self.large = large
            self.arc_centre = self.calculate_arc_centre()
        else:
            if not is_point2(p1) or not is_point2(p2):
                raise TypeError("First and second arguments must be objects of Point2")
            if not is_int_or_float(radius):
                raise TypeError("Radius must be an int or float")

    def __eq__(self, other_edge):
        """
        Compares the equality of the edge and another 2D edge

        :param   other_edge: the other 2D point
        :type    other_edge: Edge2
        :return: the edge equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_edge2(other):
            return self.p1 == other_edge.p1 and self.p2 == other_edge.p2 and \
                   self.radius == other_edge.radius and self.large == other_edge.large and \
                   self.arc_centre == other_edge.arc_centre and self.clockwise == other_edge.clockwise
        raise TypeError("Comparison must be with another object of Edge2")

    def calculate_arc_centre(self):
        """
        Calculates the centre of the arc

        :return:the 2D point of the arc centre
        :rtype: Point2
        """
        if self.p1 == self.p2:
            return self.p1

        if floats_are_close(self.radius, 0.0):
            return Point2((self.p1.x + self.p2.x) * 0.5, (self.p1.y + self.p2.y) * 0.5)

        ellipse = Ellipse(start = self.p1, end = self.p2, major_radius = self.radius, minor_radius = self.radius,
                          clockwise = self.clockwise, large_arc = self.large, angle=0.0)
        return ellipse.centre

    def is_arc(self):
        """
        Tests if the edge is an arc

        :return:if the edge is an arc
        :rtype: bool
        """
        return self.radius > double_epsilon()

    def point_parametric(self, s):
        """
        Calculates the point on the edge from 0 to 1

        :param  s: the number between 0 and 1 along the edge
        :type   s: int/float
        :return:the resulting point along the edge
        :rtype: Point2
        :raises:TypeError: wrong argument type
        """
        if is_int_or_float(s):
            if self.p1 == self.p2:
                return self.p1

            if self.is_arc():
                t = self.get_sweep() * s
                if self.clockwise:
                    t *= -1
                p1_vector = self.p1.to_vector2()
                arc_centre_vector = self.arc_centre.to_vector2()
                return p1_vector.rotate(arc_centre_vector, t)
            tangent = self.get_tangent()
            p1_p2_distance = self.p1.distance_to(self.p2)
            vector = tangent * (s * p1_p2_distance)
            return self.p1 + vector
        raise TypeError("Input variable must be an int or float")

    def parametric_point(self, point):
        """
        Calculates the number on the edge from p1 to p2

        :param  point: the 2D point between along the edge
        :type   point: Point2
        :return:the resulting number along the edge
        :rtype: int/float
        :raises:TypeError: wrong argument type
        """
        if is_point2(point):
            if self.p1 == self.p2:
                return 0.5

            if self.is_arc():
                p1_vector = self.p1.to_vector2()
                p2_vector = self.p2.to_vector2()

                point_to_centre_distance = (point - self.arc_centre)
                centre_to_arc_centre_distance = (((p1_vector + p2_vector)/2.0) - self.arc_centre.to_vector2())

                if floats_are_close(centre_to_arc_centre_distance.x, 0.0) and \
                        floats_are_close(centre_to_arc_centre_distance.y, 0.0):
                    centre_to_arc_centre_distance = (self.p2 - self.p1).get_perpendicular()

                    if not self.clockwise:
                        centre_to_arc_centre_distance = centre_to_arc_centre_distance.invert()

                else:
                    if self.large:
                        centre_to_arc_centre_distance = centre_to_arc_centre_distance.invert()

                point_to_centre_distance = point_to_centre_distance.normalise()
                centre_to_arc_centre_distance = centre_to_arc_centre_distance.normalise()

                dot_product = centre_to_arc_centre_distance.dot(point_to_centre_distance)
                determinant = (centre_to_arc_centre_distance.x * point_to_centre_distance.y) - \
                              (centre_to_arc_centre_distance.y * point_to_centre_distance.x)
                point_to_arc_centre_point_angle = atan2(determinant, dot_product)

                if self.clockwise:

                    point_to_arc_centre_point_angle = -point_to_arc_centre_point_angle

                if point_to_arc_centre_point_angle > PI:
                    point_to_arc_centre_point_angle -= TWO_PI
                point_to_arc_centre_point_angle /= self.get_sweep()

                return point_to_arc_centre_point_angle + 0.5

            tangent = self.get_tangent()
            point_p1_difference = (point - self.p1)
            p1_to_p2_distance = self.p1.distance_to(self.p2)
            distance = tangent.dot(point_p1_difference)
            return distance / p1_to_p2_distance
        raise TypeError("Argument must be an object of Point2")

    def get_tangent(self):
        """
        Calculates the tangent of the edge

        :return:the resulting tangent of the edge
        :rtype: int/float
        """
        p1_vector = self.p1.to_vector2()
        p2_vector = self.p2.to_vector2()
        return (p2_vector - p1_vector).normalise()

    def get_sweep(self):
        """
        Calculates the sweep of the edge

        :return:the resulting sweep of the edge
        :rtype: int/float
        """
        if not self.is_arc():
            return 0.0

        ellipse = Ellipse(start=self.p1, centre=self.arc_centre, end=self.p2, major_radius=self.radius,
                          minor_radius=self.radius, clockwise=self.clockwise, angle=270.0)
        return ellipse.get_arc_sweep()

    def get_edge_bounds(self):
        """
        Creates a 2D AxisAlignedBox of the edge

        :return:the resulting 2D box of the edge
        :rtype: AxisAlignedBox2
        """
        bounds = AxisAlignedBox2()
        bounds.include(self.p1)
        bounds.include(self.p2)
        return bounds

    def intersect(self, other_edge, list_of_intersections):
        """
        Creates the intersection of the edge with another edge and appends the list of intersections

        """
        if is_edge2(other_edge) and is_list(list_of_intersections):
            edges_intersection = Intersection()
            edges_intersection.intersect_lines(self.p1, self.p2, other_edge.p1, other_edge.p2)
            list_of_intersections.append(edges_intersection)
        else:
            if not is_edge2(other_edge):
                raise TypeError("First argument must be an object of Edge2")
            if not is_list(list_of_intersections):
                raise TypeError("Second argument must be a list")

    def offset_edge(self, vector):
        """
        Offsets the edge by the provided 2D vector

        :param vector: the 2D vector by which the edge is to be offset by

        """
        if is_vector2(vector):
            self.p1 += vector
            self.p2 += vector
        raise TypeError("Edge offset is done by an object of Vector2")

    def flip_xy(self):
        """
        Flips the x and y coordinates of the start and end points of the edge

        """
        self.p1.flip_xy()
        self.p2.flip_xy()
        if self.clockwise:
            self.clockwise = False

    def mirror_y(self):
        self.p1.mirror_y()
        self.p2.mirror_y()
        if self.clockwise:
            self.clockwise = False

    def is_circle(self):
        return self.is_arc() and self.p1 == self.p2

    def get_arc_start_angle(self):
        return atan2(self.p1.y - self.arc_centre.y, self.p1.x - self.arc_centre.x)

    def get_arc_end_angle(self):
        return atan2(self.p2.y - self.arc_centre.y, self.p2.x - self.arc_centre.x)

    def flatten_arc(self):
        arc_start_angle = self.get_arc_start_angle()
        arc_end_angle = self.get_arc_end_angle()

        start_number, start_diff = divmod((arc_start_angle * CIRCLE_DIVISIONS / TWO_PI) + 0.5, 1)
        end_number, end_diff = divmod((arc_end_angle * CIRCLE_DIVISIONS / TWO_PI) + 0.5, 1)

        number = int(start_number)
        if self.clockwise:
            end_number -= 1
        else:
            end_number+= 1

        points = []
        temp = Point2()

        while number != end_number:
            x_factor, y_factor = CIRCLE_FACTORS[number]
            if number == start_number:
                temp = copy.deepcopy(self.p1)
            elif number == end_number:
                temp = copy.deepcopy(self.p2)
            else:
                temp.x = self.arc_centre.x + self.radius * x_factor
                temp.y = self.arc_centre.y + self.radius * y_factor
            part_point = Point2(temp.x - self.p1.x * x_factor, temp.y - self.p1.y * y_factor)
            points.append(part_point)
            if self.clockwise:
                number -= 1
            else:
                number += 1

            if number >= CIRCLE_DIVISIONS:
                if number == end_number:
                    break
                number = 0

        list_of_arc_edges = []
        for previous_point, point in zip(points,points[1:]):
            list_of_arc_edges.append(Edge2(previous_point, point))
        return list_of_arc_edges


def is_edge2(input_variable):
    return isinstance(input_variable, Edge2)
