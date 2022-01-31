from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3


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

    def reverse(self):
        self.list_of_edges.reverse()
        for edge in self.list_of_edges:
            edge.reverse()
        return self

    def is_circle(self):
        return self.path_length == 1 and self.list_of_edges[0].is_circle()

    def convert_circle_to_edges(self):
        if self.is_circle():
            circle_centre = Point3()
            circle_centre.x = self.list_of_edges[0].centre.x
            circle_centre.y = self.list_of_edges[0].centre.y
            circle_centre.z = self.list_of_edges[0].centre.z
            circle_radius = self.list_of_edges[0].radius

            self.list_of_edges = [
                Edge3(Point3(circle_centre.x, circle_centre.y + circle_radius, circle_centre.z),
                      Point3(circle_centre.x, circle_centre.y - circle_radius, circle_centre.z), circle_radius, False),
                Edge3(Point3(circle_centre.x, circle_centre.y - circle_radius, circle_centre.z),
                      Point3(circle_centre.x, circle_centre.y + circle_radius, circle_centre.z), circle_radius, True)
            ]
            return self

    def get_bounds(self):
        """
        Derives the AxisAlignedBox2 containing the bounds of the path

        :return:the box containing the path bounds
        :rtype: AxisAlignedBox2
        """
        path_bounds = AxisAlignedBox3()
        for edge in self.list_of_edges:
            path_bounds.include(edge.get_edge_bounds())

            if edge.is_arc():
                positive_x = edge.centre + Vector3(edge.radius, 0, 0)
                positive_y = edge.centre + Vector3(0, edge.radius, 0)

                negative_x = edge.centre + Vector3(-edge.radius, 0, 0)
                negative_y = edge.centre + Vector3(0, -edge.radius, 0)

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

                if edge.p1.z != edge.p2.z:
                    positive_z = edge.centre + Vector3(0, 0, edge.radius)
                    negative_z = edge.centre + Vector3(0, 0, -edge.radius)

                    parametric_positive_z = edge.parametric_point(positive_z)
                    parametric_negative_z = edge.parametric_point(negative_z)

                    if lower_bound < parametric_positive_z < upper_bound:
                        path_bounds.include(positive_z)

                    if lower_bound < parametric_negative_z < upper_bound:
                        path_bounds.include(negative_z)

        return path_bounds


def is_path3(input_variable):
    return isinstance(input_variable, Path3)
