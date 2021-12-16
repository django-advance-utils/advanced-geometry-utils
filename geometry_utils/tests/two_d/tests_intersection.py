import unittest

from geometry_utils.two_d.intersection import Intersection
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.point2 import Point2

test_edge_1 = Edge2(Point2(1, 2), Point2(4, 2))
test_edge_2 = Edge2(Point2(2, 1), Point2(2, 4))
test_edge_circle = Edge2(Point2(1, 1), Point2(1, 1), 1)
list_of_intersection = []
intersection_1 = Intersection()
intersection_2 = Intersection()
intersection_1.intersect(test_edge_1, test_edge_2, list_of_intersection)
intersection_2.intersect(test_edge_1, test_edge_circle, list_of_intersection)


class TestIntersection(unittest.TestCase):
    def test_line_intersect_line(self):
        self.assertEqual(list_of_intersection[0].point, Point2(2, 2))

    def test_line_intersect_circle(self):
        self.assertEqual(list_of_intersection[1].point, Point2(1, 2))


if __name__ == '__main__':
    unittest.main()
