import pytest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.path3 import Path3
from geometry_utils.three_d.point3 import Point3


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
    assert path3_8.get_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.5, 0.0), 0.5)


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
