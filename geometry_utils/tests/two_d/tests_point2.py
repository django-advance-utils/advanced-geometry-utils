import unittest

from geometry_utils.two_d.vector2 import Vector2
from geometry_utils.two_d.point2 import Point2

test_vector2_1 = Vector2(1.0, 1.0)

test_point2_1 = Point2(1.0, 1.0)
test_point2_2 = Point2(1.0, 0.0)
test_point2_3 = Point2(1.0, 1.0)
test_point2_4 = Point2(0.0, 0.0)
test_point2_5 = Point2(0.0, 1.0)


class TestPoint2(unittest.TestCase):

    # Point2 Object Parameter Test
    def test_point2_string_parameter(self):
        with self.assertRaises(TypeError):
            return Point2("0", "0", "0")

    # Point2 Addition Tests
    def test_point2_point2_addition_return_type(self):
        with self.assertRaises(TypeError):
            return test_point2_1 + test_point2_2

    def test_point2_vector2_addition_return_type(self):
        self.assertIsInstance(test_point2_1 + test_vector2_1, Point2)

    def test_point2_vector2_addition_arithmetic(self):
        self.assertEqual(test_point2_1 + test_vector2_1, Point2(2.0, 2.0))

    def test_point2_float_addition(self):
        with self.assertRaises(TypeError):
            return test_point2_1 + 9.0


if __name__ == '__main__':
    unittest.main()
