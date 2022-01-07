from math import atan2, sin, cos, fabs, sqrt

from geometry_utils.maths_utility import DOUBLE_EPSILON, TWO_PI, degrees_to_radians, are_ints_or_floats
from geometry_utils.two_d.point2 import Point2, is_point2


class Ellipse:
    """
    A class to create a 2D ellipse

    Attributes:
    ___________
    start: Point2
        the 2D point of the ellipse start
    centre: Point2
        the 2D point of the ellipse centre
    end: Point2
        the 2D point of the ellipse end
    major_radius: int/float
        the major radius of the ellipse
    minor_radius: int/float
        the minor radius of the ellipse
    clockwise: bool
        check if the ellipse direction is clockwise
    large_arc: bool
        check if the ellipse is large
    angle: int/float
        the angle of inclination of the ellipse
    delta: int/float

    valid:
        check if the ellipse is a valid one

    Methods:
    ________
    calculate_centre():
        Calculates the centre of the ellipse
    test_validity(): Point2
        Tests if the ellipse has attributes that make it valid
    get_arc_sweep(): float
        Returns the sweep of the ellipse
    """

    def __init__(self,
                 start=Point2(0.0, 0.0),
                 centre=None,
                 end=Point2(0.0, 0.0),
                 major_radius=0.0,
                 minor_radius=0.0,
                 clockwise=False,
                 large_arc=False,
                 angle=None):

        if (is_point2(start) and is_point2(end) and
                are_ints_or_floats([major_radius, minor_radius])):

            self.start = start
            self.end = end
            self.major_radius = major_radius
            self.minor_radius = minor_radius
            self.clockwise = clockwise
            self.large_arc = large_arc
            self.angle = angle
            self.delta = 0.0
            self.valid = self.test_validity()
            if centre is not None and is_point2(centre):
                self.centre = centre
            else:
                self.centre = self.calculate_centre()

        else:
            if not is_point2(start) or not is_point2(centre) or not is_point2(end):
                raise TypeError("First, second and third arguments must be objects of Point2")
            if not are_ints_or_floats([major_radius, minor_radius]):
                raise TypeError("Fourth and fifth arguments must be ints or floats")

    def __str__(self):
        return ("Ellipse2(start:" + str(self.start) + ", centre:" + str(self.centre) + ", end:" + str(self.end) +
                ", major radius:" + str(self.major_radius) + ", minor radius:" + str(self.minor_radius) +
                ", clockwise:" + str(self.clockwise) + ", large arc:" + str(self.large_arc) +
                ", angle:" + str(self.angle) + ", delta:" + str(self.delta) + ", valid:" + str(self.valid) + ")")

    def calculate_centre(self):
        """
        Calculates the centre of self

        """
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
            self.valid = False

        numerator = ((rx * rx) * (ry * ry)) - ((rx * rx) * (y_dash * y_dash)) - ((ry * ry) * (x_dash * x_dash))
        denominator = ((rx * rx) * (y_dash * y_dash)) + ((ry * ry) * (x_dash * x_dash))

        root_part = 0.0
        if numerator > 0.0:
            root_part = sqrt(numerator / denominator)

        if self.large_arc != self.clockwise:
            root_part *= -1

        cx_dash = root_part * ((rx * y_dash) / ry)
        cy_dash = root_part * -((ry * x_dash) / rx)
        centre = Point2()
        centre.x = cos_phi * cx_dash - sin_phi * cy_dash + ((self.start.x + self.end.x) / 2.0)
        centre.y = sin_phi * cx_dash + cos_phi * cy_dash + ((self.start.y + self.end.y) / 2.0)
        return centre

    def test_validity(self):
        """
        Checks the validity of self

        :return:the self validity
        :rtype: bool
        """

        ellipse_validity = False
        if self.delta <= 1.0:
            ellipse_validity = True
        return ellipse_validity

    def get_arc_sweep(self):
        """
        Calculates the sweep of self

        :return:the resulting arc sweep
        :rtype: int or float
        """

        if self.start == self.end:
            return 0.0

        first_point_to_centre_distance = (self.start - self.centre)
        second_point_to_centre_distance = (self.end - self.centre)
        if self.clockwise:
            first_point_to_centre_distance.y *= -1
            second_point_to_centre_distance.y *= -1
        start = atan2(first_point_to_centre_distance.y, first_point_to_centre_distance.x)
        extent = atan2(second_point_to_centre_distance.y, second_point_to_centre_distance.x) - start
        if extent < -DOUBLE_EPSILON:
            extent += TWO_PI
        return extent
