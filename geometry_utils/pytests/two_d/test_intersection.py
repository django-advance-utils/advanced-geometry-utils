import pytest

from geometry_utils.maths_utility import floats_are_close
from geometry_utils.two_d.intersection import Intersection
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.edge2 import Edge2


def test_intersection_with_vector2(intersection1, test_vector2_1):
    with pytest.raises(TypeError):
        return intersection1.intersect(test_vector2_1, test_vector2_1)


def test_intersection_print_string(test_edge2_2, test_edge2_3):
    intersection = Intersection()
    intersection.intersect(test_edge2_2, test_edge2_3)
    assert intersection.__str__() == ("Intersection(point:Point2(x:0.00, y:0.00), Vectors Intersect:True, On First "
                                      "Segment:True, On Second Segment:True, Collinear:True")


def test_intersection_on_collinear_edge2_lines(test_edge2_2, test_edge2_3, test_point2_4):
    intersection = Intersection()
    intersection.intersect(test_edge2_2, test_edge2_3)
    assert intersection.point == test_point2_4
    assert intersection.vectors_intersect
    assert intersection.on_first_segment
    assert intersection.on_second_segment
    assert intersection.collinear
    assert not intersection.end_of_line


def test_intersection_on_non_collinear_edge2_lines(test_point2_2):
    vertical_edge = Edge2(Point2(1, 0), Point2(1, 5))
    horizontal_edge = Edge2(Point2(0, 0), Point2(5, 0))

    intersection = Intersection()
    intersection.intersect(vertical_edge, horizontal_edge)
    assert intersection.point == test_point2_2
    assert intersection.vectors_intersect
    assert intersection.on_first_segment
    assert intersection.on_second_segment
    assert not intersection.collinear
    assert intersection.end_of_line


def test_intersection_on_edge2_line_and_edge2_arc(test_edge2_2, test_edge2_5, test_point2_1):
    intersection = Intersection()
    intersection.intersect(test_edge2_2, test_edge2_5)
    assert intersection.point == test_point2_1
    assert intersection.vectors_intersect
    assert intersection.on_first_segment
    assert intersection.on_second_segment
    assert not intersection.collinear
    assert not intersection.end_of_line


def test_intersection_on_edge2_line_and_edge2_circle(test_edge2_2, test_edge2_6):
    intersection = Intersection()
    intersection.intersect(test_edge2_2, test_edge2_6)
    assert intersection.point == Point2(3.5355, 3.5355)
    assert intersection.vectors_intersect
    assert intersection.on_second_segment
    assert not intersection.on_first_segment
    assert not intersection.collinear
    assert not intersection.end_of_line


def test_intersection_on_collinear_edge3_lines(test_edge3_2, test_edge3_5, test_point3_4):
    intersection = Intersection()
    intersection.intersect(test_edge3_2, test_edge3_5)
    assert intersection.point == test_point3_4
    assert intersection.vectors_intersect
    assert intersection.on_first_segment
    assert intersection.on_second_segment
    assert intersection.collinear
    assert not intersection.end_of_line


def test_intersection_on_floats():
    intersection = Intersection()
    with pytest.raises(TypeError):
        return intersection.intersect(9.0, 9.0)
