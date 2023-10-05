import pytest
import math

from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.matrix3 import Matrix3
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.maths_utility import floats_are_close, QUARTER_PI, PI


def test_edge2_string_point_arguments():
    with pytest.raises(TypeError):
        return Edge2("Point2(0.0, 0.0)", "Point2(0.0, 0.0)")


def test_edge2_string_radius_argument():
    with pytest.raises(TypeError):
        return Edge2(Point2(0.0, 0.0), Point2(0.0, 0.0), "0.0")


def test_edge2_print_string(test_edge2_1):
    assert (test_edge2_1.__str__() == "Edge2(p1:Point2(x:0.00, y:0.00), p2:Point2(x:0.00, y:0.00), "
                                      "centre:Point2(x:0.00, y:0.00), radius:0.0, clockwise:False, "
                                      "large:False)")


def test_edge2_to_edge2_equality(test_edge2_1):
    assert test_edge2_1 == Edge2()


def test_edge2_to_float_equality(test_edge2_1):
    with pytest.raises(TypeError):
        assert test_edge2_1 == 9.0


def test_edge2_to_edge2_inequality(test_edge2_1, test_edge2_2):
    assert test_edge2_1 != test_edge2_2


def test_edge2_to_float_inequality(test_edge2_1):
    with pytest.raises(TypeError):
        return test_edge2_1 != 9.0


def test_edge2_is_arc(test_edge2_2, test_edge2_5):
    assert not test_edge2_2.is_arc()
    assert test_edge2_5.is_arc()


def test_edge2_get_sweep_angle_return_type(test_edge2_1):
    assert isinstance(test_edge2_1.get_sweep_angle(), float)


def test_edge2_get_sweep_angle_arithmetic(test_edge2_5):
    assert test_edge2_5.get_sweep_angle() == PI


def test_edge2_point_parametric_return_type(test_edge2_1):
    assert isinstance(test_edge2_1.point_parametric(0.0), Point2)


def test_edge2_line_point_parametric_arithmetic(test_edge2_1, test_edge2_2):
    assert test_edge2_2.point_parametric(0.0) == test_edge2_2.p1
    assert test_edge2_2.point_parametric(1.0) == test_edge2_2.p2
    assert test_edge2_1.point_parametric(0.5) == test_edge2_1.p1


def test_edge2_arc_point_parametric_arithmetic(test_edge2_5):
    assert test_edge2_5.point_parametric(0.00) == test_edge2_5.p1
    assert test_edge2_5.point_parametric(0.25) == Point2(0.2929, 0.7071)
    assert test_edge2_5.point_parametric(0.50) == Point2(1.00, 1.00)
    assert test_edge2_5.point_parametric(0.75) == Point2(1.7071, 0.7071)
    assert test_edge2_5.point_parametric(1.00) == test_edge2_5.p2


def test_edge2_point_parametric_with_point_argument(test_edge2_1, test_point2_1):
    with pytest.raises(TypeError):
        return test_edge2_1.point_parametric(test_point2_1)


def test_edge2_parametric_point_return_type(test_edge2_1):
    assert isinstance(test_edge2_1.parametric_point(test_edge2_1.p1), float)


