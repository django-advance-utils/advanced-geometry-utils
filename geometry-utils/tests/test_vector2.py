import pytest
import math

from two_d.vector2 import Vector2


@pytest.fixture
def test_vector_1():
    return Vector2(1.0, 1.0)


@pytest.fixture()
def test_vector_2():
    return Vector2(1.0, 0.0)


@pytest.fixture()
def test_vector_3():
    return Vector2(0.0, 1.0)


@pytest.fixture()
def test_vector_4():
    return Vector2(0.0, 0.0)


@pytest.fixture()
def test_vector_5():
    return Vector2(1.0, 1.0)


'''
Vector Addition Tests
'''


def test_vector_vector_addition_return_type(test_vector_1, test_vector_2):
    assert isinstance(test_vector_1 + test_vector_2, Vector2)


def test_vector_float_addition(test_vector_1):
    with pytest.raises(TypeError):
        test_vector_1 + 9.0


def test_vector_vector_addition_arithmetic(test_vector_1, test_vector_2):
    assert test_vector_1 + test_vector_2 == Vector2(2.0, 1.0)


'''
Vector Subtraction Tests
'''


def test_vector_vector_subtraction_return_type(test_vector_1, test_vector_2):
    assert isinstance(test_vector_1 - test_vector_2, Vector2)


def test_vector_float_subtraction(test_vector_1):
    with pytest.raises(TypeError):
        test_vector_1 - 9.0


def test_vector_vector_subtraction_arithmetic(test_vector_1, test_vector_2):
    assert test_vector_1 - test_vector_2 == Vector2(0.0, 1.0)


'''
Vector Multiplication Tests
'''


def test_vector_vector_multiplication(test_vector_1, test_vector_2):
    with pytest.raises(TypeError):
        test_vector_1 * test_vector_2


def test_vector_float_multiplication_return_type(test_vector_1, test_vector_2):
    assert isinstance(test_vector_1 * 9.0, Vector2)


def test_vector_float_multiplication_arithmetic(test_vector_1):
    assert test_vector_1 * 2.0 == Vector2(2.0, 2.0)


'''
Vector Division Tests
'''


def test_vector_vector_division(test_vector_1, test_vector_2):
    with pytest.raises(TypeError):
        test_vector_1 / test_vector_2


def test_vector_float_division(test_vector_1):
    assert test_vector_1 / 2.0 == Vector2(0.5, 0.5)


def test_vector_float_division_return_type(test_vector_1):
    assert isinstance((test_vector_1 / 9.0), Vector2)


'''
Vector Equality and Inequality Tests
'''


def test_vector_vector_equality(test_vector_1, test_vector_5):
    assert test_vector_1 == test_vector_1
    assert test_vector_1 == test_vector_5


def test_vector_vector_inequality(test_vector_1, test_vector_2):
    assert test_vector_1 != test_vector_2
    assert not (test_vector_1 == test_vector_2)
    assert not test_vector_1 == 9.0


'''
Vector Dot and Cross Tests
'''


def test_vector_dot_return_type(test_vector_1, test_vector_2):
    assert isinstance(test_vector_1.dot(test_vector_2), float)
    assert isinstance(test_vector_2.dot(test_vector_1), float)


def test_vector_dot_arithmetic(test_vector_1, test_vector_2):
    assert test_vector_1.dot(test_vector_2) == 1.0
    assert test_vector_2.dot(test_vector_1) == 1.0


def test_vector_cross_return_type(test_vector_1, test_vector_2):
    assert isinstance(test_vector_1.cross(test_vector_2), Vector2)
    assert isinstance(test_vector_2.cross(test_vector_1), Vector2)


def test_vector_cross_arithmetic(test_vector_1, test_vector_2):
    assert test_vector_1.cross(test_vector_2) == Vector2(-1.0, 1.0)
    assert test_vector_2.cross(test_vector_1) == Vector2(1.0, -1.0)


'''
Vector Length and Normalise Tests
'''


def test_vector_length_return_type(test_vector_1):
    assert isinstance(test_vector_1.length(), float)


def test_vector_length_arithmetic(test_vector_1):
    assert test_vector_1.length() == math.sqrt(2.0)


def test_vector_normalised_return_type(test_vector_1):
    assert isinstance(test_vector_1.normalise(), Vector2)


def test_vector_normalised_arithmetic(test_vector_1, test_vector_4):
    assert test_vector_1.normalise() == Vector2(1/math.sqrt(2), 1/math.sqrt(2))
    assert test_vector_4.normalise() == test_vector_4


'''
Vector Reverse Tests
'''


def test_reversed_vector_return_type(test_vector_1):
    assert isinstance(test_vector_1, Vector2)


def test_reversed_vector_arithmetic(test_vector_1, test_vector_4):
    assert test_vector_1.reverse() == Vector2(-1.0, -1.0)
    assert test_vector_4.reverse() == test_vector_4
