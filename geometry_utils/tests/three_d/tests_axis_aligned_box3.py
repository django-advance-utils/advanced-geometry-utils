import unittest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.three_d.point3 import Point3


test_box3_1 = AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))
test_box3_2 = AxisAlignedBox3()
test_box3_3 = AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))
test_box3_4 = AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))
test_box3_5 = AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))

test_vector = Vector3(1.0, 1.0, 1.0)
test_point3_1 = Point3(1.0, 1.0, 1.0)
test_point3_2 = Point3(1.0, 0.0, 0.0)


class TestAxisAlignedBox3(unittest.TestCase):
    def test_box3_box3_addition(self):
        with self.assertRaises(TypeError):
            return test_box3_1 + test_box3_2

    def test_box3_vector3_addition_return_type(self):
        self.assertIsInstance(test_box3_1 + test_vector, AxisAlignedBox3)

    def test_box3_vector3_addition_arithmetic(self):
        self.assertEqual(test_box3_1 + test_vector, AxisAlignedBox3(Point3(1.0, 1.0, 1.0), Point3(3.0, 3.0, 3.0)))

    def test_box3_contains_point3(self):
        self.assert_(test_point3_1 in test_box3_1)
        self.assert_(test_point3_2 in test_box3_1)

    def test_box3_does_not_contain_point3(self):
        self.assert_(test_point3_2 not in test_box3_2)

    def test_box3_includes_point3(self):
        test_box3_5.include(test_point3_1)
        self.assertEqual(test_box3_5.min, Point3(0.0, 0.0, 0.0))
        self.assertEqual(test_box3_5.max, Point3(1.0, 1.0, 1.0))

    def test_box3_contains_box3(self):
        self.assert_(test_box3_3 in test_box3_1)
        self.assert_(test_box3_3 in test_box3_1)

    def test_box3_does_not_contain_box3(self):
        self.assert_(test_box3_1 not in test_box3_3)
        self.assert_(test_box3_1 not in test_box3_3)

    def test_box3_includes_box3(self):
        test_box3_3.include(test_box3_1)
        self.assertEqual(test_box3_3.min, Point3(0.0, 0.0, 0.0))
        self.assertEqual(test_box3_3.max, Point3(2.0, 2.0, 2.0))

    def test_box3_intersects_box3(self):
        self.assert_(test_box3_1.intersects(test_box3_2))
        self.assert_(test_box3_1.intersects(test_box3_3))

    def test_box3_size(self):
        self.assertEqual(test_box3_1.size(), Vector3(2.0, 2.0, 2.0))

    def test_box3_offset_by_vector3(self):
        self.assertEqual(test_box3_1.offset(test_vector), AxisAlignedBox3(Point3(1.0, 1.0, 1.0), Point3(3.0, 3.0, 3.0)))

    def test_box3_centre(self):
        self.assertEqual(test_box3_1.centre(), Point3(1.0, 1.0, 1.0))

    def test_box3_equals_box3(self):
        self.assertEqual(test_box3_1, test_box3_1)
        self.assertEqual(test_box3_2, test_box3_4)

    def test_box3_not_equals_box3(self):
        self.assertNotEqual(test_box3_1, test_box3_2)

    def test_box3_is_empty(self):
        self.assert_(test_box3_4.empty())


if __name__ == '__main__':
    unittest.main()
