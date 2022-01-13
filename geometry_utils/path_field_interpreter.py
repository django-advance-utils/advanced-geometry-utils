from geometry_utils.two_d.path2 import Path2, is_path2
from geometry_utils.three_d.path3 import Path3, is_path3
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.point2 import Point2
from geometry_utils.two_d.vector2 import Vector2


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
        self.variables = {}

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

        def add_point(index, path_length, point, last):
            delimiter_buffer = ""
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
                self.write_buffer += delimiter_buffer + last[1]
                delimiter_buffer = self.POINT_ELEMENT_SEPERATOR
            else:
                delimiter_buffer += self.POINT_ELEMENT_SEPERATOR

            if is_path3(point):
                if format_num(point.z) != last[2]:
                    self.write_buffer += delimiter_buffer + format_num(point.z)
                    last[2] = format_num(point.z)

            return last

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

        last = ["0", "0", "0"]
        last_r = '0'
        indicator_buffer = ""
        path_length = path.path_length
        last_index = path_length - 1
        for index, edge in enumerate(path.list_of_edges):
            if path.is_closed and index == (path.path_length - 1):
                self.write_buffer += self.CLOSED_PATH_INDICATOR
            else:
                if index == 0 or edge.p1 != path.list_of_edges[index - 1].p2:
                    last = add_point(index, path_length, edge.p1, last)
                    if index != (path.path_length - 1):
                        self.write_buffer += self.POINT_SEPERATOR

                last = add_point(index, path_length, edge.p2, last)

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

    def parse_curve_def(self, curve_def, edit_mode):
        if curve_def[0] == self.CURVE_LARGE_ANTICLOCK:
            clockwise = False
            large = True
        elif curve_def[0] == self.CURVE_LARGE_CLOCK:
            clockwise = True
            large = True
        elif curve_def[0] == self.CURVE_SMALL_ANTICLOCK:
            clockwise = False
            large = False
        else:
            clockwise = True
            large = False

        if edit_mode:
            return clockwise, large, curve_def[1:]
        elif len(curve_def) == 1:
            return clockwise, large, -1
        else:
            return clockwise, large, float(curve_def[1:])

    def split_into_paths(self, path_field):
        paths = path_field.split(self.NEW_PATH_CHAR)
        return paths

    def load_path(self, path_field, edit_mode=False, override_data=None, return_single=None,
                  point_name_prefix='', round_value=2, enlarge_offset=0):
        if override_data is None:
            override_data = {}

        out_paths = []

        self.read_buffer = path_field

        path_fields = self.split_into_paths(self.read_buffer)

        for path_str in path_fields:
            if len(path_str) == 0:
                continue
            path = Path2()
            if path_str[0] == self.TAG_START_CHAR:
                index = path_str[1:].find(self.TAG_END_CHAR)
                if index != 1:
                    self.decode_attributes(path, path_str[1:index + 1])
                    path_str = path_str[index + 2:]

            if path_str[0] == self.TYPE_DELIMITER_CHAR:
                index = path_str[1:].find(self.TYPE_DELIMITER_CHAR)
                if index != 1:
                    path.type = path_str[1:index + 1]
                    path_str = path_str[index + 2:]

            index = path_str.find(self.LAYER_CHAR)
            if index != -1:
                path.layers = path_str[:index].split(',')
                path_str = path_str[index + 1:]

                # Check if a path name has been specified
            index = path_str.find(self.NAME_CHAR)
            if index != -1:
                path.name = path_str[:index]
                # Check if the name has been overridden
                if path.name in override_data and 'rename' in override_data[path.name]:
                    path.name = override_data[path.name]['rename']

                path_str = path_str[index + 1:]  # strip off the name now we've processed it

            # Check for special shapes

            if path_str.startswith(self.SPECIAL_SHAPES):
                point_separator = path_str.find(';')
                if point_separator == -1:
                    function_data = path_str[1:]
                    path_str = ''
                else:
                    function_data = path_str[1:point_separator]
                    path_str = path_str[point_separator + 1:]

                special_paths = PathFieldShapes.process_special_functions(path_field_interpreter=self,
                                                                          function_data=function_data,
                                                                          path2=path,
                                                                          previous_paths=out_paths,
                                                                          override_data=override_data,
                                                                          enlarge_offset=enlarge_offset)
                for special_path in special_paths:
                    out_paths.append(special_path)
                    if return_single is not None and special_path.name == return_single:
                        return special_path

                if path_str in ('', ';'):
                    continue

            points = path_str.split(self.POINT_SEPERATOR)

            # State variables
            last_point = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'r': 0.0}
            last_edge = Edge2()

            is_closed = False
            is_mirrored = False
            mirrored_point = -1
            if self.CLOSED_PATH_INDICATOR in points[len(points) - 1]:  # Check if path is closed
                is_closed = True
            elif self.MIRRORED_PATH_INDICATOR in points[len(points) - 1]:  # Check if path is mirrored
                is_mirrored = True

            for index, point in enumerate(points):
                default_point_name = "%s%d" % (point_name_prefix, index)
                edge_d = Edge2()
                # if the path is closed, process the last point differently as the format could be quite different,
                # especially if there is a fill colour specified.

                if point.startswith(self.INCLUDE_START):
                    if self.process_include_tag(point, path, last_point, edit_mode):
                        last_point['x'] = float(path.points[-1]['x'])
                        last_point['y'] = float(path.points[-1]['y'])
                        last_point['z'] = float(path.points[-1]['z'])
                elif point.startswith(self.FUNCTION_CHAR):
                    path_field_functions = PathFieldFunctions()
                    path_field_functions.process(point, path)
                    last_point['x'] = float(path.points[-1]['x'])
                    last_point['y'] = float(path.points[-1]['y'])
                    last_point['z'] = float(path.points[-1]['z'])

                elif is_closed and point is points[len(points) - 1]:
                    self.process_closed_point(point, edge_d, path, last_point, edit_mode)
                    break
                elif is_mirrored:  # mirrored point
                    if point is points[len(points) - 1]:
                        self.process_mirrored_points(point, edge_d, path,
                                                     last_point, mirrored_point, edit_mode, default_point_name,
                                                     round_value=round_value)
                        break
                    else:
                        if len(point) > 0 and point[0] == self.MIRRORED_PATH_POINT_INDICATOR:
                            mirrored_point = len(path.points) - 1
                            point = point[1:]
                            if edit_mode:
                                path.points[-1]['mirror'] = self.MIRRORED_PATH_POINT_INDICATOR
                        self.process_normal_point(point, point_dict, path, last_point,
                                                  edit_mode, default_point_name,
                                                  round_value=round_value)
                else:  # Normal point
                    self.process_normal_point(point, point_dict, path, last_point,
                                              edit_mode, default_point_name,
                                              round_value=round_value)
            out_paths.append(path)

            if return_single is not None and path.name == return_single:
                return path

        if return_single is None:
            return out_paths
        else:
            return None

    def process_include_tag(self, tag, path, last_point, edit_mode):
        function_data = tag.lstrip(self.INCLUDE_START)
        last_edge = Edge2()
        point_type = 'pp'
        offset_x = last_point['x']
        offset_y = last_point['y']
        offset_z = last_point['z']
        offset = Vector2()
        valid = True
        main_include_data = function_data.split(self.INCLUDE_CONDITION_DELIMITER)

        if len(main_include_data) > 1 and main_include_data[1] != '':
            try:
                valid = bool(int(main_include_data[1]))
            except ValueError:
                valid = True

        include_data = main_include_data[0].split(self.INCLUDE_DELIMITER)

        variable_name = include_data[0]

        if len(include_data) > 1 and include_data[1] != '':
            point_type = include_data[1]
        if len(include_data) > 2 and include_data[2] != '':
            try:
                offset_x = float(include_data[2])
            except ValueError:
                offset_x = include_data[2]
        if len(include_data) > 3 and include_data[3] != '':
            try:
                offset_y = float(include_data[3])
            except ValueError:
                offset_y = include_data[3]

        if edit_mode:
            edge = offset
            edge.name = variable_name
            edge.type = point_type
            path.list_of_edges.append(edge)
            # path.points.append({'include': "%s,%s" % (variable_name, point_type),
            #                     'x': offset_x,
            #                     'y': offset_y})
            return False

        if valid:
            path_string = self.variables.get(variable_name, ';')
            new_path2 = self.load_path(path_string,
                                       point_name_prefix=variable_name + '_')[0]
            result = new_path2.get_points(point_type, offset_x, offset_y)

            path.points += result
            return True
        else:
            path.points.append({'x': offset_x,
                                'y': offset_y,
                                'z': offset_z})

            return True

    @staticmethod
    def decode_attributes(path, attributes_str):
        attributes = attributes_str.split(';')

        for attribute_str in attributes:
            attribute = attribute_str.split(':')
            if len(attribute) == 1:
                value = True
            else:
                value = attribute[1]
            path.attributes[attribute[0]] = value

    def join_paths_left_right(self, path_field_left, path_field_right, merge_flip=True, edit_mode=False):
        path_left_list = []
        path_right_list = []

        if path_field_left is not None and path_field_left != '':
            path_left_list = self.load_path(path_field_left, edit_mode=edit_mode)

        if path_field_right is not None and path_field_right != '':
            path_right_list = self.load_path(path_field_right, edit_mode=edit_mode)

        if ((path_field_left == '' or len(path_left_list) == 0) and
                (path_field_right == '' or len(path_right_list) == 0)):
            return [None]
        elif path_field_left == '' or len(path_left_list) == 0:
            return path_right_list
        elif path_field_right == '' or len(path_right_list) == 0:
            return path_left_list

        paths = []

        for path_left, path_right in zip(path_left_list, path_right_list):
            path = Path2()

            if not edit_mode:
                offset_y = max(edge.maximum_y() for edge in path_left.list_of_edges)
                if merge_flip:
                    path_right.flip_vertical(offset_y=offset_y)
            # path.list_of_edges
            path.points = path_left.get_points() + path_right.get_points()[1:]
            paths.append(path)
        return paths

    def process_normal_point(self, point, edge_d, path, last_edge,
                             edit_mode, default_point_name, round_value):
        idx1 = point.find(self.CURVE_SMALL_CLOCK)
        if idx1 == -1:
            idx1 = point.find(self.CURVE_SMALL_ANTICLOCK)
            if idx1 == -1:
                idx1 = point.find(self.CURVE_LARGE_CLOCK)
                if idx1 == -1:
                    idx1 = point.find(self.CURVE_LARGE_ANTICLOCK)

        if idx1 == -1:
            idx1 = point.find(',')

        # extract the positon part of the point.
        if idx1 != -1:
            position = point[:idx1]
            point = point[idx1:]
        else:
            position = point
            point = ''

        xyz = position.split(self.POINT_ELEMENT_SEPERATOR)
        while len(xyz) < 3:
            xyz.append('')

        edge_d.p2.x = self.get_value(xyz[0], last_edge.p2.x, round_value)
        edge_d.p2.y = self.get_value(xyz[1], last_edge.p2.y, round_value)
        if is_path3(path):
            edge_d.z = self.get_value(xyz[2], last_edge.z, round_value)

        # Now process the curve definition if there is one
        if len(point) == 0:
            path.list_of_edges.append(edge_d)
            edge_d.name = default_point_name
            last_edge.p2.x = edge_d.p2.x
            last_edge.p2.y = edge_d.p2.y
            if is_path3(path):
                last_edge.p2.z = edge_d.p2.z
            return

        # Look for a curve definition, it should be terminated either by a comma or be the whole string
        # Extract it from the point
        if point[0] in [self.CURVE_LARGE_ANTICLOCK,
                        self.CURVE_LARGE_CLOCK,
                        self.CURVE_SMALL_ANTICLOCK,
                        self.CURVE_SMALL_CLOCK]:
            idx = point.find(',')
            if idx == -1:
                curve_def = point
                point = ''
            else:
                curve_def = point[:idx]
                point = point[idx:]

            # Process the curve def
            clock, large, radius = self.parse_curve_def(curve_def, edit_mode)
            edge_d.clockwise = clock
            edge_d.large = large
            if radius == -1:
                # point_dict['r'] = last_point['r']
                edge_d.radius = last_edge.radius
            else:
                edge_d.radius = radius
                # point_dict['r'] = radius
            edge_d.p1 = last_edge.p2
            arc_to_point_data = edge_d.flatten_arc()
            # arc_to_point_data = self.arc_to_points(last_point, point_dict)
            # point_dict['expanded_points'] = arc_to_point_data[0]
            # point_dict['expanded_points_length'] = arc_to_point_data[1]
            # point_dict['start_count'] = arc_to_point_data[2]
            # point_dict['end_count'] = arc_to_point_data[3]
            # point_dict['increment'] = arc_to_point_data[4]

            last_edge.radius = edge_d.radius

        last_edge = edge_d

        point = point[1:]

        if len(point) == 0:
            path.points.append(point_dict)
            point_dict['name'] = default_point_name
            return

        # Look for a point name and edge def if given
        parts = point.split(',')

        if parts[0] != '':
            point_dict['name'] = parts[0]
        else:
            point_dict['name'] = default_point_name

        if len(parts) > 1 and self.LINE_STYLE_INDICATOR in parts[1]:
            edge_def = parts[1].split(self.LINE_STYLE_INDICATOR)
            if edge_def[0] != '':
                point_dict['edge_name'] = edge_def[0]
            point_dict['style'] = edge_def[1]
        elif len(parts) > 1 and parts[1] != '':
            point_dict['edge_name'] = parts[1]
        if len(parts) > 2 and parts[2] != '':
            point_dict['left_name'] = parts[2]
        if len(parts) > 3 and parts[3] != '':
            point_dict['right_name'] = parts[3]

        path.points.append(point_dict)

    def get_value(self, in_value, last_value, round_value):
        if in_value == '':
            r_value = last_value
            return r_value
        relative = False
        if in_value.startswith(self.RELATIVE_CHAR):
            relative = True
            in_value = in_value[1:]
        try:
            r_value = float(in_value)
            if relative:
                r_value += last_value
            r_value = round(r_value, round_value)
        except ValueError:
            r_value = in_value
        return r_value
