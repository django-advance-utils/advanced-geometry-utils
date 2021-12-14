from copy import deepcopy

from geometry_utils.maths_utility import is_int_or_float
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.vector2 import is_vector2
from geometry_utils.two_d.point2 import is_list_of_points, get_points_orientation, get_leftmost_point_index, Point2


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
    def get_path_bounds(self):
        """
        Derives the AxisAlignedBox2 containing the bounds of the path

        :return:the box containing the path bounds
        :rtype: AxisAlignedBox2
        """
        path_bounds = AxisAlignedBox2()
        for edge in self.list_of_edges:
            path_bounds.include(edge.get_edge_bounds())
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

    def flip_xy(self):
        for edge in self.list_of_edges:
            edge.flip_xy()
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

    # to be reviewed with Simon and Tom
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


def get_convex_hull(list_of_points):
    if is_list_of_points(list_of_points):

        number_of_points = len(list_of_points)

        if number_of_points < 3:
            raise IndexError("There must be at least three points")

        leftmost_point_index = get_leftmost_point_index(list_of_points)
        print(list_of_points[leftmost_point_index].x, list_of_points[leftmost_point_index].y)

        list_of_convex_hull_points = []

        first_point_index = leftmost_point_index

        while True:
            list_of_convex_hull_points.append(list_of_points[first_point_index])
            second_point_index = (first_point_index + 1) % number_of_points

            for i in range(number_of_points):
                if get_points_orientation(list_of_points[first_point_index], list_of_points[i],
                                          list_of_points[second_point_index]) == "Counterclockwise":
                    second_point_index = i
            first_point_index = second_point_index
            if first_point_index == leftmost_point_index:
                break

        convex_hull = Path2()
        for previous_point, point in zip(list_of_convex_hull_points, list_of_convex_hull_points[1:]):
            convex_hull.list_of_edges.append(Edge2(previous_point, point))
        convex_hull.close_path()
        return convex_hull


def is_path2(input_variable):
    return isinstance(input_variable, Path2)
