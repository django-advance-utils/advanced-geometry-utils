import pytest

from geometry_utils.path_field_interpreter import PathFieldInterpreter


def test_path_field_add_field_closed_line(path2_1):
    test_path_field_interpreter = PathFieldInterpreter()
    path_str = test_path_field_interpreter.add_path(path2_1)
    assert path_str == ';1:1;2:2;#'


def test_path_field_add_field_curved_head(path2_8):
    test_path_field_interpreter = PathFieldInterpreter()
    path_str = test_path_field_interpreter.add_path(path2_8)
    assert path_str == ';1;:1;0)0.5;#'


def test_path_field_add_field_circle(path2_6):
    test_path_field_interpreter = PathFieldInterpreter()
    path_str = test_path_field_interpreter.add_path(path2_6)
    assert path_str == '1:1)1'


def test_path_field_load_path_closed_line(path2_1):
    test_path_field_interpreter = PathFieldInterpreter()
    path = test_path_field_interpreter.load_path(';1:1;2:2;#')
    assert path == path2_1


def test_path_field_load_path_curved_head(path2_8):
    test_path_field_interpreter = PathFieldInterpreter()
    path = test_path_field_interpreter.load_path(';1;:1;0)0.5;#')
    assert path == path2_8


def test_path_field_load_path_circle(path2_6):
    test_path_field_interpreter = PathFieldInterpreter()
    path = test_path_field_interpreter.load_path('1:1)1')
    assert path == path2_6
