import pytest

from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.path3 import Path3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.path2 import Path2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2


def test_path2_is_closed_with_empty_path():
    assert not Path2().is_closed


def test_path2_is_continuous_with_empty_path():
    assert not Path2().is_continuous


def test_path2_get_enclosed_area(path2_7):
    assert path2_7.get_enclosed_area() == 1.0


def test_path2_get_list_of_points(path2_1):
    assert path2_1.get_list_of_points() == [Point2(0.0, 0.0), Point2(1.0, 1.0), Point2(2.0, 2.0), Point2(0.0, 0.0)]


def test_path2_path2_equality(path2_1, path2_2, path2_4):
    assert path2_1 == path2_4
    assert not path2_1 == path2_2


def test_path2_float_equality(path2_1):
    with pytest.raises(TypeError):
        return path2_1 == 9.0


def test_path2_unequal_path_length(path2_1, path2_5):
    with pytest.raises(IndexError):
        return path2_1 == path2_5


def test_path2_path2_addition(path2_1):
    assert Path2() + path2_1 == path2_1


def test_path2_set_edges(path2_1):
    path = Path2()
    path.set_edges([Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                    Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                    Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))])
    assert path == path2_1


def test_path2_set_edges_with_float_argument():
    with pytest.raises(TypeError):
        return Path2().set_edges([9.0])


def test_path2_get_first_edge(path2_1):
    assert path2_1.get_first_edge() == Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0))


def test_path2_get_first_edge_with_empty_list():
    with pytest.raises(IndexError):
        return Path2().get_first_edge()


def test_path2_get_last_edge(path2_1):
    assert path2_1.get_last_edge() == Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))


def test_path2_get_last_edge_with_empty_list():
    with pytest.raises(IndexError):
        return Path2().get_last_edge()


def test_path2_path_length(path2_1):
    assert path2_1.path_length == 3


def test_path2_continuity(path2_1, path2_2, path2_3):
    assert path2_1.is_continuous
    assert path2_2.is_continuous
    assert not path2_3.is_continuous


def test_path2_is_rectangular(path2_1, path2_6, path2_7):
    assert path2_7.is_rectangular()
    assert not path2_1.is_rectangular()
    assert not path2_6.is_rectangular()


def test_path2_is_quadrilateral_with_curved_top(path2_8):
    assert not path2_8.is_quadrilateral()


def test_path2_closed(path2_1):
    assert path2_1.is_closed


def test_path2_get_path_bounds(path2_1, path2_8):
    assert path2_1.get_bounds() == AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))
    assert path2_8.get_bounds() == AxisAlignedBox2(Point2(0.0, 0.0), Point2(1.0, 1.5))


def test_path2_remove_duplicate_edges(path2_4):
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    path.remove_duplicate_edges()
    assert path == path2_4


def test_path2_reverse():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
    path.reverse()

    reversed_path = Path2()
    reversed_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(0.0, 1.0)),
                                   Edge2(Point2(0.0, 1.0), Point2(1.0, 1.0)),
                                   Edge2(Point2(1.0, 1.0), Point2(1.0, 0.0)),
                                   Edge2(Point2(1.0, 0.0), Point2(0.0, 0.0))]
    assert path == reversed_path


def test_path2_mirror_x():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
    path.mirror_x()

    mirrored_path = Path2()
    mirrored_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                                   Edge2(Point2(1.0, 0.0), Point2(1.0, -1.0)),
                                   Edge2(Point2(1.0, -1.0), Point2(0.0, -1.0)),
                                   Edge2(Point2(0.0, -1.0), Point2(0.0, 0.0))]


def test_path2_mirror_y():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
    path.mirror_y()

    mirrored_path = Path2()
    mirrored_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(-1.0, 0.0)),
                                   Edge2(Point2(-1.0, 0.0), Point2(-1.0, 1.0)),
                                   Edge2(Point2(-1.0, 1.0), Point2(0.0, 1.0)),
                                   Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]


