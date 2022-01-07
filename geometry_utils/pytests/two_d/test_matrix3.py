import pytest

from geometry_utils.two_d.matrix3 import Matrix3
from geometry_utils.two_d.vector2 import Vector2
from geometry_utils.two_d.point2 import Point2


def test_matrix3_string_parameter():
    with pytest.raises(TypeError):
        return Matrix3("0")


def test_matrix3_length_of_vals():
    with pytest.raises(AttributeError):
        return Matrix3([9.0])


def test_matrix3_vals_string_parameter():
    with pytest.raises(TypeError):
        return Matrix3([["1.0", 1.0, 1.0],
                        [1.0, "1.0", 1.0],
                        [1.0, 1.0, 1.0]])


def test_matrix3_print_string(test_matrix3_1):
    assert test_matrix3_1.__str__() == "Matrix3(vals:[1, 0, 0]\n\t\t\t[0, 1, 0]\n\t\t\t[0, 0, 1])"


def test_matrix3_matrix3_equality(test_matrix3_1):
    assert test_matrix3_1 == Matrix3()


def test_matrix3_float_equality(test_matrix3_1):
    with pytest.raises(TypeError):
        assert test_matrix3_1 == 9.0


def test_matrix3_matrix3_multiplication_arithmetic(test_matrix3_1, test_matrix3_2):
    assert test_matrix3_1 * test_matrix3_2 == test_matrix3_2


def test_matrix3_matrix3_multiplication_return_type(test_matrix3_1, test_matrix3_2):
    assert isinstance(test_matrix3_1 * test_matrix3_2, Matrix3)


def test_matrix3_vector2_multiplication_return_type(test_matrix3_1, test_vector2_1):
    assert isinstance(test_matrix3_1 * test_vector2_1, Vector2)


def test_matrix3_vector2_multiplication_arithmetic(test_matrix3_1, test_vector2_1):
    assert test_matrix3_1 * test_vector2_1 == test_vector2_1


def test_matrix3_point2_multiplication_return_type(test_matrix3_1, test_point2_1):
    assert isinstance(test_matrix3_1 * test_point2_1, Point2)


def test_matrix3_point2_multiplication_arithmetic(test_matrix3_1, test_point2_1):
    assert test_matrix3_1 * test_point2_1 == test_point2_1


def test_matrix3_float_multiplication_return_type(test_matrix3_1):
    assert isinstance(test_matrix3_1 * 9.0, Matrix3)


def test_matrix3_float_multiplication_arithmetic(test_matrix3_1):
    assert test_matrix3_1 * 1.0 == test_matrix3_1


def test_matrix3_string_multiplication(test_matrix3_1):
    with pytest.raises(TypeError):
        return test_matrix3_1 * "9.0"


def test_matrix3_translation_by_vector2_return_type(test_vector2_1):
    assert isinstance(Matrix3.translation(test_vector2_1), Matrix3)


def test_matrix3_translation_by_vector2_arithmetic(test_vector2_1):
    test_translation_matrix = Matrix3.translation(test_vector2_1)
    assert test_translation_matrix == Matrix3([[1.0, 0.0, 1.0],
                                               [0.0, 1.0, 1.0],
                                               [0.0, 0.0, 1.0]])


def test_matrix3_translation_by_float(test_vector2_1):
    with pytest.raises(TypeError):
        return Matrix3.translation(9.0)


def test_matrix3_rotation_by_float_return_type():
    test_rotation_matrix = Matrix3.rotation(0.0)
    assert isinstance(test_rotation_matrix, Matrix3)


def test_matrix3_rotation_by_float_arithmetic():
    test_rotation_matrix = Matrix3.rotation(0.0)
    assert test_rotation_matrix == Matrix3()


def test_matrix3_rotation_by_vector(test_vector2_1):
    with pytest.raises(TypeError):
        return Matrix3.rotation(test_vector2_1)


def test_matrix3_rotation():
    test_rotation_matrix = Matrix3.rotation(0.0)
    assert test_rotation_matrix == Matrix3([[1.0, 0.0, 0.0],
                                            [0.0, 1.0, 0.0],
                                            [0.0, 0.0, 1.0]])
