import pytest

from maths_utility import floats_are_close
from two_d.intersection import Intersection
from two_d.point2 import Point2


def test_intersection_with_edge2(intersection1, test_vector3_1):
    with pytest.raises(TypeError):
        return intersection1.intersect_lines(test_vector3_1)


def test_intersection_on_collinear_lines(intersection1):
    intersection1.intersect_lines(Point2(0.0, 0.0), Point2(1.0, 1.0), Point2(2.0, 2.0), Point2(4.0, 4.0))
    assert intersection1.point == Point2(0.0, 0.0)
    assert intersection1.vectors_intersect
    assert not intersection1.on_first_segment
    assert not intersection1.on_second_segment
    assert not intersection1.end_of_line


def test_intersection_on_non_collinear_lines(intersection1):
    intersection1.intersect_lines(Point2(1.0, 3.0), Point2(5.0, 7.0), Point2(9.0, 9.0), Point2(1.0, 3.0))
    assert floats_are_close(intersection1.point.x, 1.0) and floats_are_close(intersection1.point.y, 3.0)
    assert intersection1.vectors_intersect
    assert intersection1.on_first_segment
    assert intersection1.on_second_segment
    assert intersection1.end_of_line