def test_path2_mirror_origin():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
    path.mirror_origin()

    mirrored_path = Path2()
    mirrored_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(-1.0, 0.0)),
                                   Edge2(Point2(-1.0, 0.0), Point2(-1.0, -1.0)),
                                   Edge2(Point2(-1.0, -1.0), Point2(0.0, -1.0)),
                                   Edge2(Point2(0.0, -1.0), Point2(0.0, 0.0))]


def test_path2_offset_pp():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
    path.offset(Vector2(1.0, 1.0))

    offset_path = Path2()
    offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 1.0)),
                                 Edge2(Point2(2.0, 1.0), Point2(2.0, 2.0)),
                                 Edge2(Point2(2.0, 2.0), Point2(1.0, 2.0)),
                                 Edge2(Point2(1.0, 2.0), Point2(1.0, 1.0))]

    assert path == offset_path


def test_path2_offset_mm():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
    path.offset(Vector2(1.0, 1.0), 'mm')

    offset_path = Path2()
    offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                                 Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0)),
                                 Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                                 Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0))]

    assert path == offset_path


def test_path2_offset_pm():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]

    path.offset(Vector2(1.0, 1.0), 'pm')

    offset_path = Path2()
    offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                                 Edge2(Point2(0.0, 1.0), Point2(0.0, 2.0)),
                                 Edge2(Point2(0.0, 2.0), Point2(1.0, 2.0)),
                                 Edge2(Point2(1.0, 2.0), Point2(1.0, 1.0))]

    assert path == offset_path


def test_path2_offset_mp():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]

    path.offset(Vector2(1.0, 1.0), 'mp')

    offset_path = Path2()
    offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 1.0)),
                                 Edge2(Point2(2.0, 1.0), Point2(2.0, 0.0)),
                                 Edge2(Point2(2.0, 0.0), Point2(1.0, 0.0)),
                                 Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0))]

    assert path == offset_path


def test_path2_offset_with_float_argument(path2_1):
    with pytest.raises(TypeError):
        return path2_1.offset(9.0)


def test_path2_rotate_around():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
    path.rotate_around(Vector2(0.0, 0.0), 90.0)

    rotated_path = Path2()
    rotated_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(0.0, 1.0)),
                                  Edge2(Point2(0.0, 1.0), Point2(-1.0, 1.0)),
                                  Edge2(Point2(-1.0, 1.0), Point2(-1.0, 0.0)),
                                  Edge2(Point2(-1.0, 0.0), Point2(0.0, 0.0))]


def test_path2_close_path():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0))]
    path.close_path()

    closed_path = Path2()
    closed_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                                 Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                                 Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
                                 Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]


def test_path2_make_continuous():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(0.0, 0.0)),
                          Edge2(Point2(2.0, 0.0), Point2(0.0, 0.0), 1.0, True)]
    path.make_continuous()

    continuous_path = Path2()
    continuous_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(2.0, 0.0), 1.0, True),
                                     Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]


def test_path2_is_circle(path2_6):
    assert path2_6.is_circle()


def test_path2_complete_circle(path2_6):
    path = Path2()
    path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(0.0, 0.0), 1.0)]
    assert path.complete_circle() == path2_6


def test_path2_to_tuple_list(path2_1):
    assert path2_1.to_tuple_list() == [((0.0, 0.0), (1.0, 1.0)), ((1.0, 1.0), (2.0, 2.0)), ((2.0, 2.0), (0.0, 0.0))]


def test_path2_is_curved_top(path2_8):
    assert path2_8.is_curved_top()


def test_path2_is_curved_top_with_circle_path(path2_6):
    assert not path2_6.is_curved_top()


def test_path2_get_leftmost_point_index(path2_1):
    list_of_points = path2_1.get_list_of_points()
    assert path2_1.get_leftmost_point_index(list_of_points) == 0


def test_path2_flip_vertical_centre():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0), 0.5),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]

    path.flip_vertical_centre()

    vertical_centre_flipped_path = Path2()
    vertical_centre_flipped_path.list_of_edges = [Edge2(Point2(0.0, 1.0), Point2(1.0, 1.0)),
                                                  Edge2(Point2(1.0, 1.0), Point2(1.0, 0.0)),
                                                  Edge2(Point2(1.0, 0.0), Point2(0.0, 0.0), 0.5, True),
                                                  Edge2(Point2(0.0, 0.0), Point2(0.0, 1.0))]
    assert path == vertical_centre_flipped_path


