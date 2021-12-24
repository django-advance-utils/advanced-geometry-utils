import math
import unittest
import geometry_utils.maths_utility as maths_utility

from geometry_utils.two_d.vector2 import Vector2

test_vector2_1 = Vector2(1.0, 1.0)
test_vector2_2 = Vector2(1.0, 0.0)
test_vector2_3 = Vector2(1.0, 1.0)
test_vector2_4 = Vector2(0.0, 0.0)
test_vector2_5 = Vector2(0.0, 1.0)
test_vector2_6 = Vector2(1.0, 0.0)


class TestVector2(unittest.TestCase):
    def test_vector2_string_parameter(self):
        with self.assertRaises(TypeError):
            return Vector2("0", "0", "0")

    def test_vector2_print_string(self):
        self.assertEqual(test_vector2_1.__str__(), "Vector2(x:1.00, y:1.00)")

    def test_vector2_addition_return_type(self):
        self.assertIsInstance(test_vector2_1 + test_vector2_2, Vector2)

    def test_vector2_vector2_addition_arithmetic(self):
        self.assertEqual(test_vector2_1 + test_vector2_2, Vector2(2.0, 1.0))

    def test_vector2_float_addition(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 + 9.0

    def test_vector2_vector2_subtraction_return_type(self):
        self.assertIsInstance(test_vector2_1 - test_vector2_2, Vector2)

    def test_vector2_vector2_subtraction_arithmetic(self):
        self.assertEqual(test_vector2_1 - test_vector2_2, Vector2(0.0, 1.0))

    def test_vector2_float_subtraction(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 - 9.0

    def test_vector2_vector2_multiplication(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 * test_vector2_2

    def test_vector2_float_multiplication_return_type(self):
        self.assertIsInstance(test_vector2_1 * 9.0, Vector2)

    def test_vector2_float_multiplication_arithmetic(self):
        self.assertEqual(test_vector2_1 * 2.0, Vector2(2.0, 2.0))

    def test_vector2_vector2_division(self):
        with self.assertRaises(TypeError):
            return test_vector2_1 / test_vector2_2

    def test_vector2_float_division(self):
        self.assertEqual(test_vector2_1 / 2.0, Vector2(0.5, 0.5))

    def test_vector2_float_division_return_type(self):
        self.assertIsInstance((test_vector2_1 / 9.0), Vector2)

    def test_vector2_vector2_equality(self):
        self.assertEqual(test_vector2_1, test_vector2_3)

    def test_vector2_float_equality(self):
        with self.assertRaises(TypeError):
            self.assertEqual(test_vector2_1, 9.0)

    def test_vector2_vector2_inequality(self):
        self.assertNotEqual(test_vector2_1, test_vector2_2)
        self.assertNotEqual(test_vector2_1, test_vector2_2)

    def test_vector2_float_inequality(self):
        with self.assertRaises(TypeError):
            self.assertNotEqual(test_vector2_1, 9.0)

    def test_vector2_dot_vector2_return_type(self):
        self.assertIsInstance(test_vector2_1.dot(test_vector2_2), float)

    def test_vector2_dot_vector2_arithmetic(self):
        self.assertEqual(test_vector2_1.dot(test_vector2_2), 1.0)

    def test_vector2_dot_float(self):
        with self.assertRaises(TypeError):
            return test_vector2_1.dot(9.0)

    def test_vector2_cross_vector2_return_type(self):
        self.assertIsInstance(test_vector2_1.cross(test_vector2_2), Vector2)

    def test_vector2_cross_vector2_arithmetic(self):
        self.assertEqual(test_vector2_1.cross(test_vector2_2), Vector2(-1.0, 1.0))

    def test_vector2_cross_float(self):
        with self.assertRaises(TypeError):
            return test_vector2_1.cross(9.0)

    def test_vector2_length_return_type(self):
        self.assertIsInstance(test_vector2_1.length(), float)

    def test_vector2_length_arithmetic(self):
        self.assertEqual(test_vector2_1.length(), math.sqrt(2.0))

    def test_vector2_square_length_return_type(self):
        self.assertIsInstance(test_vector2_1.square_length(), float)

    def test_vector2_square_length_arithmetic(self):
        self.assertEqual(test_vector2_1.square_length(), 2.0)

    def test_vector2_normalise_arithmetic(self):
        self.assertEqual(test_vector2_5.normalise(), Vector2(0.0, 1.0))

    def test_vector2_normalised_return_type(self):
        self.assertIsInstance(test_vector2_1.normalised(), Vector2)

    def test_vector2_normalised_arithmetic(self):
        self.assertEqual(test_vector2_1.normalised(), Vector2(1 / math.sqrt(2.0), 1 / math.sqrt(2.0)))
        self.assertEqual(test_vector2_4.normalised(), test_vector2_4)

    def test_vector2_rotate_return_type(self):
        self.assertIsInstance(test_vector2_1.rotate(test_vector2_4, maths_utility.HALF_PI), Vector2)

    def test_vector2_rotate_arithmetic(self):
        rotated_vector = test_vector2_2.rotate(test_vector2_4, maths_utility.HALF_PI)
        self.assertEqual(rotated_vector, Vector2(0.0, 1.0))

    def test_vector2_rotate_with_float_origin(self):
        with self.assertRaises(TypeError):
            return test_vector2_2.rotate(9.0, maths_utility.HALF_PI)

    def test_vector2_rotate_with_Vector2_theta(self):
        with self.assertRaises(TypeError):
            return test_vector2_2.rotate(test_vector2_4, test_vector2_4)

    def test_vector_invert_arithmetic(self):
        self.assertEqual(test_vector2_6.invert(), Vector2(-1.0, 0.0))

    def test_vector2_inverted_return_type(self):
        self.assertIsInstance(test_vector2_2.inverted(), Vector2)

    def test_vector_inverted_arithmetic(self):
        self.assertEqual(test_vector2_2.inverted(), Vector2(-1.0, 0.0))

    def test_vector2_get_perpendicular_return_type(self):
        self.assertIsInstance(test_vector2_2.get_perpendicular(), Vector2)

    def test_vector_get_perpendicular_arithmetic(self):
        self.assertEqual(test_vector2_1.get_perpendicular(), Vector2(-1.0, 1.0))

    def test_vector_angle_to_return_type(self):
        self.assertIsInstance(test_vector2_1.angle_to(test_vector2_2), float)

    def test_vector_angle_to_arithmetic(self):
        self.assertEqual(test_vector2_2.angle_to(test_vector2_5), maths_utility.HALF_PI)

    def test_vector_signed_angle_to_return_type(self):
        self.assertIsInstance(test_vector2_1.signed_angle_to(test_vector2_2), float)

    def test_vector_signed_angle_to_arithmetic(self):
        self.assertEqual(test_vector2_2.signed_angle_to(test_vector2_5), -maths_utility.HALF_PI)

    def test_vector_angle_to_x_axis_return_type(self):
        self.assertIsInstance(test_vector2_1.angle_to_x_axis(), float)

    def test_vector_angle_to_x_axis_arithmetic(self):
        self.assertEqual(test_vector2_2.angle_to_x_axis(), 0.0)
        self.assertEqual(test_vector2_5.angle_to_x_axis(), maths_utility.HALF_PI)


if __name__ == '__main__':
    unittest.main()
