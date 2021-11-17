'''
from math import atan2

from maths_utility import floats_are_close, double_epsilon, pi, double_pi
from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.ellipse import Ellipse
from two_d.intersection import Intersection
from two_d.point2 import Point2


class Edge2:
    def __init__(self,
                 p1=Point2(0.0, 0.0),
                 p2=Point2(0.0, 0.0),
                 radius=0.0,
                 clockwise=False,
                 large=False):
        if isinstance(p1, Point2) and isinstance(p2, Point2) and isinstance(radius, float):
            self.p1 = p1
            self.p2 = p2
            self.radius = radius
            self.clockwise = clockwise
            self.large = large
            self.arc_centre = self.calculate_arc_centre()

    def calculate_arc_centre(self):
        if floats_are_close(self.radius, 0.0):
            return (self.p1 + self.p2) * 0.5

        ellipse = Ellipse()
        ellipse.initialise_from_points_and_radii(self.p1, self.p2, self.radius, self.radius, self.clockwise, self.large,
                                                 0.0)

        return ellipse.centre

    def is_arc(self):
        return self.radius > double_epsilon()

    def point_parametric(self, s):
        if isinstance(s, float):
            if self.p1 == self.p2:
                return self.p1

            if self.is_arc():
                t = self.get_sweep() * s
                if self.clockwise:
                    t *= -1
                p1_vector = self.p1.to_vector()
                arc_centre_vector = self.arc_centre.to_vector()
                return p1_vector.rotate(arc_centre_vector, t)
            tangent = self.get_tangent()
            p1_p2_distance = self.p1.distance_to(self.p2)
            vector = tangent * (s * p1_p2_distance)
            return self.p1 + vector

    def parametric_point(self, point):
        if isinstance(point, Point2):
            if self.p1 == self.p2:
                return 0.5

            if self.is_arc():
                point_to_centre_distance = (point - self.arc_centre).to_vector()
                centre_to_arc_centre_distance = (((self.p2 + self.p1).to_vector()/2.0) - self.arc_centre.to_vector())

                if floats_are_close(centre_to_arc_centre_distance.x, 0.0) and \
                        floats_are_close(centre_to_arc_centre_distance.y, 0.0):
                    centre_to_arc_centre_distance = (self.p2 - self.p1).to_vector().get_perpendicular()

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

                if point_to_arc_centre_point_angle > pi():
                    point_to_arc_centre_point_angle -= double_pi()
                point_to_arc_centre_point_angle /= self.get_sweep()

                return point_to_arc_centre_point_angle + 0.5

            tangent = self.get_tangent()  # vector
            point_p1_difference = (point - self.p1).to_vector()  # vector
            p1_to_p2_distance = self.p1.distance_to(self.p2)
            distance = tangent.dot(point_p1_difference)
            return distance / p1_to_p2_distance

    def get_tangent(self):
        p1_vector = self.p1.to_vector()
        p2_vector = self.p2.to_vector()
        return (p2_vector - p1_vector).normalise()

    def get_sweep(self):
        if not self.is_arc():
            return 0.0
        ellipse = Ellipse(self.arc_centre, self.radius, self.radius, 0.0)
        return ellipse.get_arc_sweep(self.p1, self.p2, self.clockwise)

    def get_edge_bounds(self):
        bounds = AxisAlignedBox2()
        bounds.include(self.p1)
        bounds.include(self.p2)
        return bounds

    def intersect(self, other_edge, list_of_intersections):
        if isinstance(other_edge, Edge2) and isinstance(list_of_intersections, list):
            edges_intersection = Intersection()
            edges_intersection.intersect_lines(self.p1, self.p2, other_edge.p1, other_edge.p2)
            list_of_intersections.append(edges_intersection)

'''
from math import atan2

from maths_utility import floats_are_close, double_epsilon, pi, double_pi, is_list, is_float
from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.ellipse import Ellipse
from two_d.intersection import Intersection
from two_d.point2 import Point2, is_point2


class Edge2:
    def __init__(self,
                 p1=Point2(0.0, 0.0),
                 p2=Point2(0.0, 0.0),
                 radius=0.0,
                 clockwise=False,
                 large=False):
        if is_point2(p1) and is_point2(p2) and is_float(radius):
            self.p1 = p1
            self.p2 = p2
            self.radius = radius
            self.clockwise = clockwise
            self.large = large
            self.arc_centre = self.calculate_arc_centre()

    def calculate_arc_centre(self):
        if floats_are_close(self.radius, 0.0):
            return (self.p1 + self.p2) * 0.5

        ellipse = Ellipse(start=self.p1, end=self.p2, major_radius=self.radius, minor_radius=self.radius,
                          clockwise=self.clockwise, large_arc=self.large, angle=0.0)
        return ellipse.centre

    def is_arc(self):
        return self.radius > double_epsilon()

    def point_parametric(self, s):
        if is_float(s):
            if self.p1 == self.p2:
                return self.p1

            if self.is_arc():
                t = self.get_sweep() * s
                if self.clockwise:
                    t *= -1
                p1_vector = self.p1.to_vector()
                arc_centre_vector = self.arc_centre.to_vector()
                return p1_vector.rotate(arc_centre_vector, t)
            tangent = self.get_tangent()
            p1_p2_distance = self.p1.distance_to(self.p2)
            vector = tangent * (s * p1_p2_distance)
            return self.p1 + vector

    def parametric_point(self, point):
        if is_point2(point):
            if self.p1 == self.p2:
                return 0.5

            if self.is_arc():
                point_to_centre_distance = (point - self.arc_centre).to_vector()
                centre_to_arc_centre_distance = (((self.p2 + self.p1).to_vector()/2.0) - self.arc_centre.to_vector())

                if floats_are_close(centre_to_arc_centre_distance.x, 0.0) and \
                        floats_are_close(centre_to_arc_centre_distance.y, 0.0):
                    centre_to_arc_centre_distance = (self.p2 - self.p1).to_vector().get_perpendicular()

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

                if point_to_arc_centre_point_angle > pi():
                    point_to_arc_centre_point_angle -= double_pi()
                point_to_arc_centre_point_angle /= self.get_sweep()

                return point_to_arc_centre_point_angle + 0.5

            tangent = self.get_tangent()
            point_p1_difference = (point - self.p1).to_vector()
            p1_to_p2_distance = self.p1.distance_to(self.p2)
            distance = tangent.dot(point_p1_difference)
            return distance / p1_to_p2_distance

    def get_tangent(self):
        p1_vector = self.p1.to_vector()
        p2_vector = self.p2.to_vector()
        return (p2_vector - p1_vector).normalise()

    def get_sweep(self):
        if not self.is_arc():
            return 0.0
        ellipse = Ellipse(start=self.p1, centre=self.arc_centre, end=self.p2, major_radius=self.radius,
                          minor_radius=self.radius, clockwise=self.clockwise, angle=0.0)
        return ellipse.get_arc_sweep()

    def get_edge_bounds(self):
        bounds = AxisAlignedBox2()
        bounds.include(self.p1)
        bounds.include(self.p2)
        return bounds

    def intersect(self, other_edge, list_of_intersections):
        if is_edge2(other_edge) and is_list(list_of_intersections):
            edges_intersection = Intersection()
            edges_intersection.intersect_lines(self.p1, self.p2, other_edge.p1, other_edge.p2)
            list_of_intersections.append(edges_intersection) 


def is_edge2(input_variable):
    return isinstance(input_variable, Edge2)
