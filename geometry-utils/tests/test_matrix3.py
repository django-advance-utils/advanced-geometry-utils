import pytest

from two_d.matrix3 import Matrix3
from two_d.vector2 import Vector2


@pytest.fixture
def test_matrix_1():
    return Matrix3()


@pytest.fixture()
def test_matrix_2():
    return Matrix3([[1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0]])


@pytest.fixture()
def test_matrix_3():
    return Matrix3([[1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0]])


@pytest.fixture()
def test_vector():
    return Vector2(2.0, 2.0)


def test_make_translation(test_matrix_1, test_vector):
    test_translation_matrix = test_matrix_1.make_translation(test_vector)
    assert test_translation_matrix == Matrix3([[1.0, 0.0, 2.0],
                                               [0.0, 1.0, 2.0],
                                               [0.0, 0.0, 1.0]])


'''
def test_make_rotation(test_matrix_1):
    test_rotation_matrix = test_matrix_1.make_translation(0.0)
    assert test_rotation_matrix == Matrix3([[1.0, 0.0, 0.0],
                                            [0.0, 1.0, 0.0],
                                            [0.0, 0.0, 1.0]])
'''

    
def test_matrix_to_matrix_multiplication(test_matrix_1, test_matrix_2):
    assert test_matrix_1 * test_matrix_2 == Matrix3([[1.0, 1.0, 1.0],
                                                     [1.0, 1.0, 1.0],
                                                     [1.0, 1.0, 1.0]])