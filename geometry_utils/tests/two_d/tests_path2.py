import unittest

from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.path2 import Path2
from geometry_utils.two_d.point2 import Point2

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

test_path2_4 = Path2()
test_path2_4.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                              Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                              Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                              Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))]


class TestPath2(unittest.TestCase):
    def test_path2_path2_equality(self):
        self.assertEqual(Path2(), Path2())

    def test_path2_float_equality(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Path2(), 9.0)

    def test_path2_get_first_edge(self):
        self.assertEqual(test_path2_1.get_first_edge, Edge2(Point2(), Point2(1.0, 1.0)))

    def test_path2_get_last_edge(self):
        self.assertEqual(test_path2_1.get_last_edge, Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0)))

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
        self.assert_(test_path_tuple, ((Point2(0.0, 0.0), Point2(1.0, 1.0)),
                                       (Point2(1.0, 1.0), Point2(2.0, 2.0)),
                                       (Point2(2.0, 2.0), Point2(0.0, 0.0))))

    def test_path2_remove_duplicate_edges(self):
        self.assert_(test_path2_4.remove_duplicate_edges(), test_path2_3)

    def test_path2_flip_xy(self):
        self.assert_(test_path2_1.flip_xy(), test_path2_1)

    def test_path2_mirror_y(self):
        self.assert_(test_path2_4.mirror_y(), [Edge2(Point2(-1.0, 1.0), Point2(-2.0, 2.0)),
                                               Edge2(Point2(-2.0, 2.0), Point2(-3.0, 3.0)),
                                               Edge2(Point2(-4.0, 4.0), Point2(-5.0, 5.0))])


if __name__ == '__main__':
    unittest.main()
