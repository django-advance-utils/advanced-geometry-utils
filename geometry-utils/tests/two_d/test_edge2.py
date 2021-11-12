from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.point2 import Point2
from two_d.vector2 import Vector2
from two_d.edge2 import Edge2
from maths_utility import floats_are_close

from math import sqrt


def test_edge2_point_parametric(test_edge2_1, test_edge2_2):
    assert test_edge2_2.point_parametric(0.0) == test_edge2_2.p1
    assert test_edge2_2.point_parametric(1.0) == test_edge2_2.p2
    assert test_edge2_1.point_parametric(0.5) == test_edge2_1.p1  # p1 = p2


def test_edge2_parametric_point_arcs(test_circle_points_1):
    # anticlockwise 10 deg
    e1 = Edge2(test_circle_points_1[10], test_circle_points_1[0], 600.0, False, False)

    # endpoints and centrepoint
    assert floats_are_close(e1.parametric_point(test_circle_points_1[355]), 1.5)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[0]), 1.0)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[5]), 0.5)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[10]), 0.0)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[15]), -0.5)

    e2 = Edge2(test_circle_points_1[36], test_circle_points_1[202], 600.0, True, False)

    # endpoints and centrepoint
    assert floats_are_close(e2.parametric_point(test_circle_points_1[285]), 1.5)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[202]), 1.0)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[119]), 0.5)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[36]), 0.0)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[313]), -0.5)

    # large arc
    e3 = Edge2(test_circle_points_1[40], test_circle_points_1[30], 600.0, True, True)

    assert floats_are_close(e3.parametric_point(test_circle_points_1[30]), 1.0)
    assert floats_are_close(e3.parametric_point(test_circle_points_1[215]), 0.5)
    assert floats_are_close(e3.parametric_point(test_circle_points_1[40]), 0.0)

    # clockwise semicircle (large)
    e4 = Edge2(test_circle_points_1[0], test_circle_points_1[180], 600.0, True, True)

    assert floats_are_close(e4.parametric_point(test_circle_points_1[180]), 1.0)
    assert floats_are_close(e4.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e4.parametric_point(test_circle_points_1[0]), 0.0)

    # clockwise semicircle (small) should be the same as the large version
    e5 = Edge2(test_circle_points_1[0], test_circle_points_1[180], 600.0, True, False)

    assert floats_are_close(e5.parametric_point(test_circle_points_1[180]), 1.0)
    assert floats_are_close(e5.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e5.parametric_point(test_circle_points_1[0]), 0.0)

    # anticlockwise semicircle (large)
    e6 = Edge2(test_circle_points_1[180], test_circle_points_1[0], 600.0, False, True)

    assert floats_are_close(e6.parametric_point(test_circle_points_1[0]), 1.0)
    assert floats_are_close(e6.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e6.parametric_point(test_circle_points_1[180]), 0.0)

    # anticlockwise semicircle (small) should be the same as the large version
    e7 = Edge2(test_circle_points_1[180], test_circle_points_1[0], 600.0, False, False)

    assert floats_are_close(e7.parametric_point(test_circle_points_1[0]), 1.0)
    assert floats_are_close(e7.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e7.parametric_point(test_circle_points_1[180]), 0.0)


def test_edge2_parametric_point(test_edge2_2):
    assert test_edge2_2.parametric_point(test_edge2_2.p1) == 0.0
    assert floats_are_close(test_edge2_2.parametric_point(test_edge2_2.p2), 1.0)


def test_edge2_get_tangent(test_edge2_2):
    assert test_edge2_2.get_tangent() == Vector2(2.0/sqrt(8.0), 2.0/sqrt(8.0))


def test_edge2_get_arc_centre(test_edge2_2):
    assert test_edge2_2.get_arc_centre() == Point2(1.0, 1.0)


def test_edge2_get_edge_bounds(test_edge2_2):
    assert test_edge2_2.get_edge_bounds() == AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))


def test_edge2_intersect_edge2(test_edge2_2, test_edge2_3):
    list_of_intersects = []
    test_edge2_2.intersect(test_edge2_3, list_of_intersects)
    assert list_of_intersects[-1].point == Point2(0.0, 0.0)
