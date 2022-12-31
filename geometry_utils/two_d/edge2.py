import copy
import math
import geometry_utils.three_d.edge3
import geometry_utils.two_d.axis_aligned_box2

from geometry_utils.maths_utility import (floats_are_close, DOUBLE_EPSILON, PI, TWO_PI, is_list, is_int_or_float,
    CIRCLE_FACTORS, CIRCLE_DIVISIONS, HALF_PI, ONE_AND_HALF_PI, is_float, radians_to_degrees)
from geometry_utils.two_d.ellipse import Ellipse
from geometry_utils.two_d.point2 import Point2, is_point2
from geometry_utils.two_d.vector2 import is_vector2
from geometry_utils.two_d.matrix3 import Matrix3
from geometry_utils.two_d.vector2 import Vector2


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
    __str__(): string
        Returns the attributes of the 2D edge in string format
    __eq__(Edge2): bool
        Returns the equality comparison of the edge with another 2D edge
    __ne__(Edge2): bool
        Returns the inequality comparison of the edge with another 2D edge
    calculate_arc_centre(): Point2
        returns the calculated centre of the edge
    is_arc(): bool
        returns True if the edge is an arc
    point_parametric(int/float): Point2
        returns the point along the edge from 0 = p1 to 1 = p2
    parametric_point(Point2): int/float
        returns the number along the edge from p1 = 0 to p2 = 1
    get_arc_normal(Point2): Vector2
        returns the normal to an arc edge at specified 2D point
    get_line_normal(): Vector2
        returns the normal to line edge
    get_arc_tangent(Point2): Vector2
        returns the tangent of the arc edge at a specified 2D point
    get_line_tangent(Point2): Vector2
        returns the tangent of the line edge
    get_sweep_angle(): int/float
        returns the sweep of the edge
    get_edge_bounds(): AxisAlignedBox2
        returns the bounds of the edge in 2D points
    offset(Vector2): Edge2
        offsets the edge by the specified 2D vector and direction
    reverse(): Edge2
        reverses the direction of the edge and swaps the start and end positions
    mirror_x(): Edge2
        mirrors the edge about the x axis
    mirror_y(): Edge2
        mirrors the edge about the y axis
    mirror_origin(): Edge2
        mirrors the edge about the origin
    is_circle(): bool
        tests if the arc edge is a circle
    is_line(): bool
        tests if the edge is a line
    get_arc_start_angle(bool): float
        returns the angle of the start point of the arc in radians or degrees
    get_arc_end_angle(bool): float
        returns the angle of the end point of the arc in radians or degrees
    flatten_arc(): list
        returns a list of line edges about the arc circumference
    rotate(float): Edge2
        rotates the edge about the z axis with specified rotation angle
    is_parallel_to(Edge2): bool
        returns the parallel comparison of the edge with another 2D edge
    is_perpendicular_to(Edge2): bool
        returns the perpendicular comparison of the edge with another 2D edge
    get_slope(): float/str
        returns the slope of the edge and 'vertical' if the edge is vertical
    edge_length(): float
        returns the length of the edge
    angle_to_x_axis(): flaot
        returns the angle of the edge to the x axis
    angle_to_edge(Edge2): float
        returns the angle of the edge to another 2D edge
    minimum_y(): float
        returns the minimum y coordinate of the edge
    maximum_y(): float
        returns the maximum y coordinate of the edge
    minimum_x(): float
        returns the minimum x coordinate of the edge
    maximum_x(): float
        returns the maximum x coordinate of the edge
    vector_within_arc(Vector2): bool
        tests if the specified vector is within the arc edge
    transform(Matrix3): Edge2
        returns the edge transformed with the specified 3x3 matrix
    to_edge3(): Edge3
        returns a 3D edge from the 2D edge
    """

    def __init__(self,
                 p1=Point2(),
                 p2=Point2(),
                 radius=0.0,
                 clockwise=False,
                 large=False):
        if is_point2(p1) and is_point2(p2) and is_int_or_float(radius):
            self.p1 = p1
            self.p2 = p2
            self.radius = radius
            self.clockwise = clockwise
            self.large = large
            self.centre = self.calculate_centre()

            self.name = ''
            self.style = ''
            self.type = ''
            self.left_name = ''
            self.right_name = ''
        else:
            if not is_point2(p1) or not is_point2(p2):
                raise TypeError("First and second arguments must be objects of Point2")
            if not is_int_or_float(radius):
                raise TypeError("Radius must be an int or float")

    def __str__(self):
        """
        Prints the attributes of the 2D edge

        :return: the string of the edge
        :rtype: str
        """
        return ("Edge2(p1:" + str(self.p1) + ", p2:" + str(self.p2) + ", centre:" + str(self.centre) +
                ", radius:" + str(self.radius) + ", clockwise:" + str(self.clockwise) +
                ", large:" + str(self.large) + ")")

    def __eq__(self, other_edge):
        """
        Compares the equality of the edge and another 2D edge

        :param   other_edge: the other 2D point
        :type    other_edge: Edge2
        :return: the edge equality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_edge2(other_edge):
            equality =  (self.p1 == other_edge.p1 and self.p2 == other_edge.p2 and
                         self.radius == other_edge.radius and self.large == other_edge.large and
                         self.centre == other_edge.centre and self.clockwise == other_edge.clockwise)
            return equality
        raise TypeError("Comparison must be with another object of Edge2")

    def __ne__(self, other_edge):
        """
        Compares the inequality of the edge and another 2D edge

        :param   other_edge: the other 2D point
        :type    other_edge: Edge2
        :return: the edge inequality
        :rtype:  bool
        :raises: TypeError: Wrong argument type
        """
        if is_edge2(other_edge):
            inequality = (self.p1 != other_edge.p1 or self.p2 != other_edge.p2 or
                          self.radius != other_edge.radius or self.large != other_edge.large or
                          self.centre != other_edge.centre or self.clockwise != other_edge.clockwise)
            return inequality
        raise TypeError("Comparison must be with another object of Edge2")

    def get_direction_vector(self):
        return (self.p2 - self.p1).normalised()

    def calculate_centre(self):
        """
        Calculates the centre of the arc

        :return:the 2D point of the arc centre
        :rtype: Point2
        """
        if self.p1 == self.p2:
            return self.p1

        if not self.is_arc():
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
        return self.radius > DOUBLE_EPSILON

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
                t = self.get_sweep_angle() * s
                if self.clockwise:
                    t *= -1
                p1_vector = self.p1.to_vector2()
                arc_centre_vector = self.centre.to_vector2()
                rotated_p1 = p1_vector.rotate(arc_centre_vector, t)
                return Point2(rotated_p1.x, rotated_p1.y)
            tangent = self.get_line_tangent()
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
            if self.is_circle():
                return 0.5

            if self.p1 == self.p2:
                return 1.0

            if self.is_arc():
                p1_vector = self.p1.to_vector2()
                p2_vector = self.p2.to_vector2()

                point_to_centre_distance = point - self.centre
                centre_to_arc_centre_distance = (((p1_vector + p2_vector)/2.0) - self.centre.to_vector2())

                if centre_to_arc_centre_distance == Vector2(0.0, 0.0):
                    centre_to_arc_centre_distance = (self.p2 - self.p1).get_perpendicular()

                    if not self.clockwise:
                        centre_to_arc_centre_distance.invert()

                else:
                    if self.large:
                        centre_to_arc_centre_distance.invert()

                point_to_centre_distance.normalise()
                centre_to_arc_centre_distance.normalise()

                dot_product = centre_to_arc_centre_distance.dot(point_to_centre_distance)
                determinant = (centre_to_arc_centre_distance.x * point_to_centre_distance.y) - \
                              (centre_to_arc_centre_distance.y * point_to_centre_distance.x)
                point_to_arc_centre_point_angle = math.atan2(determinant, dot_product)

                if self.clockwise:
                    point_to_arc_centre_point_angle = -point_to_arc_centre_point_angle

                if point_to_arc_centre_point_angle > PI:
                    point_to_arc_centre_point_angle -= TWO_PI
                point_to_arc_centre_point_angle /= self.get_sweep_angle()

                return point_to_arc_centre_point_angle + 0.5

            if self.is_line():
                tangent = self.get_line_tangent()
                point_p1_difference = (point - self.p1)
                p1_to_p2_distance = self.p1.distance_to(self.p2)
                distance = tangent.dot(point_p1_difference)
                return distance / p1_to_p2_distance
        raise TypeError("Argument must be an object of Point2")

    def get_arc_normal(self, point):
        """
        Gets the vector normal to an arc at a specified 2D point

        :param point: point on arc to find normal at
        :return: the resulting arc normal
        :rtype: Vector2
        :raises: wrong arguments types
        """
        if is_point2(point):
            if self.is_arc():
                return (self.centre - point).normalised()
            raise TypeError("Get Arc Normal can not be derived for a line")
        raise TypeError("Input argument must be an object of Point2")

    def get_line_normal(self):
        """
        Gets the vector normal to a line

        :return: the resulting line normal
        :rtype: Vector2
        :raises: wrong argument type
        """
        if not self.is_arc():
            return self.get_line_tangent().get_perpendicular()
        raise TypeError("Get Line Normal can not be derived for an arc")

    def get_arc_tangent(self, point):
        """
        Calculates the tangent of the arc edge at a specified 2D point

        :param point: point on arc to find tangent at
        :return:the resulting tangent of the edge
        :rtype: Vector2
        :raises: wrong arguments types
        """
        if is_point2(point):
            if self.is_arc():
                if self.clockwise:
                    return self.get_arc_normal(point).get_perpendicular()
                else:
                    return self.get_arc_normal(point).get_perpendicular().inverted()
            raise TypeError("Arc tangent can not be derived for a line")
        raise TypeError("Input argument must be an object of Point2")

    def get_line_tangent(self):
        """
        Gets the vector tangent to a line

        :return: the resulting line tangent
        :rtype: Vector2
        :raises: wrong argument type
        """
        if self.is_arc():
            raise TypeError("Line tangent can not be derived for an arc")
        return (self.p2 - self.p1).normalised()

    def get_sweep_angle(self):
        """
        Calculates the sweep of the edge which is an arc

        :return:the resulting sweep of the edge which is an arc
        :rtype: int/float
        """
        if not self.is_arc():
            return 0.0

        ellipse = Ellipse(start=self.p1, centre=self.centre, end=self.p2, major_radius=self.radius,
                          minor_radius=self.radius, clockwise=self.clockwise, angle=0.0)
        return ellipse.get_arc_sweep()

    def get_edge_bounds(self):
        """
        Creates a 2D AxisAlignedBox of the edge

        :return:the resulting 2D box of the edge
        :rtype: AxisAlignedBox2
        """
        bounds = geometry_utils.two_d.axis_aligned_box2.AxisAlignedBox2()
        bounds.include(self.p1)
        bounds.include(self.p2)
        return bounds

    def offset(self, vector):
        """
        Offsets the edge by the provided 2D vector

        :param vector: the 2D vector by which the edge is to be offset by
        :raises wrong argument type
        """
        if is_vector2(vector):
            self.p1 += vector
            self.p2 += vector
            self.centre = self.calculate_centre()
            return self
        else:
            raise TypeError("Edge offset is done by an object of Vector2")

    def reverse(self):
        """
        Reverses the direction of the edge

        """
        self.p1, self.p2 = self.p2, self.p1
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def mirror_x(self):
        """
        Mirrors the edge about the x axis

        """
        self.p1.mirror_x()
        self.p2.mirror_x()
        self.centre = self.calculate_centre()
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def mirror_y(self):
        """
        Mirrors the edge about the y axis

        """
        self.p1.mirror_y()
        self.p2.mirror_y()
        self.centre = self.calculate_centre()
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def mirror_origin(self):
        """
        Mirrors the edge about the origin

        """
        self.p1.mirror_origin()
        self.p2.mirror_origin()
        self.centre = self.calculate_centre()
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def is_circle(self):
        """
        Tests if the arc edge is a circle

        :return: if the arc edge is a circle
        :rtype bool
        """
        return self.is_arc() and self.p1 == self.p2

    def is_line(self):
        """
        Tests if the edge is a line

        :return: if the edge is a line
        :rtype bool
        """
        return (not self.is_arc()) and (not self.p1 == self.p2)

    def get_arc_start_angle(self, rad=False):
        """
        Calculates the angle of the start point of the arc

        :param rad: if the result should be in rad
        :return: arc start angle
        :rtype: float
        """
        angle = math.atan2(self.p1.y - self.centre.y, self.p1.x - self.centre.x)
        if not rad:
            angle = radians_to_degrees(angle)
        return angle

    def get_arc_end_angle(self, rad=False):
        """
        Calculates the angle of the end point of the arc

        :param rad: if the result should be in rad
        :return: arc end angle
        :rtype: float
        """
        angle = math.atan2(self.p2.y - self.centre.y, self.p2.x - self.centre.x)
        if not rad:
            angle = radians_to_degrees(angle)
        return angle

    def flatten_arc(self):
        """
        Returns a list of line edges that define the arc circumference

        :return: list of line edges
        :rtype: list
        """
        arc_start_angle = self.get_arc_start_angle(True)
        arc_end_angle = self.get_arc_end_angle(True)

        if (not self.clockwise and arc_start_angle > arc_end_angle) or (self.clockwise and arc_start_angle < arc_end_angle):
            arc_start_angle, arc_end_angle = arc_end_angle, arc_start_angle

        start_number, start_diff = divmod((arc_start_angle * CIRCLE_DIVISIONS / TWO_PI) + 0.5, 1)
        end_number, end_diff = divmod((arc_end_angle * CIRCLE_DIVISIONS / TWO_PI) + 0.5, 1)

        number = int(start_number)
        if self.clockwise:
            end_number -= 1
        else:
            end_number += 1

        points = []
        temp = Point2()

        while number != end_number:
            x_factor, y_factor = CIRCLE_FACTORS[number]
            if number == start_number:
                temp = copy.deepcopy(self.p1)
            elif number == end_number:
                temp = copy.deepcopy(self.p2)
            else:
                temp.x = self.centre.x + self.radius * x_factor
                temp.y = self.centre.y + self.radius * y_factor
            part_point = Point2(temp.x, temp.y)
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

    def rotate(self, rotation_angle):
        """
        Rotates the 2D edge about the z axis with a rotation angle

        :param rotation_angle: the angle with which the edge rotation is done
        :raises wrong angle argument type
        """
        if is_float(rotation_angle):
            rotation_matrix = Matrix3.rotation(rotation_angle)

            self.p1 = rotation_matrix * self.p1
            self.p2 = rotation_matrix * self.p2
            self.centre = self.calculate_centre()

            return self
        raise TypeError("Rotation angle must be a float")

    def is_parallel_to(self, other_edge):
        """
        Tests if the 2D edge is parallel to another 2D edge

        :param other_edge: the other 2D edge
        :return: if the two edges are parallel to each other
        :rtype: bool
        :raises: wrong argument type
        """
        if is_edge2(other_edge):
            return self.get_slope() == other_edge.get_slope()
        raise TypeError("Parallel check must be with an Edge2 object")

    def is_perpendicular_to(self, other_edge):
        """
        Tests if the 2D edge is perpendicular to another 2D edge

        :param other_edge: the other 2D edge
        :return: if the two edges are perpendicular to each other
        :rtype: bool
        :raises: wrong argument type
        """
        if is_edge2(other_edge):
            return (self.angle_to_edge(other_edge) == HALF_PI or self.angle_to_edge(other_edge) == -ONE_AND_HALF_PI or
                    self.angle_to_edge(other_edge) == -HALF_PI or self.angle_to_edge(other_edge) == ONE_AND_HALF_PI)
        raise TypeError("Perpendicular check must be with an Edge2 object")

    def get_slope(self):
        """
        Returns the slope of a line edge

        :return: the slope of the line or 'vertical' if the edge is a vertical edge
        :rtype: float/str
        :raises: edge type error if it is an arc
        """
        if self.is_arc():
            raise TypeError("Slope can not be derived for an arc")
        numerator = self.p2.y - self.p1.y
        denominator = self.p2.x - self.p1.x
        if denominator == 0:
            return "Vertical"
        return numerator / denominator

    def edge_length(self):
        """
        Returns the length of the edge if it is an arc or line

        :return: the length of the edge
        :rtype: float
        """
        if self.is_arc():
            ellipse = Ellipse(self.p1, self.centre, self.p2, self.radius, self.radius, self.clockwise)
            sweep = ellipse.get_arc_sweep()
            return sweep * self.radius
        return self.p1.distance_to(self.p2)

    def angle_to_x_axis(self):
        """
        Returns the angle the edge makes with the x axis in radians

        :return: the angle to x axis
        :rtype: float
        :raises: edge type error if it is an arc
        """
        if self.is_arc():
            raise TypeError("X-axis angle can not be derived for an arc")
        return math.atan2(self.p2.y - self.p1.y, self.p2.x - self.p1.x)

    def angle_to_edge(self, other_edge):
        """
        Returns the angle the 2D edge makes with another 2D edge in radians

        :return: the angle to the other 2D edge
        :rtype: float
        :raises: edge type error if any of the edges is an arc
        """
        if is_edge2(other_edge):
            if self.is_arc() or other_edge.is_arc():
                raise TypeError("Angle check can not be found from an arc")
            return self.angle_to_x_axis() - other_edge.angle_to_x_axis()
        raise TypeError("Angle check must be done with another object Edge2")

    def minimum_y(self):
        """
        Returns the minimum y coordinate of an edge

        :return: the minimum y coordinate value
        :rtype: float
        """
        return min(self.p1.y, self.p2.y)

    def maximum_y(self):
        """
        Returns the maximum y coordinate of an edge

        :return: the maximum y coordinate value
        :rtype: float
        """
        return max(self.p1.y, self.p2.y)

    def minimum_x(self):
        """
        Returns the minimum x coordinate of an edge

        :return: the minimum x coordinate value
        :rtype: float
        """
        return min(self.p1.x, self.p2.x)

    def maximum_x(self):
        """
        Returns the maximum x coordinate of an edge

        :return: the maximum x coordinate value
        :rtype: float
        """
        return max(self.p1.x, self.p2.x)

    def vector_within_arc(self, vector):
        """
        Tests if the 2D vector is within an arc edge

        :param vector: the 2D vector to test its position in the 2D edge
        :return: if the vector is within the arc

        """
        if is_vector2(vector) and self.is_arc():
            start_dash = self.p1 - self.centre
            end_dash = self.p2 - self.centre
            int_dash = vector - self.centre.to_vector2()

            if self.clockwise:
                start_dash.y *= -1
                end_dash.y *= -1
                int_dash.y *= -1

            start = start_dash.angle_to_x_axis()
            extent = end_dash.angle_to_x_axis() - start

            if floats_are_close(start, 0.0):
                start = 0.0
            if floats_are_close(extent, 0.0):
                extent = 0.0
            if extent < 0.0:
                extent += TWO_PI

            end = start + extent
            theta = int_dash.angle_to_x_axis()

            if floats_are_close(theta, 0.0):
                theta = 0.0

            while start < 0:
                start += TWO_PI

            while end < start:
                end += TWO_PI

            while not floats_are_close(theta, start) and theta < start:
                theta += TWO_PI

            return (((theta > start) or floats_are_close(theta, start)) and
                    ((theta < end) or floats_are_close(theta, end)))
        if not self.is_arc():
            raise TypeError("Check must be done with an arc edge")
        if not is_vector2(vector):
            raise TypeError("Argument must be a 2D vector object")

    def transform(self, transformation_matrix):
        """
        Transforms an edge with provided 3x3 matrix

        :param transformation_matrix: 3x3 matrix to transform the edge
        """
        midpoint = self.point_parametric(0.5)
        self.p1 = transformation_matrix * self.p1
        self.p2 = transformation_matrix * self.p2
        transformed_centre = transformation_matrix * self.centre
        self.centre = self.calculate_centre()
        transformed_midpoint = transformation_matrix * midpoint
        self_midpoint = self.point_parametric(0.5)

        if self.is_arc():
            if self.centre != transformed_centre or self_midpoint != transformed_midpoint:
                self.clockwise = not self.clockwise
                self.centre = self.calculate_centre()
        return self

    def to_edge3(self):
        """
        Converts the 2D edge to a 3D edge

        :return: the resulting Edge3 object
        :rtype: Edge3
        """
        edge_3d = geometry_utils.three_d.edge3.Edge3(self.p1.to_point3(), self.p2.to_point3(), None,
                                                     self.radius, self.clockwise, self.large)

        edge_3d.name = self.name
        edge_3d.style = self.style
        edge_3d.type = self.type
        edge_3d.left_name = self.left_name
        edge_3d.right_name = self.right_name

        return edge_3d

def is_edge2(input_variable):
    """
    Checks if the input variable is an object of Edge2

    :param input_variable: the input variable to be checked
    :return: bool
    """
    return isinstance(input_variable, Edge2)