def test_edge2_parametric_point_arcs_arithmetic(test_circle_points_1, test_edge2_7):
    # anticlockwise 10 deg
    e1 = Edge2(test_circle_points_1[10], test_circle_points_1[0], 600.0, False, False)

    # endpoints and centre point
    assert floats_are_close(e1.parametric_point(test_circle_points_1[355]), 1.5)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[0]), 1.0)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[5]), 0.5)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[10]), 0.0)
    assert floats_are_close(e1.parametric_point(test_circle_points_1[15]), -0.5)

    e2 = Edge2(test_circle_points_1[36], test_circle_points_1[202], 600.0, True, False)

    # endpoints and centre point
    assert floats_are_close(e2.parametric_point(test_circle_points_1[285]), 1.5)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[202]), 1.0)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[119]), 0.5)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[36]), 0.0)
    assert floats_are_close(e2.parametric_point(test_circle_points_1[313]), -0.5)

    # large arc
    e3 = Edge2(test_circle_points_1[40], test_circle_points_1[30], 600.0, True, True)

    assert floats_are_close(e3.parametric_point(test_circle_points_1[30]), 1.0)
    assert floats_are_close(e3.parametric_point(test_circle_points_1[215]), 0.5)
    assert floats_are_close(e3.parametric_point(test_circle_points_1[40]), 0.0)

    # clockwise semicircle (large)
    e4 = Edge2(test_circle_points_1[0], test_circle_points_1[180], 600.0, True, True)

    assert floats_are_close(e4.parametric_point(test_circle_points_1[180]), 1.0)
    assert floats_are_close(e4.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e4.parametric_point(test_circle_points_1[0]), 0.0)

    # clockwise semicircle (small) should be the same as the large version
    e5 = Edge2(test_circle_points_1[0], test_circle_points_1[180], 600.0, True, False)

    assert floats_are_close(e5.parametric_point(test_circle_points_1[180]), 1.0)
    assert floats_are_close(e5.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e5.parametric_point(test_circle_points_1[0]), 0.0)

    # anticlockwise semicircle (large)
    e6 = Edge2(test_circle_points_1[180], test_circle_points_1[0], 600.0, False, True)

    assert floats_are_close(e6.parametric_point(test_circle_points_1[0]), 1.0)
    assert floats_are_close(e6.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e6.parametric_point(test_circle_points_1[180]), 0.0)

    # anticlockwise semicircle (small) should be the same as the large version
    e7 = Edge2(test_circle_points_1[180], test_circle_points_1[0], 600.0, False, False)

    assert floats_are_close(e7.parametric_point(test_circle_points_1[0]), 1.0)
    assert floats_are_close(e7.parametric_point(test_circle_points_1[90]), 0.5)
    assert floats_are_close(e7.parametric_point(test_circle_points_1[180]), 0.0)

    # clockwise arc across three quadrants
    assert floats_are_close(test_edge2_7.parametric_point(Point2(0, 0)), 0.0)
    assert floats_are_close(test_edge2_7.parametric_point(Point2(1, 1)), 0.3333)
    assert floats_are_close(test_edge2_7.parametric_point(Point2(2, 0)), 0.6667)
    assert floats_are_close(test_edge2_7.parametric_point(Point2(1, -1)), 1.0)


def test_edge2_line_parametric_point(test_edge2_2):
    assert test_edge2_2.parametric_point(test_edge2_2.p1) == 0.0
    assert floats_are_close(test_edge2_2.parametric_point(test_edge2_2.p2), 1.0)


def test_edge2_circle_parametric_point(test_edge2_6):
    assert test_edge2_6.parametric_point(Point2(0.0, 0.0)) == 0.5


def test_edge2_parametric_point_with_float_argument(test_edge2_1):
    with pytest.raises(TypeError):
        return test_edge2_1.parametric_point(9.0)


def test_edge2_get_line_normal_return_type(test_edge2_2):
    assert isinstance(test_edge2_2.get_line_normal(), Vector2)


def test_edge2_get_line_normal_arithmetic(test_edge2_2):
    assert test_edge2_2.get_line_normal() == Vector2(-0.7071, 0.7071)


def test_edge2_arc_get_line_normal(test_edge2_5):
    with pytest.raises(TypeError):
        return test_edge2_5.get_line_normal()


def test_edge2_get_arc_normal_return_type(test_edge2_6, test_point2_1):
    assert isinstance(test_edge2_6.get_arc_normal(test_point2_1), Vector2)


def test_edge2_get_arc_normal_arithmetic(test_edge2_2, test_edge2_6):
    assert test_edge2_6.get_arc_normal(Point2(5.0, 0.0)) == Vector2(-1.0, 0.0)
    assert test_edge2_6.get_arc_normal(Point2(0.0, 5.0)) == Vector2(0.0, -1.0)


def test_edge2_line_get_arc_normal_arithmetic(test_edge2_2):
    with pytest.raises(TypeError):
        return test_edge2_2.get_arc_normal(Point2(0.0, 0.0))


def test_edge2_arc_normal_arithmetic_with_float_argument(test_edge2_2):
    with pytest.raises(TypeError):
        return test_edge2_2.get_arc_normal(9.0)


def test_edge2_get_line_tangent_return_type(test_edge2_4):
    assert isinstance(test_edge2_4.get_line_tangent(), Vector2)


