import copy

import geometry_utils.two_d.path2

from geometry_utils.maths_utility import is_int_or_float, is_float, floats_are_close
from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3, is_edge3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3, is_vector3


class Path3:
    """
    A class to create a 3D path

    Attributes:
    ___________
    list_of_edges: list
        the list of 3D edges to establish a path
    fill: str
        the fill colour of the path inside
    name: str
        the name of the path
    type: str
        the type name of the path
    layers: list
        list of layers in the path
    attributes: dict
        dictionary of python attributes

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
        
        self.fill = ''
        self.name = ''
        self.type = ''
        self.layers = []
        self.closed = None
        self.attributes = {}

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
            
    def __add__(self, other_path):
        path = Path3()
        path.list_of_edges = self.list_of_edges + other_path.list_of_edges
        return path
    
    def set_edges(self, list_of_edges):
        for edge in list_of_edges:
            if not is_edge3(edge):
                raise TypeError('Input has to be list of Edge2 objects')
        self.list_of_edges = list_of_edges

    def get_first_edge(self):
        if self.path_length >= 1:
            return self.list_of_edges[0]
        raise IndexError("Can not find the first edge of an empty list of edges")

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

    @property
    def is_closed(self):
        """
        Tests if the path is closed

        :return:closeness of the path
        :rtype: bool
        """
        return self.list_of_edges[-1].p2 == self.list_of_edges[0].p1 and self.is_continuous

    @property
    def is_continuous(self):
        """
        Tests if the path is continuous

        :return:continuity of the path
        :rtype: bool
        """
        if self.path_length < 2:
            return False
        else:
            for edge, next_edge in zip(self.list_of_edges, self.list_of_edges[1:]):
                if edge.p2 != next_edge.p1:
                    return False
            return True
    
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
                parametric_negative_x = edge.parametric_point(negative_x)

                parametric_positive_y = edge.parametric_point(positive_y)
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
    
    def to_tuple_list(self):
        path_tuple_list = []
        for edge in self.list_of_edges:
            path_tuple_list.append(((edge.p1.x, edge.p1.y, edge.p1.z), (edge.p2.x, edge.p2.y, edge.p2.z)))
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
    
    def reverse(self):
        self.list_of_edges.reverse()
        for edge in self.list_of_edges:
            edge.reverse()
        return self

    def mirror_x(self):
        for edge in self.list_of_edges:
            edge.mirror_x()
        return self

    def mirror_y(self):
        for edge in self.list_of_edges:
            edge.mirror_y()
        return self

    def mirror_z(self):
        for edge in self.list_of_edges:
            edge.mirror_z()
        return self
    
    def mirror_origin(self):
        for edge in self.list_of_edges:
            edge.mirror_origin()
        return self
    
    def offset(self, vector, point_type=None):
        if is_vector3(vector):
            if point_type is None or point_type.lower() == 'ppp':
                for edge in self.list_of_edges:
                    edge.offset(vector)
                return self
            elif point_type.lower() == 'mmm':
                for edge in self.list_of_edges:
                    edge.mirror_origin().offset(vector)
                return self
            elif point_type.lower() == 'pmp':
                for edge in self.list_of_edges:
                    edge.mirror_y().offset(vector)
                return self
            elif point_type.lower() == 'mpp':
                for edge in self.list_of_edges:
                    edge.mirror_x().offset(vector)
                return self
            elif point_type.lower() == 'ppm':
                for edge in self.list_of_edges:
                    edge.mirror_z().offset(vector)
                return self
        else:
            raise TypeError("Path offset must be done with a vector")
        
    def rotate_around(self, rotation_vector, rotation_angle):
        if is_vector3(rotation_vector) and is_float(rotation_angle):
            reversed_rotation_vector = rotation_vector.invert()
            self.offset(reversed_rotation_vector)
            self.rotate(rotation_angle)
            self.offset(rotation_vector)
            return self
        
    def close_path(self):
        if self.path_length > 1 and not self.is_closed:
            if not self.is_continuous:
                for index, edge in enumerate(self.list_of_edges):
                    if index == 0:
                        continue
                    if self.list_of_edges[index - 1].p2 != edge.p1:
                        self.list_of_edges.insert(index, Edge3(self.list_of_edges[index - 1].p2, edge.p1))
            self.list_of_edges.append(Edge3(copy.deepcopy(self.list_of_edges[-1].p2),
                                            copy.deepcopy(self.list_of_edges[0].p1)))
        return self
    
    def make_continuous(self):
        if self.path_length > 1 and not self.is_continuous:
            for index in range(self.path_length - 1):
                if self.list_of_edges[index].p2 != self.list_of_edges[index + 1].p1:
                    self.list_of_edges[index].p2 = copy.deepcopy(self.list_of_edges[index + 1].p1)
                    if self.list_of_edges[index + 1].is_arc():
                        self.list_of_edges[index].radius = self.list_of_edges[index + 1].radius
                        self.list_of_edges[index].clockwise = self.list_of_edges[index + 1].clockwise
                        self.list_of_edges[index].large = self.list_of_edges[index + 1].large

                        self.list_of_edges[index + 1].radius = 0
                        self.list_of_edges[index + 1].clockwise = False
                        self.list_of_edges[index + 1].large = False
            self.update_path()
        return self

    def rotate(self, rotation_angle):
        for edge in self.list_of_edges:
            edge.rotate(rotation_angle)
        return self

    def is_circle(self):
        return self.path_length == 1 and self.list_of_edges[0].is_circle()

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

        return self

    def get_enclosed_area(self):
        path_2d = self.to_path2()
        return path_2d.get_enclosed_area()
        # if not self.is_closed or self.path_length <= 0:
        #     return None
        #
        # path = copy.deepcopy(self)
        # path.remove_duplicate_edges()
        # path.remove_arcs()
        # twice_area = 0
        # for edge in path.list_of_edges:
        #     twice_area += edge.p1.x * edge.p2.y - edge.p2.x * edge.p1.y
        # return twice_area * 0.5


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
        if self.path_length != 4 or not self.is_continuous:
            return False

        arc_found = False
        for edge in self.list_of_edges:
            if edge.is_arc():
                if arc_found:
                    return False
                arc_found = True

        return arc_found

    def convert_circle_to_edges(self):
        if self.is_circle():
            circle_centre = Point3()
            circle_centre.x = self.list_of_edges[0].centre.x
            circle_centre.y = self.list_of_edges[0].centre.y
            circle_centre.z = self.list_of_edges[0].centre.z
            circle_radius = self.list_of_edges[0].radius

            self.list_of_edges = [
                Edge3(Point3(circle_centre.x, circle_centre.y + circle_radius, circle_centre.z),
                      Point3(circle_centre.x, circle_centre.y - circle_radius, circle_centre.z), radius=circle_radius, clockwise=False),
                Edge3(Point3(circle_centre.x, circle_centre.y - circle_radius, circle_centre.z),
                      Point3(circle_centre.x, circle_centre.y + circle_radius, circle_centre.z), radius=circle_radius, clockwise=False)
            ]
            return self

    def transform(self, transformation_matrix):
        # old_area = self.get_enclosed_area()
        for edge in self.list_of_edges:
            edge.transform(transformation_matrix)
        # new_area = self.get_enclosed_area()
        #
        # if old_area is not None and new_area is not None:
        #     if not floats_are_close(old_area, new_area):
        #         for edge in self.list_of_edges:
        #             if edge.is_arc():
        #                 edge.clockwise = not edge.clockwise
        self.update_path()
        return self

    def to_path2(self):
        path_2d = geometry_utils.two_d.path2.Path2()
        for edge in self.list_of_edges:
            path_2d.list_of_edges.append(edge.to_edge2())
        return path_2d

    def update_path(self):
        for edge in self.list_of_edges:
            edge.centre = edge.calculate_centre()
            edge.via = edge.get_via()
        return self

    def get_oriented_bounding_box(self):
        path_2d = self.to_path2()
        box = path_2d.get_oriented_bounding_box()
        return box

    def is_incomplete_circle(self):
        return (self.path_length == 1 and
                self.list_of_edges[0].is_arc() and
                self.list_of_edges[0].p2 != self.list_of_edges[0].p1)

    def complete_circle(self):
        if self.is_incomplete_circle():
            self.list_of_edges[0].p2 = copy.deepcopy(self.list_of_edges[0].p1)
            self.update_path()
        return self


def is_path3(input_variable):
    return isinstance(input_variable, Path3)
