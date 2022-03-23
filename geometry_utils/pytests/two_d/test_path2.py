import pytest

from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.path2 import Path2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2


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
    path = Path2()
    with pytest.raises(TypeError):
        return path.set_edges([9.0])


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


def test_path2_closed(path2_1):
    assert path2_1.is_closed


def test_path2_get_path_bounds(path2_1):
    assert path2_1.get_bounds() == AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))


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
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    path.reverse()

    reversed_path = Path2()
    reversed_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(2.0, 2.0)),
                                   Edge2(Point2(2.0, 2.0), Point2(1.0, 1.0)),
                                   Edge2(Point2(1.0, 1.0), Point2(0.0, 0.0))]
    assert path == reversed_path


def test_path2_mirror_x():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    path.mirror_x()

    mirrored_path = Path2()
    mirrored_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, -1.0)),
                                   Edge2(Point2(1.0, -1.0), Point2(2.0, -2.0)),
                                   Edge2(Point2(2.0, -2.0), Point2(0.0, -0.0))]


def test_path2_mirror_y():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    path.mirror_y()

    mirrored_path = Path2()
    mirrored_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(-1.0, 1.0)),
                                   Edge2(Point2(-1.0, 1.0), Point2(-2.0, 2.0)),
                                   Edge2(Point2(-2.0, 2.0), Point2(0.0, 0.0))]


def test_path2_mirror_origin():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    path.mirror_origin()

    mirrored_path = Path2()
    mirrored_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(-1.0, -1.0)),
                                   Edge2(Point2(-1.0, -1.0), Point2(-2.0, -2.0)),
                                   Edge2(Point2(-2.0, -2.0), Point2(0.0, 0.0))]


def test_path2_offset():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    path.offset(Vector2(1.0, 1.0))

    offset_path = Path2()
    offset_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                 Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                                 Edge2(Point2(3.0, 3.0), Point2(1.0, 1.0))]

    assert path == offset_path


def test_path2_offset_with_float_argument(path2_1):
    with pytest.raises(TypeError):
        return path2_1.offset(9.0)


def test_path2_rotate_around():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    path.rotate_around(Vector2(0.0, 0.0), 90.0)

    rotated_path = Path2()
    rotated_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(-1.0, 1.0)),
                                  Edge2(Point2(-1.0, 1.0), Point2(-2.0, 2.0)),
                                  Edge2(Point2(-2.0, 2.0), Point2(0.0, 0.0))]


def test_path2_close_path():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0))]
    path.close_path()

    closed_path = Path2()
    closed_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                                 Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                 Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                                 Edge2(Point2(3.0, 3.0), Point2(0.0, 0.0))]


def test_path2_make_continuous():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(0.0, 0.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0), 1.0, True)]
    path.make_continuous()

    continuous_path = Path2()
    continuous_path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(2.0, 2.0), 1.0, True),
                                     Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]

    del path
    del continuous_path


def test_path2_is_circle(path2_6):
    assert path2_6.is_circle()


def test_path2_complete_circle(path2_6):
    path = Path2()
    path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(0.0, 0.0), 1.0)]
    assert path.complete_circle() == path2_6


def test_path2_is_rectangular(path2_1, path2_6):
    assert not path2_1.is_rectangular()
    assert not path2_6.is_rectangular()


def test_path2_to_tuple_list(path2_1):
    assert path2_1.to_tuple_list() == [((0.0, 0.0), (1.0, 1.0)), ((1.0, 1.0), (2.0, 2.0)), ((2.0, 2.0), (0.0, 0.0))]
