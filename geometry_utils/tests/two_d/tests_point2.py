import unittest

from geometry_utils.two_d.vector2 import Vector2
from geometry_utils.two_d.point2 import Point2, get_leftmost_point_index, get_points_orientation

test_vector2_1 = Vector2(1.0, 1.0)

test_point2_1 = Point2(1.0, 1.0)
test_point2_2 = Point2(1.0, 0.0)
test_point2_3 = Point2(1.0, 1.0)
test_point2_4 = Point2(0.0, 0.0)
test_point2_5 = Point2(0.0, 1.0)

list_of_points = [
        Point2(0, 0), Point2(1, 1), Point2(3, 2), Point2(0, 5), Point2(5, 2)
    ]


class TestPoint2(unittest.TestCase):
    # Point2 Object Parameter Test
    def test_point2_string_parameter(self):
        with self.assertRaises(TypeError):
            return Point2("0", "0", "0")

    # Point2 Addition Tests
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

    # Point Subtraction Tests
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

    # Point Equality and Inequality Tests
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

    # Less Than or Equal To Tests
    def test_point2_less_than_or_equal_to_point2(self):
        self.assertLessEqual(test_point2_2, test_point2_1)

    def test_point2_less_than_or_equal_to_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1 <= 9.0

    # Greater Than or Equal To Test
    def test_point2_greater_than_or_equal_to_point2(self):
        self.assertGreaterEqual(test_point2_1, test_point2_2)

    def test_point2_greater_than_or_equal_to_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1 >= 9.0

    # To_Vector Tests
    def test_point2_to_vector_return_type(self):
        self.assertIsInstance(test_point2_1.to_vector2(), Vector2)

    def test_point2_to_vector_arithmetic(self):
        self.assertEqual(test_point2_1.to_vector2(), Vector2(1.0, 1.0))

    # Distance_To Tests
    def test_point2_distance_to_point2_return_type(self):
        self.assertIsInstance(test_point2_1.distance_to(test_point2_2), float)

    def test_point2_distance_to_point2_arithmetic(self):
        self.assertEqual(test_point2_1.distance_to(test_point2_2), 1.0)

    def test_point2_distance_to_float(self):
        with self.assertRaises(TypeError):
            return test_point2_1.distance_to(9.0)

    # Flip_XY Test
    def test_point2_flip_xy(self):
        self.assertEqual(Point2(1.0, 0.0).flip_xy(), test_point2_5)

    # Mirror_Y Test
    def test_point2_mirror_y(self):
        self.assertEqual(Point2(1.0, 1.0).mirror_y(), Point2(-1.0, 1.0))

    # Get_Leftmost_Point_Index Tests
    def test_get_leftmost_point_index(self):
        self.assertEqual(get_leftmost_point_index(list_of_points), 3)

    def test_get_leftmost_point_index_return_type(self):
        self.assertIsInstance(get_leftmost_point_index(list_of_points), int)

    def test_get_leftmost_point_with_float_argument(self):
        with self.assertRaises(TypeError):
            return get_leftmost_point_index(9.0)

    # Get_Points_Orientation Tests
    def test_get_points_orientation_arithmetic(self):
        self.assertEqual(get_points_orientation(Point2(0, 0), Point2(1, 1), Point2(2, 2)), "Collinear")
        self.assertEqual(get_points_orientation(Point2(0, 0), Point2(0, 1), Point2(1, 1)), "Clockwise")
        self.assertEqual(get_points_orientation(Point2(0, 0), Point2(1, 0), Point2(1, 1)), "Counterclockwise")

    def test_get_points_orientation_return_type(self):
        self.assertIsInstance(get_points_orientation(test_point2_1, test_point2_2, test_point2_3), str)

    def test_get_points_orientation_with_float_arguments(self):
        with self.assertRaises(TypeError):
            return get_leftmost_point_index(9.0, 9.0, 9.0)


if __name__ == '__main__':
    unittest.main()
