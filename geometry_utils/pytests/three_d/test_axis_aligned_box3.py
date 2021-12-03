import pytest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3


def test_box3_box3_addition_return_arithmetic(test_box3_1, test_box3_2):
    with pytest.raises(TypeError):
        return test_box3_1 + test_box3_2


def test_box3_vector3_addition_return_type(test_box3_1, test_vector3_1):
    assert isinstance(test_box3_1 + test_vector3_1, AxisAlignedBox3)


def test_box3_vector3_addition_arithmetic(test_box3_1, test_vector3_1):
    assert test_box3_1 + test_vector3_1 == AxisAlignedBox3(Point3(1.0, 1.0, 1.0), Point3(3.0, 3.0, 3.0))


def test_box3_contains_point3(test_box3_1, test_point3_1, test_point3_2):
    assert test_point3_1 in test_box3_1
    assert test_point3_2 in test_box3_1


def test_box3_does_not_contain_point3(test_box3_2, test_point3_2):
    assert test_point3_2 not in test_box3_2


def test_box3_includes_point3(test_box3_3, test_point3_3):
    test_box3_3.include(test_point3_3)
    assert test_box3_3.min == Point3(0.0, 0.0, 0.0) and test_box3_3.max == Point3(1.0, 1.0, 1.0)


def test_box3_contains_box3(test_box3_1, test_box3_3):
    assert test_box3_3 in test_box3_1
    assert test_box3_3 in test_box3_1


def test_box3_does_not_contain_box3(test_box3_1, test_box3_3):
    assert test_box3_1 not in test_box3_3
    assert test_box3_1 not in test_box3_3


def test_box3_includes_box3(test_box3_1, test_box3_3):
    test_box3_3.include(test_box3_1)
    assert test_box3_3.min == Point3(0.0, 0.0, 0.0) and test_box3_3.max == Point3(2.0, 2.0, 2.0)


def test_box3_intersects_box3(test_box3_1, test_box3_2, test_box3_3):
    assert test_box3_1.intersects(test_box3_2)
    assert test_box3_1.intersects(test_box3_3)


def test_box3_size(test_box3_1):
    assert test_box3_1.size() == Vector3(2.0, 2.0, 2.0)


def test_box3_offset_by_vector3(test_box3_1, test_vector3_1):
    assert test_box3_1.offset(test_vector3_1) == AxisAlignedBox3(Point3(1.0, 1.0, 1.0), Point3(3.0, 3.0, 3.0))


def test_box3_centre(test_box3_1):
    assert test_box3_1.centre() == Point3(1.0, 1.0, 1.0)


def test_box3_equals_box3(test_box3_1, test_box3_2, test_box3_4):
    assert test_box3_1 == test_box3_1
    assert test_box3_2 == test_box3_4


def test_box3_not_equals_box3(test_box3_1, test_box3_2):
    assert test_box3_1 != test_box3_2


def test_box3_is_empty(test_box3_4):
    assert test_box3_4.empty()
