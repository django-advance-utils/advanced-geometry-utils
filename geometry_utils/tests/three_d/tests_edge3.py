import unittest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.three_d.edge3 import Edge3

from math import sqrt


test_vector3_1 = Vector3(1.0, 1.0, 1.0)
test_vector3_2 = Vector3(1.0, 0.0, 0.0)
test_vector3_3 = Vector3(1.0, 1.0, 1.0)
test_vector3_4 = Vector3(0.0, 0.0, 0.0)

test_edge3_1 = Edge3()
test_edge3_2 = Edge3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))


class TestEdge3(unittest.TestCase):
    def test_edge3_point_parametric(self):
        self.assertEqual(test_edge3_2.point_parametric(0.0), test_edge3_2.p1)
        self.assertEqual(test_edge3_2.point_parametric(1.0), test_edge3_2.p2)
        self.assertEqual(test_edge3_1.point_parametric(0.5), test_edge3_1.p1)

    def test_edge3_parametric_point(self):
        self.assertEqual(test_edge3_2.parametric_point(test_edge3_2.p1), 0.0)
        self.assertAlmostEquals(test_edge3_2.parametric_point(test_edge3_2.p2), 1.0)

    def test_edge3_get_tangent(self):
        self.assertEqual(test_edge3_2.get_tangent(), Vector3(2.0 / sqrt(12.0), 2.0 / sqrt(12.0), 2.0 / sqrt(12.0)))

    def test_edge3_get_arc_centre(self):
        self.assertEqual(test_edge3_2.calculate_arc_centre(), Point3(1.0, 1.0, 1.0))

    def test_edge3_get_edge_bounds(self):
        self.assertEqual(test_edge3_2.get_edge_bounds(), AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0)))


if __name__ == '__main__':
    unittest.main()
