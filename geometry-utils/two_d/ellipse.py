from math import atan2, sin, cos, fabs, sqrt

from maths_utility import double_epsilon, double_pi, degrees_to_radians
from two_d.point2 import Point2


class Ellipse:
    def __init__(self, centre=Point2(0.0, 0.0), radius_x=0.0, radius_y=0.0, angle=0.0):
        if isinstance(centre, Point2) and isinstance(radius_x, float) and \
           isinstance(radius_y, float) and isinstance(angle, float):
            self.centre = centre
            self.major_radius = radius_x
            self.minor_radius = radius_y
            self.angle = angle
            self.valid = True

    def initialise_from_points_and_radii(self,
                                         start=Point2(0.0, 0.0),
                                         end=Point2(0.0, 0.0),
                                         major_radius=0.0,
                                         minor_radius=0.0,
                                         large_arc=False,
                                         clockwise=False,
                                         angle=0.0):
        if isinstance(start, Point2) and isinstance(end, Point2) and \
                isinstance(major_radius, float) and isinstance(minor_radius, float) and isinstance(angle, float):
            self.major_radius = major_radius
            self.minor_radius = minor_radius
            self.angle = angle
            self.valid = self.calculate_centre(start, end, major_radius, minor_radius, large_arc, clockwise, angle)

    def calculate_centre(self,
                         start=Point2(0.0, 0.0),
                         end=Point2(0.0, 0.0),
                         major_radius=0.0,
                         minor_radius=0.0,
                         large_arc=False,
                         clockwise=False,
                         angle=0.0):
        if isinstance(start, Point2) and isinstance(end, Point2) and \
                isinstance(major_radius, float) and isinstance(minor_radius, float) and isinstance(angle, float):
            valid = True

            angle_in_radians = degrees_to_radians(angle)
            sin_phi = sin(angle_in_radians)
            cos_phi = cos(angle_in_radians)

            x_dash = (cos_phi * ((start.x - end.x)/2.0)) + (sin_phi * ((start.y - end.y)/2.0))
            y_dash = (-sin_phi * ((start.x - end.x)/2.0)) + (cos_phi * ((start.y - end.y)/2.0))

            rx = fabs(major_radius)
            ry = fabs(minor_radius)

            delta = ((x_dash * x_dash) / (rx * rx)) + ((y_dash * y_dash) / (ry * ry))

            if delta > 1.0:
                root_delta = sqrt(delta)
                rx *= root_delta
                ry *= root_delta

                valid = False

            numerator = ((rx * rx) * (ry * ry)) - ((rx * rx) * (y_dash * y_dash)) - ((ry * ry) * (x_dash * x_dash))
            denominator = ((rx * rx) * (y_dash * y_dash)) + ((ry * ry) * (x_dash * x_dash))
            root_part = sqrt(numerator / denominator)

            if numerator < 0:
                root_part = 0

            if large_arc != clockwise:
                root_part *= -1

            cx_dash = root_part * ((rx * y_dash) / ry)
            cy_dash = root_part * -((ry * x_dash) / rx)

            self.centre.x = cos_phi * cx_dash - sin_phi * cy_dash + ((start.x + end.x) / 2.0)
            self.centre.y = sin_phi * cx_dash + cos_phi * cy_dash + ((start.y + end.y) / 2.0)

            return valid

    def get_arc_sweep(self, first_point, second_point, clockwise):
        if isinstance(first_point, Point2) and isinstance(second_point, Point2):
            if first_point == second_point:
                return 0.0

            first_point_to_centre_distance = (first_point - self.centre).to_vector()
            second_point_to_centre_distance = (second_point - self.centre).to_vector()
            if clockwise:
                first_point_to_centre_distance.y *= -1
                second_point_to_centre_distance.y *= -1
            start = atan2(first_point_to_centre_distance.y, first_point_to_centre_distance.x)
            extent = atan2(second_point_to_centre_distance.y, second_point_to_centre_distance.x) - start
            if extent < -double_epsilon():
                extent += double_pi()
            return extent
