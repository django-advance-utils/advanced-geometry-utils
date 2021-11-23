from maths_utility import is_list
from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.edge2 import is_edge2


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
        Returns the result of the test if the path is closed
    is_continuous(): bool
        Returns the result of the test if the path is continuous
    get_path_bounds(): AxisAlignedBox2()
        Returns 2D box containing the edges of the path
    """

    def __init__(self, list_of_edges):
        if is_list(list_of_edges) and all(is_edge2(edge) for edge in list_of_edges):
            self.list_of_edges = list_of_edges
            self.first_edge = self.list_of_edges[0]
            self.last_edge = self.list_of_edges[-1]
        else:
            raise TypeError("Path2 argument must be a list of objects of Edge2")

    def is_closed(self):
        """
        Tests if the path is closed

        :return:closeness of the path
        :rtype: bool
        """
        return self.last_edge.p2 == self.first_edge.p1 and self.is_continuous()

    def is_continuous(self):
        """
        Tests if the path is continuous

        :return:continuity of the path
        :rtype: bool
        """
        continuity = True
        for edge, next_edge in zip(self.list_of_edges, self.list_of_edges[1:]):
            if edge.p2 != next_edge.p1:
                continuity = False
        return continuity

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

