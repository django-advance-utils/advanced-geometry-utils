from math import atan2, sin, cos, fabs, sqrt

from maths_utility import double_epsilon, double_pi, degrees_to_radians, is_float, is_int_or_float, are_ints_or_floats
from two_d.point2 import Point2, is_point2


class Ellipse:
    def __init__(self,
                 start=Point2(0.0, 0.0),
                 centre=Point2(0.0, 0.0),
                 end=Point2(0.0, 0.0),
                 major_radius=0.0,
                 minor_radius=0.0,
                 clockwise=False,
                 large_arc=False,
                 angle=0.0):

        if (is_point2(start) and is_point2(centre) and is_point2(end) and
                are_ints_or_floats([major_radius, minor_radius])):

            self.start = start
            if centre:
                self.centre = centre
            else:
                self.calculate_centre()
            self.end = end
            self.major_radius = major_radius
            self.minor_radius = minor_radius
            self.clockwise = clockwise
            self.large_arc = large_arc
            self.angle = angle
            self.delta = 0.0
            self.valid = self.test_validity()

        else:
            if not is_point2(start) or not is_point2(centre) or not is_point2(end):
                raise TypeError("First, second and third arguments must be objects of Point2")
            if not are_ints_or_floats(major_radius, minor_radius):
                raise TypeError("Fourth and fifth arguments must be ints or floats")

    def calculate_centre(self):
        angle_in_radians = degrees_to_radians(self.angle)
        sin_phi = sin(angle_in_radians)
        cos_phi = cos(angle_in_radians)

        x_dash = (cos_phi * ((self.start.x - self.end.x) / 2.0)) + (sin_phi * ((self.start.y - self.end.y) / 2.0))
        y_dash = (-sin_phi * ((self.start.x - self.end.x) / 2.0)) + (cos_phi * ((self.start.y - self.end.y) / 2.0))

        rx = fabs(self.major_radius)
        ry = fabs(self.minor_radius)

        self.delta = ((x_dash * x_dash) / (rx * rx)) + ((y_dash * y_dash) / (ry * ry))

        if self.delta > 1.0:
            root_delta = sqrt(self.delta)
            rx *= root_delta
            ry *= root_delta

        numerator = ((rx * rx) * (ry * ry)) - ((rx * rx) * (y_dash * y_dash)) - ((ry * ry) * (x_dash * x_dash))
        denominator = ((rx * rx) * (y_dash * y_dash)) + ((ry * ry) * (x_dash * x_dash))

        if numerator < 0:
            root_part = 0
        else:
            root_part = sqrt(numerator / denominator)

        if self.large_arc != self.clockwise:
            root_part *= -1

        cx_dash = root_part * ((rx * y_dash) / ry)
        cy_dash = root_part * -((ry * x_dash) / rx)

        self.centre.x = cos_phi * cx_dash - sin_phi * cy_dash + ((self.start.x + self.end.x) / 2.0)
        self.centre.y = sin_phi * cx_dash + cos_phi * cy_dash + ((self.start.y + self.end.y) / 2.0)

    def test_validity(self):
        ellipse_validity = False
        if self.delta <= 1.0:
            ellipse_validity = True
        return ellipse_validity

    def get_arc_sweep(self):
        if self.start == self.end:
            return 0.0

        first_point_to_centre_distance = (self.start - self.centre).to_vector()
        second_point_to_centre_distance = (self.end - self.centre).to_vector()
        if self.clockwise:
            first_point_to_centre_distance.y *= -1
            second_point_to_centre_distance.y *= -1
        start = atan2(first_point_to_centre_distance.y, first_point_to_centre_distance.x)
        extent = atan2(second_point_to_centre_distance.y, second_point_to_centre_distance.x) - start
        if extent < -double_epsilon():
            extent += double_pi()
        return extent