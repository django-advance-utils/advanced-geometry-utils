import unittest

from geometry_utils.two_d.matrix3 import Matrix3
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2

test_vector2_1 = Vector2(1.0, 1.0)
test_point2_1 = Point2(1.0, 1.0)

test_matrix3_1 = Matrix3()
test_matrix3_2 = Matrix3([[1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0]])


class TestMatrix3(unittest.TestCase):
    def test_matrix3_string_parameter(self):
        with self.assertRaises(TypeError):
            return Matrix3("0")

    def test_matrix_length_of_vals(self):
        with self.assertRaises(AttributeError):
            return Matrix3([3])

    def test_matrix_vals_string_parameter(self):
        with self.assertRaises(AttributeError):
            return Matrix3([["1.0", 1.0, 1.0],
                            [1.0, "1.0", 1.0],
                            [1.0, 1.0, 1.0]])

    def test_matrix_matrix_equality(self):
        self.assertEqual(test_matrix3_1, test_matrix3_2)

    def test_matrix3_make_translation(self):
        test_translation_matrix = Matrix3.translation(test_vector2_1)
        self.assertEqual(test_translation_matrix, Matrix3([[1.0, 0.0, 1.0],
                                                           [0.0, 1.0, 1.0],
                                                           [0.0, 0.0, 1.0]]))

    def test_matrix3_make_rotation(self):
        test_rotation_matrix = Matrix3.rotation(0.0)
        self.assertEqual(test_rotation_matrix, Matrix3())

    def test_matrix3_to_matrix3_multiplication(self):
        self.assertEqual(test_matrix3_1 * test_matrix3_2, Matrix3([[1.0, 1.0, 1.0],
                                                                   [1.0, 1.0, 1.0],
                                                                   [1.0, 1.0, 1.0]]))

    def test_matrix_vector_multiplication_return_type(self):
        self.assertIsInstance(Matrix3() * test_vector2_1, Vector2)

    def test_matrix_vector_multiplication_arithmetic(self):
        self.assertEqual(Matrix3() * test_vector2_1, test_vector2_1)

    def test_matrix_point_multiplication_return_type(self):
        self.assertIsInstance(Matrix3() * test_point2_1, Point2)

    def test_matrix_point_multiplication_arithmetic(self):
        self.assertEqual(Matrix3() * test_point2_1, test_point2_1)


if __name__ == '__main__':
    unittest.main()
