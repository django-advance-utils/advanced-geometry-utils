import pytest
from math import sqrt

from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.two_d.vector2 import Vector2


def test_vector3_string_parameter():
    with pytest.raises(TypeError):
        return Vector3("0", "0", "0")


def test_vector3_print_string(test_vector3_1):
    assert test_vector3_1.__str__() == "Vector3(x:1.00, y:1.00, z:1.00)"

'''
Vector Addition Tests
'''


def test_vector3_vector3_addition_return_type(test_vector3_1, test_vector3_2):
    assert isinstance(test_vector3_1 + test_vector3_2, Vector3)


def test_vector3_float_addition(test_vector3_1):
    with pytest.raises(TypeError):
        return test_vector3_1 + 9.0


def test_vector3_vector3_addition_arithmetic(test_vector3_1, test_vector3_2):
    assert test_vector3_1 + test_vector3_2 == Vector3(2.0, 1.0, 1.0)


'''
Vector Subtraction Tests
'''


def test_vector3_vector3_subtraction_return_type(test_vector3_1, test_vector3_2):
    assert isinstance(test_vector3_1 - test_vector3_2, Vector3)


def test_vector3_float_subtraction(test_vector3_1):
    with pytest.raises(TypeError):
        return test_vector3_1 - 9.0


def test_vector3_vector3_subtraction_arithmetic(test_vector3_1, test_vector3_2):
    assert test_vector3_1 - test_vector3_2 == Vector3(0.0, 1.0, 1.0)


'''
Vector Multiplication Tests
'''


def test_vector3_vector3_multiplication(test_vector3_1, test_vector3_2):
    with pytest.raises(TypeError):
        return test_vector3_1 * test_vector3_2


def test_vector3_float_multiplication_return_type(test_vector3_1, test_vector3_2):
    assert isinstance(test_vector3_1 * 9.0, Vector3)


def test_vector_float_multiplication_arithmetic(test_vector3_1):
    assert test_vector3_1 * 2.0 == Vector3(2.0, 2.0, 2.0)


'''
Vector Division Tests
'''


def test_vector3_vector3_division(test_vector3_1, test_vector3_2):
    with pytest.raises(TypeError):
        return test_vector3_1 / test_vector3_2


def test_vector3_float_division(test_vector3_1):
    assert test_vector3_1 / 2.0 == Vector3(0.5, 0.5, 0.5)


def test_vector3_float_division_return_type(test_vector3_1):
    assert isinstance((test_vector3_1 / 9.0), Vector3)


'''
Vector Equality and Inequality Tests
'''


def test_vector3_vector3_equality(test_vector3_1, test_vector3_3):
    assert test_vector3_1 == test_vector3_1
    assert test_vector3_1 == test_vector3_3


def test_vector3_float_equality(test_vector3_1):
    with pytest.raises(TypeError):
        assert test_vector3_1 == 9.0


def test_vector3_vector3_inequality(test_vector3_1, test_vector3_2):
    assert test_vector3_1 != test_vector3_2
    assert not (test_vector3_1 == test_vector3_2)


def test_vector3_float_inequality(test_vector3_1):
    with pytest.raises(TypeError):
        assert test_vector3_1 != 9.0


'''
Vector Dot and Cross Tests
'''


def test_vector3_dot_vector3_return_type(test_vector3_1, test_vector3_2):
    assert isinstance(test_vector3_1.dot(test_vector3_2), float)
    assert isinstance(test_vector3_2.dot(test_vector3_1), float)


def test_vector3_dot_vector3_arithmetic(test_vector3_1, test_vector3_2):
    assert test_vector3_1.dot(test_vector3_2) == 1.0
    assert test_vector3_2.dot(test_vector3_1) == 1.0


def test_vector3_dot_float(test_vector3_1):
    with pytest.raises(TypeError):
        return test_vector3_1.dot(9.0)


def test_vector3_cross_vector3_return_type(test_vector3_1, test_vector3_2):
    assert isinstance(test_vector3_1.cross(test_vector3_2), Vector3)
    assert isinstance(test_vector3_2.cross(test_vector3_1), Vector3)


