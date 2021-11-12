import pytest

from three_d.point3 import Point3
from three_d.vector3 import Vector3

from math import sqrt


'''
Point Addition Tests
'''


def test_point3_point3_addition_return_type(test_point3_1, test_point3_2):
    assert isinstance(test_point3_1 + test_point3_2, Point3)


def test_point3_point3_addition_arithmetic(test_point3_1, test_point3_2):
    assert test_point3_1 + test_point3_2 == Point3(2.0, 1.0, 1.0)


def test_point3_vector3_addition_return_type(test_point3_1, test_vector3_1):
    assert isinstance(test_point3_1 + test_vector3_1, Point3)


def test_point3_vector3_addition_arithmetic(test_point3_1, test_vector3_1):
    assert test_point3_1 + test_vector3_1 == Point3(2.0, 2.0, 2.0)


def test_point3_float_addition(test_point3_1):
    with pytest.raises(TypeError):
        return test_point3_1 + 9.0


'''
Point Subtraction Tests
'''


def test_point3_point3_subtraction_return_type(test_point3_1, test_point3_2):
    assert isinstance(test_point3_1 - test_point3_2, Point3)


def test_point3_point3_subtraction_arithmetic(test_point3_1, test_point3_2):
    assert test_point3_1 - test_point3_2 == Point3(0.0, 1.0, 1.0)


def test_point3_vector3_subtraction_solution_type(test_point3_1, test_vector3_1):
    assert isinstance(test_point3_1 - test_vector3_1, Point3)


def test_point3_vector3_subtraction_arithmetic(test_point3_1, test_vector3_1):
    assert test_point3_1 - test_vector3_1 == Point3(0.0, 0.0, 0.0)


def test_point3_float_subtraction(test_point3_1):
    with pytest.raises(TypeError):
        return test_point3_1 - 9.0


'''
Point Multiplication Tests
'''


def test_point3_point3_multiplication(test_point3_1, test_point3_2):
    with pytest.raises(TypeError):
        return test_point3_1 * test_point3_2


def test_point3_float_multiplication_return_type(test_point3_1):
    assert isinstance(test_point3_1 * 9.0, Point3)


def test_point3_float_multiplication_arithmetic(test_point3_1):
    assert test_point3_1 * 2.0 == Point3(2.0, 2.0, 2.0)


'''
Point Equality and Inequality Tests
'''


def test_point3_to_point3_equality(test_point3_1, test_point3_3):
    assert test_point3_1 == test_point3_1
    assert test_point3_1 == test_point3_3


def test_point3_to_matrix4_equality(test_point3_1, test_matrix4_2):
    with pytest.raises(AttributeError):
        return test_point3_1 == test_matrix4_2


def test_point3_to_point3_inequality(test_point3_1, test_point3_2):
    assert test_point3_1 != test_point3_2
    assert not (test_point3_1 == test_point3_2)


def test_point3_to_matrix4_inequality(test_point3_1, test_matrix4_2):
    with pytest.raises(AttributeError):
        return test_point3_1 != test_matrix4_2


'''
Less Than or Equal To Tests
'''


def test_point3_less_than_or_equal_to_point3(test_point3_1, test_point3_2):
    assert test_point3_2 <= test_point3_1


def test_point3_less_than_or_equal_to_edge3(test_point3_1, test_edge3_1):
    with pytest.raises(TypeError):
        return test_point3_1 <= test_edge3_1


'''
Greater Than or Equal To Tests
'''


def test_point3_greater_than_or_equal_to_point3(test_point3_1, test_point3_2):
    assert test_point3_1 >= test_point3_2


def test_point3_greater_than_or_equal_to_edge3(test_point3_1, test_edge3_1):
    with pytest.raises(TypeError):
        return test_point3_1 >= test_edge3_1


'''
To_Vector Tests
'''


def test_point3_to_vector_return_type(test_point3_1):
    assert isinstance(test_point3_1.to_vector(), Vector3)


def test_point3_to_vector_arithmetic(test_point3_1):
    assert test_point3_1.to_vector() == Vector3(1.0, 1.0, 1.0)


'''
Distance_To Tests
'''


def test_distance_to_point3_return_type(test_point3_1, test_point3_2):
    assert isinstance(test_point3_1.distance_to(test_point3_1), float)


def test_distance_to_point3_arithmetic(test_point3_1, test_point3_2):
    assert test_point3_1.distance_to(test_point3_2) == sqrt(2)
