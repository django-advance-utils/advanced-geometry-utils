import math

PI = float(3.141592653589793238)

QUARTER_PI = float(PI * 1/4)
HALF_PI = float(PI * 1/2)
ONE_AND_HALF_PI = float(PI * 3/2)
TWO_PI = float(PI * 2)

DEG_TO_RAD = PI / 180.0
RAD_TO_DEG = 180.0 / PI

CIRCLE_DIVISIONS = 512

CIRCLE_FACTORS = [[1.000000, 0.000000],
                  [0.999925, 0.012272],
                  [0.999699, 0.024541],
                  [0.999322, 0.036807],
                  [0.998795, 0.049068],
                  [0.998118, 0.061321],
                  [0.997290, 0.073565],
                  [0.996313, 0.085797],
                  [0.995185, 0.098017],
                  [0.993907, 0.110222],
                  [0.992480, 0.122411],
                  [0.990903, 0.134581],
                  [0.989177, 0.146730],
                  [0.987301, 0.158858],
                  [0.985278, 0.170962],
                  [0.983105, 0.183040],
                  [0.980785, 0.195090],
                  [0.978317, 0.207111],
                  [0.975702, 0.219101],
                  [0.972940, 0.231058],
                  [0.970031, 0.242980],
                  [0.966976, 0.254866],
                  [0.963776, 0.266713],
                  [0.960431, 0.278520],
                  [0.956940, 0.290285],
                  [0.953306, 0.302006],
                  [0.949528, 0.313682],
                  [0.945607, 0.325310],
                  [0.941544, 0.336890],
                  [0.937339, 0.348419],
                  [0.932993, 0.359895],
                  [0.928506, 0.371317],
                  [0.923880, 0.382683],
                  [0.919114, 0.393992],
                  [0.914210, 0.405241],
                  [0.909168, 0.416430],
                  [0.903989, 0.427555],
                  [0.898674, 0.438616],
                  [0.893224, 0.449611],
                  [0.887640, 0.460539],
                  [0.881921, 0.471397],
                  [0.876070, 0.482184],
                  [0.870087, 0.492898],
                  [0.863973, 0.503538],
                  [0.857729, 0.514103],
                  [0.851355, 0.524590],
                  [0.844854, 0.534998],
                  [0.838225, 0.545325],
                  [0.831470, 0.555570],
                  [0.824589, 0.565732],
                  [0.817585, 0.575808],
                  [0.810457, 0.585798],
                  [0.803208, 0.595699],
                  [0.795837, 0.605511],
                  [0.788346, 0.615232],
                  [0.780737, 0.624859],
                  [0.773010, 0.634393],
                  [0.765167, 0.643832],
                  [0.757209, 0.653173],
                  [0.749136, 0.662416],
                  [0.740951, 0.671559],
                  [0.732654, 0.680601],
                  [0.724247, 0.689541],
                  [0.715731, 0.698376],
                  [0.707107, 0.707107],
                  [0.698376, 0.715731],
                  [0.689541, 0.724247],
                  [0.680601, 0.732654],
                  [0.671559, 0.740951],
                  [0.662416, 0.749136],
                  [0.653173, 0.757209],
                  [0.643832, 0.765167],
                  [0.634393, 0.773010],
                  [0.624859, 0.780737],
                  [0.615232, 0.788346],
                  [0.605511, 0.795837],
                  [0.595699, 0.803208],
                  [0.585798, 0.810457],
                  [0.575808, 0.817585],
                  [0.565732, 0.824589],
                  [0.555570, 0.831470],
                  [0.545325, 0.838225],
                  [0.534998, 0.844854],
                  [0.524590, 0.851355],
                  [0.514103, 0.857729],
                  [0.503538, 0.863973],
                  [0.492898, 0.870087],
                  [0.482184, 0.876070],
                  [0.471397, 0.881921],
                  [0.460539, 0.887640],
                  [0.449611, 0.893224],
                  [0.438616, 0.898674],
                  [0.427555, 0.903989],
                  [0.416430, 0.909168],
                  [0.405241, 0.914210],
                  [0.393992, 0.919114],
                  [0.382683, 0.923880],
                  [0.371317, 0.928506],
                  [0.359895, 0.932993],
                  [0.348419, 0.937339],
                  [0.336890, 0.941544],
                  [0.325310, 0.945607],
                  [0.313682, 0.949528],
                  [0.302006, 0.953306],
                  [0.290285, 0.956940],
                  [0.278520, 0.960431],
                  [0.266713, 0.963776],
                  [0.254866, 0.966976],
                  [0.242980, 0.970031],
                  [0.231058, 0.972940],
                  [0.219101, 0.975702],
                  [0.207111, 0.978317],
                  [0.195090, 0.980785],
                  [0.183040, 0.983105],
                  [0.170962, 0.985278],
                  [0.158858, 0.987301],
                  [0.146730, 0.989177],
                  [0.134581, 0.990903],
                  [0.122411, 0.992480],
                  [0.110222, 0.993907],
                  [0.098017, 0.995185],
                  [0.085797, 0.996313],
                  [0.073565, 0.997290],
                  [0.061321, 0.998118],
                  [0.049068, 0.998795],
                  [0.036807, 0.999322],
                  [0.024541, 0.999699],
                  [0.012272, 0.999925],
                  [0.000000, 1.000000],
                  [-0.012272, 0.999925],
                  [-0.024541, 0.999699],
                  [-0.036807, 0.999322],
                  [-0.049068, 0.998795],
                  [-0.061321, 0.998118],
                  [-0.073565, 0.997290],
                  [-0.085797, 0.996313],
                  [-0.098017, 0.995185],
                  [-0.110222, 0.993907],
                  [-0.122411, 0.992480],
                  [-0.134581, 0.990903],
                  [-0.146730, 0.989177],
                  [-0.158858, 0.987301],
                  [-0.170962, 0.985278],
                  [-0.183040, 0.983105],
                  [-0.195090, 0.980785],
                  [-0.207111, 0.978317],
                  [-0.219101, 0.975702],
                  [-0.231058, 0.972940],
                  [-0.242980, 0.970031],
                  [-0.254866, 0.966976],
                  [-0.266713, 0.963776],
                  [-0.278520, 0.960431],
                  [-0.290285, 0.956940],
                  [-0.302006, 0.953306],
                  [-0.313682, 0.949528],
                  [-0.325310, 0.945607],
                  [-0.336890, 0.941544],
                  [-0.348419, 0.937339],
                  [-0.359895, 0.932993],
                  [-0.371317, 0.928506],
                  [-0.382683, 0.923880],
                  [-0.393992, 0.919114],
                  [-0.405241, 0.914210],
                  [-0.416430, 0.909168],
                  [-0.427555, 0.903989],
                  [-0.438616, 0.898674],
                  [-0.449611, 0.893224],
                  [-0.460539, 0.887640],
                  [-0.471397, 0.881921],
                  [-0.482184, 0.876070],
                  [-0.492898, 0.870087],
                  [-0.503538, 0.863973],
                  [-0.514103, 0.857729],
                  [-0.524590, 0.851355],
                  [-0.534998, 0.844854],
                  [-0.545325, 0.838225],
                  [-0.555570, 0.831470],
                  [-0.565732, 0.824589],
                  [-0.575808, 0.817585],
                  [-0.585798, 0.810457],
                  [-0.595699, 0.803208],
                  [-0.605511, 0.795837],
                  [-0.615232, 0.788346],
                  [-0.624859, 0.780737],
                  [-0.634393, 0.773010],
                  [-0.643832, 0.765167],
                  [-0.653173, 0.757209],
                  [-0.662416, 0.749136],
                  [-0.671559, 0.740951],
                  [-0.680601, 0.732654],
                  [-0.689541, 0.724247],
                  [-0.698376, 0.715731],
                  [-0.707107, 0.707107],
                  [-0.715731, 0.698376],
                  [-0.724247, 0.689541],
                  [-0.732654, 0.680601],
                  [-0.740951, 0.671559],
                  [-0.749136, 0.662416],
                  [-0.757209, 0.653173],
                  [-0.765167, 0.643832],
                  [-0.773010, 0.634393],
                  [-0.780737, 0.624859],
                  [-0.788346, 0.615232],
                  [-0.795837, 0.605511],
                  [-0.803208, 0.595699],
                  [-0.810457, 0.585798],
                  [-0.817585, 0.575808],
                  [-0.824589, 0.565732],
                  [-0.831470, 0.555570],
                  [-0.838225, 0.545325],
                  [-0.844854, 0.534998],
                  [-0.851355, 0.524590],
                  [-0.857729, 0.514103],
                  [-0.863973, 0.503538],
                  [-0.870087, 0.492898],
                  [-0.876070, 0.482184],
                  [-0.881921, 0.471397],
                  [-0.887640, 0.460539],
                  [-0.893224, 0.449611],
                  [-0.898674, 0.438616],
                  [-0.903989, 0.427555],
                  [-0.909168, 0.416430],
                  [-0.914210, 0.405241],
                  [-0.919114, 0.393992],
                  [-0.923880, 0.382683],
                  [-0.928506, 0.371317],
                  [-0.932993, 0.359895],
                  [-0.937339, 0.348419],
                  [-0.941544, 0.336890],
                  [-0.945607, 0.325310],
                  [-0.949528, 0.313682],
                  [-0.953306, 0.302006],
                  [-0.956940, 0.290285],
                  [-0.960431, 0.278520],
                  [-0.963776, 0.266713],
                  [-0.966976, 0.254866],
                  [-0.970031, 0.242980],
                  [-0.972940, 0.231058],
                  [-0.975702, 0.219101],
                  [-0.978317, 0.207111],
                  [-0.980785, 0.195090],
                  [-0.983105, 0.183040],
                  [-0.985278, 0.170962],
                  [-0.987301, 0.158858],
                  [-0.989177, 0.146730],
                  [-0.990903, 0.134581],
                  [-0.992480, 0.122411],
                  [-0.993907, 0.110222],
                  [-0.995185, 0.098017],
                  [-0.996313, 0.085797],
                  [-0.997290, 0.073565],
                  [-0.998118, 0.061321],
                  [-0.998795, 0.049068],
                  [-0.999322, 0.036807],
                  [-0.999699, 0.024541],
                  [-0.999925, 0.012272],
                  [-1.000000, 0.000000],
                  [-0.999925, -0.012272],
                  [-0.999699, -0.024541],
                  [-0.999322, -0.036807],
                  [-0.998795, -0.049068],
                  [-0.998118, -0.061321],
                  [-0.997290, -0.073565],
                  [-0.996313, -0.085797],
                  [-0.995185, -0.098017],
                  [-0.993907, -0.110222],
                  [-0.992480, -0.122411],
                  [-0.990903, -0.134581],
                  [-0.989177, -0.146730],
                  [-0.987301, -0.158858],
                  [-0.985278, -0.170962],
                  [-0.983105, -0.183040],
                  [-0.980785, -0.195090],
                  [-0.978317, -0.207111],
                  [-0.975702, -0.219101],
                  [-0.972940, -0.231058],
                  [-0.970031, -0.242980],
                  [-0.966976, -0.254866],
                  [-0.963776, -0.266713],
                  [-0.960431, -0.278520],
                  [-0.956940, -0.290285],
                  [-0.953306, -0.302006],
                  [-0.949528, -0.313682],
                  [-0.945607, -0.325310],
                  [-0.941544, -0.336890],
                  [-0.937339, -0.348419],
                  [-0.932993, -0.359895],
                  [-0.928506, -0.371317],
                  [-0.923880, -0.382683],
                  [-0.919114, -0.393992],
                  [-0.914210, -0.405241],
                  [-0.909168, -0.416430],
                  [-0.903989, -0.427555],
                  [-0.898674, -0.438616],
                  [-0.893224, -0.449611],
                  [-0.887640, -0.460539],
                  [-0.881921, -0.471397],
                  [-0.876070, -0.482184],
                  [-0.870087, -0.492898],
                  [-0.863973, -0.503538],
                  [-0.857729, -0.514103],
                  [-0.851355, -0.524590],
                  [-0.844854, -0.534998],
                  [-0.838225, -0.545325],
                  [-0.831470, -0.555570],
                  [-0.824589, -0.565732],
                  [-0.817585, -0.575808],
                  [-0.810457, -0.585798],
                  [-0.803208, -0.595699],
                  [-0.795837, -0.605511],
                  [-0.788346, -0.615232],
                  [-0.780737, -0.624859],
                  [-0.773010, -0.634393],
                  [-0.765167, -0.643832],
                  [-0.757209, -0.653173],
                  [-0.749136, -0.662416],
                  [-0.740951, -0.671559],
                  [-0.732654, -0.680601],
                  [-0.724247, -0.689541],
                  [-0.715731, -0.698376],
                  [-0.707107, -0.707107],
                  [-0.698376, -0.715731],
                  [-0.689541, -0.724247],
                  [-0.680601, -0.732654],
                  [-0.671559, -0.740951],
                  [-0.662416, -0.749136],
                  [-0.653173, -0.757209],
                  [-0.643832, -0.765167],
                  [-0.634393, -0.773010],
                  [-0.624859, -0.780737],
                  [-0.615232, -0.788346],
                  [-0.605511, -0.795837],
                  [-0.595699, -0.803208],
                  [-0.585798, -0.810457],
                  [-0.575808, -0.817585],
                  [-0.565732, -0.824589],
                  [-0.555570, -0.831470],
                  [-0.545325, -0.838225],
                  [-0.534998, -0.844854],
                  [-0.524590, -0.851355],
                  [-0.514103, -0.857729],
                  [-0.503538, -0.863973],
                  [-0.492898, -0.870087],
                  [-0.482184, -0.876070],
                  [-0.471397, -0.881921],
                  [-0.460539, -0.887640],
                  [-0.449611, -0.893224],
                  [-0.438616, -0.898674],
                  [-0.427555, -0.903989],
                  [-0.416430, -0.909168],
                  [-0.405241, -0.914210],
                  [-0.393992, -0.919114],
                  [-0.382683, -0.923880],
                  [-0.371317, -0.928506],
                  [-0.359895, -0.932993],
                  [-0.348419, -0.937339],
                  [-0.336890, -0.941544],
                  [-0.325310, -0.945607],
                  [-0.313682, -0.949528],
                  [-0.302006, -0.953306],
                  [-0.290285, -0.956940],
                  [-0.278520, -0.960431],
                  [-0.266713, -0.963776],
                  [-0.254866, -0.966976],
                  [-0.242980, -0.970031],
                  [-0.231058, -0.972940],
                  [-0.219101, -0.975702],
                  [-0.207111, -0.978317],
                  [-0.195090, -0.980785],
                  [-0.183040, -0.983105],
                  [-0.170962, -0.985278],
                  [-0.158858, -0.987301],
                  [-0.146730, -0.989177],
                  [-0.134581, -0.990903],
                  [-0.122411, -0.992480],
                  [-0.110222, -0.993907],
                  [-0.098017, -0.995185],
                  [-0.085797, -0.996313],
                  [-0.073565, -0.997290],
                  [-0.061321, -0.998118],
                  [-0.049068, -0.998795],
                  [-0.036807, -0.999322],
                  [-0.024541, -0.999699],
                  [-0.012272, -0.999925],
                  [0.000000, -1.000000],
                  [0.012272, -0.999925],
                  [0.024541, -0.999699],
                  [0.036807, -0.999322],
                  [0.049068, -0.998795],
                  [0.061321, -0.998118],
                  [0.073565, -0.997290],
                  [0.085797, -0.996313],
                  [0.098017, -0.995185],
                  [0.110222, -0.993907],
                  [0.122411, -0.992480],
                  [0.134581, -0.990903],
                  [0.146730, -0.989177],
                  [0.158858, -0.987301],
                  [0.170962, -0.985278],
                  [0.183040, -0.983105],
                  [0.195090, -0.980785],
                  [0.207111, -0.978317],
                  [0.219101, -0.975702],
                  [0.231058, -0.972940],
                  [0.242980, -0.970031],
                  [0.254866, -0.966976],
                  [0.266713, -0.963776],
                  [0.278520, -0.960431],
                  [0.290285, -0.956940],
                  [0.302006, -0.953306],
                  [0.313682, -0.949528],
                  [0.325310, -0.945607],
                  [0.336890, -0.941544],
                  [0.348419, -0.937339],
                  [0.359895, -0.932993],
                  [0.371317, -0.928506],
                  [0.382683, -0.923880],
                  [0.393992, -0.919114],
                  [0.405241, -0.914210],
                  [0.416430, -0.909168],
                  [0.427555, -0.903989],
                  [0.438616, -0.898674],
                  [0.449611, -0.893224],
                  [0.460539, -0.887640],
                  [0.471397, -0.881921],
                  [0.482184, -0.876070],
                  [0.492898, -0.870087],
                  [0.503538, -0.863973],
                  [0.514103, -0.857729],
                  [0.524590, -0.851355],
                  [0.534998, -0.844854],
                  [0.545325, -0.838225],
                  [0.555570, -0.831470],
                  [0.565732, -0.824589],
                  [0.575808, -0.817585],
                  [0.585798, -0.810457],
                  [0.595699, -0.803208],
                  [0.605511, -0.795837],
                  [0.615232, -0.788346],
                  [0.624859, -0.780737],
                  [0.634393, -0.773010],
                  [0.643832, -0.765167],
                  [0.653173, -0.757209],
                  [0.662416, -0.749136],
                  [0.671559, -0.740951],
                  [0.680601, -0.732654],
                  [0.689541, -0.724247],
                  [0.698376, -0.715731],
                  [0.707107, -0.707107],
                  [0.715731, -0.698376],
                  [0.724247, -0.689541],
                  [0.732654, -0.680601],
                  [0.740951, -0.671559],
                  [0.749136, -0.662416],
                  [0.757209, -0.653173],
                  [0.765167, -0.643832],
                  [0.773010, -0.634393],
                  [0.780737, -0.624859],
                  [0.788346, -0.615232],
                  [0.795837, -0.605511],
                  [0.803208, -0.595699],
                  [0.810457, -0.585798],
                  [0.817585, -0.575808],
                  [0.824589, -0.565732],
                  [0.831470, -0.555570],
                  [0.838225, -0.545325],
                  [0.844854, -0.534998],
                  [0.851355, -0.524590],
                  [0.857729, -0.514103],
                  [0.863973, -0.503538],
                  [0.870087, -0.492898],
                  [0.876070, -0.482184],
                  [0.881921, -0.471397],
                  [0.887640, -0.460539],
                  [0.893224, -0.449611],
                  [0.898674, -0.438616],
                  [0.903989, -0.427555],
                  [0.909168, -0.416430],
                  [0.914210, -0.405241],
                  [0.919114, -0.393992],
                  [0.923880, -0.382683],
                  [0.928506, -0.371317],
                  [0.932993, -0.359895],
                  [0.937339, -0.348419],
                  [0.941544, -0.336890],
                  [0.945607, -0.325310],
                  [0.949528, -0.313682],
                  [0.953306, -0.302006],
                  [0.956940, -0.290285],
                  [0.960431, -0.278520],
                  [0.963776, -0.266713],
                  [0.966976, -0.254866],
                  [0.970031, -0.242980],
                  [0.972940, -0.231058],
                  [0.975702, -0.219101],
                  [0.978317, -0.207111],
                  [0.980785, -0.195090],
                  [0.983105, -0.183040],
                  [0.985278, -0.170962],
                  [0.987301, -0.158858],
                  [0.989177, -0.146730],
                  [0.990903, -0.134581],
                  [0.992480, -0.122411],
                  [0.993907, -0.110222],
                  [0.995185, -0.098017],
                  [0.996313, -0.085797],
                  [0.997290, -0.073565],
                  [0.998118, -0.061321],
                  [0.998795, -0.049068],
                  [0.999322, -0.036807],
                  [0.999699, -0.024541],
                  [0.999925, -0.012272]]

