import math
import unittest

from geometry_utils.maths_utility import floats_are_close
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2
from geometry_utils.maths_utility import HALF_PI, QUARTER_PI

test_edge2_1 = Edge2()
test_edge2_2 = Edge2(Point2(0.0, 0.0), Point2(2.0, 2.0))
test_edge2_3 = Edge2(Point2(2.0, 2.0), Point2(4.0, 4.0))
test_edge2_4 = Edge2(Point2(0.0, 0.0), Point2(2.0, 2.0))
test_edge2_5 = Edge2(Point2(0.0, 0.0), Point2(2.0, 2.0), 2.0)
test_edge2_6 = Edge2(Point2(0.0, 0.0), Point2(0.0, 0.0), 5.0)

radius = 600.0
test_circle_points_1 = []
for i in range(360):
    t = ((math.pi * 2) / 360.0) * float(i)
    test_circle_points_1.append(Point2((math.sin(t) * radius), (math.cos(t) * radius)))


class TestEdge2(unittest.TestCase):
    def test_edge2_float_arguments(self):
        with self.assertRaises(TypeError):
            return Edge2("0", "0", "0")

    def test_edge2_to_edge2_equality(self):
        self.assertEqual(test_edge2_2, test_edge2_4)

    def test_edge2_to_float_equality(self):
        with self.assertRaises(TypeError):
            self.assertEqual(test_edge2_1, 9.0)

    def test_edge2_to_edge2_inequality(self):
        self.assertNotEqual(test_edge2_2, test_edge2_1)

    def test_edge2_to_float_inequality(self):
        with self.assertRaises(TypeError):
            return test_edge2_1 != 9.0

    def test_edge2_is_arc(self):
        self.assert_(not test_edge2_2.is_arc())
        self.assert_(test_edge2_5.is_arc())

    def test_edge2_get_sweep_angle(self):
        self.assertEqual(test_edge2_5.get_sweep_angle(), HALF_PI)

    def test_edge2_point_parametric(self):
        self.assertEqual(test_edge2_2.point_parametric(0.0), test_edge2_2.p1)
        self.assertEqual(test_edge2_2.point_parametric(1.0), test_edge2_2.p2)
        self.assertEqual(test_edge2_1.point_parametric(0.5), test_edge2_1.p1)

    def test_edge2_point_parametric_with_point_argument(self):
        with self.assertRaises(TypeError):
            return test_edge2_1.point_parametric(test_edge2_2)

    def test_edge2_parametric_point_arcs(self):
        # anticlockwise 10 deg
        e1 = Edge2(test_circle_points_1[10], test_circle_points_1[0], 600.0, False, False)

        # endpoints and centre point
        assert floats_are_close(e1.parametric_point(test_circle_points_1[355]), 1.5)
        assert floats_are_close(e1.parametric_point(test_circle_points_1[0]), 1.0)
        assert floats_are_close(e1.parametric_point(test_circle_points_1[5]), 0.5)
        assert floats_are_close(e1.parametric_point(test_circle_points_1[10]), 0.0)
        assert floats_are_close(e1.parametric_point(test_circle_points_1[15]), -0.5)

        e2 = Edge2(test_circle_points_1[36], test_circle_points_1[202], 600.0, True, False)

        # endpoints and centre point
        assert floats_are_close(e2.parametric_point(test_circle_points_1[285]), 1.5)
        assert floats_are_close(e2.parametric_point(test_circle_points_1[202]), 1.0)
        assert floats_are_close(e2.parametric_point(test_circle_points_1[119]), 0.5)
        assert floats_are_close(e2.parametric_point(test_circle_points_1[36]), 0.0)
        assert floats_are_close(e2.parametric_point(test_circle_points_1[313]), -0.5)

        # large arc
        e3 = Edge2(test_circle_points_1[40], test_circle_points_1[30], 600.0, True, True)

        assert floats_are_close(e3.parametric_point(test_circle_points_1[30]), 1.0)
        assert floats_are_close(e3.parametric_point(test_circle_points_1[215]), 0.5)
        assert floats_are_close(e3.parametric_point(test_circle_points_1[40]), 0.0)

        # clockwise semicircle (large)
        e4 = Edge2(test_circle_points_1[0], test_circle_points_1[180], 600.0, True, True)

        assert floats_are_close(e4.parametric_point(test_circle_points_1[180]), 1.0)
        assert floats_are_close(e4.parametric_point(test_circle_points_1[90]), 0.5)
        assert floats_are_close(e4.parametric_point(test_circle_points_1[0]), 0.0)

        # clockwise semicircle (small) should be the same as the large version
        e5 = Edge2(test_circle_points_1[0], test_circle_points_1[180], 600.0, True, False)

        assert floats_are_close(e5.parametric_point(test_circle_points_1[180]), 1.0)
        assert floats_are_close(e5.parametric_point(test_circle_points_1[90]), 0.5)
        assert floats_are_close(e5.parametric_point(test_circle_points_1[0]), 0.0)

        # anticlockwise semicircle (large)
        e6 = Edge2(test_circle_points_1[180], test_circle_points_1[0], 600.0, False, True)

        assert floats_are_close(e6.parametric_point(test_circle_points_1[0]), 1.0)
        assert floats_are_close(e6.parametric_point(test_circle_points_1[90]), 0.5)
        assert floats_are_close(e6.parametric_point(test_circle_points_1[180]), 0.0)

        # anticlockwise semicircle (small) should be the same as the large version
        e7 = Edge2(test_circle_points_1[180], test_circle_points_1[0], 600.0, False, False)

        assert floats_are_close(e7.parametric_point(test_circle_points_1[0]), 1.0)
        assert floats_are_close(e7.parametric_point(test_circle_points_1[90]), 0.5)
        assert floats_are_close(e7.parametric_point(test_circle_points_1[180]), 0.0)

    def test_edge2_parametric_point(self):
        self.assertEqual(test_edge2_2.parametric_point(test_edge2_2.p1), 0.0)
        self.assert_(floats_are_close(test_edge2_2.parametric_point(test_edge2_2.p2), 1.0))

    def test_edge2_parametric_point_with_float(self):
        with self.assertRaises(TypeError):
            return test_edge2_1.parametric_point(9.0)

    def test_edge2_get_tangent(self):
        self.assertEqual(test_edge2_2.get_tangent(test_edge2_2.p1), Vector2(2.0 / math.sqrt(8.0), 2.0 / math.sqrt(8.0)))

    def test_edge2_calculate_centre(self):
        self.assertEqual(test_edge2_2.calculate_centre(), Point2(1.0, 1.0))
        self.assertEqual(test_edge2_5.calculate_centre(), Point2(0.0, 2.0))
        self.assertEqual(test_edge2_6.calculate_centre(), test_edge2_6.p2)

    def test_edge2_get_edge_bounds(self):
        self.assertEqual(test_edge2_2.get_edge_bounds(), AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0)))
    '''
    def test_edge2_intersect_edge2(self):
        list_of_intersects = []
        test_edge2_2.intersect(test_edge2_3, list_of_intersects)
        self.assertEqual(list_of_intersects[-1].point, Point2(0.0, 0.0))

    def test_edge2_intersect_float(self):
        with self.assertRaises(TypeError):
            return test_edge2_1.intersect(9.0, 9.0)
    '''
    def test_edge2_offset_edge(self):
        offset_vector = Vector2(1.0, 1.0)
        edge_to_be_offset = Edge2(Point2(0, 0), Point2(3, 3))
        edge_to_be_offset.offset_edge(offset_vector)
        offset_edge = Edge2(Point2(1, 1), Point2(4, 4))

        self.assertEqual(edge_to_be_offset, offset_edge)

    def test_edge2_offset_edge_with_float(self):
        with self.assertRaises(TypeError):
            return test_edge2_1.offset_edge(9.0)

    def test_edge2_flip_xy(self):
        edge_to_be_flipped = Edge2(Point2(0, 1), Point2(2, 3))
        edge_to_be_flipped.flip_xy()
        flipped_edge = Edge2(Point2(1, 0), Point2(3, 2))

        self.assertEqual(edge_to_be_flipped, flipped_edge)

    def test_edge2_mirror_y(self):
        edge_to_be_mirrored = Edge2(Point2(1, 0), Point2(2, 3))
        edge_to_be_mirrored.mirror_y()
        mirrored_edge = Edge2(Point2(-1, 0), Point2(-2, 3))

        self.assertEqual(edge_to_be_mirrored, mirrored_edge)

    def test_edge2_is_circle(self):
        circle = Edge2(Point2(1, 1), Point2(1, 1), 2)
        self.assert_(circle.is_circle())

    def test_edge2_get_arc_start_angle(self):
        start_angle = test_edge2_5.get_arc_start_angle()
        self.assertEqual(start_angle, -HALF_PI)

    def test_edge2_get_arc_end_angle(self):
        end_angle = test_edge2_5.get_arc_end_angle()
        self.assertEqual(end_angle, 0.0)

    def test_edge2_flatten_arc(self):
        list_of_arc_edges = test_edge2_5.flatten_arc()
        arc = False
        for edge in list_of_arc_edges:
            if edge.is_arc():
                arc = True

        self.assert_(not arc)
        self.assertEqual(list_of_arc_edges[0].p1, test_edge2_5.p1)
        self.assertEqual(list_of_arc_edges[-1].p2, test_edge2_5.p2)

    def test_edge2_rotate(self):
        edge_to_be_rotated = Edge2(Point2(0, 0), Point2(1, 0), 1)
        edge_to_be_rotated.rotate(90.0)

        self.assertEqual(edge_to_be_rotated.p1, Point2(0, 0))
        self.assertEqual(edge_to_be_rotated.p2, Point2(0, 1))

    def test_edge2_rotate_with_string(self):
        with self.assertRaises(TypeError):
            return test_edge2_5.rotate("0")

    def test_edge2_parallel_to_edge(self):
        parallel_edge = Edge2(Point2(1, 1), Point2(3, 3))
        self.assert_(parallel_edge.is_parallel_to(test_edge2_2))

    def test_edge2_parallel_to_float(self):
        with self.assertRaises(TypeError):
            test_edge2_1.is_parallel_to(9.0)

    def test_edge2_perpendicular_to_edge(self):
        perpendicular_1 = Edge2(Point2(-1.0, 0.0), Point2(1.0, 0.0))
        perpendicular_2 = Edge2(Point2(0.0, 0.0), Point2(0.0, 1.0))

        self.assert_(perpendicular_1.is_perpendicular_to(perpendicular_2))

    def test_edge2_perpendicular_to_float(self):
        with self.assertRaises(TypeError):
            return test_edge2_1.is_perpendicular_to(9.0)

    def test_edge2_get_slope(self):
        self.assertEqual(test_edge2_2.get_slope(), 1.0)

    def test_edge2_get_slope_vertical(self):
        vertical_edge = Edge2(Point2(1, 1), Point2(1, 2))
        self.assertEqual(vertical_edge.get_slope(), "Vertical")

    def test_edge2_get_slope_arc(self):
        with self.assertRaises(TypeError):
            return test_edge2_5.get_slope()

    def test_edge2_edge_length(self):
        self.assert_(floats_are_close(test_edge2_2.edge_length(), 2.828427))

    '''
    def test_edge2_edge_length_arc(self):
        with self.assertRaises(TypeError):
            return test_edge2_5.edge_length()
    '''

    def test_edge2_angle_to_x_axis(self):
        self.assertEqual(test_edge2_2.angle_to_x_axis(), QUARTER_PI)

    def test_edge2_angle_to_edge(self):
        self.assertEqual(test_edge2_2.angle_to_edge(test_edge2_4), 0.0)

    def test_edge2_angle_to_edge_arc(self):
        with self.assertRaises(TypeError):
            return test_edge2_5.angle_to_edge(test_edge2_4)

    def test_edge2_minimum_y(self):
        self.assertEqual(test_edge2_2.minimum_y(), 0.0)

    def test_edge2_maximum_y(self):
        self.assertEqual(test_edge2_2.maximum_y(), 2.0)


if __name__ == '__main__':
    unittest.main()
