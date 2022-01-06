import pytest

from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2

'''
Point2 Initialisation
'''


def test_point2_with_string_inputs():
    with pytest.raises(TypeError):
        return Point2("0", "0", "0")


def test_point2_print_string(test_point2_1):
    assert test_point2_1.__str__() == "Point2(x:1.00, y:1.00)"


'''
Point2 Addition Tests
'''


def test_point2_point2_addition_return_type(test_point2_1, test_point2_2):
    with pytest.raises(TypeError):
        return test_point2_1 + test_point2_2


def test_point2_vector2_addition_return_type(test_point2_1, test_vector2_1):
    assert isinstance(test_point2_1 + test_vector2_1, Point2)


def test_point2_vector2_addition_arithmetic(test_point2_1, test_vector2_1):
    assert test_point2_1 + test_vector2_1 == Point2(2.0, 2.0)


def test_point2_float_addition(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 + 9.0


'''
Point2 Subtraction Tests
'''


def test_point2_point2_subtraction_return_type(test_point2_1, test_point2_2):
    assert isinstance(test_point2_1 - test_point2_2, Vector2)


def test_point2_point2_subtraction_arithmetic(test_point2_1, test_point2_2):
    assert test_point2_1 - test_point2_2 == Vector2(0.0, 1.0)


def test_point2_vector2_subtraction_solution_type(test_point2_1, test_vector2_1):
    assert isinstance(test_point2_1 - test_vector2_1, Point2)


def test_point2_vector2_subtraction_arithmetic(test_point2_1, test_vector2_1):
    assert test_point2_1 - test_vector2_1 == Point2(0.0, 0.0)


def test_point2_float_subtraction(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 - 9.0


'''
Point2 Equality and Inequality Tests
'''


def test_point2_to_point2_equality(test_point2_1, test_point2_3):
    assert test_point2_1 == test_point2_1
    assert test_point2_1 == test_point2_3


def test_point2_to_float_equality(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 == 9.0


def test_point2_to_point2_inequality(test_point2_1, test_point2_2):
    assert test_point2_1 != test_point2_2
    assert not (test_point2_1 == test_point2_2)


def test_point2_to_float_inequality(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 != 9.0


'''
Less Than or Equal To Tests
'''


def test_point2_less_than_or_equal_to_point2(test_point2_1, test_point2_2):
    assert test_point2_2 <= test_point2_1


def test_point2_less_than_or_equal_to_float(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 <= 9.0


'''
Greater Than or Equal To Tests
'''


def test_point2_greater_than_or_equal_to_point2(test_point2_1, test_point2_2):
    assert test_point2_1 >= test_point2_2


def test_point2_greater_than_or_equal_to_float(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 >= 9.0


'''
Less Than Tests
'''


def test_point2_less_than_point2(test_point2_1, test_point2_4):
    assert test_point2_4 < test_point2_1


def test_point2_less_than_float(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 < 9.0


'''
Greater Than Tests
'''


def test_point2_greater_than_point2(test_point2_1, test_point2_4):
    assert test_point2_1 > test_point2_4


def test_point2_greater_than_float(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1 > 9.0


'''
To_Vector Tests
'''


def test_point2_to_vector_return_type(test_point2_1):
    assert isinstance(test_point2_1.to_vector2(), Vector2)


def test_point2_to_vector_arithmetic(test_point2_1):
    assert test_point2_1.to_vector2() == Vector2(1.0, 1.0)


'''
Distance_To Tests
'''


def test_point2_distance_to_point2_return_type(test_point2_1, test_point2_2):
    assert isinstance(test_point2_1.distance_to(test_point2_2), float)


def test_point2_distance_to_point2_arithmetic(test_point2_1, test_point2_2):
    assert test_point2_1.distance_to(test_point2_2) == 1.0


def test_point2_distance_to_float(test_point2_1):
    with pytest.raises(TypeError):
        return test_point2_1.distance_to(9.0)


def test_point2_mirror_y():
    assert Point2(1.0, 1.0).mirror_y() == Point2(-1.0, 1.0)
