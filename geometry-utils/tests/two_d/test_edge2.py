import pytest

from two_d.edge2 import Edge2
from two_d.point2 import Point2


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
