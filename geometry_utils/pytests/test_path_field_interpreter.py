import pytest

from geometry_utils.path_field_interpreter import PathFieldInterpreter


def test_path_field(path2_1):
    test_path_field_interpreter = PathFieldInterpreter()
    test_path_field_interpreter.add_path(path2_1)
