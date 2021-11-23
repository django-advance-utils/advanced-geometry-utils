from two_d.point2 import Point2, is_point2
from maths_utility import floats_are_close, ranges_overlap


class Intersection:
    """
    A class to create a 2D intersection

    Attributes:
    ___________
    point: Point2
        the intersection point
    vectors_intersect: bool
        check if edges intersect
    on_first_segment: bool
        check if the edges intersect on first segment
    on_second_segment: bool
        check if the edges intersect on the second segment
    minor_radius: int or float
        the minor radius of the ellipse
    collinear: bool
        check if the edges are collinear
    end_of_line: bool
        check if the end of the edge has been reached
    do_collinear_test: bool
        check if collinear test is to be done

    Methods:
    ________
    intersect_lines(Point2, Point2, Point2, Point2):
        perform intersection of two edges   
    """

    def __init__(self,
                 point=Point2(0.0, 0.0),
                 vectors_intersect=False,
                 on_first_segment=False,
                 on_second_segment=False,
                 collinear=False,
                 end_of_line=False,
                 do_collinear_test=False):

        if is_point2(point):
            self.vectors_intersect = vectors_intersect
            self.on_first_segment = on_first_segment
            self.on_second_segment = on_second_segment
            self.collinear = collinear
            self.end_of_line = end_of_line
            self.point = point
            self.do_collinear_test = do_collinear_test
        else:
            raise TypeError("First argument must be an object of Point2")

    def intersect_lines(self, p1, p2, p3, p4):
        if is_point2(p1) and is_point2(p2) and is_point2(p3) and is_point2(p4):
            u = p2 - p1
            v = p4 - p3
            w = p1 - p3

            denominator = u.x * v.y - u.y * v.x

            if floats_are_close(denominator, 0.0):
                self.vectors_intersect = False
                self.on_first_segment = False
                self.on_second_segment = False
                self.point = p1
                self.do_collinear_test = True

                if self.do_collinear_test:
                    w_normalised = w.to_vector().normalise()
                    u_normalised = u.to_vector().normalise()
                    det = (w_normalised.x * u_normalised.y) - (w_normalised.y * u_normalised.x)

                    if floats_are_close(det, 0.0):
                        self.vectors_intersect = True
                        self.collinear = True

                        if ranges_overlap(min(p1.x, p2.x), max(p1.x, p2.x),
                                          min(p3.x, p4.x), max(p3.x, p4.x)) and \
                           ranges_overlap(min(p1.y, p2.y), max(p1.y, p2.y),
                                          min(p3.y, p4.y), max(p3.y, p4.y)):
                            self.on_first_segment = True
                            self.on_second_segment = True

            else:
                self.vectors_intersect = True

                s = (v.x * w.y - v.y * w.x) / denominator
                # t = (u.x * w.y - u.y * w.x) / denominator

                self.point.x = p1.x + s * u.x
                self.point.y = p1.y + s * u.y

                intersect_point_to_point1_distance = self.point.distance_to(p1)
                intersect_point_to_point2_distance = self.point.distance_to(p2)
                intersect_point_to_point3_distance = self.point.distance_to(p3)
                intersect_point_to_point4_distance = self.point.distance_to(p4)

                if floats_are_close(intersect_point_to_point1_distance, 0.0) or \
                   floats_are_close(intersect_point_to_point2_distance, 0.0) or \
                   floats_are_close(intersect_point_to_point3_distance, 0.0) or \
                   floats_are_close(intersect_point_to_point4_distance, 0.0):
                    self.end_of_line = True

                length_of_side1 = p1.distance_to(p2)
                length_of_side2 = p3.distance_to(p4)

                self.on_first_segment = floats_are_close(intersect_point_to_point1_distance +
                                                         intersect_point_to_point2_distance, length_of_side1)

                self.on_second_segment = floats_are_close(intersect_point_to_point3_distance +
                                                          intersect_point_to_point4_distance, length_of_side2)
        else:
            raise TypeError("Arguments must be objects of Point2")