def test_edge2_get_line_tangent_arithmetic(test_edge2_4):
    assert test_edge2_4.get_line_tangent() == Vector2(1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0))


def test_edge2_arc_get_line_tangent(test_edge2_5):
    with pytest.raises(TypeError):
        return test_edge2_5.get_line_tangent()


def test_edge2_get_arc_tangent_return_type(test_edge2_5):
    assert isinstance(test_edge2_5.get_arc_tangent(Point2(0, 1)), Vector2)


def test_edge2_get_arc_tangent_arithmetic(test_edge2_5, test_edge2_2):
    assert test_edge2_5.get_arc_tangent(Point2(0, 1)) == Vector2(1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0))
    assert Edge2(Point2(2, 0), Point2(0, 0), 1).get_arc_tangent(Point2(0, 1)) == Vector2(-1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0))


def test_edge2_line_get_arc_tangent(test_edge2_2, test_point2_3):
    with pytest.raises(TypeError):
        return test_edge2_2.get_arc_tangent(test_point2_3)


def test_edge2_get_arc_tangent_with_float_argument(test_edge2_5):
    with pytest.raises(TypeError):
        return test_edge2_5.get_arc_tangent(9.0)


def test_edge2_calculate_centre_return_type(test_edge2_1):
    assert isinstance(test_edge2_1.calculate_centre(), Point2)


def test_edge2_calculate_centre_arithmetic(test_edge2_2, test_edge2_5, test_edge2_6, test_point2_1):
    assert test_edge2_2.calculate_centre() == test_point2_1
    assert test_edge2_5.calculate_centre() == Point2(1.0, 0.0)
    assert test_edge2_6.calculate_centre() == test_edge2_6.p2


def test_edge2_get_edge_bounds_return_type(test_edge2_1):
    assert isinstance(test_edge2_1.get_edge_bounds(), AxisAlignedBox2)


def test_edge2_get_edge_bounds_arithmetic(test_edge2_2, test_box2_1):
    assert test_edge2_2.get_edge_bounds() == test_box2_1


def test_edge2_offset_edge_arithmetic(test_vector2_1):
    assert (Edge2(Point2(0.0, 0.0), Point2(0.0, 0.0)).offset(test_vector2_1) ==
            Edge2(Point2(1.0, 1.0), Point2(1.0, 1.0)))


def test_edge2_offset_edge_with_float(test_edge2_1):
    with pytest.raises(TypeError):
        return test_edge2_1.offset(9.0)


def test_edge2_reverse():
    assert (Edge2(Point2(1.0, 0.0), Point2(0.0, 1.0), 1.0, False).reverse() ==
            Edge2(Point2(0.0, 1.0), Point2(1.0, 0.0), 1.0, True))


def test_edge2_mirror_x():
    assert (Edge2(Point2(0, 1), Point2(2, 3), 1.0, False).mirror_x() ==
            Edge2(Point2(0, -1), Point2(2, -3), 1.0, True))


def test_edge2_mirror_y():
    assert (Edge2(Point2(1, 0), Point2(2, 3), 1.0, False).mirror_y() ==
            Edge2(Point2(-1, 0), Point2(-2, 3), 1.0, True))


def test_edge2_mirror_origin():
    assert (Edge2(Point2(1, 1), Point2(3, 1), 1.0, False).mirror_origin() ==
            Edge2(Point2(-1, -1), Point2(-3, -1), 1.0, True))


def test_edge2_is_circle(test_edge2_6):
    assert test_edge2_6.is_circle()


def test_edge2_get_arc_start_angle(test_edge2_5):
    assert test_edge2_5.get_arc_start_angle() == 180.0


def test_edge2_get_arc_end_angle(test_edge2_5):
    assert test_edge2_5.get_arc_end_angle() == 0.0


def test_edge2_flatten_arc(test_edge2_5):
    list_of_arc_edges = test_edge2_5.flatten_arc()
    for edge in list_of_arc_edges:
        assert not edge.is_arc()

    assert list_of_arc_edges[0].p1 == test_edge2_5.p1
    assert list_of_arc_edges[-1].p2 == test_edge2_5.p2


