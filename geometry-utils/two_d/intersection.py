from two_d.point2 import Point2
from maths_utility import floats_are_close, ranges_overlap


class Intersection:
    def __init__(self,
                 point=Point2(0.0, 0.0),
                 vectors_intersect=False,
                 on_first_segment=False,
                 on_second_segment=False,
                 colinear=False,
                 end_of_line=False):

        self.vectors_intersect = vectors_intersect
        self.on_first_segment = on_first_segment
        self.on_second_segment = on_second_segment
        self.colinear = colinear
        self.end_of_line = end_of_line
        self.point = point

    def intersect_lines(self, point1, point2, point3, point4, do_colinear_test=False):
        if isinstance(point1, Point2) and isinstance(point2, Point2) and \
           isinstance(point3, Point2) and isinstance(point4, Point2):

            u = point2 - point1
            v = point4 - point3
            w = point1 - point3

            denominator = u.x * v.y - u.y * v.x

            if floats_are_close(denominator, 0.0):
                self.vectors_intersect = False
                self.on_first_segment = False
                self.on_second_segment = False
                self.point = point1

                if do_colinear_test:
                    w_normalised = w.to_vector().normalise()
                    u_normalised = u.to_vector().normalise()
                    det = w_normalised.x * u_normalised.y - w_normalised.y - u_normalised.x

                    if floats_are_close(det, 0.0):
                        self.vectors_intersect = True
                        self.colinear = True

                        if ranges_overlap(min(point1.x, point2.x), max(point1.x, point2.x),
                                          min(point3.x, point4.x), max(point3.x, point4.x)) and \
                           ranges_overlap(min(point1.y, point2.y), max(point1.y, point2.y),
                                          min(point3.y, point4.y), max(point3.y, point4.y)):

                            self.on_first_segment = True
                            self.on_second_segment = True

            self.vectors_intersect = True

            s = (v.x * w.y - v.y * w.x) / denominator
            # t = (u.x * w.y - u.y * w.x) / denominator

            self.point.x = point1.x + s * u.x
            self.point.y = point1.y + s * u.y

            intersect_point_to_point1_distance = self.point.distance_to(point1)
            intersect_point_to_point2_distance = self.point.distance_to(point2)
            intersect_point_to_point3_distance = self.point.distance_to(point3)
            intersect_point_to_point4_distance = self.point.distance_to(point4)

            if floats_are_close(intersect_point_to_point1_distance, 0.0) or \
               floats_are_close(intersect_point_to_point2_distance, 0.0) or \
               floats_are_close(intersect_point_to_point3_distance, 0.0) or \
               floats_are_close(intersect_point_to_point4_distance, 0.0):
                self.end_of_line = True

            length_of_side1 = point1.distance_to(point2)
            length_of_side2 = point3.distance_to(point4)

            self.on_first_segment = floats_are_close(intersect_point_to_point1_distance +
                                                     intersect_point_to_point2_distance, length_of_side1)

            self.on_second_segment = floats_are_close(intersect_point_to_point3_distance +
                                                      intersect_point_to_point4_distance, length_of_side2)
