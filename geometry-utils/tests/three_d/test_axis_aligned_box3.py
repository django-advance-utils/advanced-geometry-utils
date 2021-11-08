import pytest

from three_d.axis_aligned_box3 import AxisAlignedBox3
from three_d.point3 import Point3
from three_d.vector3 import Vector3


@pytest.fixture()
def box1():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))


@pytest.fixture()
def box2():
    return AxisAlignedBox3()


@pytest.fixture()
def box3():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))


@pytest.fixture()
def box4():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))


@pytest.fixture()
def test_point3_1():
    return Point3(0.0, 0.0, 0.0)


@pytest.fixture()
def test_point3_2():
    return Point3(1.0, 1.0, 1.0)


@pytest.fixture()
def test_vector3():
    return Vector3(1.0, 1.0, 1.0)


def test_box_contains_point(box1, test_point3_1, test_point3_2):
    assert test_point3_1 in box1
    assert test_point3_2 in box1


def test_box_does_not_contain_point(box2, test_point3_2):
    assert test_point3_2 not in box2


def test_box_includes_point(box3, test_point3_2):
    box3.include(test_point3_2)
    assert box3.min == Point3(0.0, 0.0, 0.0) and box3.max == Point3(1.0, 1.0, 1.0)


def test_box_intersects_box(box1, box2, box3):
    assert box1.intersects(box2)
    assert box1.intersects(box3)


def test_box_size(box1):
    assert box1.size() == Vector3(2.0, 2.0, 2.0)


def test_box_offset(box1, test_vector3):
    assert box1.offset(test_vector3) == AxisAlignedBox3(Point3(1.0, 1.0, 1.0), Point3(3.0, 3.0, 3.0))


def test_box_centre(box1):
    assert box1.centre() == Vector3(1.0, 1.0, 1.0)


def test_box_equals_box(box1):
    assert box1 == box1


def test_box_not_equals_box(box1, box2):
    assert box1 != box2


def test_box_is_empty(box4):
    assert box4.empty()
