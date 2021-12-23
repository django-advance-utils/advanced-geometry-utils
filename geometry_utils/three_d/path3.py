from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3


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
        Returns the result of the tests if the path is closed
    is_continuous(): bool
        Returns the result of the tests if the path is continuous
    get_path_bounds(): AxisAlignedBox3()
        Returns 3D box containing the edges of the path
    """
    def __init__(self):
        self.list_of_edges = []

    def print_edges(self):
        print "Path3(list of edges: "
        for index, edge in enumerate(self.list_of_edges):
            print ("\t" + str(index) + "\t" + str(edge))
        print ")"

    def __str__(self):
        self.print_edges()
        return ""

    def __eq__(self, other_path):
        if is_path3(other_path) and self.path_length == other_path.path_length:
            for index in range(self.path_length):
                if self.list_of_edges[index] != other_path.list_of_edges[index]:
                    return False
            return True
        else:
            if not is_path3(other_path):
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
        Calculates the number of Edge3 edges in the path

        :return: number of edges in the path
        :rtype: int
        """
        return len(self.list_of_edges)

    def is_closed(self):
        """
        Tests if the path is closed

        :return:closeness of the path
        :rtype: bool
        """
        return self.list_of_edges[-1].p2 == self.list_of_edges[0].p1 and self.is_continuous()

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

    def get_bounds(self):
        """
        Derives the AxisAlignedBox3 containing the bounds of the path

        :return:the box containing the path bounds
        :rtype: AxisAlignedBox3
        """
        path_bounds = AxisAlignedBox3()
        for edge in self.list_of_edges:
            path_bounds.include(edge.get_edge_bounds())
        return path_bounds


def is_path3(input_variable):
    return isinstance(input_variable, Path3)
