import unittest

from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2

test_vector2_1 = Vector2(1.0, 1.0)
test_point2_1 = Point2(1.0, 1.0)
test_point2_2 = Point2(1.0, 0.0)
test_box2_1 = AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))
test_box2_2 = AxisAlignedBox2()
test_box2_3 = AxisAlignedBox2(Point2(0.0, 0.0), Point2(0.0, 0.0))
test_box2_4 = AxisAlignedBox2(Point2(0.0, 0.0), Point2(0.0, 0.0))


class TestAxisAlignedBox2(unittest.TestCase):
    def test_box2_string_parameter(self):
        with self.assertRaises(TypeError):
            return AxisAlignedBox2(("0", "0"), ("0", "0"))

    def test_box2_box2_addition_return_arithmetic(self):
        with self.assertRaises(TypeError):
            return test_box2_1 + test_box2_2

    def test_box2_vector2_addition_return_type(self):
        self.assertIsInstance(test_box2_1 + test_vector2_1, AxisAlignedBox2)

    def test_box2_vector2_addition_arithmetic(self):
        self.assertEqual(test_box2_1 + test_vector2_1, AxisAlignedBox2(Point2(1.0, 1.0), Point2(3.0, 3.0)))

    def test_box2_contains_point2(self):
        self.assert_(test_point2_1 in test_box2_1)
        self.assert_(test_point2_2 in test_box2_1)

    def test_box2_contains_float(self):
        with self.assertRaises(TypeError):
            self.assert_(1.0 in test_box2_1)

    def test_box2_does_not_contain_point2(self):
        self.assert_(test_point2_2 not in test_box2_2)

    def test_box2_includes_point2(self):
        test_box2_3.include(test_point2_1)
        self.assertEqual(test_box2_3.min, Point2(0.0, 0.0)) and self.assertEqual(test_box2_3.max, Point2(1.0, 1.0))

    def test_box2_includes_float(self):
        with self.assertRaises(TypeError):
            test_box2_3.include(9.0)

    def test_box2_contains_box2(self):
        self.assert_(test_box2_3 in test_box2_1)
        self.assert_(test_box2_3 in test_box2_1)

    def test_box2_does_not_contain_box2(self):
        self.assert_(test_box2_1 not in test_box2_3)
        self.assert_(test_box2_1 not in test_box2_3)

    def test_box2_includes_box2(self):
        test_box2_3.include(test_box2_1)
        self.assert_(test_box2_3.min, Point2(0.0, 0.0)) and self.assertEqual(test_box2_3.max, Point2(2.0, 2.0))

    def test_box2_intersects_box2(self):
        self.assert_(test_box2_1.intersects(test_box2_2))
        self.assert_(test_box2_1.intersects(test_box2_3))

    def test_box2_intersects_float(self):
        with self.assertRaises(TypeError):
            self.assert_(test_box2_1.intersects(9.0))

    def test_box2_size(self):
        self.assert_(test_box2_1.size(), Vector2(2.0, 2.0))

    def test_box2_offset_by_vector2(self):
        self.assert_(test_box2_1.offset(test_vector2_1), AxisAlignedBox2(Point2(1.0, 1.0), Point2(3.0, 3.0)))

    def test_box2_offset_by_float(self):
        with self.assertRaises(TypeError):
            self.assert_(test_box2_1.offset(9.0))

    def test_box2_centre(self):
        self.assert_(test_box2_1.centre(), Point2(1.0, 1.0))

    def test_box2_equals_box2(self):
        self.assertEqual(test_box2_1, test_box2_1)
        self.assertEqual(test_box2_2, test_box2_4)

    def test_box2_equals_float(self):
        with self.assertRaises(TypeError):
            self.assertEqual(test_box2_1, 9.0)

    def test_box2_not_equals_box2(self):
        self.assertNotEqual(test_box2_1, test_box2_2)

    def test_box2_not_equals_float(self):
        with self.assertRaises(TypeError):
            self.assertNotEqual(test_box2_1, 9.0)

    def test_box2_is_empty(self):
        self.assert_(test_box2_4.empty())


if __name__ == '__main__':
    unittest.main()
