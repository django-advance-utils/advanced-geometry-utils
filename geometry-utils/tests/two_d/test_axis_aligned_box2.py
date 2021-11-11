from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.point2 import Point2
from two_d.vector2 import Vector2


def test_box_contains_point(box2_1, test_point2_1, test_point2_2):
    assert test_point2_1 in box2_1
    assert test_point2_2 in box2_1


def test_box_does_not_contain_point(box2_2, test_point2_2):
    assert test_point2_2 not in box2_2


def test_box_includes_point(box2_3, test_point2_3):
    box2_3.include(test_point2_3)
    assert box2_3.min == Point2(0.0, 0.0) and box2_3.max == Point2(1.0, 1.0)


def test_box_contains_box(box2_1, box2_3):
    assert box2_3 in box2_1
    assert box2_3 in box2_1


def test_box_does_not_contain_box(box2_1, box2_3):
    assert box2_1 not in box2_3
    assert box2_1 not in box2_3


def test_box_includes_box(box2_1, box2_3):
    box2_3.include(box2_1)
    assert box2_3.min == Point2(0.0, 0.0) and box2_3.max == Point2(2.0, 2.0)


def test_box_intersects_box(box2_1, box2_2, box2_3):
    assert box2_1.intersects(box2_2)
    assert box2_1.intersects(box2_3)


def test_box_size(box2_1):
    assert box2_1.size() == Vector2(2.0, 2.0)


def test_box_offset(box2_1, test_vector2_1):
    assert box2_1.offset(test_vector2_1) == AxisAlignedBox2(Point2(1.0, 1.0), Point2(3.0, 3.0))


def test_box_centre(box2_1):
    assert box2_1.centre() == Vector2(1.0, 1.0)


def test_box_equals_box(box2_1, box2_2, box2_4):
    assert box2_1 == box2_1
    assert box2_2 == box2_4


def test_box_not_equals_box(box2_1, box2_2):
    assert box2_1 != box2_2


def test_box_is_empty(box2_4):
    assert box2_4.empty()
