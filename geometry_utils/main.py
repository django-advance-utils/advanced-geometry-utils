import math

from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.point2 import Point2

if __name__ == '__main__':
    test_edge = Edge2(Point2(0.0, 0.0), Point2(5.0, 5.0), 2.5, True, True)
    test_centre = test_edge.arc_centre
    test_parametric_point = test_edge.parametric_point(Point2(4.0, 4.0))
    radius = 600.0

    circle = []
    for i in range(360):
        t = ((math.pi * 2) / 360.0) * float(i)
        circle.append(Point2((math.sin(t) * radius),
                             (math.cos(t) * radius)))

    test_edge2 = Edge2(circle[60], circle[0], 600.0, True, True)
    test_parametric_point2 = test_edge2.parametric_point(circle[0])
    print(test_parametric_point2)
