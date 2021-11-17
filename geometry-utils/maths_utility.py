def pi():
    return 3.14159265358


def double_pi():
    return pi() * 2


def double_epsilon():
    return 0.0001


def deg_to_rad():
    return pi() / 180.0


def degrees_to_radians(theta_in_degrees):
    if isinstance(theta_in_degrees, float):
        return theta_in_degrees * deg_to_rad()


def is_float(input_variable):
    return isinstance(input_variable, float)


def is_int(input_variable):
    return isinstance(input_variable, int)


def is_list(input_variable):
    return isinstance(input_variable, list)


def floats_are_close(a, b, rel_tol=1e-9, abs_tol=double_epsilon()):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def is_in_range(value, minimum_value_in_range, maximum_value_in_range):
    return (value >= (minimum_value_in_range - double_epsilon())) and \
           (value <= (maximum_value_in_range + double_epsilon()))


def ranges_overlap(range1_minimum, range1_maximum, range2_minimum, range2_maximum):
    return (is_in_range(range1_minimum, range2_minimum, range2_maximum)) or \
           (is_in_range(range1_maximum, range2_minimum, range2_maximum)) or \
           (is_in_range(range2_minimum, range1_minimum, range1_maximum)) or \
           (is_in_range(range2_maximum, range1_minimum, range1_maximum))
