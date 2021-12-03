from copy import deepcopy

from geometry_utils.maths_utility import degrees_to_radians, is_int_or_float
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.matrix3 import Matrix3
from geometry_utils.two_d.vector2 import is_vector2


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
        if is_path2(other_path):
            return self.list_of_edges == other_path.list_of_edges
        raise TypeError("Comparison must be done with another object of Path2")

    @property
    def get_first_edge(self):
        if self.path_length >= 1:
            return self.list_of_edges[0]
        raise TypeError("Can not find the first edge of an empty list of edges")

    @property
    def get_last_edge(self):
        if self.path_length >= 1:
            return self.list_of_edges[-1]
        raise TypeError("Can not find the last edge of an empty list of edges")

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
        if self.path_length < 3:
            return False
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
        return [(edge.p1, edge.p2) for edge in self.list_of_edges]

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

    def flip_xy(self):
        for edge in self.list_of_edges:
            edge.flip_xy()

    def mirror_y(self):
        for edge in self.list_of_edges:
            edge.mirror_y()

    def offset_path(self, vector):
        if is_vector2(vector):
            for edge in self.list_of_edges:
                edge.offset_edge(vector)
        else:
            raise TypeError("Path offset must be done with a vector")

    def rotate_around(self, rotation_vector, rotation_angle):
        if is_vector2(rotation_vector) and is_int_or_float(rotation_angle):
            reversed_rotation_vector = rotation_vector.reverse()
            self.offset_path(reversed_rotation_vector)
            self.rotate(rotation_angle)
            self.offset_path(rotation_vector)

    def rotate(self, rotation_angle):
        rotation_angle_in_radians = degrees_to_radians(rotation_angle)

        rotation_matrix = Matrix3()
        rotation_matrix.make_rotation(rotation_angle_in_radians)

        for edge in self.list_of_edges:
            edge.p1 = rotation_matrix * edge.p1
            edge.p2 = rotation_matrix * edge.p2

    def close_path(self):
        if self.path_length > 1 and not self.is_closed:
            self.list_of_edges.append(Edge2(self.list_of_edges[-1].p2, self.list_of_edges[0].p1))

    def is_circle(self):
        return self.path_length == 1 and self.list_of_edges[0].is_circle()

    def get_enclosed_area(self):
        if not self.is_closed or self.path_length == 0:
            raise TypeError("The path must be closed and have more than one edge")

        path = deepcopy(self)

        path.remove_duplicate_edges()

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
            self.list_of_edges[offset_location] = new_edge[1]
            index_offset += len(new_edge[1]) - 1

    def is_quadrilateral(self):
        if self.path_length != 4 or not self.is_closed or not self.is_continuous:
            return False

        for edge in self.list_of_edges:
            if edge.is_arc():
                return False

        return True


def is_path2(input_variable):
    return isinstance(input_variable, Path2)
