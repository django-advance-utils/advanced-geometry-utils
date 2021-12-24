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
    def test_point2_string_parameter(self):
        with self.assertRaises(TypeError):
            return Point2("0", "0", "0")

    def test_point2_print_string(self):
        self.assertEqual(test_point2_1.__str__(), "Point2(x:1.00, y:1.00)")

    def test_point2_point2_addition(self):
        with self.assertRaises(TypeError):
            return test_point2_1 + test_point2_2

    def test_point2_vector2_addition_return_type(self):
        self.assertIsInstance(test_point2_1 + test_vector2_1, Point2)

    def test_point2_vector2_addition_arithmetic(self):
        self.assertEqual(test_point2_1 + test_vector2_1, Point2(2.0, 2.0))

    def test_point2_float_addition(self):
        with self.assertRaises(TypeError):
            return test_point2_1 + 9.0

    def test_point2_point2_subtraction_return_type(self):
        self.assertIsInstance(test_point2_1 - test_point2_2, Vector2)

    def test_point2_point2_subtraction_arithmetic(self):
        self.assertEqual(test_point2_1 - test_point2_3, Vector2(0.0, 0.0))

    def test_point2_vector2_subtraction_solution_type(self):
        self.assertIsInstance(test_point2_1 - test_vector2_1, Point2)

    def test_point2_vector2_subtraction_arithmetic(self):
        self.assertEqual(test_point2_1 - test_vector2_1, Point2(0.0, 0.0))

    def test_point2_float_subtraction(self):
        with self.assertRaises(TypeError):
            return test_point2_1 - 9.0

    def test_point2_to_point2_equality(self):
        self.assertEqual(test_point2_1, test_point2_1)
        self.assertEqual(test_point2_1, test_point2_3)

    def test_point2_to_float_equality(self):
        with self.assertRaises(TypeError):
            return test_point2_1 == 9.0

    def test_point2_to_point2_inequality(self):
        self.assertNotEqual(test_point2_1, test_point2_2)

    def test_point2_to_float_inequality(self):
        with self.assertRaises(TypeError):
            self.assertNotEqual(test_point2_1, 9.0)

    def test_point2_less_than_or_equal_to_point2(self):
        self.assertLessEqual(test_point2_2, test_point2_1)

    def test_point2_less_than_or_equal_to_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1 <= 9.0

    def test_point2_greater_than_or_equal_to_point2(self):
        self.assertGreaterEqual(test_point2_1, test_point2_2)

    def test_point2_greater_than_or_equal_to_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1 >= 9.0

    def test_point2_less_than_point2(self):
        self.assertLess(test_point2_4, test_point2_1)

    def test_point2_less_than_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1 < 9.0

    def test_point2_greater_than_point2(self):
        self.assertGreater(test_point2_1, test_point2_4)

    def test_point2_greater_than_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1 > 9.0

    def test_point2_to_vector_return_type(self):
        self.assertIsInstance(test_point2_1.to_vector2(), Vector2)

    def test_point2_to_vector_arithmetic(self):
        self.assertEqual(test_point2_1.to_vector2(), Vector2(1.0, 1.0))

    def test_point2_distance_to_point2_return_type(self):
        self.assertIsInstance(test_point2_1.distance_to(test_point2_2), float)

    def test_point2_distance_to_point2_arithmetic(self):
        self.assertEqual(test_point2_1.distance_to(test_point2_2), 1.0)

    def test_point2_distance_to_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1.distance_to(9.0)

    def test_point2_mirror_y(self):
        self.assertEqual(Point2(1.0, 1.0).mirror_y(), Point2(-1.0, 1.0))


if __name__ == '__main__':
    unittest.main()
