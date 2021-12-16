import unittest

from geometry_utils.two_d.ellipse import Ellipse
from geometry_utils.two_d.point2 import Point2
from geometry_utils.maths_utility import PI

test_ellipse = Ellipse(Point2(0, 1), end=Point2(2, 1), major_radius=1, minor_radius=1, clockwise=True, angle=0.0)


class TestEllipse(unittest.TestCase):
    def test_ellipse_string_parameters(self):
        with self.assertRaises(TypeError):
            return Ellipse(("0", "0"), ("0", "0"), (0, 0))

    def test_ellipse_centre(self):
        self.assertEqual(test_ellipse.centre, Point2(1, 1))

    def test_ellipse_validity(self):
        self.assert_(test_ellipse.test_validity())

    def test_ellipse_get_arc_sweep(self):
        self.assertEqual(test_ellipse.get_arc_sweep(), PI)


if __name__ == '__main__':
    unittest.main()
