class Edge2:
    def __init__(self, p1, p2, clockwise, radius, large, arc_centre):
        self.p1 = [0.0, 0.0]
        self.p2 = [0.0, 0.0]
        self.clockwise = False
        self.large = False
        self.arc_centre = [0.0, 0.0]

    def point_parametric(self, s):
        if s == 0:
            return self.p1
        elif s == 1:
            return self.p2
        elif s == 0.5:
            midpoint = ((self.p1[0] + self.p1[0])/2) + ((self.p1[1] + self.p1[1])/2)
            return midpoint
