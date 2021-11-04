from two_d.point2 import Point2


class AxisAlignedBox2:
    def __init__(self, minimum, maximum):
        if isinstance(minimum, Point2) and isinstance(maximum, Point2):
            self.min = minimum
            self.max = maximum
