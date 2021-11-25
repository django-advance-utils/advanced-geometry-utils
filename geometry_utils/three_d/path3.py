from geometry_utils.maths_utility import is_list
from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import is_edge3


class Path3:
    """
    A class to create a 3D path

    Attributes:
    ___________
    list_of_edges: list
        the list of 3D edges to establish a path
    first_edge: Edge3
        the first 3D edge on the path
    last_edge: Edge3
        the last 3D edge on the path

    Methods:
    ________
    is_closed(): bool
        Returns the result of the test if the path is closed
    is_continuous(): bool
        Returns the result of the test if the path is continuous
    get_path_bounds(): AxisAlignedBox3()
        Returns 3D box containing the edges of the path
    """
    def __init__(self, list_of_edges):
        if is_list(list_of_edges) and all(is_edge3(edge) for edge in list_of_edges):
            self.list_of_edges = list_of_edges
            self.first_edge = self.list_of_edges[0]
            self.last_edge = self.list_of_edges[-1]
        else:
            raise TypeError("Path3 argument must be a list of objects of Edge3")

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
        Derives the AxisAlignedBox3 containing the bounds of the path

        :return:the box containing the path bounds
        :rtype: AxisAlignedBox3
        """
        path_bounds = AxisAlignedBox3()
        for edge in self.list_of_edges:
            path_bounds.include(edge.get_edge_bounds())
        return path_bounds

