import pytest

from two_d.matrix3 import Matrix3
from two_d.vector2 import Vector2


@pytest.fixture
def test_matrix3_1():
    return Matrix3()


@pytest.fixture()
def test_matrix3_2():
    return Matrix3([[1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0]])


@pytest.fixture()
def test_matrix3_3():
    return Matrix3([[1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0]])


@pytest.fixture()
def test_vector2():
    return Vector2(2.0, 2.0)


def test_make_translation(test_matrix3_1, test_vector2):
    test_translation_matrix = test_matrix3_1.make_translation(test_vector2)
    assert test_translation_matrix == Matrix3([[1.0, 0.0, 2.0],
                                               [0.0, 1.0, 2.0],
                                               [0.0, 0.0, 1.0]])


def test_make_rotation(test_matrix3_1):
    test_rotation_matrix = test_matrix3_1.make_rotation(0.0)
    assert test_rotation_matrix == Matrix3([[1.0, 0.0, 0.0],
                                            [0.0, 1.0, 0.0],
                                            [0.0, 0.0, 1.0]])


def test_matrix_to_matrix_multiplication(test_matrix3_1, test_matrix3_2):
    assert test_matrix3_1 * test_matrix3_2 == Matrix3([[1.0, 1.0, 1.0],
                                                     [1.0, 1.0, 1.0],
                                                     [1.0, 1.0, 1.0]])