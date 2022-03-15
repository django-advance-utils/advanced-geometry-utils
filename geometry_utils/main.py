from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.matrix4 import Matrix4
from geometry_utils.three_d.path3 import Path3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.ellipse import Ellipse
from geometry_utils.two_d.intersection import Intersection
from geometry_utils.two_d.matrix3 import Matrix3
from geometry_utils.two_d.path2 import Path2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2

import geometry_utils.maths_utility as maths_utility

from geometry_utils.path_field_interpreter import PathFieldInterpreter

import math

if __name__ == '__main__':
    perp = Vector3(-0.0, -0.0, -1.0)
    y_vec = Vector3(-1, 0.0, 0.0)
    print perp
