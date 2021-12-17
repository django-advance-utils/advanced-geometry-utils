import unittest

from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.matrix4 import Matrix4
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3

from math import sqrt

test_point3_1 = Point3(1.0, 1.0, 1.0)
test_point3_2 = Point3(1.0, 0.0, 0.0)
test_point3_3 = Point3(1.0, 1.0, 1.0)

test_vector3 = Vector3(1.0, 1.0, 1.0)

test_matrix4 = Matrix4([[1.0, 1.0, 1.0, 1.0],
                        [1.0, 1.0, 1.0, 1.0],
                        [1.0, 1.0, 1.0, 1.0],
                        [1.0, 1.0, 1.0, 1.0]])

test_edge3 = Edge3()


class MyTestCase(unittest.TestCase):
    def test_point3_point3_addition(self):
        with self.assertRaises(TypeError):
            return test_point3_1 + test_point3_2

    def test_point3_vector3_addition_return_type(self):
        self.assertIsInstance(test_point3_1 + test_vector3, Point3)

    def test_point3_vector3_addition_arithmetic(self):
        self.assertEqual(test_point3_1 + test_vector3, Point3(2.0, 2.0, 2.0))

    def test_point3_float_addition(self):
        with self.assertRaises(TypeError):
            return test_point3_1 + 9.0

    def test_point3_point3_subtraction_return_type(self):
        self.assertIsInstance(test_point3_1 - test_point3_2, Vector3)

    def test_point3_point3_subtraction_arithmetic(self):
        self.assertEqual(test_point3_1 - test_point3_2, Vector3(0.0, 1.0, 1.0))

    def test_point3_vector3_subtraction_solution_type(self):
        self.assertIsInstance(test_point3_1 - test_vector3, Point3)

    def test_point3_vector3_subtraction_arithmetic(self):
        self.assertEqual(test_point3_1 - test_vector3, Point3(0.0, 0.0, 0.0))

    def test_point3_float_subtraction(self):
        with self.assertRaises(TypeError):
            return test_point3_1 - 9.0

    def test_point3_point3_multiplication(self):
        with self.assertRaises(TypeError):
            return test_point3_1 * test_point3_2

    def test_point3_to_point3_equality(self):
        self.assertEqual(test_point3_1, test_point3_1)
        self.assertEqual(test_point3_1, test_point3_3)

    def test_point3_to_matrix4_equality(self):
        with self.assertRaises(TypeError):
            return test_point3_1 == test_matrix4

    def test_point3_to_point3_inequality(self):
        self.assertNotEqual(test_point3_1, test_point3_2)
        self.assertNotEqual(test_point3_1, test_point3_2)

    def test_point3_to_matrix4_inequality(self):
        with self.assertRaises(TypeError):
            return test_point3_1 != test_matrix4

    def test_point3_less_than_or_equal_to_point3(self):
        self.assertLessEqual(test_point3_2, test_point3_1)

    def test_point3_less_than_or_equal_to_edge3(self):
        with self.assertRaises(TypeError):
            self.assertLessEqual(test_point3_1, test_edge3)

    def test_point3_greater_than_or_equal_to_point3(self):
        self.assertGreaterEqual(test_point3_1, test_point3_2)

    def test_point3_greater_than_or_equal_to_edge3(self):
        with self.assertRaises(TypeError):
            self.assertGreaterEqual(test_point3_1, test_edge3)

    def test_point3_to_vector_return_type(self):
        self.assertIsInstance(test_point3_1.to_vector3(), Vector3)

    def test_point3_to_vector_arithmetic(self):
        self.assertEqual(test_point3_1.to_vector3(), Vector3(1.0, 1.0, 1.0))

    def test_point3_distance_to_point3_return_type(self):
        self.assertIsInstance(test_point3_1.distance_to(test_point3_1), float)

    def test_point3_distance_to_point3_arithmetic(self):
        self.assertEqual(test_point3_1.distance_to(test_point3_2), sqrt(2))


if __name__ == '__main__':
    unittest.main()