def test_path2_flip_vertical():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0), 0.5),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]

    path.flip_vertical()

    vertical_flipped_path = Path2()
    vertical_flipped_path.list_of_edges = [Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0)),
                                           Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0), 0.5),
                                           Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                                           Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0))]
    assert path == vertical_flipped_path


def test_path2_flip_horizontal_centre():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0), 0.5),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]

    path.flip_horizontal_center()

    horizontal_centre_flipped_path = Path2()
    horizontal_centre_flipped_path.list_of_edges = [Edge2(Point2(1.0, 0.0), Point2(0.0, 0.0)),
                                                    Edge2(Point2(0.0, 0.0), Point2(0.0, 1.0)),
                                                    Edge2(Point2(0.0, 1.0), Point2(1.0, 1.0), 0.5, True),
                                                    Edge2(Point2(1.0, 1.0), Point2(1.0, 0.0))]
    assert path == horizontal_centre_flipped_path


def test_path2_to_path3(path2_1):
    path_3d = Path3()
    path_3d.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 0.0)),
                             Edge3(Point3(1.0, 1.0, 0.0), Point3(2.0, 2.0, 0.0)),
                             Edge3(Point3(2.0, 2.0, 0.0), Point3(0.0, 0.0, 0.0))]

    assert path2_1.to_path3() == path_3d


def test_path2_convert_circle_to_edges():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(1.0, 1.0), 1.0)]
    path.convert_circle_to_edges()

    circle = Path2()
    circle.list_of_edges = [Edge2(Point2(1.0, 2.0), Point2(1.0, 0.0), 1.0),
                            Edge2(Point2(1.0, 0.0), Point2(1.0, 2.0), 1.0),
                            Edge2(Point2(1.0, 2.0), Point2(1.0, 2.0))]


def test_path2_get_points_orientation(path2_7):
    points = path2_7.get_list_of_points()
    assert path2_7.get_points_orientation([0, 1, 3], points) == 'Counterclockwise'
    assert path2_7.get_points_orientation([0, 2, 1], points) == 'Clockwise'
    assert path2_7.get_points_orientation([0, 0, 3], points) == 'Collinear'


def test_path2_get_points_orientation_with_float_argument(path2_7):
    with pytest.raises(TypeError):
        return path2_7.get_points_orientation(9.0, 9.0)


def test_path2_transform(test_matrix3_3):
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                          Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0), 0.5),
                          Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]

    path.transform(test_matrix3_3)

    transformed_path = Path2()
    transformed_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(-1.0, 0.0)),
                                      Edge2(Point2(-1.0, 0.0), Point2(-1.0, -1.0)),
                                      Edge2(Point2(-1.0, -1.0), Point2(0.0, -1.0), 0.5, True),
                                      Edge2(Point2(0.0, -1.0), Point2(0.0, 0.0))]

    assert path == transformed_path


def test_path2_get_convex_hull():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(1.0, 0.0), Point2(0.0, 0.0)),
                          Edge2(Point2(0.0, 0.0), Point2(0.0, 1.0)),
                          Edge2(Point2(0.0, 1.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(1.0, 0.0))]

    convex_hull = Path2()
    convex_hull.list_of_edges = [Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0)),
                                 Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
                                 Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
                                 Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0))]

    assert path.get_convex_hull() == convex_hull


def test_path2_simplify():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(10.0, 0.0)),
                          Edge2(Point2(10.0, 0.0), Point2(20.0, 0.0)),
                          Edge2(Point2(20.0, 0.0), Point2(20.0, 15.0)),
                          Edge2(Point2(20.0, 15.0), Point2(20.0, 30.0))]

    path.simplify()

    simplified_edges = Path2()
    simplified_edges.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(20.0, 0.0)),
                                      Edge2(Point2(20.0, 0.0), Point2(20.0, 30.0))]

    assert path == simplified_edges
