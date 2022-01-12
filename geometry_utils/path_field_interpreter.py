from geometry_utils.two_d.path2 import Path2, is_path2
from geometry_utils.three_d.path3 import Path3, is_path3


class PathFieldInterpreter(Path2, object):
    # Symbols used in the pathfield
    NEW_PATH_CHAR = '|'
    LAYER_CHAR = '&'
    NAME_CHAR = '@'
    POINT_SEPERATOR = ';'
    POINT_ELEMENT_SEPERATOR = ':'
    CLOSED_PATH_INDICATOR = '#'
    MIRRORED_PATH_INDICATOR = '^'
    MIRRORED_PATH_POINT_INDICATOR = '*'
    LINE_STYLE_INDICATOR = '%'
    FILL_INDICATOR = '#'
    CURVE_LARGE_CLOCK = '{'
    CURVE_LARGE_ANTICLOCK = '}'
    CURVE_SMALL_CLOCK = '('
    CURVE_SMALL_ANTICLOCK = ')'
    RELATIVE_CHAR = '~'
    TYPE_DELIMITER_CHAR = '"'
    INCLUDE_START = '?'
    INCLUDE_DELIMITER = ','
    INCLUDE_CONDITION_DELIMITER = '?'
    SPECIAL_SHAPES = '_'
    FUNCTION_CHAR = '!'

    TAG_START_CHAR = '<'
    TAG_END_CHAR = '>'

    def __init__(self):
        super(PathFieldInterpreter, self).__init__()
        self.write_buffer = ""
        self.read_buffer = ""

    def clear_path(self):
        self.write_buffer = ""
        self.read_buffer = ""
        self.list_of_edges = []

    def add_path(self, path):
        def format_num(num):
            try:
                str_num = "%.2f" % float(num)
            except ValueError:
                return "%s" % num
            if str_num == '0.00':
                return '0'
            return str_num.rstrip('0').rstrip('.')

        def get_curve_indicator(edge):
            """
            Retrieves the correct curve indicator given large and clockwise parameters
            for a curve.
            @param edge:
            @return:
            """
            if edge.large and edge.clockwise:
                return self.CURVE_LARGE_CLOCK
            elif edge.large and not edge.clockwise:
                return self.CURVE_LARGE_ANTICLOCK
            elif not edge.large and edge.clockwise:
                return self.CURVE_SMALL_CLOCK
            elif not edge.large and not edge.clockwise:
                return self.CURVE_SMALL_ANTICLOCK

        def add_point(index, path_length, point, last, delimiter_buffer, is_3d):
            if format_num(point.x) != last[0]:
                self.write_buffer += format_num(point.x)
                last[0] = format_num(point.x)
            elif index == 0 and path_length == 1:
                self.write_buffer += format_num(point.x)

            delimiter_buffer += self.POINT_ELEMENT_SEPERATOR

            if format_num(point.y) != last[1]:
                self.write_buffer += delimiter_buffer + format_num(point.y)
                last[1] = format_num(point.y)
                delimiter_buffer = self.POINT_ELEMENT_SEPERATOR
            elif index == 0 and path_length == 1:
                self.write_buffer += delimiter_buffer + last_y
                delimiter_buffer = self.POINT_ELEMENT_SEPERATOR
            else:
                delimiter_buffer += self.POINT_ELEMENT_SEPERATOR

            if is_3d:
                if format_num(point.z) != last[2]:
                    self.write_buffer += delimiter_buffer + format_num(point.z)
                    last[2] = point.z

            return last, delimiter_buffer

        if self.write_buffer != "":
            self.write_buffer += self.NEW_PATH_CHAR

        if path.layers:
            first = True
            for layer in path.layers:
                if not first:
                    self.write_buffer += ","
                self.write_buffer += layer
                first = False

            self.write_buffer += self.LAYER_CHAR

        if path.name != "":
            self.write_buffer += path.name + self.NAME_CHAR

        is_3d = False
        if is_path3(path):
            is_3d = True

        last = ["0", "0", "0"]
        last_x = '0'
        last_y = '0'
        last_z = '0'
        last_r = '0'
        indicator_buffer = ""
        path_length = path.path_length
        last_index = path_length - 1
        for index, edge in enumerate(path.list_of_edges):

            if path.is_closed and index == (path.path_length - 1):
                self.write_buffer += self.CLOSED_PATH_INDICATOR
            else:
                delimiter_buffer = ""
                if index == 0 or edge.p1 != path.list_of_edges[index - 1].p2:
                    last, delimiter_buffer = add_point(index, path_length, edge.p1, last, delimiter_buffer, is_3d)
                    # if format_num(edge.p1.x) != last_x:
                    #     self.write_buffer += format_num(edge.p1.x)
                    #     last_x = format_num(edge.p1.x)
                    # elif index == 0 and path.path_length == 1:
                    #     self.write_buffer += format_num(edge.p1.x)
                    #
                    # delimiter_buffer += self.POINT_ELEMENT_SEPERATOR
                    #
                    # if format_num(edge.p1.y) != last_y:
                    #     self.write_buffer += delimiter_buffer + format_num(edge.p1.y)
                    #     last_y = format_num(edge.p1.y)
                    #     delimiter_buffer = self.POINT_ELEMENT_SEPERATOR
                    # elif index == 0 and path.path_length == 1:
                    #     self.write_buffer += delimiter_buffer + last_y
                    #     delimiter_buffer = self.POINT_ELEMENT_SEPERATOR
                    # else:
                    #     delimiter_buffer += self.POINT_ELEMENT_SEPERATOR
                    #
                    # if is_3d:
                    #     if format_num(edge.p1.z) != last_z:
                    #         self.write_buffer += delimiter_buffer + format_num(edge.p1.z)
                    #         last_z = format_num(edge.p1.z)
                    if index != (path.path_length - 1):
                         self.write_buffer += self.POINT_SEPERATOR

                delimiter_buffer = ""
                last, delimiter_buffer = add_point(index, path_length, edge.p2, last, delimiter_buffer, is_3d)

                # if format_num(edge.p2.x) != last_x:
                #     self.write_buffer += format_num(edge.p2.x)
                #     last_x = format_num(edge.p2.x)
                #
                # elif index == 0 and path.path_length == 1:
                #     self.write_buffer += format_num(edge.p2.x)
                #
                # delimiter_buffer += self.POINT_ELEMENT_SEPERATOR
                #
                # if format_num(edge.p2.y) != last_y:
                #     self.write_buffer += delimiter_buffer + format_num(edge.p2.y)
                #     last_y = format_num(edge.p1.y)
                #     delimiter_buffer = self.POINT_ELEMENT_SEPERATOR
                # elif index == 0 and path.path_length == 1:
                #     self.write_buffer += delimiter_buffer + last_y
                #     delimiter_buffer = self.POINT_ELEMENT_SEPERATOR
                # else:
                #     delimiter_buffer += self.POINT_ELEMENT_SEPERATOR
                #
                # if is_3d:
                #     if format_num(edge.p2.z) != last_z:
                #         self.write_buffer += delimiter_buffer + format_num(edge.p2.z)
                #         last_z = format_num(edge.p2.z)

            if edge.is_arc():
                self.write_buffer += get_curve_indicator(edge)

                if format_num(edge.radius) != last_r:
                    self.write_buffer += format_num(edge.radius)
                    last_r = format_num(edge.radius)

            indicator_buffer = ""

            if not (index == (path.path_length - 1) and path.is_closed):
                indicator_buffer += ","
                if edge.p2.name:
                    self.write_buffer += indicator_buffer + edge.p2.name
                    indicator_buffer = ""

            indicator_buffer += ","
            if edge.name:
                self.write_buffer += indicator_buffer + edge.name

            if edge.style:
                self.write_buffer += indicator_buffer + self.LINE_STYLE_INDICATOR + edge.style
                indicator_buffer = ""

            if index != (path.path_length - 1):
                self.write_buffer += self.POINT_SEPERATOR

        if path.fill:
            if indicator_buffer != "":
                if edge.is_arc():
                    self.write_buffer += indicator_buffer + self.FILL_INDICATOR
                self.write_buffer += path.fill
            else:
                self.write_buffer += self.FILL_INDICATOR + path.fill

        outbuf = self.write_buffer.replace(";;", ";")

        return outbuf