def test_edge2_rotate():
    assert Edge2(Point2(0, 0), Point2(1, 0)).rotate(90.0) == Edge2(Point2(0, 0), Point2(0, 1))


def test_edge2_rotate_with_string(test_edge2_5):
    with pytest.raises(TypeError):
        return test_edge2_5.rotate("0")


def test_edge2_parallel_to_edge(test_edge2_4):
    assert Edge2(Point2(1, 1), Point2(3, 3)).is_parallel_to(test_edge2_4)


def test_edge2_parallel_to_float(test_edge2_1):
    with pytest.raises(TypeError):
        test_edge2_1.is_parallel_to(9.0)


def test_edge2_perpendicular_to_edge():
    assert Edge2(Point2(-1.0, 0.0), Point2(1.0, 0.0)).is_perpendicular_to(Edge2(Point2(0.0, 0.0), Point2(0.0, 1.0)))


def test_edge2_perpendicular_to_float(test_edge2_1):
    with pytest.raises(TypeError):
        return test_edge2_1.is_perpendicular_to(9.0)


def test_edge2_get_slope(test_edge2_4):
    assert test_edge2_4.get_slope() == 1.0


def test_edge2_get_slope_vertical():
    assert Edge2(Point2(1, 1), Point2(1, 2)).get_slope() is None


def test_edge2_get_slope_arc(test_edge2_5):
    with pytest.raises(TypeError):
        return test_edge2_5.get_slope()


def test_edge2_edge_length(test_edge2_2, test_edge2_5):
    assert floats_are_close(test_edge2_2.edge_length(), 2.828427)
    assert test_edge2_5.edge_length() == PI


def test_edge2_angle_to_x_axis(test_edge2_2):
    assert test_edge2_2.angle_to_x_axis() == QUARTER_PI


def test_edge2_arc_angle_to_x_axis(test_edge2_5):
    with pytest.raises(TypeError):
        return test_edge2_5.angle_to_x_axis()


def test_edge2_angle_to_edge(test_edge2_2, test_edge2_4):
    assert test_edge2_2.angle_to_edge(test_edge2_4) == 0.0


def test_edge2_angle_to_edge_arc(test_edge2_4, test_edge2_5):
    with pytest.raises(TypeError):
        return test_edge2_5.angle_to_edge(test_edge2_4)


def test_edge2_angle_to_edge_arc_with_float_argument(test_edge2_1):
    with pytest.raises(TypeError):
        return test_edge2_1.angle_to_edge(9.0)


def test_edge2_minimum_x(test_edge2_3):
    assert test_edge2_3.minimum_x() == 2.0


def test_edge2_maximum_x(test_edge2_3):
    assert test_edge2_3.maximum_x() == 4.0


def test_edge2_minimum_y(test_edge2_4):
    assert test_edge2_4.minimum_y() == 0.0


def test_edge2_maximum_y(test_edge2_2):
    assert test_edge2_2.maximum_y() == 2.0


def test_edge2_vector_within_arc(test_edge2_6):
    assert test_edge2_6.vector_within_arc(Vector2(5.0, 0.0))


def test_edge2_line_vector_within_arc(test_edge2_2):
    with pytest.raises(TypeError):
        test_edge2_2.vector_within_arc(Vector2(0.0, 0.0))


def test_edge2_vector_within_arc_float_argument(test_edge2_5):
    with pytest.raises(TypeError):
        test_edge2_5.vector_within_arc(9.0)


def test_edge2_transform():
    edge_to_be_transformed = Edge2(Point2(0, 0), Point2(1, 0))
    transformation_matrix = Matrix3.translation(Vector2(0.0, -1.0))

    edge_to_be_transformed.transform(transformation_matrix)
    transformed_edge = Edge2(Point2(0.0, -1.0), Point2(1.0, -1.0))

    assert edge_to_be_transformed == transformed_edge


def test_edge2_calculate_arc_centre(test_edge2_2):
    assert test_edge2_2.calculate_centre() == Point2(1.0, 1.0)


def test_edge2_get_edge_bounds(test_edge2_2):
    assert test_edge2_2.get_edge_bounds() == AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))


def test_edge2_to_edge3(test_edge2_1):
    assert test_edge2_1.to_edge3() == Edge3()
