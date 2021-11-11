import pytest

from two_d.point2 import Point2
from two_d.vector2 import Vector2


'''
Point Addition Tests
'''


def test_point_point_addition_return_type(test_point2_1, test_point2_2):
    assert isinstance(test_point2_1 + test_point2_2, Point2)


def test_point_point_addition_arithmetic(test_point2_1, test_point2_2):
    assert test_point2_1 + test_point2_2 == Point2(2.0, 1.0)


def test_point_vector_addition_return_type(test_point2_1, test_vector2_1):
    assert isinstance(test_point2_1 + test_vector2_1, Point2)


def test_point_vector_addition_arithmetic(test_point2_1, test_vector2_1):
    assert test_point2_1 + test_vector2_1 == Point2(2.0, 2.0)


def test_point_float_addition(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 + 9.0


'''
Point Subtraction Tests
'''


def test_point_point_subtraction_return_type(test_point2_1, test_point2_2):
    assert isinstance(test_point2_1 - test_point2_2, Point2)


def test_point_point_subtraction_arithmetic(test_point2_1, test_point2_2):
    assert test_point2_1 - test_point2_2 == Point2(0.0, 1.0)


def test_point_vector_subtraction_solution_type(test_point2_1, test_vector2_1):
    assert isinstance(test_point2_1 - test_vector2_1, Point2)


def test_point_vector_subtraction_arithmetic(test_point2_1, test_vector2_1):
    assert test_point2_1 - test_vector2_1 == Point2(0.0, 0.0)


def test_point_float_subtraction(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 - 9.0


'''
Point Multiplication Tests
'''


def test_point_point_multiplication(test_point2_1, test_point2_2):
    with pytest.raises(TypeError):
        return test_point2_1 * test_point2_2


def test_point_float_multiplication_return_type(test_point2_1):
    assert isinstance(test_point2_1 * 9.0, Point2)


def test_point_float_multiplication_arithmetic(test_point2_1):
    assert test_point2_1 * 2.0 == Point2(2.0, 2.0)


'''
Point Equality and Inequality Tests
'''


def test_point_to_point_equality(test_point2_1, test_point2_3):
    assert test_point2_1 == test_point2_1
    assert test_point2_1 == test_point2_3


def test_point_to_point_inequality(test_point2_1, test_point2_2):
    assert test_point2_1 != test_point2_2
    assert not (test_point2_1 == test_point2_2)
    assert not test_point2_1 == 9.0


'''
To_Vector Tests
'''


def test_point_to_vector_return_type(test_point2_1):
    assert isinstance(test_point2_1.to_vector(), Vector2)


def test_point_to_vector_arithmetic(test_point2_1):
    assert test_point2_1.to_vector() == Vector2(1.0, 1.0)


'''
Distance_To Tests
'''


def test_distance_to_point_return_type(test_point2_1, test_point2_2):
    assert isinstance(test_point2_1.distance_to(test_point2_2), float)


def test_distance_to_point_arithmetic(test_point2_1, test_point2_2):
    assert test_point2_1.distance_to(test_point2_2) == 1.0
