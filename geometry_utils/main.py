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

if __name__ == '__main__':
    # 2D
    test_vector2 = Vector2()
    test_point2 = Point2()
    test_matrix3 = Matrix3()
    test_edge2 = Edge2()
    test_box2 = AxisAlignedBox2()
    test_path2 = Path2()
    test_intersection = Intersection()
    test_ellipse = Ellipse()

    # 3D
    test_vector3 = Vector3()
    test_point3 = Point3()
    test_matrix4 = Matrix4()
    test_edge3 = Edge3()
    test_box3 = AxisAlignedBox3()
    test_path3 = Path3([test_edge3])
