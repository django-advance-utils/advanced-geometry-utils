import pytest

from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2


def test_box2_box2_addition_return_arithmetic(test_box2_1, test_box2_2):
    with pytest.raises(TypeError):
        return test_box2_1 + test_box2_2


def test_box2_vector2_addition_return_type(test_box2_1, test_vector2_1):
    assert isinstance(test_box2_1 + test_vector2_1, AxisAlignedBox2)


def test_box2_vector2_addition_arithmetic(test_box2_1, test_vector2_1):
    assert test_box2_1 + test_vector2_1 == AxisAlignedBox2(Point2(1.0, 1.0), Point2(3.0, 3.0))


def test_box2_contains_point2(test_box2_1, test_point2_1, test_point2_2):
    assert test_point2_1 in test_box2_1
    assert test_point2_2 in test_box2_1


def test_box2_does_not_contain_point2(test_box2_2, test_point2_2):
    assert test_point2_2 not in test_box2_2


def test_box2_includes_point2(test_box2_3, test_point2_3):
    test_box2_3.include(test_point2_3)
    assert test_box2_3.min == Point2(0.0, 0.0) and test_box2_3.max == Point2(1.0, 1.0)


def test_box2_contains_box2(test_box2_1, test_box2_3):
    assert test_box2_3 in test_box2_1
    assert test_box2_3 in test_box2_1


def test_box2_does_not_contain_box2(test_box2_1, test_box2_3):
    assert test_box2_1 not in test_box2_3
    assert test_box2_1 not in test_box2_3


def test_box2_includes_box2(test_box2_1, test_box2_3):
    test_box2_3.include(test_box2_1)
    assert test_box2_3.min == Point2(0.0, 0.0) and test_box2_3.max == Point2(2.0, 2.0)


def test_box2_intersects_box2(test_box2_1, test_box2_2, test_box2_3):
    assert test_box2_1.intersects(test_box2_2)
    assert test_box2_1.intersects(test_box2_3)


def test_box2_size(test_box2_1):
    assert test_box2_1.size() == Vector2(2.0, 2.0)


def test_box2_offset_by_vector2(test_box2_1, test_vector2_1):
    assert test_box2_1.offset(test_vector2_1) == AxisAlignedBox2(Point2(1.0, 1.0), Point2(3.0, 3.0))


def test_box2_centre(test_box2_1):
    assert test_box2_1.centre() == Point2(1.0, 1.0)


def test_box2_equals_box2(test_box2_1, test_box2_2, test_box2_4):
    assert test_box2_1 == test_box2_1
    assert test_box2_2 == test_box2_4


def test_box2_not_equals_box2(test_box2_1, test_box2_2):
    assert test_box2_1 != test_box2_2


def test_box2_is_empty(test_box2_4):
    assert test_box2_4.empty()
