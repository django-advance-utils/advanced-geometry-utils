import math

from geometry_utils.maths_utility import is_int_or_float, DOUBLE_EPSILON, sqr, PI, is_float, HALF_PI, ONE_AND_HALF_PI
from geometry_utils.three_d.matrix4 import Matrix4
from geometry_utils.three_d.point3 import Point3, is_point3
from geometry_utils.three_d.vector3 import Vector3, is_vector3

import geometry_utils.two_d.edge2
import geometry_utils.two_d.point2
import geometry_utils.two_d.vector2
import geometry_utils.three_d.axis_aligned_box3


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
                 via=None,
                 radius=0.0,
                 clockwise=False,
                 large=False):
        if is_point3(p1) and is_point3(p2) and is_int_or_float(radius):
            self.p1 = p1
            self.p2 = p2
            self.radius = radius
            self.clockwise = clockwise
            self.large = large
            if is_point3(via):
                self.via = via
            elif via is None:
                self.via = self.get_via()
            self.sweep_angle = 0.0
            self.centre = self.calculate_centre()

            self.name = ''
            self.style = ''
            self.type = ''
            self.left_name = ''
            self.right_name = ''
        else:
            if not is_point3(p1) or not is_point3(p2) or not is_point3(via):
                raise TypeError("First, second and third arguments must be objects of Point2")
            if not is_int_or_float(radius):
                raise TypeError("Fourth argument must be an int or float")

    def get_via(self):
        edge_2d = geometry_utils.two_d.edge2.Edge2(geometry_utils.two_d.point2.Point2(self.p1.x, self.p1.y),
                                                   geometry_utils.two_d.point2.Point2(self.p2.x, self.p2.y),
                                                   self.radius, self.clockwise, self.large)
        edge_2d_midpoint = edge_2d.point_parametric(0.5)
        return Point3(edge_2d_midpoint.x, edge_2d_midpoint.y, self.p1.z)

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

    def is_clockwise(self):
        se = self.p2 - self.via
        sm = self.p1 - self.via

        cp = se.cross(sm)

        return cp > 0

    def calculate_centre(self):
        """
        Calculates the centre of the arc

        :return:the 3D point of the arc centre
        :rtype: Point3
        """
        if self.is_circle():
            return self.p1

        elif self.is_arc():
            try:
                p1_vector = self.p1.to_vector3()
                p2_vector = self.p2.to_vector3()
                via_vector = self.via.to_vector3()

                n = (p1_vector.cross(via_vector) + via_vector.cross(p2_vector) + p2_vector.cross(p1_vector)).normalised()
                s = (p2_vector - p1_vector)
                u = s.cross(n).normalised()
                v = n.cross(u).normalised()
                d = n.dot(p1_vector)

                a = geometry_utils.two_d.vector2.Vector2()
                b = geometry_utils.two_d.vector2.Vector2()
                c = geometry_utils.two_d.vector2.Vector2()

                a.x = (u.x * p1_vector.x) + (u.y * p1_vector.y) + (u.z * p1_vector.z)
                a.y = (v.x * p1_vector.x) + (v.y * p1_vector.y) + (v.z * p1_vector.z)

                b.x = (u.x * via_vector.x) + (u.y * via_vector.y) + (u.z * via_vector.z)
                b.y = (v.x * via_vector.x) + (v.y * via_vector.y) + (v.z * via_vector.z)

                c.x = (u.x * p2_vector.x) + (u.y * p2_vector.y) + (u.z * p2_vector.z)
                c.y = (v.x * p2_vector.x) + (v.y * p2_vector.y) + (v.z * p2_vector.z)

                sol = geometry_utils.two_d.vector2.Vector2()
                sol.x = ((sqr(b.x) + sqr(b.y)) - (sqr(a.x) + sqr(a.y))) / 2
                sol.y = ((sqr(c.x) + sqr(c.y)) - (sqr(a.x) + sqr(a.y))) / 2

                tol = geometry_utils.two_d.vector2.Vector2(b.x - a.x, b.y - a.y)
                yol = geometry_utils.two_d.vector2.Vector2(c.x - a.x, c.y - a.y)

                ans = geometry_utils.two_d.vector2.Vector2()
                ans.y = ((sol.x * yol.x) - (sol.y * tol.x)) / ((tol.y * yol.x) - (tol.x * yol.y))
                ans.x = (sol.x - (tol.y * ans.y)) / tol.x

                ans_3d = Vector3()
                ans_3d.x = (u.x * ans.x) + (v.x * ans.y)
                ans_3d.y = (u.y * ans.x) + (v.y * ans.y)
                ans_3d.z = (u.z * ans.x) + (v.z * ans.y)
                m = n * d
                q = m + ans_3d

                self.sweep_angle = math.acos(
                    ((p2_vector - q).dot(p1_vector - q)) / ((p2_vector - q).length() * (p1_vector - q).length()))
                return Point3(q.x, q.y, q.z)
            except ZeroDivisionError:
                return Point3()

        else:
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

            # if self.is_arc():
            #     t = self.sweep_angle * s
            #     norm = self.get_plane_normal()
            #
            #     p1v = self.p1 - self.centre
            #
            #     plane_x = p1v.normalised()
            #     plane_y = norm.cross(p1v).normalised()
            #
            #     point = ((plane_x * (self.radius * math.cos(t))) + (plane_y * (self.radius * math.sin(t))))
            #
            #     point = self.centre + point
            #
            #     return point

            if self.is_arc():
                # gotten from https://stackoverflow.com/questions/10550874/how-to-calc-a-cyclic-arc-through-3-points-and-parameterize-it-0-1-in-3d
                o = (self.via.to_vector3() + self.p2.to_vector3()) / 2
                c = (self.p1.to_vector3() + self.p2.to_vector3()) / 2
                x = (self.via - self.p1) / -2

                n = (self.p2 - self.p1).cross(self.via - self.p1)
                d = n.normalised().cross(self.via.to_vector3() - o)
                v = (self.p1.to_vector3() - c).normalised()

                check = d.dot(v)
                angle = PI

                if check != 0:
                    t = (x.dot(v)) / check
                    v1 = (self.p1.to_vector3() - self.centre.to_vector3()).normalised()

                    f_dir_p1 = v1
                    v2 = (self.p2 - self.centre).normalised()
                    angle = math.acos(v1.dot(v2))

                    if angle != 0:
                        v1 = self.via - self.p1
                        v2 = self.via - self.p2

                        if v1.dot(v2) > 0:
                            angle = PI * 2 - angle

                f_dir_p2 = ((n * -1).cross(self.p1 - self.centre)).normalised()

                x = s * angle
                return self.centre + f_dir_p1 * self.radius * math.cos(x) + f_dir_p2 * self.radius * math.sin(x)

            tangent = self.get_line_tangent()  # vector
            p1_p2_distance = self.p1.distance_to(self.p2)  # vector
            vector = tangent * (s * p1_p2_distance)  # vector
            return self.p1 + vector  # point

        else:
            raise TypeError("Point parametric must be with an int or float")

    def get_plane_normal(self):
        return self.p1.to_vector3().cross(self.p2.to_vector3())

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
            if self.is_circle():
                return 0.5

            # elif self.is_arc():
            #     p1_vector = self.p1.to_vector3()
            #     p2_vector = self.p2.to_vector3()
            #
            #     arc_norm = self.get_arc_normal(self.via)
            #
            #     v = point - self.centre
            #     vc = ((p1_vector + p2_vector) / 2.0) - self.centre.to_vector3()
            #
            #     if vc == Vector3(0.0, 0.0, 0.0):
            #         perpendicular_1 = Vector3()
            #         perpendicular_2 = Vector3()
            #         perpendicular_1, perpendicular_2 = (self.p2 - self.p1).get_perpendicular(perpendicular_1,
            #                                                                                  perpendicular_2)
            #         vc = perpendicular_1
            #
            #         dp = vc.dot(self.via - self.p1)
            #
            #         if dp < 0:
            #             vc.invert()
            #     else:
            #         if self.large:
            #             vc.invert()
            #
            #     vc.normalise()
            #     v.normalise()
            #
            #     a = math.atan2(v.cross(vc).dot(arc_norm), vc.dot(v))
            #
            #     if a > PI:
            #         a -= TWO_PI
            #
            #     a = a / self.sweep_angle
            #
            #     return a + 0.5
            elif self.is_arc():
                p1_2d = geometry_utils.two_d.point2.Point2(self.p1.x, self.p1.y)
                p2_2d = geometry_utils.two_d.point2.Point2(self.p2.x, self.p2.y)
                point_2d = geometry_utils.two_d.point2.Point2(point.x, point.y)
                edge_2d = geometry_utils.two_d.edge2.Edge2(p1_2d, p2_2d, self.radius, self.clockwise, self.large)
                s = edge_2d.parametric_point(point_2d)
                return s
            elif self.is_line:
                tangent = self.get_line_tangent()  # vector
                point_p1_difference = (point - self.p1)  # vector
                distance = tangent.dot(point_p1_difference)
                return distance / self.p1.distance_to(self.p2)
        else:
            raise TypeError("Argument must be an object of Point3")

    def is_line(self):
        return not self.is_arc and not self.p1 == self.p2

    def get_line_tangent(self):
        """
        Calculates the tangent of the edge

        :return:the resulting tangent of the edge
        :rtype: int/float
        """
        if self.is_arc():
            raise TypeError("Line tangent can not be derived for an arc")
        return (self.p2 - self.p1).normalised()

    def get_arc_normal(self, point):
        if is_point3(point):
            if self.is_arc():
                return (self.centre - point).normalised()
            raise TypeError("Get Arc Normal can not be derived for a line")
        raise TypeError("Input argument must be an object of Point2")

    def get_arc_tangent(self, point):
        """
        Calculates the tangent of the edge

        :return:the resulting tangent of the edge
        :rtype: int/float
        """
        if is_point3(point):
            if self.is_arc():
                if self.clockwise:
                    return self.get_arc_normal(point).get_perpendicular()
                else:
                    return self.get_arc_normal(point).get_perpendicular().inverse()
            raise TypeError("Arc tangent can not be derived for a line")
        raise TypeError("Input argument must be an object of Point3")

    def get_edge_bounds(self):
        """
        Creates a 3D AxisAlignedBox of the edge

        :return:the resulting 3D box of the edge
        :rtype: AxisAlignedBox3
        """
        bounds = geometry_utils.three_d.axis_aligned_box3.AxisAlignedBox3()
        bounds.include(self.p1)
        bounds.include(self.p2)
        return bounds

    def is_circle(self):
        return self.is_arc() and self.p1 == self.p2

    def get_arc_start_angle(self, rad=False):
        edge_2d = self.to_edge2()
        angle = edge_2d.get_arc_start_angle(rad)
        return angle

    def get_arc_end_angle(self, rad=False):
        edge_2d = self.to_edge2()
        angle = edge_2d.get_arc_end_angle(rad)
        return angle

    def reverse(self):
        self.p1, self.p2 = self.p2, self.p1
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def mirror_x(self):
        self.p1.mirror_x()
        self.p2.mirror_x()
        self.centre = self.calculate_centre()
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def mirror_y(self):
        self.p1.mirror_y()
        self.p2.mirror_y()
        self.centre = self.calculate_centre()
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def mirror_z(self):
        self.p1.mirror_z()
        self.p2.mirror_z()
        self.centre = self.calculate_centre()
        if self.is_arc():
            self.clockwise = not self.clockwise
        return self

    def mirror_origin(self):
        self.p1.mirror_origin()
        self.p2.mirror_origin()
        self.centre = self.calculate_centre()
        if self.clockwise:
            self.clockwise = False
        return self

    def transform(self, transformation_matrix):
        self.p1 = transformation_matrix * self.p1
        self.p2 = transformation_matrix * self.p2
        self.centre = self.calculate_centre()
        return self

    def offset(self, vector):
        if is_vector3(vector):
            self.p1 += vector
            self.p2 += vector
            self.centre = self.calculate_centre()
            self.via = self.get_via()
        else:
            raise TypeError("Edge offset is done by an object of Vector3")

    def rotate(self, rotation_angle):
        if is_float(rotation_angle):
            rotation_matrix = Matrix4.z_rotation(rotation_angle)

            self.p1 = rotation_matrix * self.p1
            self.p2 = rotation_matrix * self.p2
            self.centre = self.calculate_centre()
            self.via = self.get_via()

            return self
        raise TypeError("Rotation angle must be a float")

    def to_vector3(self):
        return self.p2 - self.p1

    def to_edge2(self):
        edge_2d = geometry_utils.two_d.edge2.Edge2(self.p1.to_point2(), self.p2.to_point2(),
                                                   self.radius, self.clockwise, self.large)
        edge_2d.name = self.name
        edge_2d.style = self.style
        edge_2d.type = self.type
        edge_2d.left_name = self.left_name
        edge_2d.right_name = self.right_name

        return edge_2d

    def angle_to_edge(self, other_edge):
        if is_edge3(other_edge):
            if self.is_arc() or other_edge.is_arc():
                raise TypeError("Angle check can not be found from an arc")
            return self.angle_to_x_axis() - other_edge.angle_to_x_axis()
        raise TypeError("Angle check must be done with another object Edge2")

    def angle_to_x_axis(self):
        if self.is_arc():
            raise TypeError()
        self_vector = self.to_vector3()
        if self_vector.length() != 0:
            return math.acos(self_vector.x / self_vector.length())
        else:
            return math.acos(self_vector.x)

    def is_perpendicular_to(self, other_edge):
        if is_edge3(other_edge):
            return (self.angle_to_edge(other_edge) == HALF_PI or self.angle_to_edge(other_edge) == -ONE_AND_HALF_PI or
                    self.angle_to_edge(other_edge) == -HALF_PI or self.angle_to_edge(other_edge) == ONE_AND_HALF_PI)
        raise TypeError("Perpendicular check must be with an Edge3 object")

    def minimum_z(self):
        return min(self.p1.z, self.p2.z)

    def maximum_z(self):
        return max(self.p1.z, self.p2.z)

    def minimum_y(self):
        return min(self.p1.y, self.p2.y)

    def maximum_y(self):
        return max(self.p1.y, self.p2.y)

    def minimum_x(self):
        return min(self.p1.x, self.p2.x)

    def maximum_x(self):
        return max(self.p1.x, self.p2.x)


def is_edge3(input_variable):
    return isinstance(input_variable, Edge3)
