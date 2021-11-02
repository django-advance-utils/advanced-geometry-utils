from Point2 import Point2
from Vector2 import Vector2
from Matrix3 import Matrix3


if __name__ == '__main__':
    newVector = Vector2(3, 6)
    #newVector2 = newVector.reverse()
    newMatrix = Matrix3([[4, 3, 2], [1, 4, 5], [6, 7, 8]])
    newMatrix2 = Matrix3([[9, 7, 4], [2, 9, 6], [3, 9, 0]])
    #newMatrix.make_rotation(2.1)
    #newMatrix.make_translation(newVector)
    #newMatrix3 = Matrix3()
    newMatrix3 = newMatrix * newMatrix2
    #newMatrix4 = Matrix3()
    #newMatrix4 = newMatrix.make_translation(newVector)
    print(newMatrix3.vals)
