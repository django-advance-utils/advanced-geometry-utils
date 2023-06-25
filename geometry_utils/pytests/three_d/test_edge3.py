import pytest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.maths_utility import floats_are_close

from math import sqrt


def test_edge2_string_point_arguments():
    with pytest.raises(TypeError):
        return Edge3("Point3(0.0, 0.0)", "Point3(0.0, 0.0)", "Point3(0.0, 0.0")


def test_edge2_string_radius_argument():
    with pytest.raises(TypeError):
        return Edge3(Point3(0.0, 0.0), Point3(0.0, 0.0), Point3(0.0, 0.0), "0.0")


def test_edge3_print_string(test_edge3_1):
    assert (test_edge3_1.__str__() ==
            "Edge3(p1:Point3(x:0.00, y:0.00, z:0.00), p2:Point3(x:0.00, y:0.00, z:0.00), "
            "via:None, centre:None)")


def test_edge2_to_edge2_equality(test_edge3_1):
    assert test_edge3_1 == Edge3()


def test_edge2_to_float_equality(test_edge3_1):
    with pytest.raises(TypeError):
        assert test_edge3_1 == 9.0


def test_edge3_point_parametric(test_edge3_1, test_edge3_2, test_edge3_3):
    assert test_edge3_2.point_parametric(0.0) == test_edge3_2.p1
    assert test_edge3_2.point_parametric(1.0) == test_edge3_2.p2
    assert test_edge3_1.point_parametric(0.5) == test_edge3_1.p1
    assert test_edge3_3.point_parametric(0.5) == Point3(1.0, 1.0, 0.0)


def test_edge3_point_parametric_with_point_argument(test_edge3_1, test_point3_1):
    with pytest.raises(TypeError):
        return test_edge3_1.point_parametric(test_point3_1)


def test_edge3_parametric_point(test_edge3_2, test_edge3_4):
    assert test_edge3_2.parametric_point(test_edge3_2.p1) == 0.0
    assert floats_are_close(test_edge3_2.parametric_point(test_edge3_2.p2), 1.0)
    assert test_edge3_4.parametric_point(Point3(1.0, 0.0, 0.0)) == 0.5


def test_edge3_parametric_point_with_float_argument(test_edge3_2):
    with pytest.raises(TypeError):
        return test_edge3_2.parametric_point(9.0)


def test_edge3_is_line(test_edge3_2):
    assert test_edge3_2.is_line()


def test_edge3_get_line_tangent(test_edge3_2):
    assert test_edge3_2.get_line_tangent() == Vector3(2.0 / sqrt(12.0), 2.0 / sqrt(12.0), 2.0 / sqrt(12.0))


def test_edge3_arc_get_line_tangent(test_edge3_3):
    with pytest.raises(TypeError):
        return test_edge3_3.get_line_tangent()


def test_edge3_get_arc_tangent(test_edge3_3):
    arc_tangent = test_edge3_3.get_arc_tangent(Point3(1.0, 1.0, 0.0))
    assert arc_tangent == Vector3(1.0, 0.0, 0.0)
    assert Edge3(Point3(0.0, 0.0, 0.0), Point3(2.0, 0.0, 0.0), via=Point3(1.0, -1.0, 0.0)).get_arc_tangent(Point3(1.0, -1.0, 0.0)) == Vector3(1.0, 0.0, 0.0)

    assert Edge3(Point3(2.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0), via=Point3(1.0, -1.0, 0.0)).get_arc_tangent(Point3(1.0, -1.0, 0.0)) == Vector3(-1.0, 0.0, 0.0)


def test_edge3_line_get_arc_tangent(test_edge3_2):
    with pytest.raises(TypeError):
        test_edge3_2.get_arc_tangent(Point3(0.0, 0.0, 0.0))


def test_edge3_get_arc_tangent_with_float_argument(test_edge3_3):
    with pytest.raises(TypeError):
        test_edge3_3.get_arc_tangent(9.0)


def test_edge3_calculate_centre(test_edge3_2, test_edge3_3, test_edge3_4):
    assert test_edge3_2.calculate_centre() == Point3(1.0, 1.0, 1.0)
    assert test_edge3_3.calculate_centre() == Point3(1.0, 0.0, 0.0)
    assert test_edge3_4.calculate_centre() == Point3(0.0, 0.0, 0.0)


def test_edge3_get_arc_normal_return_type(test_edge3_3, test_point3_1):
    assert isinstance(test_edge3_3.get_arc_normal(test_point3_1), Vector3)


def test_edge3_get_arc_normal_arithmetic(test_edge3_3):
    assert test_edge3_3.get_arc_normal(Point3(2.0, 0.0, 0.0)) == Vector3(-1.0, 0.0, 0.0)
    assert test_edge3_3.get_arc_normal(Point3(1.0, 1.0, 0.0)) == Vector3(0.0, -1.0, 0.0)


def test_edge3_line_get_arc_normal_arithmetic(test_edge3_2):
    with pytest.raises(TypeError):
        return test_edge3_2.get_arc_normal(Point3(0.0, 0.0, 0.0))


def test_edge3_arc_normal_arithmetic_with_float_argument(test_edge3_3):
    with pytest.raises(TypeError):
        return test_edge3_3.get_arc_normal(9.0)


def test_edge3_get_plane_normal(test_edge3_2):
    assert test_edge3_2.get_plane_normal() == Vector3(0.0, 0.0, 0.0)


def test_edge3_get_edge_bounds(test_edge3_2):
    assert test_edge3_2.get_edge_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))


def test_edge3_get_arc_start_angle(test_edge3_3):
    #assert test_edge3_3.get_arc_start_angle() == 180.0
    # TODO: what is start angle for 3d edge?
    assert True

def test_edge3_get_arc_end_angle(test_edge3_3):
    #assert test_edge3_3.get_arc_end_angle() == 0.0
    # TODO: what is end angle for 3d edge?
    assert True

def test_edge3_reverse():
    e1 = Edge3(Point3(0.0, 0.0, 0.0), Point3(2.0, 0.0, 0.0), via=Point3(1.0, 1.0, 0.0))
    expected = Edge3(Point3(2.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0), via=Point3(1.0, 1.0, 0.0))
    rev = e1.reverse()
    assert rev == expected
    assert rev.centre == e1.centre
