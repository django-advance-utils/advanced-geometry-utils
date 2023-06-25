import pytest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.path3 import Path3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3


def test_path3_inequality(path3_1, path3_2):
    assert not path3_1 == path3_2


def test_path3_inequality_with_float_argument(path3_1):
    with pytest.raises(TypeError):
        return path3_1 == 9.0


def test_path3_equality_with_unequal_path_lengths(path3_1, path3_5):
    with pytest.raises(IndexError):
        return path3_1 == path3_5


def test_path3_continuity(path3_1, path3_2, path3_3, path3_6):
    assert path3_1.is_continuous
    assert path3_2.is_continuous
    assert not path3_3.is_continuous
    assert not path3_6.is_continuous


def test_path3_closed(path3_1):
    assert path3_1.is_closed


def test_get_path3_bounds(path3_1):
    assert path3_1.get_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))


def test_path3_path3_addition(path3_1):
    assert path3_1 + Path3() == path3_1


def test_path3_set_edges(path3_1):
    path = Path3()
    path.set_edges([Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                    Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                    Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))])
    assert path == path3_1


def test_path3_set_edges_with_float_argument():
    with pytest.raises(TypeError):
        return Path3().set_edges([9.0])


def test_path3_get_first_edge(path3_1):
    assert path3_1.get_first_edge() == Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0))


def test_path3_get_first_edge_with_empty_list():
    with pytest.raises(IndexError):
        return Path3().get_first_edge()


def test_path3_get_last_edge(path3_1):
    assert path3_1.get_last_edge() == Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))


def test_path3_get_last_edge_with_empty_list():
    with pytest.raises(IndexError):
        return Path3().get_last_edge()


def test_path3_get_path_bounds(path3_1, path3_8):
    assert path3_1.get_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))
    assert path3_8.get_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.5, 0.0))


def test_path3_remove_duplicate_edges(path3_4):
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    path.remove_duplicate_edges()
    assert path == path3_4


def test_path3_to_tuple_list(path3_1):
    assert path3_1.to_tuple_list() == [((0.0, 0.0, 0.0), (1.0, 1.0, 1.0)),
                                       ((1.0, 1.0, 1.0), (2.0, 2.0, 2.0)),
                                       ((2.0, 2.0, 2.0), (0.0, 0.0, 0.0))]


def test_path3_reverse():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0))]
    path.reverse()

    reversed_path = Path3()
    reversed_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0)),
                                   Edge3(Point3(2.0, 2.0, 2.0), Point3(1.0, 1.0, 1.0)),
                                   Edge3(Point3(1.0, 1.0, 1.0), Point3(0.0, 0.0, 0.0))]
    assert path == reversed_path


def test_path3_mirror_x():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    path.mirror_x()

    mirrored_path = Path3()
    mirrored_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, -1.0, -1.0)),
                                   Edge3(Point3(1.0, -1.0, -1.0), Point3(2.0, -2.0, -2.0)),
                                   Edge3(Point3(2.0, -2.0, -2.0), Point3(0.0, 0.0, 0.0))]


def test_path3_mirror_y():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    path.mirror_y()

    mirrored_path = Path3()
    mirrored_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(-1.0, 1.0, -1.0)),
                                   Edge3(Point3(-1.0, 1.0, -1.0), Point3(-2.0, 2.0, -2.0)),
                                   Edge3(Point3(-2.0, 2.0, -2.0), Point3(0.0, 0.0, 0.0))]


def test_path3_mirror_z():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    path.mirror_z()

    mirrored_path = Path3()
    mirrored_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(-1.0, -1.0, 1.0)),
                                   Edge3(Point3(-1.0, -1.0, 1.0), Point3(-2.0, -2.0, 2.0)),
                                   Edge3(Point3(-2.0, -2.0, 2.0), Point3(0.0, 0.0, 0.0))]


def test_path3_mirror_origin():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    path.mirror_origin()

    mirrored_path = Path3()
    mirrored_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(-1.0, -1.0, -1.0)),
                                   Edge3(Point3(-1.0, -1.0, -1.0), Point3(-2.0, -2.0, -2.0)),
                                   Edge3(Point3(-2.0, -2.0, -2.0), Point3(0.0, 0.0, 0.0))]


def test_path3_offset():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    path.offset(Vector3(1.0, 1.0, 1.0))

    offset_path = Path3()
    offset_path.list_of_edges = [Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                                 Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                                 Edge3(Point3(3.0, 3.0, 3.0), Point3(1.0, 1.0, 1.0))]

    assert path == offset_path


