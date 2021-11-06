from three_d.axis_aligned_box3 import AxisAlignedBox3
from two_d.axis_aligned_box2 import AxisAlignedBox2

if __name__ == '__main__':
    def box4():
        return AxisAlignedBox2()

    box = AxisAlignedBox2()

    print(box4().max.x)
