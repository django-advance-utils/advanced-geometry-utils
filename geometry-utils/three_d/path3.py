from maths_utility import is_list
from three_d.axis_aligned_box3 import AxisAlignedBox3
from three_d.edge3 import is_edge3


class Path3:
    def __init__(self, list_of_edges):
        if is_list(list_of_edges) and all(is_edge3(edge) for edge in list_of_edges):
            self.list_of_edges = list_of_edges
            self.first_edge = self.list_of_edges[0]
            self.last_edge = self.list_of_edges[-1]

    def is_closed(self):
        return self.last_edge.p2 == self.first_edge.p1 and self.is_continuous()

    def is_continuous(self):
        continuity = True
        for edge, next_edge in zip(self.list_of_edges, self.list_of_edges[1:]):
            if edge.p2 != next_edge.p1:
                continuity = False
        return continuity

    def get_path_bounds(self):
        path_bounds = AxisAlignedBox3()
        for edge in self.list_of_edges:
            path_bounds.include(edge.get_edge_bounds())
        return path_bounds

