import math


class Vector3:
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        if isinstance(self, Vector3) and isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(self, Vector3) and isinstance(other, float):
            return Vector3(self.x + other, self.y + other, self.z + other)
        elif isinstance(self, float) and isinstance(other, Vector3):
            return Vector3(self + other.x, self + other.y, self + other.z)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(self, Vector3) and isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(self, Vector3) and isinstance(other, float):
            return Vector3(self.x - other, self.y - other, self.z - other)
        elif isinstance(self, float) and isinstance(other, Vector3):
            return Vector3(other.x - self, other.y - self, other.z - self)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(self, Vector3) and isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(self, Vector3) and isinstance(other, float):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(self, float) and isinstance(other, Vector3):
            return Vector3(self * other.x, self * other.y, self * other.z)
        else:
            return NotImplemented

    def __div__(self, other):
        if isinstance(self, Vector3) and isinstance(other, float):
            return Vector3(self.x / other, self.y / other, self.z / other)
        elif isinstance(self, float) and isinstance(other, Vector3):
            return Vector3(other.x / self, other.y / self, other.z / self)
        else:
            return NotImplemented

    def __eq__(self, other):
        return bool(self.x == other.x and self.y == other.y and self.z == other.z)

    def __ne__(self, other):
        return bool(self.x != other.x or self.y != other.y or self.z != other.z)

    def normalise(self):
        vector_length = self.length()
        if vector_length == 0:
            return self
        return self / vector_length

    def reverse(self):
        return Vector3(self.x * -1, self.y * -1, self.z * -1)

    def length(self):
        return float(math.sqrt(self * self))

    def dot(self, other):
        return float(self.x * other.x + self.y * other.y + self.z * other.z)

    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - other.x * self.z,
                       self.x * other.y - other.y * self.x)
