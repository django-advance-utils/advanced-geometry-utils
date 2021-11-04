from two_d.point2 import Point2


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

            intersect = Intersection()

            u = point2 - point1
            v = point4 - point3
            w = point1 - point3

            denominator = u.x * v.y - u.y * v.x

            if denominator == 0.0:
                intersect.vectors_intersect = False
                intersect.on_first_segment = False
                intersect.on_second_segment = False
                intersect.point = point1

                if do_colinear_test:
                    w_normalised = w.to_vector().normalise()
                    u_normalised = u.to_vector().normalise()
                    det = w_normalised.x * u_normalised.y - w_normalised.y - u_normalised.x

                    if det == 0.0:
                        intersect.vectors_intersect = True
                        intersect.colinear = True
