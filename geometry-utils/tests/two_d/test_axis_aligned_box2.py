import pytest

from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.point2 import Point2


@pytest.fixture()
def box1():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))


@pytest.fixture()
def box2():
    return AxisAlignedBox2()


@pytest.fixture()
def test_point2_1():
    return Point2(0.0, 0.0)


def test_box_contains_point(box2, test_point2_1):
    assert test_point2_1 in box2
