from two_d.edge2 import Edge2


class Path2:
    def __init__(self, list_of_edges):
        if isinstance(list_of_edges, list) and all(isinstance(edge, Edge2) for edge in list_of_edges):
            self.list_of_edges = list_of_edges
            self.first_edge = self.list_of_edges[0]
            self.last_edge = self.list_of_edges[-1]

    def is_continuous(self):
        continuity = True
        for edge, next_edge in zip(self.list_of_edges, self.list_of_edges[1:]):
            if edge.p2 != next_edge.p1:
                continuity = False
        return continuity

    def is_closed(self):
        return self.last_edge.p2 == self.first_edge.p1 and self.is_continuous()
