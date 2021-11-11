from three_d.axis_aligned_box3 import AxisAlignedBox3
from three_d.point3 import Point3
from three_d.vector3 import Vector3


def test_box_contains_point(box3_1, test_point3_1, test_point3_2):
    assert test_point3_1 in box3_1
    assert test_point3_2 in box3_1


def test_box_does_not_contain_point(box3_2, test_point3_2):
    assert test_point3_2 not in box3_2


def test_box_includes_point(box3_3, test_point3_3):
    box3_3.include(test_point3_3)
    assert box3_3.min == Point3(0.0, 0.0, 0.0) and box3_3.max == Point3(1.0, 1.0, 1.0)


def test_box_contains_box(box3_1, box3_3):
    assert box3_3 in box3_1
    assert box3_3 in box3_1


def test_box_does_not_contain_box(box3_1, box3_3):
    assert box3_1 not in box3_3
    assert box3_1 not in box3_3


def test_box_includes_box(box3_1, box3_3):
    box3_3.include(box3_1)
    assert box3_3.min == Point3(0.0, 0.0, 0.0) and box3_3.max == Point3(2.0, 2.0, 2.0)


def test_box_intersects_box(box3_1, box3_2, box3_3):
    assert box3_1.intersects(box3_2)
    assert box3_1.intersects(box3_3)


def test_box_size(box3_1):
    assert box3_1.size() == Vector3(2.0, 2.0, 2.0)


def test_box_offset(box3_1, test_vector3_1):
    assert box3_1.offset(test_vector3_1) == AxisAlignedBox3(Point3(1.0, 1.0, 1.0), Point3(3.0, 3.0, 3.0))


def test_box_centre(box3_1):
    assert box3_1.centre() == Vector3(1.0, 1.0, 1.0)


def test_box_equals_box(box3_1, box3_2, box3_4):
    assert box3_1 == box3_1
    assert box3_2 == box3_4


def test_box_not_equals_box(box3_1, box3_2):
    assert box3_1 != box3_2


def test_box_is_empty(box3_4):
    assert box3_4.empty()
