import unittest

from math import sqrt

from geometry_utils.three_d.vector3 import Vector3

test_vector3_1 = Vector3(1.0, 1.0, 1.0)
test_vector3_2 = Vector3(1.0, 0.0, 0.0)
test_vector3_3 = Vector3(1.0, 1.0, 1.0)
test_vector3_4 = Vector3(0.0, 0.0, 0.0)


class TestVector3(unittest.TestCase):
    def test_vector3_vector3_addition_return_type(self):
        self.assertIsInstance(test_vector3_1 + test_vector3_2, Vector3)

    def test_vector3_float_addition(self):
        with self.assertRaises(TypeError):
            return test_vector3_1 + 9.0

    def test_vector3_vector3_addition_arithmetic(self):
        self.assertEqual(test_vector3_1 + test_vector3_2, Vector3(2.0, 1.0, 1.0))

    def test_vector3_vector3_subtraction_return_type(self):
        self.assertIsInstance(test_vector3_1 - test_vector3_2, Vector3)

    def test_vector3_float_subtraction(self):
        with self.assertRaises(TypeError):
            return test_vector3_1 - 9.0

    def test_vector3_vector3_subtraction_arithmetic(self):
        self.assertEqual(test_vector3_1 - test_vector3_2, Vector3(0.0, 1.0, 1.0))

    def test_vector3_vector3_multiplication(self):
        with self.assertRaises(TypeError):
            return test_vector3_1 * test_vector3_2

    def test_vector3_float_multiplication_return_type(self):
        self.assertIsInstance(test_vector3_1 * 9.0, Vector3)

    def test_vector_float_multiplication_arithmetic(self):
        self.assertEqual(test_vector3_1 * 2.0, Vector3(2.0, 2.0, 2.0))

    def test_vector3_vector3_division(self):
        with self.assertRaises(TypeError):
            return test_vector3_1 / test_vector3_2

    def test_vector3_float_division(self):
        self.assertEqual(test_vector3_1 / 2.0, Vector3(0.5, 0.5, 0.5))

    def test_vector3_float_division_return_type(self):
        self.assertIsInstance((test_vector3_1 / 9.0), Vector3)

    def test_vector3_vector3_equality(self):
        self.assertEqual(test_vector3_1, test_vector3_1)
        self.assertEqual(test_vector3_1, test_vector3_3)

    def test_vector3_vector3_inequality(self):
        self.assertNotEqual(test_vector3_1, test_vector3_2)
        self.assertNotEqual(test_vector3_1, test_vector3_2)

    def test_vector3_dot_vector3_return_type(self):
        self.assertIsInstance(test_vector3_1.dot(test_vector3_2), float)
        self.assertIsInstance(test_vector3_2.dot(test_vector3_1), float)

    def test_vector3_dot_vector3_arithmetic(self):
        self.assertEqual(test_vector3_1.dot(test_vector3_2), 1.0)
        self.assertEqual(test_vector3_2.dot(test_vector3_1), 1.0)

    def test_vector3_cross_vector3_return_type(self):
        self.assertIsInstance(test_vector3_1.cross(test_vector3_2), Vector3)
        self.assertIsInstance(test_vector3_2.cross(test_vector3_1), Vector3)

    def test_vector3_cross_vector3_arithmetic(self):
        self.assertEqual(test_vector3_1.cross(test_vector3_2), Vector3(0.0, 1.0, -1.0))
        self.assertEqual(test_vector3_2.cross(test_vector3_1), Vector3(0.0, -1.0, 1.0))

    def test_vector3_length_return_type(self):
        self.assertIsInstance(test_vector3_1.length(), float)

    def test_vector3_length_arithmetic(self):
        self.assertEqual(test_vector3_1.length(), sqrt(3.0))

    def test_vector3_normalised_return_type(self):
        self.assertIsInstance(test_vector3_1.normalised(), Vector3)

    def test_vector3_normalised_arithmetic(self):
        self.assertEqual(test_vector3_1.normalised(), Vector3(1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3)))
        self.assertEqual(test_vector3_4.normalised(), test_vector3_4)

    def test_reversed_vector3_return_type(self):
        self.assertIsInstance(test_vector3_1, Vector3)

    def test_reversed_vector3_arithmetic(self):
        self.assertEqual(test_vector3_1.reverse(), Vector3(-1.0, -1.0, -1.0))
        self.assertEqual(test_vector3_4.reverse(), test_vector3_4)


if __name__ == '__main__':
    unittest.main()