# def test_path3_offset_ppp():
#     path = Path3()
#     path.list_of_edges = [Edge3(Point3(0.0, 0.0, 1.0), Point3(1.0, 0.0, 1.0)),
#                           Edge3(Point3(1.0, 0.0, 1.0), Point3(1.0, 1.0, 1.0)),
#                           Edge3(Point3(1.0, 1.0, 1.0), Point3(0.0, 1.0, 1.0)),
#                           Edge3(Point3(0.0, 1.0, 1.0), Point3(0.0, 0.0, 1.0))]
#     path.offset(Vector3(1.0, 1.0, 1.0))
#
#     offset_path = Path2()
#     offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 1.0)),
#                                  Edge2(Point2(2.0, 1.0), Point2(2.0, 2.0)),
#                                  Edge2(Point2(2.0, 2.0), Point2(1.0, 2.0)),
#                                  Edge2(Point2(1.0, 2.0), Point2(1.0, 1.0))]
#
#     assert path == offset_path
#
#
# def test_path2_offset_mm():
#     path = Path2()
#     path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
#                           Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
#                           Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
#                           Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
#     path.offset(Vector2(1.0, 1.0), 'mm')
#
#     offset_path = Path2()
#     offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
#                                  Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0)),
#                                  Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
#                                  Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0))]
#
#     assert path == offset_path
#
#
# def test_path2_offset_pm():
#     path = Path2()
#     path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
#                           Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
#                           Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
#                           Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
#
#     path.offset(Vector2(1.0, 1.0), 'pm')
#
#     offset_path = Path2()
#     offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
#                                  Edge2(Point2(0.0, 1.0), Point2(0.0, 2.0)),
#                                  Edge2(Point2(0.0, 2.0), Point2(1.0, 2.0)),
#                                  Edge2(Point2(1.0, 2.0), Point2(1.0, 1.0))]
#
#     assert path == offset_path
#
#
# def test_path2_offset_mp():
#     path = Path2()
#     path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 0.0)),
#                           Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0)),
#                           Edge2(Point2(1.0, 1.0), Point2(0.0, 1.0)),
#                           Edge2(Point2(0.0, 1.0), Point2(0.0, 0.0))]
#
#     path.offset(Vector2(1.0, 1.0), 'mp')
#
#     offset_path = Path2()
#     offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 1.0)),
#                                  Edge2(Point2(2.0, 1.0), Point2(2.0, 0.0)),
#                                  Edge2(Point2(2.0, 0.0), Point2(1.0, 0.0)),
#                                  Edge2(Point2(1.0, 0.0), Point2(1.0, 1.0))]
#
#     assert path == offset_path


def test_path2_offset_with_float_argument(path2_1):
    with pytest.raises(TypeError):
        return path2_1.offset(9.0)




def test_path3_offset_with_float_argument(path3_1):
    with pytest.raises(TypeError):
        return path3_1.offset(9.0)


def test_path3_rotate_around():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    path.rotate_around(Vector3(0.0, 0.0, 0.0), 90.0)

    rotated_path = Path3()
    rotated_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(-1.0, 1.0, 1.0)),
                                  Edge3(Point3(-1.0, 1.0, 1.0), Point3(-2.0, 2.0, 2.0)),
                                  Edge3(Point3(-2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]


def test_path3_close_path():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0))]
    path.close_path()

    closed_path = Path3()
    closed_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                                 Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                                 Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                                 Edge3(Point3(3.0, 3.0, 3.0), Point3(0.0, 0.0, 0.0))]


def test_path3_make_continuous():
    # TODO: rewrite test
    assert True


def test_path3_is_circle(path3_6):
    assert path3_6.is_circle()


def test_path3_is_rectangular(path3_1, path3_6, path3_7):
    assert path3_7.is_rectangular()
    assert not path3_1.is_rectangular()
    assert not path3_6.is_rectangular()


def test_path3_is_quadrilateral_with_curved_top(path3_8):
    assert not path3_8.is_quadrilateral()


def test_path3_convert_circle_to_edges():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(1.0, 1.0, 0.0), Point3(1.0, 1.0, 0.0), via=Point3(0.0, 1.0, 0.0))]
    path.convert_circle_to_edges()

    circle = Path3()
    circle.list_of_edges = [Edge3(Point3(1.0, 2.0, 0.0), Point3(1.0, 0.0, 0.0), via=Point3(2.0, 1.0, 0.0)),
                            Edge3(Point3(1.0, 0.0, 0.0), Point3(1.0, 2.0, 0.0), via=Point3(0.0, 1.0, 0.0))]

    assert path == circle


def test_path2_transform(test_matrix4_3):
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 0.0, 0.0)),
                          Edge3(Point3(1.0, 0.0, 0.0), Point3(1.0, 1.0, 0.0)),
                          Edge3(Point3(1.0, 1.0, 0.0), Point3(0.0, 1.0, 0.0), via=Point3(0.5, 1.5, 0.0)),
                          Edge3(Point3(0.0, 1.0, 0.0), Point3(0.0, 0.0, 0.0))]

    path.transform(test_matrix4_3)

    transformed_path = Path3()
    transformed_path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(-1.0, 0.0, 0.0)),
                                      Edge3(Point3(-1.0, 0.0, 0.0), Point3(-1.0, -1.0, 0.0)),
                                      Edge3(Point3(-1.0, -1.0, 0.0), Point3(0.0, -1.0, 0.0), via=Point3(-0.5, -1.5, 0.0)),
                                      Edge3(Point3(0.0, -1.0, 0.0), Point3(0.0, 0.0, 0.0))]

    assert path == transformed_path
