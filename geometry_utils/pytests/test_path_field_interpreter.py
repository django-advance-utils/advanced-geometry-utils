import pytest

from geometry_utils.path_field_interpreter import PathFieldInterpreter
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.path2 import Path2
from geometry_utils.two_d.point2 import Point2


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
    assert path[0] == path2_1


def test_path_field_load_path_curved_head(path2_8):
    test_path_field_interpreter = PathFieldInterpreter()
    path = test_path_field_interpreter.load_path(';1;:1;0)0.5;#')
    assert path[0] == path2_8


def test_path_field_load_path_circle(path2_6):
    test_path_field_interpreter = PathFieldInterpreter()
    path = test_path_field_interpreter.load_path('1:1)1')
    assert path[0] == path2_6


def test_old_1a_in(path2_9):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_9)
    assert result == ':950;1000'


def test_old_1a_out(path2_9):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.load_path(':950;1000')
    assert result[0] == path2_9


def test_old_1b_in(path2_10):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_10)
    assert result == 'Path1@:950;1000'


def test_old_1b_out(path2_10):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.load_path('Path1@:950;1000')
    assert result[0] == path2_10


def test_old_1c_in(path2_11):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_11)
    assert result == ':950,P1;1000,P2'


def test_old_1c_out(path2_11):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.load_path(':950,P1;1000,P2')
    assert result[0] == path2_11


def test_old_1d_in(path2_12):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_12)
    assert result == ':950;1000,,E1'


def test_old_1d_out(path2_12):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.load_path(':950;1000,,E1')
    assert result[0] == path2_12


def test_old_1e_in(path2_13):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_13)
    assert result == ':950;1000,,%Bold'


def test_old_1e_out(path2_13):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.load_path(':950;1000,,%Bold')
    assert result[0] == path2_13


def test_old_1f_in(path2_14):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_14)
    assert result == ':950,P1;1000,P2,%Bold'


def test_old_1f_out(path2_14):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.load_path(':950,P1;1000,P2,%Bold')
    assert result[0] == path2_14


def test_old_1g_in(path2_15):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_15)
    assert result == ':950,P1;1000,P2,E1%Bold'


def test_old_1g_out(path2_15):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.load_path(':950,P1;1000,P2,E1%Bold')
    assert result[0] == path2_15


def test_old_1h_in(path2_16):
    test_path_field_interpreter = PathFieldInterpreter()
    result = test_path_field_interpreter.add_path(path2_16)
    assert result == ':950;1000'
