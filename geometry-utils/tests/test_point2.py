import pytest

from two_d.point2 import Point2
from two_d.vector2 import Vector2


@pytest.fixture
def test_point_1():
    return Point2(1.0, 1.0)


@pytest.fixture
def test_point_2():
    return Point2(1.0, 0.0)


@pytest.fixture
def test_point_3():
    return Point2(0.0, 1.0)


@pytest.fixture
def test_point_4():
    return Point2(0.0, 0.0)


@pytest.fixture
def test_point_5():
    return Point2(1.0, 1.0)


@pytest.fixture
def test_vector():
    return Vector2(1.0, 1.0)


'''
Point Addition Tests
'''


def test_point_point_addition_return_type(test_point_1, test_point_2):
    assert isinstance(test_point_1 + test_point_2, Point2)


def test_point_point_addition_arithmetic(test_point_1, test_point_2):
    assert test_point_1 + test_point_2 == Point2(2.0, 1.0)


def test_point_vector_addition_return_type(test_point_1, test_vector):
    assert isinstance(test_point_1 + test_vector, Point2)


def test_point_vector_addition_arithmetic(test_point_1, test_vector):
    assert test_point_1 + test_vector == Point2(2.0, 2.0)


def test_point_float_addition(test_point_1):
    # point should not be able to be added to a float or int
    with pytest.raises(TypeError):
        test_point_1 + 9.0


'''
Point Subtraction Tests
'''


def test_point_point_subtraction_return_type(test_point_1, test_point_2):
    assert isinstance(test_point_1 - test_point_2, Point2)


def test_point_point_subtraction_arithmetic(test_point_1, test_point_2):
    assert test_point_1 - test_point_2 == Point2(0.0, 1.0)


def test_point_vector_subtraction_solution_type(test_point_1, test_vector):
    assert isinstance(test_point_1 - test_vector, Point2)


def test_point_vector_subtraction_arithmetic(test_point_1, test_vector):
    assert test_point_1 - test_vector == Point2(0.0, 0.0)


def test_point_float_subtraction(test_point_1):
    # point should not be able to be subtracted from a float or int
    with pytest.raises(TypeError):
        test_point_1 - 9.0


'''
Point Multiplication Tests
'''


def test_point_point_multiplication(test_point_1, test_point_2):
    with pytest.raises(TypeError):
        test_point_1 * test_point_2


def test_point_float_multiplication_return_type(test_point_1):
    assert isinstance(test_point_1 * 9.0, Point2)


def test_point_float_multiplication_arithmetic(test_point_1):
    assert test_point_1 * 2.0 == Point2(2.0, 2.0)


'''
Point Equality and Inequality Tests
'''


def test_point_to_point_equality(test_point_1, test_point_5):
    assert test_point_1 == test_point_1
    assert test_point_1 == test_point_5


def test_point_to_point_inequality(test_point_1, test_point_2):
    assert test_point_1 != test_point_2
    assert not (test_point_1 == test_point_2)
    assert not test_point_1 == 9.0

'''
To_Vector Tests
'''

def test_point_to_vector_return_type(test_point_1):
    assert isinstance(test_point_1.to_vector(), Vector2)