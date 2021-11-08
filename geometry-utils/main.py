from two_d.edge2 import Edge2
from two_d.path2 import Path2
from two_d.point2 import Point2

if __name__ == '__main__':

    first_edge = Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0))
    second_edge = Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0))
    third_edge = Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))

    list_of_edges = [first_edge, second_edge, third_edge]
    path = Path2(list_of_edges)
    print(path.is_continuous())
    print(path.is_closed())

