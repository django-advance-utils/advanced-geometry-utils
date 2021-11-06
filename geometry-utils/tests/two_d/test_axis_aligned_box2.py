import pytest

from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.point2 import Point2
from two_d.vector2 import Vector2


@pytest.fixture()
def box1():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))


@pytest.fixture()
def box2():
    return AxisAlignedBox2()


@pytest.fixture()
def box3():
    return AxisAlignedBox2()


@pytest.fixture()
def box4():
    return AxisAlignedBox2()


@pytest.fixture()
def test_point2_1():
    return Point2(0.0, 0.0)


@pytest.fixture()
def test_point2_2():
    return Point2(1.0, 1.0)


@pytest.fixture()
def test_vector2():
    return Vector2(1.0, 1.0)


def test_box_contains_point(box1, test_point2_1, test_point2_2):
    assert test_point2_1 in box1
    assert test_point2_2 in box1


def test_box_does_not_contain_point(box2, test_point2_2):
    assert test_point2_2 not in box2


def test_box_includes_point(box3, test_point2_2):
    box3.include(test_point2_2)
    assert box3.min == Point2(0.0, 0.0) and box3.max == Point2(1.0, 1.0)


def test_box_intersects_box(box1, box2, box3):
    assert box1.intersects(box2)
    assert box1.intersects(box3)


def test_box_size(box1):
    assert box1.size() == Vector2(2.0, 2.0)


def test_box_offset(box1, test_vector2):
    assert box1.offset(test_vector2) == AxisAlignedBox2(Point2(1.0, 1.0), Point2(3.0, 3.0))


def test_box_centre(box1):
    assert box1.centre() == Vector2(1.0, 1.0)


def test_box_equals_box(box1):
    assert box1 == box1


def test_box_not_equals_box(box1, box2):
    assert box1 != box2


def test_box_is_empty(box4):
    # assert box2.empty()
    print(box4.max.y)

