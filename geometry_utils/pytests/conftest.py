import math

import pytest

from geometry_utils.three_d.axis_aligned_box3 import AxisAlignedBox3
from geometry_utils.three_d.edge3 import Edge3
from geometry_utils.three_d.matrix4 import Matrix4
from geometry_utils.three_d.path3 import Path3
from geometry_utils.three_d.point3 import Point3
from geometry_utils.three_d.vector3 import Vector3
from geometry_utils.two_d.axis_aligned_box2 import AxisAlignedBox2
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.intersection import Intersection
from geometry_utils.two_d.matrix3 import Matrix3
from geometry_utils.two_d.path2 import Path2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2

'''
Point2 
'''


@pytest.fixture(scope="session")
def test_point2_1():
    return Point2(1.0, 1.0)


@pytest.fixture(scope="session")
def test_point2_2():
    return Point2(1.0, 0.0)


@pytest.fixture(scope="session")
def test_point2_3():
    return Point2(1.0, 1.0)


@pytest.fixture(scope="session")
def test_point2_4():
    return Point2(0.0, 0.0)


@pytest.fixture(scope="session")
def test_point2_5():
    return Point2(0.0, 1.0)


'''
Point3
'''


@pytest.fixture(scope="session")
def test_point3_1():
    return Point3(1.0, 1.0, 1.0)


@pytest.fixture(scope="session")
def test_point3_2():
    return Point3(1.0, 0.0, 0.0)


@pytest.fixture(scope="session")
def test_point3_3():
    return Point3(1.0, 1.0, 1.0)


'''
Vector2
'''


@pytest.fixture(scope="session")
def test_vector2_1():
    return Vector2(1.0, 1.0)


@pytest.fixture(scope="session")
def test_vector2_2():
    return Vector2(1.0, 0.0)


@pytest.fixture(scope="session")
def test_vector2_3():
    return Vector2(1.0, 1.0)


@pytest.fixture(scope="session")
def test_vector2_4():
    return Vector2(0.0, 0.0)


@pytest.fixture(scope="session")
def test_vector2_5():
    return Vector2(0.0, 1.0)


@pytest.fixture(scope="session")
def test_vector2_6():
    return Vector2(1.0, 0.0)


'''
Vector3
'''


@pytest.fixture(scope="session")
def test_vector3_1():
    return Vector3(1.0, 1.0, 1.0)


@pytest.fixture(scope="session")
def test_vector3_2():
    return Vector3(1.0, 0.0, 0.0)


@pytest.fixture(scope="session")
def test_vector3_3():
    return Vector3(1.0, 1.0, 1.0)


@pytest.fixture(scope="session")
def test_vector3_4():
    return Vector3(0.0, 0.0, 0.0)


'''
Edge2
'''


@pytest.fixture(scope="session")
def test_edge2_1():
    return Edge2()


@pytest.fixture(scope="session")
def test_edge2_2():
    p1 = Point2(0.0, 0.0)
    p2 = Point2(2.0, 2.0)
    return Edge2(p1, p2)


@pytest.fixture(scope="session")
def test_edge2_3():
    p1 = Point2(2.0, 2.0)
    p2 = Point2(4.0, 4.0)
    return Edge2(p1, p2)


@pytest.fixture(scope="session")
def test_edge2_4():
    p1 = Point2(0.0, 0.0)
    p2 = Point2(2.0, 2.0)
    return Edge2(p1, p2)


@pytest.fixture(scope="session")
def test_edge2_5():
    p1 = Point2(0.0, 0.0)
    p2 = Point2(2.0, 2.0)
    return Edge2(p1, p2, 2.0)


@pytest.fixture(scope="session")
def test_edge2_6():
    p1 = Point2(0.0, 0.0)
    p2 = Point2(0.0, 0.0)
    return Edge2(p1, p2, 5.0)


@pytest.fixture(scope="session")
def test_circle_points_1():
    # this just generates a list of points in a circle at 1 degree increments at a radius of 600
    radius = 600.0

    circle = []
    for i in range(360):
        t = ((math.pi * 2) / 360.0) * float(i)
        circle.append(Point2((math.sin(t) * radius),
                             (math.cos(t) * radius)))

    return circle


'''
Edge3
'''


@pytest.fixture(scope="session")
def test_edge3_1():
    return Edge3()


@pytest.fixture(scope="session")
def test_edge3_2():
    p1 = Point3(0.0, 0.0, 0.0)
    p2 = Point3(2.0, 2.0, 2.0)
    return Edge3(p1, p2)


'''
Matrix3
'''


@pytest.fixture(scope="session")
def test_matrix3_1():
    return Matrix3()


@pytest.fixture(scope="session")
def test_matrix3_2():
    return Matrix3([[1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0]])


'''
Matrix4
'''


@pytest.fixture(scope="session")
def test_matrix4_1():
    return Matrix4()


@pytest.fixture(scope="session")
def test_matrix4_2():
    return Matrix4([[1.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0]])


'''
AxisAlignedBox2
'''


@pytest.fixture(scope="session")
def test_box2_1():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))


@pytest.fixture(scope="session")
def test_box2_2():
    return AxisAlignedBox2(Point2(), Point2())


@pytest.fixture(scope="session")
def test_box2_3():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(0.0, 0.0))


@pytest.fixture(scope="session")
def test_box2_4():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(0.0, 0.0))


'''
AxisAlignedBox3
'''


@pytest.fixture(scope="session")
def test_box3_1():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))


@pytest.fixture(scope="session")
def test_box3_2():
    return AxisAlignedBox3(Point3(), Point3())


@pytest.fixture(scope="session")
def test_box3_3():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))


@pytest.fixture(scope="session")
def test_box3_4():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))


'''
Path2
'''


@pytest.fixture(scope="session")
def path2_1():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                          Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))]
    return path


@pytest.fixture(scope="session")
def path2_2():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                          Edge2(Point2(3.0, 3.0), Point2(4.0, 4.0))]
    return path


@pytest.fixture(scope="session")
def path2_3():
    path = Path2()
    path.list_of_edges = [Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                          Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                          Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))]
    return path


'''
Path3
'''


@pytest.fixture(scope="session")
def path3_1():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                          Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))]
    return path


@pytest.fixture(scope="session")
def path3_2():
    path = Path3()
    path.list_of_edges = [Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                          Edge3(Point3(3.0, 3.0, 3.0), Point3(4.0, 4.0, 4.0))]
    return path


@pytest.fixture(scope="session")
def path3_3():
    path = Path2()
    path.list_of_edges = [Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                          Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                          Edge3(Point3(4.0, 4.0, 4.0), Point3(5.0, 5.0, 5.0))]
    return path


'''
Intersection
'''


@pytest.fixture(scope="session")
def intersection1():
    return Intersection()
