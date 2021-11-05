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


@pytest.fixture()
def test_point2_2():
    return Point2(1.0, 1.0)


def test_box_contains_point(box1, test_point2_1, test_point2_2):
    assert test_point2_1 in box1
    assert test_point2_2 in box1


def test_box_does_not_contain_point(box2, test_point2_2):
    assert test_point2_2 not in box2


def test_box_includes_point(box2, test_point2_2):
    box2.include(test_point2_2)
    assert box2.min == Point2(0.0, 0.0) and box2.max == Point2(1.0, 1.0)
