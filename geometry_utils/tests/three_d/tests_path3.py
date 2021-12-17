import unittest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.path3 import Path3
from geometry_utils.three_d.point3 import Point3

path3_1 = Path3([Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                 Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                 Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))])
path3_2 = Path3([Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                 Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                 Edge3(Point3(3.0, 3.0, 3.0), Point3(4.0, 4.0, 4.0))])

path3_3 = Path3([Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                 Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                 Edge3(Point3(4.0, 4.0, 4.0), Point3(5.0, 5.0, 5.0))])


class MyTestCase(unittest.TestCase):
    def test_path3_continuity(self):
        self.assert_(path3_1.is_continuous())
        self.assert_(path3_2.is_continuous())
        self.assert_(not path3_3.is_continuous())

    def test_path3_closed(self):
        self.assert_(path3_1.is_closed())

    def test_get_path3_bounds(self):
        self.assertEqual(path3_1.get_path_bounds(), AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0)))


if __name__ == '__main__':
    unittest.main()
