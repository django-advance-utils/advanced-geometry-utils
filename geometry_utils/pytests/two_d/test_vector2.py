import pytest
from math import sqrt
import geometry_utils.maths_utility as maths_utility
from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.two_d.vector2 import Vector2


def test_vector2_string_parameter():
    with pytest.raises(TypeError):
        return Vector2("0", "0", "0")


def test_edge2_print_string(test_vector2_1):
    assert test_vector2_1.__str__() == "Vector2(x:1.00, y:1.00)"


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


def test_vector2_float_equality(test_vector2_1):
    with pytest.raises(TypeError):
        assert test_vector2_1 == 9.0


def test_vector2_vector2_inequality(test_vector2_1, test_vector2_2):
    assert test_vector2_1 != test_vector2_2
    assert not (test_vector2_1 == test_vector2_2)


def test_vector2_float_inequality(test_vector2_1):
    with pytest.raises(TypeError):
        assert test_vector2_1 != 9.0


'''
Vector Dot and Cross Tests
'''


def test_vector2_dot_vector2_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1.dot(test_vector2_2), float)
    assert isinstance(test_vector2_2.dot(test_vector2_1), float)


def test_vector2_dot_vector2_arithmetic(test_vector2_1, test_vector2_2):
    assert test_vector2_1.dot(test_vector2_2) == 1.0
    assert test_vector2_2.dot(test_vector2_1) == 1.0


def test_vector2_dot_float(test_vector2_1):
    with pytest.raises(TypeError):
        return test_vector2_1.dot(9.0)


def test_vector2_cross_vector2_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1.cross(test_vector2_2), Vector2)
    assert isinstance(test_vector2_2.cross(test_vector2_1), Vector2)


def test_vector2_cross_vector2_arithmetic(test_vector2_1, test_vector2_2):
    assert test_vector2_1.cross(test_vector2_2) == Vector2(-1.0, 1.0)
    assert test_vector2_2.cross(test_vector2_1) == Vector2(1.0, -1.0)


def test_vector2_cross_float(test_vector2_1):
    with pytest.raises(TypeError):
        return test_vector2_1.cross(9.0)


'''
Vector Length and Normalise Tests
'''


def test_vector2_length_return_type(test_vector2_1):
    assert isinstance(test_vector2_1.length(), float)


def test_vector2_length_arithmetic(test_vector2_1):
    assert test_vector2_1.length() == sqrt(2.0)


def test_vector2_normalised_return_type(test_vector2_1):
    assert isinstance(test_vector2_1.normalised(), Vector2)


def test_vector2_normalised_arithmetic(test_vector2_1, test_vector2_4):
    assert test_vector2_1.normalised() == Vector2(1 / sqrt(2.0), 1 / sqrt(2.0))
    assert test_vector2_4.normalised() == test_vector2_4


def test_vector2_normalise(test_vector2_4, test_vector2_5):
    assert test_vector2_4.normalise() == test_vector2_4
    assert test_vector2_5.normalise() == Vector2(0.0, 1.0)


'''
Vector Reverse Tests
'''


def test_vector2_rotate_return_type(test_vector2_1, test_vector2_4):
    assert isinstance(test_vector2_1.rotate(test_vector2_4, maths_utility.HALF_PI), Vector2)


def test_vector2_rotate_arithmetic(test_vector2_2, test_vector2_4):
    rotated_vector = test_vector2_2.rotate(test_vector2_4, maths_utility.HALF_PI)
    assert rotated_vector == Vector2(0.0, 1.0)


def test_vector2_rotate_with_float_origin(test_vector2_2):
    with pytest.raises(TypeError):
        return test_vector2_2.rotate(9.0, maths_utility.HALF_PI)


def test_vector2_rotate_with_vector2_theta(test_vector2_2, test_vector2_4):
    with pytest.raises(TypeError):
        return test_vector2_2.rotate(test_vector2_4, test_vector2_4)


def test_vector2_invert_arithmetic(test_vector2_6):
    assert test_vector2_6.invert() == Vector2(-1.0, 0.0)


def test_vector2_inverted_return_type(test_vector2_2):
    assert isinstance(test_vector2_2.inverted(), Vector2)


def test_vector2_inverted_arithmetic(test_vector2_2):
    assert test_vector2_2.inverted() == Vector2(-1.0, 0.0)


def test_vector2_get_perpendicular_return_type(test_vector2_2):
    assert isinstance(test_vector2_2.get_perpendicular(), Vector2)


def test_vector2_get_perpendicular_arithmetic(test_vector2_1):
    assert test_vector2_1.get_perpendicular() == Vector2(-1.0, 1.0)


def test_vector2_angle_to_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1.angle_to(test_vector2_2), float)


def test_vector2_angle_to_arithmetic(test_vector2_2, test_vector2_5):
    assert test_vector2_2.angle_to(test_vector2_5) == 90.0
    assert test_vector2_2.angle_to(test_vector2_2) == 0.0


def test_vector2_signed_angle_to_return_type(test_vector2_1, test_vector2_2):
    assert isinstance(test_vector2_1.signed_angle_to(test_vector2_2), float)


def test_vector2_signed_angle_to_arithmetic(test_vector2_2, test_vector2_5):
    assert test_vector2_2.signed_angle_to(test_vector2_5) == 90.0


def test_vector2_angle_to_x_axis_return_type(test_vector2_1):
    assert isinstance(test_vector2_1.angle_to_x_axis(), float)


def test_vector2_angle_to_x_axis_arithmetic(test_vector2_2, test_vector2_5):
    assert test_vector2_2.angle_to_x_axis() == 0.0
    assert test_vector2_5.angle_to_x_axis() == 90.0


def test_vector2_from_comma_string(test_2d_string):
    assert Vector2.from_comma_string(test_2d_string) == Vector2(1.0, 2.0)


def test_vector2_to_vector3(test_vector2_2):
    assert test_vector2_2.to_vector3() == Vector3(1.0, 0.0, 0.0)


def test_vector2_accuracy_fix():
    low_accuracy_vector = Vector2(0.0000003, 0.0000005)
    low_accuracy_vector.accuracy_fix()
    assert low_accuracy_vector == Vector2(0.0, 0.0)


def test_vector2_vector2_equal(test_vector2_1, test_vector2_3):
    assert test_vector2_1.equal(test_vector2_3)
