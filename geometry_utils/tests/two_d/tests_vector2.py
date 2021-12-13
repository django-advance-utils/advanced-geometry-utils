import math
import unittest

from geometry_utils import maths_utility
from geometry_utils.two_d.vector2 import Vector2

test_vector2_1 = Vector2(1.0, 1.0)
test_vector2_2 = Vector2(1.0, 0.0)
test_vector2_3 = Vector2(1.0, 1.0)
test_vector2_4 = Vector2(0.0, 0.0)
test_vector2_5 = Vector2(0.0, 1.0)


class TestVector2(unittest.TestCase):

    # Vector2 Object Parameter Test
    def test_vector2_string_parameter(self):
        with self.assertRaises(TypeError):
            return Vector2("0", "0", "0")

    # Vector2 Addition Tests
    def test_vector2_addition_return_type(self):
        self.assertIsInstance(test_vector2_1 + test_vector2_2, Vector2)

    def test_vector2_vector2_addition_arithmetic(self):
        self.assertEqual(test_vector2_1 + test_vector2_2, Vector2(2.0, 1.0))

    def test_vector2_float_addition(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 + 9.0

    # Vector2 Subtraction Tests
    def test_vector2_vector2_subtraction_return_type(self):
        self.assertIsInstance(test_vector2_1 - test_vector2_2, Vector2)

    def test_vector2_vector2_subtraction_arithmetic(self):
        self.assertEqual(test_vector2_1 - test_vector2_2, Vector2(0.0, 1.0))

    def test_vector2_float_subtraction(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 - 9.0

    # Vector2 Multiplication Tests
    def test_vector2_vector2_multiplication(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 * test_vector2_2

    def test_vector2_float_multiplication_return_type(self):
        self.assertIsInstance(test_vector2_1 * 9.0, Vector2)

    def test_vector2_float_multiplication_arithmetic(self):
        self.assertEqual(test_vector2_1 * 2.0, Vector2(2.0, 2.0))

    # Vector2 Division Tests
    def test_vector2_vector2_division(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 / test_vector2_2

    def test_vector2_float_division(self):
        self.assertEqual(test_vector2_1 / 2.0, Vector2(0.5, 0.5))

    def test_vector2_float_division_return_type(self):
        self.assertIsInstance((test_vector2_1 / 9.0), Vector2)

    # Vector2 Equality Tests
    def test_vector2_vector2_equality(self):
        self.assertEqual(test_vector2_1, test_vector2_3)

    def test_vector2_float_equality(self):
        with self.assertRaises(TypeError):
            self.assertEqual(test_vector2_1, 9.0)

    # Vector2 Inequality Tests
    def test_vector2_vector2_inequality(self):
        self.assertNotEqual(test_vector2_1, test_vector2_2)
        self.assertNotEqual(test_vector2_1, test_vector2_2)

    def test_vector2_float_inequality(self):
        with self.assertRaises(TypeError):
            self.assertNotEqual(test_vector2_1, 9.0)

    # Vector2 Dot Tests
    def test_vector2_dot_vector2_return_type(self):
        self.assertIsInstance(test_vector2_1.dot(test_vector2_2), float)

    def test_vector2_dot_vector2_arithmetic(self):
        self.assertEqual(test_vector2_1.dot(test_vector2_2), 1.0)

    def test_vector2_dot_float(self):
        with self.assertRaises(TypeError):
            return test_vector2_1.dot(9.0)

    # Vector2 Cross Tests
    def test_vector2_cross_vector2_return_type(self):
        self.assertIsInstance(test_vector2_1.cross(test_vector2_2), Vector2)

    def test_vector2_cross_vector2_arithmetic(self):
        self.assertEqual(test_vector2_1.cross(test_vector2_2), Vector2(-1.0, 1.0))

    def test_vector2_cross_float(self):
        with self.assertRaises(TypeError):
            return test_vector2_1.cross(9.0)

    # Vector Length Tests
    def test_vector2_length_return_type(self):
        self.assertIsInstance(test_vector2_1.length(), float)

    def test_vector2_length_arithmetic(self):
        self.assertEqual(test_vector2_1.length(), math.sqrt(2.0))

    # Vector Normalise Tests
    def test_vector2_normalised_return_type(self):
        self.assertIsInstance(test_vector2_1.normalise(), Vector2)

    def test_vector2_normalised_arithmetic(self):
        self.assertEqual(test_vector2_1.normalise(), Vector2(1 / math.sqrt(2.0), 1 / math.sqrt(2.0)))
        self.assertEqual(test_vector2_4.normalise(), test_vector2_4)

    # Vector Reverse Tests
    def test_reversed_vector2_return_type(self):
        self.assertIsInstance(test_vector2_1, Vector2)

    def test_reversed_vector2_arithmetic(self):
        self.assertEqual(test_vector2_1.reverse(), Vector2(-1.0, -1.0))
        self.assertEqual(test_vector2_4.reverse(), test_vector2_4)

    # Vector Rotate Tests
    def test_vector2_rotate_return_type(self):
        self.assertIsInstance(test_vector2_1.rotate(test_vector2_4, maths_utility.HALF_PI), Vector2)

    def test_vector2_rotate_arithmetic(self):
        rotated_vector = test_vector2_2.rotate(test_vector2_4, maths_utility.HALF_PI)
        self.assert_(maths_utility.floats_are_close(rotated_vector.x, 0.0) and
                     maths_utility.floats_are_close(rotated_vector.y, 1.0))

    def test_vector2_rotate_with_float_origin(self):
        with self.assertRaises(TypeError):
            return test_vector2_2.rotate(9.0, maths_utility.HALF_PI)

    def test_vector2_rotate_with_Vector2_theta(self):
        with self.assertRaises(TypeError):
            return test_vector2_2.rotate(test_vector2_4, test_vector2_4)

    # Vector Invert Tests
    def test_vector2_invert_return_type(self):
        self.assertIsInstance(test_vector2_2.invert(), Vector2)

    def test_vector_invert_arithmetic(self):
        self.assertEqual(test_vector2_2.invert(), Vector2(0.0, 1.0))

    # Vector Get_Perpendicular Tests
    def test_vector2_get_perpendicular_return_type(self):
        self.assertIsInstance(test_vector2_2.get_perpendicular(), Vector2)

    def test_vector_get_perpendicular_arithmetic(self):
        self.assertEqual(test_vector2_1.get_perpendicular(), Vector2(-1.0, 1.0))


if __name__ == '__main__':
    unittest.main()
