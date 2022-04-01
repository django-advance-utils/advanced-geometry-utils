import pytest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.maths_utility import floats_are_close

from math import sqrt


def test_edge2_string_point_arguments():
    with pytest.raises(TypeError):
        return Edge3("Point3(0.0, 0.0)", "Point3(0.0, 0.0)")


def test_edge2_string_radius_argument():
    with pytest.raises(TypeError):
        return Edge3(Point3(0.0, 0.0), Point3(0.0, 0.0), "0.0")


def test_edge3_print_string(test_edge3_1):
    assert (test_edge3_1.__str__() ==
            "Edge3(p1:Point3(x:0.00, y:0.00, z:0.00), p2:Point3(x:0.00, y:0.00, z:0.00), "
            "via:Point3(x:0.00, y:0.00, z:0.00), centre:Point3(x:0.00, y:0.00, z:0.00), "
            "radius:0.0, clockwise:False, large:False)")


def test_edge2_to_edge2_equality(test_edge3_1):
    assert test_edge3_1 == Edge3()


def test_edge2_to_float_equality(test_edge3_1):
    with pytest.raises(TypeError):
        assert test_edge3_1 == 9.0


def test_edge3_point_parametric(test_edge3_1, test_edge3_2):
    assert test_edge3_2.point_parametric(0.0) == test_edge3_2.p1
    assert test_edge3_2.point_parametric(1.0) == test_edge3_2.p2
    assert test_edge3_1.point_parametric(0.5) == test_edge3_1.p1  # p1 = p2


def test_edge3_parametric_point(test_edge3_2, test_edge3_4):
    assert test_edge3_2.parametric_point(test_edge3_2.p1) == 0.0
    assert floats_are_close(test_edge3_2.parametric_point(test_edge3_2.p2), 1.0)
    assert test_edge3_4.parametric_point(Point3(1.0, 0.0, 0.0)) == 0.5


def test_edge3_parametric_point_with_float_argument(test_edge3_2):
    with pytest.raises(TypeError):
        return test_edge3_2.parametric_point(9.0)


def test_edge3_is_line(test_edge3_2):
    assert test_edge3_2.is_line()


def test_edge2_is_clockwise_arc(test_edge3_3):
    assert test_edge3_3.is_clockwise_arc()


def test_edge3_get_line_tangent(test_edge3_2):
    assert test_edge3_2.get_line_tangent() == Vector3(2.0 / sqrt(12.0), 2.0 / sqrt(12.0), 2.0 / sqrt(12.0))


def test_edge3_arc_get_line_tangent(test_edge3_3):
    with pytest.raises(TypeError):
        return test_edge3_3.get_line_tangent()


def test_edge3_calculate_centre(test_edge3_2, test_edge3_3, test_edge3_4):
    assert test_edge3_2.calculate_centre() == Point3(1.0, 1.0, 1.0)
    assert test_edge3_3.calculate_centre() == Point3(1.0, 0.0, 0.0)
    assert test_edge3_4.calculate_centre() == Point3(0.0, 0.0, 0.0)


def test_edge3_get_arc_normal_return_type(test_edge3_3, test_point3_1):
    assert isinstance(test_edge3_3.get_arc_normal(test_point3_1), Vector3)


def test_edge3_get_arc_normal_arithmetic(test_edge3_3):
    assert test_edge3_3.get_arc_normal(Point3(1.0, 0.0, 0.0)) == Vector3(-1.0, 0.0, 0.0)
    assert test_edge3_3.get_arc_normal(Point3(0.0, 1.0, 0.0)) == Vector3(0.0, -1.0, 0.0)


def test_edge3_line_get_arc_normal_arithmetic(test_edge3_3):
    with pytest.raises(TypeError):
        return test_edge3_3.get_arc_normal(Point3(0.0, 0.0, 0.0))


def test_edge3_arc_normal_arithmetic_with_float_argument(test_edge3_3):
    with pytest.raises(TypeError):
        return test_edge3_3.get_arc_normal(9.0)


def test_edge3_get_edge_bounds(test_edge3_2):
    assert test_edge3_2.get_edge_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))
