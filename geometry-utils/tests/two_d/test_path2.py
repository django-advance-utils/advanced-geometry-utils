import pytest

from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.edge2 import Edge2
from two_d.path2 import Path2
from two_d.point2 import Point2


@pytest.fixture()
def path1():
    return Path2([Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                  Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                  Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))])


@pytest.fixture()
def path2():
    return Path2([Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                  Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                  Edge2(Point2(3.0, 3.0), Point2(4.0, 4.0))])


@pytest.fixture()
def path3():
    return Path2([Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                  Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                  Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))])


def test_path_continuity(path1, path2, path3):
    assert path1.is_continuous()
    assert path2.is_continuous()
    assert not path3.is_continuous()


def test_path_closed(path1):
    assert path1.is_closed()


def test_get_path_bounds(path1):
    assert path1.get_path_bounds() == AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))
