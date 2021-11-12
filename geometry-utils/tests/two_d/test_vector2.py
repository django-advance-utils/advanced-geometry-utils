import pytest
from math import sqrt

from two_d.vector2 import Vector2

'''
Vector2 Addition Tests
'''


def test_vector2_vector2_addition_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1 + test_vector2_2, Vector2)


def test_vector2_float_addition(test_vector2_1):
    with pytest.raises(TypeError):
        return test_vector2_1 + 9.0


def test_vector2_vector2_addition_arithmetic(test_vector2_1, test_vector2_2):
    assert test_vector2_1 + test_vector2_2 == Vector2(2.0, 1.0)


'''
Vector2 Subtraction Tests
'''


def test_vector2_vector2_subtraction_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1 - test_vector2_2, Vector2)


def test_vector2_float_subtraction(test_vector2_1):
    with pytest.raises(TypeError):
        return test_vector2_1 - 9.0


def test_vector2_vector2_subtraction_arithmetic(test_vector2_1, test_vector2_2):
    assert test_vector2_1 - test_vector2_2 == Vector2(0.0, 1.0)


'''
Vector Multiplication Tests
'''


def test_vector2_vector2_multiplication(test_vector2_1, test_vector2_2):
    with pytest.raises(TypeError):
        return test_vector2_1 * test_vector2_2


def test_vector2_float_multiplication_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1 * 9.0, Vector2)


def test_vector2_float_multiplication_arithmetic(test_vector2_1):
    assert test_vector2_1 * 2.0 == Vector2(2.0, 2.0)


'''
Vector Division Tests
'''


def test_vector2_vector2_division(test_vector2_1, test_vector2_2):
    with pytest.raises(TypeError):
        return test_vector2_1 / test_vector2_2


def test_vector2_float_division(test_vector2_1):
    assert test_vector2_1 / 2.0 == Vector2(0.5, 0.5)


def test_vector2_float_division_return_type(test_vector2_1):
    assert isinstance((test_vector2_1 / 9.0), Vector2)


'''
Vector Equality and Inequality Tests
'''


def test_vector2_vector2_equality(test_vector2_1, test_vector2_3):
    assert test_vector2_1 == test_vector2_1
    assert test_vector2_1 == test_vector2_3


def test_vector2_vector2_inequality(test_vector2_1, test_vector2_2):
    assert test_vector2_1 != test_vector2_2
    assert not (test_vector2_1 == test_vector2_2)
    assert not test_vector2_1 == 9.0


'''
Vector Dot and Cross Tests
'''


def test_vector2_dot_vector2_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1.dot(test_vector2_2), float)
    assert isinstance(test_vector2_2.dot(test_vector2_1), float)


def test_vector2_dot_vector2_arithmetic(test_vector2_1, test_vector2_2):
    assert test_vector2_1.dot(test_vector2_2) == 1.0
    assert test_vector2_2.dot(test_vector2_1) == 1.0


def test_vector2_cross_vector2_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1.cross(test_vector2_2), Vector2)
    assert isinstance(test_vector2_2.cross(test_vector2_1), Vector2)


def test_vector2_cross_vector2_arithmetic(test_vector2_1, test_vector2_2):
    assert test_vector2_1.cross(test_vector2_2) == Vector2(-1.0, 1.0)
    assert test_vector2_2.cross(test_vector2_1) == Vector2(1.0, -1.0)


'''
Vector Length and Normalise Tests
'''


def test_vector2_length_return_type(test_vector2_1):
    assert isinstance(test_vector2_1.length(), float)


def test_vector2_length_arithmetic(test_vector2_1):
    assert test_vector2_1.length() == sqrt(2.0)


def test_vector2_normalised_return_type(test_vector2_1):
    assert isinstance(test_vector2_1.normalise(), Vector2)


def test_vector2_normalised_arithmetic(test_vector2_1, test_vector2_4):
    assert test_vector2_1.normalise() == Vector2(1 / sqrt(2.0), 1 / sqrt(2.0))
    assert test_vector2_4.normalise() == test_vector2_4


'''
Vector Reverse Tests
'''


def test_reversed_vector2_return_type(test_vector2_1):
    assert isinstance(test_vector2_1, Vector2)


def test_reversed_vector2_arithmetic(test_vector2_1, test_vector2_4):
    assert test_vector2_1.reverse() == Vector2(-1.0, -1.0)
    assert test_vector2_4.reverse() == test_vector2_4
