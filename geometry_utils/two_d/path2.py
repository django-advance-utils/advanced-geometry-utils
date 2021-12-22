import copy
from copy import deepcopy

from geometry_utils.maths_utility import is_int_or_float, is_list
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.vector2 import is_vector2, Vector2
from geometry_utils.two_d.point2 import Point2, is_point2


class Path2:
    """
    A class to create a 2D path

    Attributes:
    ___________
    list_of_edges: list
        the list of 2D edges to establish a path
    first_edge: Edge2
        the first 2D edge on the path
    last_edge: Edge2
        the last 2D edge on the path

    Methods:
    ________
    is_closed(): bool
        Returns the result of the tests if the path is closed
    is_continuous(): bool
        Returns the result of the tests if the path is continuous
    get_path_bounds(): AxisAlignedBox2()
        Returns 2D box containing the edges of the path
    """

    def __init__(self):
        self.list_of_edges = []

    def __repr__(self):
        return repr({'list of edges': self.list_of_edges})

    def __str__(self):
        self.print_edges()
        return ""

    def print_edges(self):
        print "Path2(list of edges: "
        for index, edge in enumerate(self.list_of_edges):
            print ("\t" + str(index) + "\t" + str(edge))
        print ")"

    def __eq__(self, other_path):
        if is_path2(other_path) and self.path_length == other_path.path_length:
            for index in range(self.path_length):
                if self.list_of_edges[index] != other_path.list_of_edges[index]:
                    return False
            return True
        else:
            if not is_path2(other_path):
                raise TypeError("Comparison must be done with another object of Path2")
            if self.path_length != other_path.path_length:
                raise IndexError("Comparison must be done with another path of equal number of edges")

    @property
    def get_first_edge(self):
        if self.path_length >= 1:
            return self.list_of_edges[0]
        raise IndexError("Can not find the first edge of an empty list of edges")

    @property
    def get_last_edge(self):
        if self.path_length >= 1:
            return self.list_of_edges[-1]
        raise IndexError("Can not find the last edge of an empty list of edges")

    @property
    def path_length(self):
        """
        Calculates the number of Edge2 edges in the path

        :return: number of edges in the path
        :rtype: int
        """
        return len(self.list_of_edges)

    @property
    def is_closed(self):
        """
        Tests if the path is closed

        :return: closeness of the path
        :rtype:  bool
        """
        if self.path_length > 2:
            return self.list_of_edges[-1].p2 == self.list_of_edges[0].p1 and self.is_continuous
        return False

    @property
    def is_continuous(self):
        """
        Tests if the path is continuous

        :return:continuity of the path
        :rtype: bool
        """
        continuity = True

        if self.path_length < 2:
            continuity = False
        else:
            for edge, next_edge in zip(self.list_of_edges, self.list_of_edges[1:]):
                if edge.p2 != next_edge.p1:
                    continuity = False
        return continuity

    @property
    def get_bounds(self):
        """
        Derives the AxisAlignedBox2 containing the bounds of the path

        :return:the box containing the path bounds
        :rtype: AxisAlignedBox2
        """
        path_bounds = AxisAlignedBox2()
        for edge in self.list_of_edges:
            path_bounds.include(edge.get_edge_bounds())

            if edge.is_arc():
                positive_x = edge.centre + Vector2(edge.radius, 0)
                positive_y = edge.centre + Vector2(0, edge.radius)
                negative_x = edge.centre + Vector2(-edge.radius, 0)
                negative_y = edge.centre + Vector2(0, -edge.radius)

                parametric_positive_x = edge.parametric_point(positive_x)
                parametric_positive_y = edge.parametric_point(positive_y)
                parametric_negative_x = edge.parametric_point(negative_x)
                parametric_negative_y = edge.parametric_point(negative_y)

                lower_bound = -0.0001
                upper_bound = 1.0001

                if lower_bound < parametric_positive_x < upper_bound:
                    path_bounds.include(positive_x)
                if lower_bound < parametric_positive_y < upper_bound:
                    path_bounds.include(positive_y)
                if lower_bound < parametric_negative_x < upper_bound:
                    path_bounds.include(negative_x)
                if lower_bound < parametric_negative_y < upper_bound:
                    path_bounds.include(negative_y)

        return path_bounds

    def to_tuple_list(self):
        path_tuple_list = []
        for edge in self.list_of_edges:
            path_tuple_list.append((edge.p1, edge.p2))
        return path_tuple_list

    def remove_duplicate_edges(self):
        indices_of_edges_to_remove = []
        last_edge = None

        for index, edge in enumerate(self.list_of_edges):
            if last_edge is not None:
                if edge == last_edge:
                    indices_of_edges_to_remove.append(index)
            last_edge = edge

        indices_of_edges_to_remove.sort(reverse=True)
        for index in indices_of_edges_to_remove:
            del self.list_of_edges[index]
        return self

    def mirror_y(self):
        for edge in self.list_of_edges:
            edge.mirror_y()
        return self

    def offset_path(self, vector):
        if is_vector2(vector):
            for edge in self.list_of_edges:
                edge.offset_edge(vector)
            return self
        else:
            raise TypeError("Path offset must be done with a vector")

    def rotate_around(self, rotation_vector, rotation_angle):
        if is_vector2(rotation_vector) and is_int_or_float(rotation_angle):
            reversed_rotation_vector = rotation_vector.reverse()
            self.offset_path(reversed_rotation_vector)
            self.rotate(rotation_angle)
            self.offset_path(rotation_vector)
        return self

    def rotate(self, rotation_angle):
        for edge in self.list_of_edges:
            edge.rotate(rotation_angle)
        return self

    def close_path(self):
        if self.path_length > 1 and not self.is_closed:
            if not self.is_continuous:
                for index, edge in enumerate(self.list_of_edges):
                    if index == 0:
                        continue
                    if self.list_of_edges[index - 1].p2 != edge.p1:
                        self.list_of_edges.insert(index, Edge2(self.list_of_edges[index - 1].p2, edge.p1))
                        index += 1
            self.list_of_edges.append(Edge2(deepcopy(self.list_of_edges[-1].p2), deepcopy(self.list_of_edges[0].p1)))
        return self

    def is_circle(self):
        return self.path_length == 1 and self.list_of_edges[0].is_circle()

    def get_enclosed_area(self):
        path = deepcopy(self)

        path.remove_duplicate_edges()
        if path.is_closed and path.path_length != 0:
            return path
        raise TypeError("The path must be closed and have more than one edge")

    def remove_arcs(self):
        index = 0
        list_of_edges_to_remove = []
        for edge in self.list_of_edges:
            if edge.is_arc():
                list_of_edges_to_remove.append((index, edge.flatten_arc()))
                edge.radius = 0
                edge.clockwise = False
                edge.large = False
            index += 1

        index_offset = 0
        for new_edge in list_of_edges_to_remove:
            offset_location = new_edge[0] + index_offset
            del self.list_of_edges[offset_location]
            self.list_of_edges[offset_location:offset_location] = new_edge[1]
            index_offset += len(new_edge[1]) - 1

    def is_quadrilateral(self):
        if self.path_length != 4 or not self.is_closed or not self.is_continuous:
            return False

        for edge in self.list_of_edges:
            if edge.is_arc():
                return False

        return True

    def is_rectangular(self):
        if not self.is_quadrilateral():
            return False
        return (self.list_of_edges[0].is_perpendicular_to(self.list_of_edges[1]) and
                self.list_of_edges[1].is_perpendicular_to(self.list_of_edges[2]) and
                self.list_of_edges[2].is_perpendicular_to(self.list_of_edges[3]) and
                self.list_of_edges[3].is_perpendicular_to(self.list_of_edges[0]))

    def is_curved_top(self):
        if self.path_length != 5:
            return False

        for edge in self.list_of_edges:
            if not edge.is_arc() and not self.is_continuous:
                return False

        return True

    def convert_circle_to_points(self):
        if self.is_circle():
            circle_centre = Point2()
            circle_centre.x = self.list_of_edges[0].centre.x
            circle_centre.y = self.list_of_edges[0].centre.y
            circle_radius = self.list_of_edges[0].radius

            circle_list_of_points = [
                Point2(circle_centre.x - circle_radius, circle_centre.y),
                Point2(circle_centre.x, circle_centre.y + circle_radius),
                Point2(circle_centre.x + circle_radius, circle_centre.y),
                Point2(circle_centre.x, circle_centre.y - circle_radius)
            ]

            return circle_list_of_points

    def get_points_orientation(self, list_of_point_indices):
        # https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
        if is_list(list_of_point_indices):
            val = (((self.list_of_edges[list_of_point_indices[1]].minimum_y() - self.list_of_edges[
                list_of_point_indices[0]].minimum_y()) *
                    (self.list_of_edges[list_of_point_indices[2]].minimum_x() - self.list_of_edges[
                        list_of_point_indices[1]].minimum_x())) -
                   ((self.list_of_edges[list_of_point_indices[1]].minimum_x() - self.list_of_edges[
                       list_of_point_indices[0]].minimum_x()) *
                    (self.list_of_edges[list_of_point_indices[2]].minimum_y() - self.list_of_edges[
                        list_of_point_indices[1]].minimum_y())))

            if val == 0:
                return "Collinear"
            elif val > 0:
                return "Clockwise"
            else:
                return "Counterclockwise"
        raise TypeError("Input arguments must be objects of Point2")

    def get_leftmost_point_index(self):
        minimum_point_index = 0
        for index in range(1, self.path_length):
            if self.list_of_edges[index].p1.x < self.list_of_edges[minimum_point_index].p1.x:
                minimum_point_index = index
            elif self.list_of_edges[index].p1.x == self.list_of_edges[minimum_point_index].p1.x:
                if self.list_of_edges[index].p1.y > self.list_of_edges[minimum_point_index].p1.y:
                    minimum_point_index = index
        return minimum_point_index

    def get_convex_hull(self):
        convex_hull = Path2()
        if self.is_continuous:
            convex_hull = copy.deepcopy(self)
            if not self.is_closed:
                convex_hull.close_path()
            return convex_hull

        number_of_edges = self.path_length

        if number_of_edges < 3:
            raise IndexError("There must be at least three edges")

        leftmost_point_index = self.get_leftmost_point_index()

        first_point_index = leftmost_point_index

        while True:
            convex_hull.list_of_edges.append(self.list_of_edges[first_point_index])
            second_point_index = (first_point_index + 1) % number_of_edges

            for i in range(number_of_edges):
                if self.get_points_orientation([first_point_index, i, second_point_index]) == "Counterclockwise":
                    second_point_index = i

            first_point_index = second_point_index
            if first_point_index == leftmost_point_index:
                break
        convex_hull.close_path()
        return convex_hull

    def reverse(self):
        self.list_of_edges.reverse()
        for edge in self.list_of_edges:
            edge.reverse()


'''
    def get_oriented_bounding_box(self):
        class Box:
            def __init__(self):
                self.U0 = Vector2()
                self.U1 = Vector2()
                self.index = [0, 0, 0, 0]
                self.sqr_len_min = 0.0
                self.area = 0.0

        def perp(point):
            if is_point2(point):
                return Point2(point.y, -point.x)

        def inv(point):
            if is_point2(point):
                return Point2(-point.x, -point.y)

        def sub(point1, point2):
            if is_point2(point1) and is_point2(point2):
                return Point2(point1.x - point2.x, point1.y - point2.y)

        def smallest_box(start_index, end_index):
            box = Box()
            box.U0 = self.list_of_edges[end_index].p2 - self.list_of_edges[start_index].p1
            box.U1 = box.U0.get_perpendicular()
            box.index = [end_index, end_index, end_index, end_index]
            box.sqr_len_min = box.U0.dot(box.U0)

            origin = self.list_of_edges[end_index]
            support = []

            for index in range(4):
                support.append(Point2())

            index = 0
            for edge in self.list_of_edges:
                diff = 
'''


def is_path2(input_variable):
    return isinstance(input_variable, Path2)
