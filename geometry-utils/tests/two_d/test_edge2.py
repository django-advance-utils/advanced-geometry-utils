import pytest

from two_d.edge2 import Edge2
from two_d.point2 import Point2
from two_d.vector2 import Vector2
from maths_utility import floats_are_close

from math import sqrt


@pytest.fixture()
def test_edge2_1():
    return Edge2


@pytest.fixture()
def test_edge2_2():
    p1 = Point2(0.0, 0.0)
    p2 = Point2(2.0, 2.0)
    radius = 1.0

    return Edge2(p1, p2, radius)


def test_edge_point_parametric(test_edge2_2):
    assert test_edge2_2.point_parametric(0.0) == test_edge2_2.p1
    assert test_edge2_2.point_parametric(1.0) == test_edge2_2.p2


def test_edge_parametric_point(test_edge2_2):
    assert test_edge2_2.parametric_point(test_edge2_2.p1) == 0.0
    assert floats_are_close(test_edge2_2.parametric_point(test_edge2_2.p2), 1.0)


def test_get_tangent(test_edge2_2):
    assert test_edge2_2.get_tangent() == Vector2(2.0/sqrt(8.0), 2.0/sqrt(8.0))
