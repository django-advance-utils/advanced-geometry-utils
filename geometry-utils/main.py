from three_d.matrix4 import Matrix4
from three_d.vector3 import Vector3
from two_d.edge2 import Edge2
from two_d.matrix3 import Matrix3
from two_d.point2 import Point2
from two_d.vector2 import Vector2

if __name__ == '__main__':
    new_point = Point2(1, 2)
    new_point2 = Point2(5, 8)

    newVector = Vector2(3, 6)
    newVector2 = newVector.reverse()

    newVector3 = Vector3(1.0, 2.0, 3.0)

    newMatrix = Matrix3([[4, 3, 2], [1, 4, 5], [6, 7, 8]])
    newMatrix2 = Matrix3([[9, 7, 4], [2, 9, 6], [3, 9, 0]])
    newMatrix.make_rotation(2.1)
    newMatrix.make_translation(newVector)
    newMatrix3 = Matrix3()
    newMatrix3 = newMatrix * newMatrix2
    newMatrix4 = Matrix4()
    newMatrix4.make_x_rotation(0.0)
    newMatrix5 = Matrix4()
    newMatrix6 = newMatrix5 * newMatrix4

    newEdge = Edge2(new_point, new_point2, 15.0)

    print(newMatrix6.vals)
