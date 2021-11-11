from three_d.axis_aligned_box3 import AxisAlignedBox3
from three_d.point3 import Point3


def test_path_continuity(path3_1, path3_2, path3_3):
    assert path3_1.is_continuous()
    assert path3_2.is_continuous()
    assert not path3_3.is_continuous()


def test_path_closed(path3_1):
    assert path3_1.is_closed()


def test_get_path_bounds(path3_1):
    assert path3_1.get_path_bounds() == AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))
