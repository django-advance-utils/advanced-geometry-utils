from three_d.edge3 import Edge3
from three_d.point3 import Point3
from three_d.path3 import Path3

if __name__ == '__main__':

    first_edge = Edge3(Point3(0.0, 0.0, 0.0), Point3(1.0, 1.0, 1.0))
    second_edge = Edge3(Point3(1.0, 1.0, 1.0), Point3(2.0, 2.0, 2.0))
    third_edge = Edge3(Point3(2.0, 2.0, 2.0), Point3(0.0, 0.0, 0.0))
    list_of_edges = [first_edge, second_edge, third_edge]
    path = Path3(list_of_edges)
    print(path.is_continuous())
    print(path.is_closed())
    print(path.get_path_bounds().min.x)
    print(path.get_path_bounds().min.y)
    print(path.get_path_bounds().min.z)
    print(path.get_path_bounds().max.x)
    print(path.get_path_bounds().max.y)
    print(path.get_path_bounds().max.z)


