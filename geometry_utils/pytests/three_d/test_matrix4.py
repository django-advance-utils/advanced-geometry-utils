from geometry_utils.three_d.matrix4 import Matrix4


def test_matrix4_make_translation(test_matrix4_1, test_vector3_1):
    test_translation_matrix = Matrix4.translation(test_vector3_1)
    assert test_translation_matrix == Matrix4([[1.0, 0.0, 0.0, 1.0],
                                               [0.0, 1.0, 0.0, 1.0],
                                               [0.0, 0.0, 1.0, 1.0],
                                               [0.0, 0.0, 0.0, 1.0]])


def test_matrix4_make_x_rotation():
    test_x_rotation_matrix = Matrix4.x_rotation(0.0)
    assert test_x_rotation_matrix == Matrix4([[1.0, 0.0, 0.0, 0.0],
                                              [0.0, 1.0, 0.0, 0.0],
                                              [0.0, 0.0, 1.0, 0.0],
                                              [0.0, 0.0, 0.0, 1.0]])


def test_matrix4_make_y_rotation():
    test_y_rotation_matrix = Matrix4.y_rotation(0.0)
    assert test_y_rotation_matrix == Matrix4([[1.0, 0.0, 0.0, 0.0],
                                              [0.0, 1.0, 0.0, 0.0],
                                              [0.0, 0.0, 1.0, 0.0],
                                              [0.0, 0.0, 0.0, 1.0]])


def test_matrix4_make_z_rotation():
    test_z_rotation_matrix = Matrix4.z_rotation(0.0)
    assert test_z_rotation_matrix == Matrix4([[1.0, 0.0, 0.0, 0.0],
                                              [0.0, 1.0, 0.0, 0.0],
                                              [0.0, 0.0, 1.0, 0.0],
                                              [0.0, 0.0, 0.0, 1.0]])


def test_matrix4_to_matrix4_multiplication(test_matrix4_1, test_matrix4_2):
    test_multiplication_matrix = test_matrix4_1 * test_matrix4_2
    assert test_multiplication_matrix == Matrix4([[1.0, 1.0, 1.0, 1.0],
                                                  [1.0, 1.0, 1.0, 1.0],
                                                  [1.0, 1.0, 1.0, 1.0],
                                                  [1.0, 1.0, 1.0, 1.0]])
