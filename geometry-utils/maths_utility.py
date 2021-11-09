def double_epsilon():
    return 0.0001


def floats_are_close(a, b, rel_tol=1e-9, abs_tol=0.0005):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def is_in_range(value, minimum_value_in_range, maximum_value_in_range):
    return (value >= (minimum_value_in_range - double_epsilon())) and \
           (value <= (maximum_value_in_range + double_epsilon()))


def ranges_overlap(range1_minimum, range1_maximum, range2_minimum, range2_maximum):
    return (is_in_range(range1_minimum, range2_minimum, range2_maximum)) or \
           (is_in_range(range1_maximum, range2_minimum, range2_maximum)) or \
           (is_in_range(range2_minimum, range1_minimum, range1_maximum)) or \
           (is_in_range(range2_maximum, range1_minimum, range1_maximum))
