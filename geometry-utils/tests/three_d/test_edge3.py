from three_d.axis_aligned_box3 import AxisAlignedBox3
from three_d.point3 import Point3
from three_d.vector3 import Vector3
from maths_utility import floats_are_close

from math import sqrt


def test_edge_point_parametric(test_edge3_1, test_edge3_2):
    assert test_edge3_2.point_parametric(0.0) == test_edge3_2.p1
    assert test_edge3_2.point_parametric(1.0) == test_edge3_2.p2
    assert test_edge3_1.point_parametric(0.5) == test_edge3_1.p1  # p1 = p2


def test_edge_parametric_point(test_edge3_2):
    assert test_edge3_2.parametric_point(test_edge3_2.p1) == 0.0
    assert floats_are_close(test_edge3_2.parametric_point(test_edge3_2.p2), 1.0)


def test_get_tangent(test_edge3_2):
    assert test_edge3_2.get_tangent() == Vector3(2.0/sqrt(12.0), 2.0/sqrt(12.0), 2.0/sqrt(12.0))


def test_get_arc_centre(test_edge3_2):
    assert test_edge3_2.get_arc_centre() == Point3(1.0, 1.0, 1.0)


def test_get_edge_bounds(test_edge3_2):
    assert test_edge3_2.get_edge_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))
