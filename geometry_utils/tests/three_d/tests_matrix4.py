import unittest

from geometry_utils.three_d.matrix4 import Matrix4
from geometry_utils.three_d.vector3 import Vector3

test_matrix4_1 = Matrix4()
test_matrix4_2 = Matrix4([[1.0, 1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0, 1.0],
                          [1.0, 1.0, 1.0, 1.0]])

test_vector = Vector3(1.0, 1.0, 1.0)


class TestMatrix4(unittest.TestCase):
    def test_matrix4_make_translation(self):
        test_translation_matrix = test_matrix4_1.make_translation(test_vector)
        self.assertEqual(test_translation_matrix, Matrix4([[1.0, 0.0, 0.0, 1.0],
                                                           [0.0, 1.0, 0.0, 1.0],
                                                           [0.0, 0.0, 1.0, 1.0],
                                                           [0.0, 0.0, 0.0, 1.0]]))

    def test_matrix4_make_x_rotation(self):
        test_x_rotation_matrix = test_matrix4_1.make_x_rotation(0.0)
        self.assertEqual(test_x_rotation_matrix, Matrix4([[1.0, 0.0, 0.0, 0.0],
                                                          [0.0, 1.0, 0.0, 0.0],
                                                          [0.0, 0.0, 1.0, 0.0],
                                                          [0.0, 0.0, 0.0, 1.0]]))

    def test_matrix4_make_y_rotation(self):
        test_y_rotation_matrix = test_matrix4_1.make_y_rotation(0.0)
        self.assertEqual(test_y_rotation_matrix, Matrix4([[1.0, 0.0, 0.0, 0.0],
                                                          [0.0, 1.0, 0.0, 0.0],
                                                          [0.0, 0.0, 1.0, 0.0],
                                                          [0.0, 0.0, 0.0, 1.0]]))

    def test_matrix4_make_z_rotation(self):
        test_z_rotation_matrix = test_matrix4_1.make_z_rotation(0.0)
        self.assertEqual(test_z_rotation_matrix, Matrix4([[1.0, 0.0, 0.0, 0.0],
                                                          [0.0, 1.0, 0.0, 0.0],
                                                          [0.0, 0.0, 1.0, 0.0],
                                                          [0.0, 0.0, 0.0, 1.0]]))

    def test_matrix4_to_matrix4_multiplication(self):
        test_multiplication_matrix = test_matrix4_1 * test_matrix4_2
        self.assertEqual(test_multiplication_matrix, Matrix4([[1.0, 1.0, 1.0, 1.0],
                                                              [1.0, 1.0, 1.0, 1.0],
                                                              [1.0, 1.0, 1.0, 1.0],
                                                              [1.0, 1.0, 1.0, 1.0]]))


if __name__ == '__main__':
    unittest.main()