def test_vector3_cross_vector3_arithmetic(test_vector3_1, test_vector3_2):
    assert test_vector3_1.cross(test_vector3_2) == Vector3(0.0, 1.0, -1.0)
    assert test_vector3_2.cross(test_vector3_1) == Vector3(0.0, -1.0, 1.0)


def test_vector3_cross_float(test_vector3_1):
    with pytest.raises(TypeError):
        return test_vector3_1.cross(9.0)


'''
Vector Length and Normalise Tests
'''


def test_vector3_length_return_type(test_vector3_1):
    assert isinstance(test_vector3_1.length(), float)


def test_vector3_length_arithmetic(test_vector3_1):
    assert test_vector3_1.length() == sqrt(3.0)


def test_vector3_normalised_return_type(test_vector3_1):
    assert isinstance(test_vector3_1.normalised(), Vector3)


def test_vector3_normalised_arithmetic(test_vector3_1, test_vector3_4):
    assert test_vector3_1.normalised() == Vector3(1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3))
    assert test_vector3_4.normalised() == test_vector3_4


def test_vector3_normalise(test_vector3_4, test_vector3_5):
    assert test_vector3_4.normalise() == test_vector3_4
    assert test_vector3_5.normalise() == Vector3(0.0, 1.0, 0.0)


'''
Vector Reverse Tests
'''


def test_inverted_vector3_return_type(test_vector3_1):
    assert isinstance(test_vector3_1.inverted(), Vector3)


def test_inverted_vector3_arithmetic(test_vector3_1, test_vector3_4):
    assert test_vector3_1.inverted() == Vector3(-1.0, -1.0, -1.0)
    assert test_vector3_4.inverted() == test_vector3_4


def test_invert_vector3_arithmetic():
    assert Vector3(1.0, 1.0, 1.0) == Vector3(-1.0, -1.0, -1.0)


def test_vector3_get_perpendicular_arithmetic(test_vector3_2, test_vector3_4, test_vector3_5):
    assert test_vector3_2.get_perpendicular(test_vector3_4, test_vector3_5) == (Vector3(0, 0, 1), Vector3(0, -1, 0))


def test_vector3_from_comma_string(test_3d_string):
    assert Vector3.from_comma_string(test_3d_string) == Vector3(1.0, 2.0, 3.0)


def test_vector3_angle_to_return_type(test_vector3_1, test_vector3_2):
    assert isinstance(test_vector3_1.angle_to(test_vector3_2), float)


def test_vector3_angle_to_arithmetic(test_vector3_2, test_vector3_5):
    assert test_vector3_2.angle_to(test_vector3_5) == 90.0
    assert test_vector3_2.angle_to(test_vector3_2) == 0.0


def test_vector3_signed_angle_to_return_type(test_vector3_1, test_vector3_2):
    assert isinstance(test_vector3_1.signed_angle_to(test_vector3_2), float)


def test_vector3_signed_angle_to_arithmetic(test_vector3_2, test_vector3_5):
    assert test_vector3_2.signed_angle_to(test_vector3_5) == 90.0


def test_vector3_invert_arithmetic(test_vector3_6):
    assert test_vector3_6.invert() == Vector3(-1.0, 0.0, 0.0)


def test_vector3_inverted_return_type(test_vector3_2):
    assert isinstance(test_vector3_2.inverted(), Vector3)


def test_vector3_inverted_arithmetic(test_vector3_2):
    assert test_vector3_2.inverted() == Vector3(-1.0, 0.0, 0.0)


def test_vector3_to_vector2(test_vector3_2):
    assert test_vector3_2.to_vector2() == Vector2(1.0, 0.0)


def test_vector3_accuracy_fix():
    low_accuracy_vector = Vector3(0.0000003, 0.0000005, 0.0000007)
    low_accuracy_vector.accuracy_fix()
    assert low_accuracy_vector == Vector3(0.0, 0.0, 0.0)


def test_vector3_vector3_equal(test_vector3_1, test_vector3_3):
    assert test_vector3_1.equal(test_vector3_3)

