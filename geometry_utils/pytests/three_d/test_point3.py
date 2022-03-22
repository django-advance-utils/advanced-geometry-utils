import pytest

from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3

from math import sqrt

from geometry_utils.two_d.point2 import Point2

'''
Point Addition Tests
'''


def test_point3_point3_addition(test_point3_1, test_point3_2):
    with pytest.raises(TypeError):
        return test_point3_1 + test_point3_2


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
    assert isinstance(test_point3_1 - test_point3_2, Vector3)


def test_point3_point3_subtraction_arithmetic(test_point3_1, test_point3_2):
    assert test_point3_1 - test_point3_2 == Vector3(0.0, 1.0, 1.0)


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


'''
Point Equality and Inequality Tests
'''


def test_point3_to_point3_equality(test_point3_1, test_point3_3):
    assert test_point3_1 == test_point3_1
    assert test_point3_1 == test_point3_3


def test_point3_to_matrix4_equality(test_point3_1, test_matrix4_2):
    with pytest.raises(TypeError):
        return test_point3_1 == test_matrix4_2


def test_point3_to_point3_inequality(test_point3_1, test_point3_2):
    assert test_point3_1 != test_point3_2
    assert not (test_point3_1 == test_point3_2)


def test_point3_to_matrix4_inequality(test_point3_1, test_matrix4_2):
    with pytest.raises(TypeError):
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
Less Than Tests
'''


def test_point3_less_than_point3(test_point3_1, test_point3_4):
    assert test_point3_4 < test_point3_1


def test_point2_less_than_float(test_point3_1):
    with pytest.raises(TypeError):
        return test_point3_1 < 9.0


'''
Greater Than Tests
'''


def test_point3_greater_than_point3(test_point3_1, test_point3_4):
    assert test_point3_1 > test_point3_4


def test_point3_greater_than_float(test_point3_1):
    with pytest.raises(TypeError):
        return test_point3_1 > 9.0


'''
To_Vector Tests
'''


def test_point3_to_vector_return_type(test_point3_1):
    assert isinstance(test_point3_1.to_vector3(), Vector3)


def test_point3_to_vector_arithmetic(test_point3_1):
    assert test_point3_1.to_vector3() == Vector3(1.0, 1.0, 1.0)


'''
Distance_To Tests
'''


def test_point3_distance_to_point3_return_type(test_point3_1, test_point3_2):
    assert isinstance(test_point3_1.distance_to(test_point3_1), float)


def test_point3_distance_to_point3_arithmetic(test_point3_1, test_point3_2):
    assert test_point3_1.distance_to(test_point3_2) == sqrt(2)


def test_point3_distance_to_float(test_point3_1):
    with pytest.raises(TypeError):
        return test_point3_1.distance_to(9.0)


def test_point3_mirror_x():
    assert Point3(1.0, 1.0, 1.0).mirror_x() == Point3(1.0, -1.0, -1.0)


def test_point3_mirror_y():
    assert Point3(1.0, 1.0, 1.0).mirror_y() == Point3(-1.0, 1.0, -1.0)


def test_point3_mirror_z():
    assert Point3(1.0, 1.0, 1.0).mirror_z() == Point3(-1.0, -1.0, 1.0)


def test_point3_mirror_origin():
    assert Point3(1.0, 1.0, 1.0).mirror_origin() == Point3(-1.0, -1.0, -1.0)


def test_point3_mirrored_origin():
    assert Point3(1.0, 1.0, 1.0).mirrored_origin() == Point3(-1.0, -1.0, -1.0)


def test_point3_to_point2(test_point3_2):
    assert test_point3_2.to_point2() == Point2(1.0, 0.0)


def test_point3_point3_equal(test_vector3_1, test_vector3_3):
    assert test_vector3_1.equal(test_vector3_3)


def test_point2_accuracy_fix():
    low_accuracy_point = Point3(0.0000003, 0.0000005, 0.0000007)
    low_accuracy_point.accuracy_fix()
    assert low_accuracy_point == Point3(0.0, 0.0, 0.0)
