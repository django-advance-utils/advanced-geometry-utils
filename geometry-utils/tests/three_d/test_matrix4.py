import pytest

from three_d.matrix4 import Matrix4
from three_d.vector3 import Vector3


@pytest.fixture
def test_matrix4_1():
    return Matrix4()


@pytest.fixture()
def test_matrix4_2():
    return Matrix4([[1.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0]])


@pytest.fixture()
def test_matrix4_3():
    return Matrix4([[1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]])


@pytest.fixture()
def test_vector3():
    return Vector3(2.0, 2.0, 2.0)


def test_make_translation(test_matrix4_1, test_vector3):
    test_translation_matrix = test_matrix4_1.make_translation(test_vector3)
    assert test_translation_matrix == Matrix4([[1.0, 0.0, 0.0, 2.0],
                                               [0.0, 1.0, 0.0, 2.0],
                                               [0.0, 0.0, 1.0, 2.0],
                                               [0.0, 0.0, 0.0, 1.0]])


def test_make_x_rotation(test_matrix4_1):
    test_x_rotation_matrix = test_matrix4_1.make_x_rotation(0.0)
    assert test_x_rotation_matrix == Matrix4([[1.0, 0.0, 0.0, 0.0],
                                            [0.0, 1.0, 0.0, 0.0],
                                            [0.0, 0.0, 1.0, 0.0],
                                            [0.0, 0.0, 0.0, 1.0]])


def test_make_y_rotation(test_matrix4_1):
    test_y_rotation_matrix = test_matrix4_1.make_y_rotation(0.0)
    assert test_y_rotation_matrix == Matrix4([[1.0, 0.0, 0.0, 0.0],
                                            [0.0, 1.0, 0.0, 0.0],
                                            [0.0, 0.0, 1.0, 0.0],
                                            [0.0, 0.0, 0.0, 1.0]])


def test_make_z_rotation(test_matrix4_1):
    test_z_rotation_matrix = test_matrix4_1.make_z_rotation(0.0)
    assert test_z_rotation_matrix == Matrix4([[1.0, 0.0, 0.0, 0.0],
                                            [0.0, 1.0, 0.0, 0.0],
                                            [0.0, 0.0, 1.0, 0.0],
                                            [0.0, 0.0, 0.0, 1.0]])


def test_matrix_to_matrix_multiplication(test_matrix4_1, test_matrix4_2):
    test_multiplication_matrix = test_matrix4_1 * test_matrix4_2
    assert test_multiplication_matrix == Matrix4([[1.0, 1.0, 1.0, 1.0],
                                                  [1.0, 1.0, 1.0, 1.0],
                                                  [1.0, 1.0, 1.0, 1.0],
                                                  [1.0, 1.0, 1.0, 1.0]])
