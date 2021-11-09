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
