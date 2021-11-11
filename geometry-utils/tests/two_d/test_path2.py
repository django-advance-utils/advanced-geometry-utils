from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.point2 import Point2


def test_path_continuity(path2_1, path2_2, path2_3):
    assert path2_1.is_continuous()
    assert path2_2.is_continuous()
    assert not path2_3.is_continuous()


def test_path_closed(path2_1):
    assert path2_1.is_closed()


def test_get_path_bounds(path2_1):
    assert path2_1.get_path_bounds() == AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))
