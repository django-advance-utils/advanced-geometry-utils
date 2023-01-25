import math

from geometry_utils.maths_utility import floats_are_close, ranges_overlap
from geometry_utils.three_d.edge3 import is_edge3
from geometry_utils.two_d.edge2 import is_edge2
from geometry_utils.two_d.point2 import Point2


class Intersection:
    """
    A class to create a 2D intersection

    Attributes:
    ___________
    point: Point2
        the intersection point
    vectors_intersect: bool
        check if edges intersect
    on_first_segment: bool
        check if the edges intersect on first segment
    on_second_segment: bool
        check if the edges intersect on the second segment
    minor_radius: int/float
        the minor radius of the ellipse
    collinear: bool
        check if the edges are collinear
    end_of_line: bool
        check if the end of the edge has been reached
    do_collinear_test: bool
        check if collinear tests is to be done

    Methods:
    ________
    intersect_lines(Point2, Point2, Point2, Point2):
        perform intersection of two edges   
    """

    def __init__(self):
        self.vectors_intersect = False
        self.on_first_segment = False
        self.on_second_segment = False
        self.collinear = False
        self.end_of_line = False
        self.point = None

    def __str__(self):
        if isinstance(self, list):
            for intersection in self:
                return ("Intersection(point:" + str(intersection.point) + ", Vectors Intersect:" + str(intersection.vectors_intersect) +
                        ", On First Segment:" + str(intersection.on_first_segment) +
                        ", On Second Segment:" + str(intersection.on_second_segment) + ", Collinear:" + str(intersection.collinear))
        else:
            return ("Intersection(point:" + str(self.point) + ", Vectors Intersect:" + str(self.vectors_intersect) +
                    ", On First Segment:" + str(self.on_first_segment) +
                    ", On Second Segment:" + str(self.on_second_segment) + ", Collinear:" + str(self.collinear))

    def intersect(self, first_edge, second_edge):
        """
        Creates the intersection of the edge with another edge and appends the list of intersections

        """
        if is_edge3(first_edge) and is_edge3(second_edge):
            first_edge = first_edge.to_edge2()
            second_edge = second_edge.to_edge2()
            intersection = self.intersect(first_edge, second_edge)
            if isinstance(intersection, list):
                for intersect in intersection:
                    intersect.point = intersect.point.to_point3()
            else:
                intersection.point = intersection.point.to_point3()
            return intersection

        if is_edge2(first_edge) and is_edge2(second_edge):
            if second_edge.is_arc():
                if second_edge.is_circle():
                    intersection = self.intersect_line_circle(first_edge, second_edge)
                    return intersection
                else:
                    intersection = self.intersect_line_arc(first_edge, second_edge)
                    return intersection
            else:
                intersection = self.intersect_lines(first_edge, second_edge)
                return intersection

        else:
            if not is_edge2(first_edge) or not is_edge2(second_edge):
                raise TypeError("First and second arguments must be objects of Edge2")

    def intersect_lines(self, first_edge, second_edge):
        """
        Creates an intersection between two edges

        :param: p1: first point of the first edge
                p2: second point of the first edge
                p3: first point of the second edge
                p4: second point of the second edge
        :type:  p1: Point2
                p2: Point2
                p3: Point2
                p4: Point2
        :return:the resulting intersection
        :rtype: Intersection
        :raises:TypeError: wrong argument type
        """

        if is_edge2(first_edge) and is_edge2(second_edge):
            u = first_edge.p2 - first_edge.p1
            v = second_edge.p2 - second_edge.p1
            w = first_edge.p1 - second_edge.p1

            denominator = u.x * v.y - u.y * v.x

            if floats_are_close(denominator, 0.0):
                self.vectors_intersect = False
                self.on_first_segment = False
                self.on_second_segment = False
                self.point = first_edge.p1
                self.do_collinear_test = True

                w_normalised = w.normalised()
                u_normalised = u.normalised()
                det = (w_normalised.x * u_normalised.y) - (w_normalised.y * u_normalised.x)

                if floats_are_close(det, 0.0):
                    self.vectors_intersect = True
                    self.collinear = True

                    if ranges_overlap(first_edge.minimum_x(), first_edge.maximum_x(),
                                      second_edge.minimum_x(), second_edge.maximum_x()) and \
                            ranges_overlap(first_edge.minimum_y(), first_edge.maximum_y(),
                                           second_edge.minimum_y(), second_edge.maximum_y()):
                        self.on_first_segment = True
                        self.on_second_segment = True

            else:
                self.vectors_intersect = True
                # This seems to produce a more accurate intersection point than the other code below,
                # which could have been over a mm off at times!
                l1_a = first_edge.p1.y - first_edge.p2.y
                l1_b = first_edge.p2.x - first_edge.p1.x
                l1_c = -(first_edge.p1.x * first_edge.p2.y - first_edge.p2.x * first_edge.p1.y)

                l2_a = second_edge.p1.y - second_edge.p2.y
                l2_b = second_edge.p2.x - second_edge.p1.x
                l2_c = -(second_edge.p1.x * second_edge.p2.y - second_edge.p2.x * second_edge.p1.y)

                d = l1_a * l2_b - l1_b * l2_a
                dx = l1_c * l2_b - l1_b * l2_c
                dy = l1_a * l2_c - l1_c * l2_a

                self.point = Point2(dx / d, dy / d)

                # s = float(v.x * w.y - v.y * w.x) / denominator
                # t = float(u.x * w.y - u.y * w.x) / denominator
                #
                # self.point = Point2()
                # self.point.x = first_edge.p1.x + s * u.x
                # self.point.y = first_edge.p1.y + t * u.y

                intersect_point_to_point1_distance = self.point.distance_to(first_edge.p1)
                intersect_point_to_point2_distance = self.point.distance_to(first_edge.p2)
                intersect_point_to_point3_distance = self.point.distance_to(second_edge.p1)
                intersect_point_to_point4_distance = self.point.distance_to(second_edge.p2)

                if floats_are_close(intersect_point_to_point1_distance, 0.0) or \
                        floats_are_close(intersect_point_to_point2_distance, 0.0) or \
                        floats_are_close(intersect_point_to_point3_distance, 0.0) or \
                        floats_are_close(intersect_point_to_point4_distance, 0.0):
                    self.end_of_line = True

                length_of_side1 = first_edge.edge_length()
                length_of_side2 = second_edge.edge_length()

                self.on_first_segment = floats_are_close(intersect_point_to_point1_distance +
                                                         intersect_point_to_point2_distance, length_of_side1)

                self.on_second_segment = floats_are_close(intersect_point_to_point3_distance +
                                                          intersect_point_to_point4_distance, length_of_side2)
            return self
        else:
            raise TypeError("Arguments must be objects of Edge2")

    def intersect_line_circle(self, line_edge, circle_edge):
        if is_edge2(line_edge) and is_edge2(circle_edge):
            result = []

            lu = line_edge.p2 - line_edge.p1
            lw = line_edge.p1 - circle_edge.centre
            a = lu.dot(lu)
            b = 2.0 * lu.dot(lw)
            c = lw.dot(lw) - (circle_edge.radius * circle_edge.radius)

            d = (b * b) - (4.0 * a * c)

            if d < 0.0:
                return result
            elif floats_are_close(d, 0.0):
                u = float(-b) / (2.0 * a)
                self.point = line_edge.p1 + (lu * u)
                self.vectors_intersect = True
                self.on_first_segment = 0.0 <= u <= 1.0
                self.on_second_segment = True
                if floats_are_close(u, 0.0):
                    self.end_of_line = True
                    self.point = line_edge.p1
                elif floats_are_close(u, 1.0):
                    self.end_of_line = True
                    self.point = line_edge.p2
                result.append(self)
                return result
            else:
                sqrt_d = math.sqrt(d)
                u_1 = (-b + sqrt_d) / (2.0 * a)
                u_2 = (-b - sqrt_d) / (2.0 * a)

                self.point = line_edge.p1 + (lu * u_1)
                self.vectors_intersect = True
                self.on_first_segment = 0.0 <= u_1 <= 1.0
                self.on_second_segment = True

                if floats_are_close(u_1, 0.0):
                    self.point = line_edge.p1
                    self.end_of_line = True
                elif floats_are_close(u_1, 1.0):
                    self.point = line_edge.p2
                    self.end_of_line = True

                other_intersection = Intersection()
                other_intersection.point = line_edge.p1 + (lu * u_2)
                other_intersection.vectors_intersect = True
                other_intersection.on_first_segment = 0.0 <= u_2 <= 1.0
                other_intersection.on_second_segment = True

                if floats_are_close(u_2, 0.0) or floats_are_close(u_2, 1.0):
                    other_intersection.end_of_line = True
                result.append(self)
                result.append(other_intersection)
                return result

    def intersect_line_arc(self, line_edge, arc_edge):
        if is_edge2(line_edge) and is_edge2(arc_edge) and arc_edge.is_arc():
            intersections = self.intersect_line_circle(line_edge, arc_edge)

            out = []

            if len(intersections) < 1:
                return out

            for intersection in intersections:
                if intersection.vectors_intersect:
                    intersection_point_vector = intersection.point.to_vector2()
                    intersection.on_second_segment = arc_edge.vector_within_arc(intersection_point_vector)
                    out.append(intersection)

            return out
