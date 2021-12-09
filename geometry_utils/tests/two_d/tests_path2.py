import unittest

from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.path2 import Path2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2

test_path2_1 = Path2()
test_path2_1.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                              Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                              Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]

test_path2_2 = Path2()
test_path2_2.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                              Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                              Edge2(Point2(3.0, 3.0), Point2(4.0, 4.0))]

test_path2_3 = Path2()
test_path2_3.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                              Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                              Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))]

test_path2_5 = Path2()
test_path2_5.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                              Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                              Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))]


class TestPath2(unittest.TestCase):
    def test_path2_path2_equality(self):
        self.assertEqual(test_path2_3, test_path2_5)

    def test_path2_float_equality(self):
        with self.assertRaises(TypeError):
            self.assertEqual(test_path2_1, 9.0)

    def test_path2_equality_with_unequal_number_of_edges(self):
        test_path = Path2()
        with self.assertRaises(IndexError):
            self.assertEqual(test_path2_1, test_path)

    def test_path2_get_first_edge(self):
        self.assertEqual(test_path2_1.get_first_edge, Edge2(Point2(), Point2(1.0, 1.0)))

    def test_path2_get_first_edge_from_empty_list_of_edges(self):
        test_path = Path2()
        with self.assertRaises(IndexError):
            self.assert_(test_path.get_first_edge)

    def test_path2_get_last_edge(self):
        self.assertEqual(test_path2_1.get_last_edge, Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0)))

    def test_path2_get_last_edge_from_empty_list_of_edges(self):
        test_path = Path2()
        with self.assertRaises(IndexError):
            self.assert_(test_path.get_last_edge)

    def test_path2_path_length(self):
        self.assertEqual(test_path2_1.path_length, 3)

    def test_path2_continuity(self):
        self.assert_(test_path2_1.is_continuous)
        self.assert_(test_path2_2.is_continuous)

    def test_path2_no_continuity(self):
        self.assert_(not test_path2_3.is_continuous)

    def test_path2_closed(self):
        self.assert_(test_path2_1.is_closed)

    def test_path2_not_closed(self):
        self.assert_(not test_path2_3.is_closed)

    def test_path2_get_path_bounds(self):
        assert test_path2_1.get_path_bounds == AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))

    def test_path2_to_tuple_list(self):
        test_path_tuple = test_path2_1.to_tuple_list()
        self.assertEqual(test_path_tuple, [(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                                           (Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                           (Point2(2.0, 2.0), Point2(0.0, 0.0))])

    def test_path2_remove_duplicate_edges(self):
        test_path2_4 = Path2()
        test_path2_4.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                      Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                                      Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                                      Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))]
        self.assert_(test_path2_4.remove_duplicate_edges() == test_path2_3)

    def test_path2_flip_xy(self):
        self.assert_(test_path2_1.flip_xy() == test_path2_1)

    def test_path2_mirror_y(self):
        test_path2_4 = Path2()
        test_path2_4.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                      Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0))]
        mirrored_path = Path2()
        mirrored_path.list_of_edges = [Edge2(Point2(-1.0, 1.0), Point2(-2.0, 2.0)),
                                       Edge2(Point2(-2.0, 2.0), Point2(-3.0, 3.0))]
        test_path2_4.mirror_y()
        self.assertEqual(test_path2_4, mirrored_path)

    def test_path2_offset_path(self):
        offset_vector = Vector2(1.0, 1.0)
        offset_path = Path2()
        offset_path.list_of_edges = [Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                                     Edge2(Point2(3.0, 3.0), Point2(4.0, 4.0)),
                                     Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))]
        self.assertEqual(test_path2_2.offset_path(offset_vector), offset_path)

    def test_path2_rotate_around_vector_and_angle(self):
        test_path_to_rotate = Path2()
        test_path_to_rotate.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                             Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0))]
        rotation_vector = Vector2(0.0, 0.0)

        test_path_to_rotate.rotate_around(rotation_vector, 90.0)

        rotated_path = Path2()
        rotated_path.list_of_edges = [Edge2(Point2(-1.0, 1.0), Point2(-2.0, 2.0)),
                                      Edge2(Point2(-2.0, 2.0), Point2(-3.0, 3.0))]

        self.assertEqual(test_path_to_rotate, rotated_path)

    def test_path2_close_path(self):
        test_path_to_close = Path2()
        test_path_to_close.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                            Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0))]
        test_path_to_close.close_path()

        closed_path = Path2()
        closed_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                     Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                                     Edge2(Point2(3.0, 3.0), Point2(1.0, 1.0))]

        self.assertEqual(test_path_to_close, closed_path)

    def test_path2_is_circle(self):
        test_circle_path = Path2()
        test_circle_path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(1.0, 1.0), 1.0)]

        self.assert_(test_circle_path.is_circle())

    def test_path2_get_enclosed_area(self):
        test_path2_4 = Path2()
        test_path2_4.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                                      Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                      Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                      Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
        self.assert_(test_path2_4.get_enclosed_area() == test_path2_1)

    def test_path2_remove_arcs(self):
        test_path_to_remove_arcs = Path2()
        test_path_to_remove_arcs.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0), 1.0, True),
                                                  Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0))]
        test_path_to_remove_arcs.remove_arcs()

        self.assertEqual(test_path_to_remove_arcs.list_of_edges[0].p1, Point2(0.0, 0.0))
        self.assertEqual(test_path_to_remove_arcs.list_of_edges[-2].p2, Point2(1.0, 1.0))


if __name__ == '__main__':
    unittest.main()
