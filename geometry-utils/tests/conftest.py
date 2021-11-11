import pytest

from three_d.axis_aligned_box3 import AxisAlignedBox3
from three_d.edge3 import Edge3
from three_d.matrix4 import Matrix4
from three_d.path3 import Path3
from three_d.point3 import Point3
from three_d.vector3 import Vector3
from two_d.axis_aligned_box2 import AxisAlignedBox2
from two_d.edge2 import Edge2
from two_d.intersection import Intersection
from two_d.matrix3 import Matrix3
from two_d.path2 import Path2
from two_d.point2 import Point2
from two_d.vector2 import Vector2

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
def box2_1():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(2.0, 2.0))


@pytest.fixture(scope="session")
def box2_2():
    return AxisAlignedBox2()


@pytest.fixture(scope="session")
def box2_3():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(0.0, 0.0))


@pytest.fixture(scope="session")
def box2_4():
    return AxisAlignedBox2(Point2(0.0, 0.0), Point2(0.0, 0.0))


'''
AxisAlignedBox3
'''


@pytest.fixture(scope="session")
def box3_1():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(2.0, 2.0, 2.0))


@pytest.fixture(scope="session")
def box3_2():
    return AxisAlignedBox3()


@pytest.fixture(scope="session")
def box3_3():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))


@pytest.fixture(scope="session")
def box3_4():
    return AxisAlignedBox3(Point3(0.0, 0.0, 0.0), Point3(0.0, 0.0, 0.0))


'''
Path2
'''


@pytest.fixture(scope="session")
def path2_1():
    return Path2([Edge2(Point2(0.0, 0.0), Point2(1.0, 1.0)),
                  Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                  Edge2(Point2(2.0, 2.0), Point2(0.0, 0.0))])


@pytest.fixture(scope="session")
def path2_2():
    return Path2([Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                  Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                  Edge2(Point2(3.0, 3.0), Point2(4.0, 4.0))])


@pytest.fixture(scope="session")
def path2_3():
    return Path2([Edge2(Point2(1.0, 1.0), Point2(2.0, 2.0)),
                  Edge2(Point2(2.0, 2.0), Point2(3.0, 3.0)),
                  Edge2(Point2(4.0, 4.0), Point2(5.0, 5.0))])


'''
Path3
'''


@pytest.fixture(scope="session")
def path3_1():
    return Path3([Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0)),
                  Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                  Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))])


@pytest.fixture(scope="session")
def path3_2():
    return Path3([Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                  Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                  Edge3(Point3(3.0, 3.0, 3.0), Point3(4.0, 4.0, 4.0))])


@pytest.fixture(scope="session")
def path3_3():
    return Path3([Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0)),
                  Edge3(Point3(2.0, 2.0, 2.0), Point3(3.0, 3.0, 3.0)),
                  Edge3(Point3(4.0, 4.0, 4.0), Point3(5.0, 5.0, 5.0))])


'''
Intersection
'''


@pytest.fixture(scope="session")
def intersection1():
    return Intersection()