DOUBLE_EPSILON = 0.0001


def degrees_to_radians(theta_in_degrees):
    if is_float(theta_in_degrees):
        return theta_in_degrees * DEG_TO_RAD


def radians_to_degrees(theta_in_radians):
    if is_float(theta_in_radians):
        return theta_in_radians * RAD_TO_DEG


def is_float(input_variable):
    return isinstance(input_variable, float)


def is_int(input_variable):
    return isinstance(input_variable, int)


def is_list(input_variable):
    return isinstance(input_variable, list)


def is_int_or_float(input_variable):
    return is_float(input_variable) or is_int(input_variable)


def are_ints_or_floats(input_list):
    check = True
    if isinstance(input_list, list):
        for input_variable in input_list:
            if not is_int_or_float(input_variable):
                check = False
        return check
    else:
        raise TypeError("Input argument must be a list")


def sqr(input_variable):
    return math.pow(input_variable, 2)


def floats_are_close(a, b, rel_tol=1e-9, abs_tol=DOUBLE_EPSILON):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def is_in_range(value, minimum_value_in_range, maximum_value_in_range):
    return (value >= (minimum_value_in_range - DOUBLE_EPSILON)) and \
           (value <= (maximum_value_in_range + DOUBLE_EPSILON))


def ranges_overlap(range1_minimum, range1_maximum, range2_minimum, range2_maximum):
    return (is_in_range(range1_minimum, range2_minimum, range2_maximum)) or \
           (is_in_range(range1_maximum, range2_minimum, range2_maximum)) or \
           (is_in_range(range2_minimum, range1_minimum, range1_maximum)) or \
           (is_in_range(range2_maximum, range1_minimum, range1_maximum))


def chord_length_from_height_radius(h, r):
    chord_angle = 2 * math.acos((r - h) / r)
    chord_length = 2.0 * r * math.sin(chord_angle / 2.0)
    return chord_length
