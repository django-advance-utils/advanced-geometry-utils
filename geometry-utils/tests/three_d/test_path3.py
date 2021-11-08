import pytest

from three_d.axis_aligned_box3 import AxisAlignedBox3
from three_d.edge3 import Edge3
from three_d.path3 import Path3
from three_d.point3 import Point3


@pytest.fixture()
def path1():
    return Path3([Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                  Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                  Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))])


@pytest.fixture()
def path2():
    return Path3([Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                  Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                  Edge3(Point3(3.0, 3.0, 3.0), Point3(4.0, 4.0, 4.0))])


@pytest.fixture()
def path3():
    return Path3([Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                  Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                  Edge3(Point3(4.0, 4.0, 4.0), Point3(5.0, 5.0, 5.0))])


def test_path_continuity(path1, path2, path3):
    assert path1.is_continuous()
    assert path2.is_continuous()
    assert not path3.is_continuous()


def test_path_closed(path1):
    assert path1.is_closed()


def test_get_path_bounds(path1):
    assert path1.get_path_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))
