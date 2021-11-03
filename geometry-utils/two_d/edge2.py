from two_d.point2 import Point2


class Edge2:
    def __init__(self,
                 p1=Point2(0.0, 0.0),
                 p2=Point2(0.0, 0.0),
                 radius=0.0,
                 clockwise=False,
                 large=False):

        self.p1 = p1
        self.p2 = p2
        self.radius = radius
        self.clockwise = clockwise
        self.large = large
        self.arc_centre = (p1 + p2) * 0.5

    def point_parametric(self, s):
        if s == 0:
            return self.p1
        elif s == 1:
            return self.p2
        elif s == 0.5:
            return self.arc_centre


'''
Point Equality and Inequality Tests
'''


def test_vector_vector_equality(test_point_1, test_point_5):
    assert test_point_1 == test_point_1
    assert test_point_1 == test_point_5


def test_vector_vector_inequality(test_point_1, test_point_2):
    assert test_point_1 != test_point_2
    assert not (test_point_1 == test_point_2)
    assert not test_point_1 == 9.0
