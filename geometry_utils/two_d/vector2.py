import math
import geometry_utils.three_d.vector3

from geometry_utils.maths_utility import is_int_or_float, are_ints_or_floats, floats_are_close, radians_to_degrees, EPSILON, HALF_PI, PI, ONE_AND_HALF_PI, TWO_PI


class Vector2:
    """
    A class to create a 2D vector

    Attributes:
    ___________
    x: int/float
        the x-coordinate of the vector
    y: int/float
        the y-coordinate of the vector
    w: int/float
        the w-coordinate of the vector
        w=0 leave the vector unchanged when multiplied by a translation matrix

    Methods:
    ________
    __str__(): string
        Returns the attributes of the 2D vector in string format
    __add__(Vector2): Vector2
        Returns the addition of the vector with another 2D vector
    __sub__(Vector2): Vector2
        Returns the subtraction of another 2D vector from the vector
    __mul__(int/float): Vector2
        Returns the multiplication of the vector with an int or float scalar
    __div__(int/float): Vector2
        Returns the division of the vector by an int or float scalar
    __eq__(Vector2): bool
        Returns the equality comparison of the vector with another 2D vector
    __ne__(Vector2): bool
        Returns the inequality comparison of the vector with another 2D vector
    equal(Vector2, float): bool
        Returns the equality comparison of the vector with another 2D vector with specified tolerance
    normalised(): Vector2
        Returns the normal of the vector
    normalise(): Vector2
        Converts the 2D vector into a normal of itself
    length(): int/float
        Returns the pythagorean length of the vector
    square_length(): int/float
        Returns the square of the pythagorean length of the vector
    dot(Vector2): int/float
        Returns the dot product of vector with another 2D vector
    cross(Vector2): Vector2
        Returns the cross product of vector with another 2D vector
    get_perpendicular(): Vector2
        Returns the perpendicular of the vector
    invert(): Vector2
        Converts the 2D vector into an inverse of itself
    inverted(): Vector2
        Returns the inverse of the vector
    rotate(Vector2, int/float): Vector2
        Returns the rotation of the vector at angle theta with respect to 2D vector origin
    angle_to(Vector2, bool): float
        Returns the angle of the vector to another vector in radians or degrees
    signed_angle_to(Vector2, bool): float
        Returns the signed angle of the vector to another vector in radians or degrees
    angle_to_x_axis(bool): float
        Returns the angle of the vector the x-axis in radians or degrees
    from_comma_string(str): Vector2
        Returns a 2D vector from a string input
    to_vector3(): Vector3
        Returns a 3D vector from the 2D vector with a z coordinate value of 0.0
    accuracy_fix(): Vector2
        Converts the 2D vector coordinates with very low values to 0.0
    """
    def __init__(self, x=0.0, y=0.0, w=0):
        if are_ints_or_floats([x, y, w]):
            self.x = x
            self.y = y
            self.w = w
        else:
            raise TypeError("Vector2 argument must be an int or float")

    def __neg__(self):
        return self.inverted()

    def __str__(self):
        """
        Prints the attributes of the 2D vector

        :return: the string of the vector
        :rtype: str
        """
        return "Vector2(x:" + str("{:.2f}".format(self.x)) + ", y:" + str("{:.2f}".format(self.y)) + ")"

    def __add__(self, other_vector):
        """
        Calculates the addition of vector with another 2D vector

        :param   other_vector: the addition 2D vector
        :type    other_vector: Vector2
        :return: the resulting added vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x + other_vector.x, self.y + other_vector.y)
        raise TypeError("Addition must be with an object of Vector2")

    def __sub__(self, other_vector):
        """
        Calculates the subtraction of another 2D vector from the vector

        :param   other_vector: the subtraction 2D vector
        :type    other_vector: Vector2
        :return: the resulting subtracted vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x - other_vector.x, self.y - other_vector.y)
        raise TypeError("Subtraction must be with an object of Vector2")

    def __mul__(self, scalar):
        """
        Calculates the multiplication of the vector with a scalar of type int or float

        :param   scalar: the multiplication scalar
        :type    scalar: int/float
        :return: the resulting multiplied vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector2(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication must be by a scalar of type int or float")

    def __div__(self, scalar):
        """
        Calculates the division of the vector by a scalar of type int or float

        :param   scalar: the division scalar
        :type    scalar: int/float
        :return: the resulting divided vector
        :rtype:  Vector2
        :raises: TypeError: wrong argument type
        """
        if is_int_or_float(scalar):
            return Vector2(self.x / scalar, self.y / scalar)
        raise TypeError("Division must be by a scalar of type int or float")

    # division in Python 3.x = division in Python 2.x
    __truediv__ = __div__

    def __eq__(self, other_vector):
        """
        Compares the equality of the vector and another 2D vector

        :param  other_vector: the other 2D vector
        :type   other_vector: Vector2
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return floats_are_close(self.x, other_vector.x) and floats_are_close(self.y, other_vector.y)
        raise TypeError("Comparison must be with another object of Vector2")

    def __ne__(self, other_vector):
        """
        Compares the inequality of the vector and another 2D vector

        :param  other_vector: the other 2D vector
        :type   other_vector: Vector2
        :return:the vector inequality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return (not floats_are_close(self.x, other_vector.x)) or (not floats_are_close(self.y, other_vector.y))
        raise TypeError("Comparison must be with another object of Vector2")

    def equal(self, other, tol=0.01):
        """
        Compares the equality of the vector and another 2D vector with tolerance input

        :param  other_vector: the other 2D vector
        :param  tol: equality tolerance
        :type   other_vector: Vector2
        :type   tol: float
        :return:the vector equality
        :rtype: bool
        :raises:TypeError: Wrong argument type
        """
        return abs(self.x - other.x) <= tol and abs(self.y - other.y) <= tol

    def normalised(self):
        """
        Calculates the normal vector of the vector

        :return: the normal vector
        :rtype: Vector2
        """
        vector_length = self.length()
        if floats_are_close(vector_length, 0.0):
            return self
        return self / vector_length

    def normalise(self):
        """
        Converts the 2D vector into a normal of itself

        """
        vector_length = self.length()
        if floats_are_close(vector_length, 0.0):
            return self
        self.x /= vector_length
        self.y /= vector_length
        return self

    def length(self):
        """
        Calculates the pythagorean length of the vector

        :return: the vector length
        :rtype: int/float
        """
        return math.sqrt(self.square_length())

    def square_length(self):
        """
        Caclulates the square of the pythagorean length of the vector

        :return: the squared vector length
        :rtype: int/float
        """
        return self.dot(self)

    def dot(self, other_vector):
        """
        Calculates the dot product of self and another 2D vector

        :param:  other_vector: the other vector
        :type:   other_vector: Vector2
        :return:the dot product
        :rtype: float
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return (self.x * other_vector.x) + (self.y * other_vector.y)
        raise TypeError("Dot product must be with another object of Vector2")

    def cross(self, other_vector):
        """
        Calculates the cross product of the vector and another 2D vector

        :param  other_vector: the other vector
        :type   other_vector: Vector2
        :return:the cross product
        :rtype: Vector2
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(other_vector):
            return Vector2(self.x * other_vector.y - self.y * other_vector.x,
                           self.y * other_vector.x - self.x * other_vector.y)
        raise TypeError("Cross product must be with another object of Vector2")

    def get_perpendicular(self):
        """
        Calculates the 2D vector perpendicular to the vector

        :return: the perpendicular vector
        :rtype: Vector2
        """
        return Vector2(-self.y, self.x)

    def invert(self):
        """
        Converts the 2D vector into an inverse of itself

        """
        self.x *= -1
        self.y *= -1
        return self

    def inverted(self):
        """
        Calculates the 2D vector inverse to the vector

        :return:the inverse vector
        :rtype: Vector2
        """
        return Vector2(-self.x, -self.y)

    def rotate(self, origin, theta):
        """
        Calculates the vector rotation of self

        :param: origin: the origin vector of rotation
        :param: theta:  the angle of rotation
        :type:  origin: Vector2
        :type:  theta:  int/float
        :return:the cross product
        :rtype: Vector2
        :raises:TypeError: Wrong argument type
        """
        if is_vector2(origin) and is_int_or_float(theta):
            cos_theta = math.cos(theta)
            sin_theta = math.sin(theta)

            self_origin_difference = self - origin
            result = Vector2()

            result.x = (self_origin_difference.x * cos_theta) - (self_origin_difference.y * sin_theta)
            result.y = (self_origin_difference.x * sin_theta) + (self_origin_difference.y * cos_theta)

            return result + origin

        if not is_vector2(origin):
            raise TypeError("Origin of rotation must be an object of Vector2")
        if not is_int_or_float(theta):
            raise TypeError("Angle of rotation must be a float or int")

    def angle_to(self, other_vector, rad=False):
        """
        Calculates the angle of the 2D vector to another 2D vector

        :param: other_vector: the other 2D vector
        :param: rad: check if the angle should be in radians
        :type: other_vector: Vector2
        :type: rad: Bool
        :return: float
        """
        if is_vector2(other_vector):
            self_unit_vector = self.normalised()
            other_unit_vector = other_vector.normalised()

            dot_product = self_unit_vector.dot(other_unit_vector)
            if floats_are_close(dot_product, 1.0):
                return 0.0

            angle = math.acos(dot_product)
            if not rad:
                angle = radians_to_degrees(angle)
            return angle

    def signed_angle_to(self, other_vector, rad=False):
        """
        Calculates the signed angle of the 2D vector to another 2D vector

        :param: other_vector: the other 2D vector
        :param: rad: check if the angle should be in radians
        :type: other_vector: Vector2
        :type: rad: Bool
        :return: float
        """
        if is_vector2(other_vector):
            angle = other_vector.angle_to_x_axis(rad) - self.angle_to_x_axis(rad)
            return angle

    def angle_to_x_axis(self, rad=False):
        """
        Calculates the angle of the 2D vector to the x_axis

        :param: rad: check if the angle should be in radians
        :type:  rad: Bool
        :return: float
        """
        angle = math.atan2(self.y, self.x)
        if not rad:
            angle = radians_to_degrees(angle)
        return angle

    @classmethod
    def from_comma_string(cls, string):
        """
        Creates a 2D vector from a string input

        :param string: the 2D vector in string format
        :return: str
        """
        v = string.split(',')
        return cls(float(v[0]), float(v[1]))

    def to_vector3(self):
        """
        Creates a 3D vector of the 2D vector with a z coordinate value of 0.0

        :return: the 3D vector
        """
        vector_3d = geometry_utils.three_d.vector3.Vector3(self.x, self.y, 0.0, self.w)
        return vector_3d

    def accuracy_fix(self):
        """
        Converts the 2D vector coordinates with very low values to 0.0

        """
        if -EPSILON < self.x < EPSILON:
            self.x = 0.0
        if -EPSILON < self.y < EPSILON:
            self.y = 0.0
        return self


def is_vector2(input_variable):
    """
    Checks if the input variable is an object of Vector2

    :param input_variable: the input variable to be checked
    :return: bool
    """
    return isinstance(input_variable, Vector2)
