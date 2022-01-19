import copy

from geometry_utils.two_d.path2 import Path2
from geometry_utils.three_d.path3 import is_path3
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.point2 import Point2


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

            # if path_str.startswith(self.SPECIAL_SHAPES):
            #     point_separator = path_str.find(';')
            #     if point_separator == -1:
            #         function_data = path_str[1:]
            #         path_str = ''
            #     else:
            #         function_data = path_str[1:point_separator]
            #         path_str = path_str[point_separator + 1:]
            #
            #     special_paths = PathFieldShapes.process_special_functions(path_field_interpreter=self,
            #                                                               function_data=function_data,
            #                                                               path2=path,
            #                                                               previous_paths=out_paths,
            #                                                               override_data=override_data,
            #                                                               enlarge_offset=enlarge_offset)
            #     for special_path in special_paths:
            #         out_paths.append(special_path)
            #         if return_single is not None and special_path.name == return_single:
            #             return special_path
            #
            #     if path_str in ('', ';'):
            #         continue

            points = path_str.split(self.POINT_SEPERATOR)

            # State variables
            # last_point = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'r': 0.0}
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
                edge_d = Edge2(Point2(), Point2(), 0, False, False)
                # if the path is closed, process the last point differently as the format could be quite different,
                # especially if there is a fill colour specified.

                if point.startswith(self.INCLUDE_START):
                    if self.process_include_tag(point, path, last_edge, edit_mode):
                        last_edge = path.list_of_edges[-1]

                elif point.startswith(self.FUNCTION_CHAR):
                    path_field_functions = PathFieldFunctions()
                    path_field_functions.process(point, path)
                    last_edge = path.list_of_edges[-1]

                elif is_closed and point is points[len(points) - 1]:
                    self.process_closed_point(point, edge_d, path, last_edge, edit_mode)
                    break
                elif is_mirrored:  # mirrored point
                    if point is points[len(points) - 1]:
                        self.process_mirrored_points(point, edge_d, path,
                                                     last_edge, mirrored_point, edit_mode, default_point_name,
                                                     round_value=round_value)
                        break
                    else:
                        if len(point) > 0 and point[0] == self.MIRRORED_PATH_POINT_INDICATOR:
                            mirrored_point = path.path_length - 1
                            point = point[1:]
                            # if edit_mode:
                                # path.points[-1]['mirror'] = self.MIRRORED_PATH_POINT_INDICATOR
                        self.process_normal_point(point, edge_d, path, last_edge,
                                                  edit_mode, default_point_name,
                                                  round_value=round_value)
                else:  # Normal point
                    self.process_normal_point(point, edge_d, path, last_edge,
                                              edit_mode, default_point_name,
                                              round_value=round_value)
                    last_edge = path.list_of_edges[-1]

            # dont forget to revisit as well as account for the edge attributes and name and style when processing
            # the last edge
            path.make_continuous()
            # if not path.is_closed:
            #     path.list_of_edges[-2].p2 = copy.deepcopy(path.list_of_edges[-1].p1)
            #     del(path.list_of_edges[-1])

            if return_single is not None and path.name == return_single:
                return path
            out_paths.append(path)

        if return_single is None:
            return out_paths
        else:
            return None

    def process_include_tag(self, tag, path, last_edge, edit_mode):
        function_data = tag.lstrip(self.INCLUDE_START)
        point_type = 'pp'
        offset_vector = last_edge.p2.to_vector2()
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
                offset_vector.x = float(include_data[2])
            except ValueError:
                offset_vector.x = include_data[2]
        if len(include_data) > 3 and include_data[3] != '':
            try:
                offset_vector.y = float(include_data[3])
            except ValueError:
                offset_vector.y = include_data[3]

        if edit_mode:
            edge = Edge2(Point2(offset_vector.x, offset_vector.y), Point2())
            edge.name = variable_name
            edge.type = point_type
            path.list_of_edges.append(edge)
            last_edge.p2 = copy.deepcopy(edge.p1)
            return False

        if valid:
            path_string = self.variables.get(variable_name, ';')
            new_path2 = self.load_path(path_string, point_name_prefix=variable_name + '_')[0]
            result = new_path2.offset(offset_vector)
            path += result
            return True
        else:
            path.list_of_edges.append(Edge2(Point2(offset_vector.x, offset_vector.y, Point2())))
            return True

    def process_mirrored_points(self, point, edge_d, path, last_edge, mirrored_point, edit_mode, default_point_name,
                                round_value):
        self.process_normal_point(point[:-1], edge_d, path, last_edge, edit_mode, default_point_name, round_value)
        if not path.is_closed:
            path.list_of_edges[-2].p2 = copy.deepcopy(path.list_of_edges[-1].p1)
            del (path.list_of_edges[-1])
        if edit_mode:
            # path.list_of_edges.append('mirror')
            return
        local_path_edges = copy.deepcopy(path.list_of_edges)
        if (path.list_of_edges[0].p1.y == path.list_of_edges[mirrored_point].p1.y or
                path.list_of_edges[0].p1.x == path.list_of_edges[mirrored_point].p1.x):
            held_arc = None
            if path.list_of_edges[0].p1.x == path.list_of_edges[mirrored_point].p1.x:
                offset = path.list_of_edges[0].p1.x * 2
                mirror_x = True
            else:
                offset = path.list_of_edges[0].p1.y * 2
                mirror_x = False
            if mirrored_point != -1:
                end_point_x = path.list_of_edges[-1].p1.x  # why not end_edge
                end_point_y = path.list_of_edges[-1].p1.y
                for local_path_edge in reversed(local_path_edges[:mirrored_point]):
                    mirrored_point -= 1
                    if (not mirror_x and offset - local_path_edge.p1.y == end_point_y and
                            local_path_edge.p1.x == end_point_x):
                        break
                    elif (mirror_x and local_path_edge.p1.y == end_point_y and
                          offset - local_path_edge.p1.x == end_point_x):
                        break

                for local_path_edge in reversed(local_path_edges[:mirrored_point]):
                    if mirror_x:
                        edge_d.p1.x = offset - local_path_edge.p1.x
                        edge_d.p1.y = local_path_edge.p1.y
                        edge_d.p2.x = offset - local_path_edge.p2.x
                        edge_d.p2.y = local_path_edge.p2.y
                    else:
                        edge_d.p1.x = local_path_edge.p1.x
                        edge_d.p1.y = offset - local_path_edge.p1.y
                        edge_d.p2.x = local_path_edge.p2.x
                        edge_d.p2.y = offset - local_path_edge.p2.y
                    if is_path3(path):
                        edge_d.p1.z = local_path_edge.p1.z
                        edge_d.p2.z = local_path_edge.p2.z

                    if held_arc is not None:
                        edge_d.radius = held_arc.radius
                        edge_d.clockwise = held_arc.clockwise
                        edge_d.large = held_arc.large

                        # arc_to_point_data = edge_d.flatten_arc()
                        # path.list_of_edges.append(arc_to_point_data)
                        # edge_d = path.list_of_edges[-1]

                        held_arc = None

                    if local_path_edge.radius:
                        held_arc = local_path_edge

                    path.list_of_edges.append(edge_d)
            else:
                return

    def process_closed_point(self, point, edge_d, path, last_edge, edit_mode):
        # edge_d = Edge2(path.list_of_edges[-1].p2, path.list_of_edges[0].p1)
        path.list_of_edges[-1].p2 = copy.deepcopy(path.list_of_edges[0].p1)
        if len(point) == 1:
            # path.list_of_edges.append(edge_d)
            return
        point = point[1:]

        edge_d = path.list_of_edges[-1]

        if (point[0] == self.CURVE_SMALL_CLOCK or point[0] == self.CURVE_SMALL_ANTICLOCK or
                point[0] == self.CURVE_LARGE_CLOCK or point[0] == self.CURVE_LARGE_ANTICLOCK):
            idx = point.find(',')
            if idx == -1:
                curve_def = point
                point = ''
            else:
                curve_def = point[:idx]
                point = point[idx + 1:]

            clock, large, radius = self.parse_curve_def(curve_def, edit_mode)
            edge_d.clockwise = clock
            edge_d.large = large
            if radius == -1:
                edge_d.radius = last_edge.radius
            else:
                edge_d.radius = radius
                last_edge.radius = edge_d.radius

            if len(point) == 0:
                path.list_of_edges.append(edge_d)
                return
        if point[0] == ',':
            point = point[1:]

            idx = point.find(self.FILL_INDICATOR)
            if idx == -1:
                edge_def = point
                point = ''
            else:
                edge_def = point[:idx]
                point = point[idx + 1:]

            parts = edge_def.split(self.LINE_STYLE_INDICATOR)
            if parts[0] != '':
                edge_d.name = parts[0]
            if len(parts) > 1 and parts[1] != '':
                edge_d.style = parts[1]

        # path.list_of_edges.append(edge_d)

        if len(point) > 0 and point[0] == self.FILL_INDICATOR:
            point = point[1:]
        path.fill = point

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

    def process_normal_point(self, point, edge_d, path, last_edge, edit_mode, default_point_name, round_value):
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

        edge_d.p1.x = self.get_value(xyz[0], last_edge.p1.x, round_value)
        edge_d.p1.y = self.get_value(xyz[1], last_edge.p1.y, round_value)
        if is_path3(path):
            edge_d.p1.z = self.get_value(xyz[2], last_edge.p1.z, round_value)
        # last_edge.p2 = copy.deepcopy(edge_d.p1)
        # Now process the curve definition if there is one
        if len(point) == 0:
            edge_d.p1.name = default_point_name
            path.list_of_edges.append(edge_d)
            last_edge = copy.deepcopy(edge_d)
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
                edge_d.radius = last_edge.radius
            else:
                edge_d.radius = radius
            # arc_to_point_data = edge_d.flatten_arc()
            # path.list_of_edges.append(arc_to_point_data)
            # edge_d = path.list_of_edges[-1]

        last_edge = edge_d

        point = point[1:]

        if len(point) == 0:
            path.list_of_edges.append(edge_d)
            edge_d.name = default_point_name
            return

        # Look for a point name and edge def if given
        parts = point.split(',')

        if parts[0] != '':
            edge_d.p1.name = parts[0]
        else:
            edge_d.p1.name = default_point_name

        if len(parts) > 1 and self.LINE_STYLE_INDICATOR in parts[1]:
            edge_def = parts[1].split(self.LINE_STYLE_INDICATOR)
            if edge_def[0] != '':
                edge_d.name = edge_def[0]
            edge_d.style = edge_def[1]
        elif len(parts) > 1 and parts[1] != '':
            edge_d.name = parts[1]
        if len(parts) > 2 and parts[2] != '':
            edge_d.left_name = parts[2]
        if len(parts) > 3 and parts[3] != '':
            edge_d.right_name = parts[3]

        path.list_of_edges.append(edge_d)

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


class PathFieldFunctions:
    def __init__(self):
        pass

    def process(self, point, path):
        arguments = point.split(',')
        function_type = arguments[0][1:].upper()
        if function_type == 'STR':
            return self.swept_top_rail(arguments[1:], path)
        else:
            assert False, 'unknown function type'

    def swept_top_rail(self, arguments, path):
        current_edge = path.list_of_edges[-1]

        end_style = arguments[0]
        chord_height = float(arguments[1])
        end_x = float(arguments[2])
        if len(arguments) > 3:
            number_of_inclusive_bars = float(arguments[3])
            inclusive_bars_width = float(arguments[4])
        else:
            number_of_inclusive_bars = 0
            inclusive_bars_width = 0
        if end_style == "":
            chord_width = ((end_x - current_edge.p1.x - number_of_inclusive_bars * inclusive_bars_width) /
                           (number_of_inclusive_bars + 1))
            if chord_height > chord_width / 2:
                chord_height = chord_width / 2
            new_x = current_edge.p1.x + chord_width
            radius = radius_of_chord(chord_width / 2, chord_height)
            path.list_of_edges.append(Edge2(Point2(new_x, current_edge.y), Point2(), radius, True, False))
            while number_of_inclusive_bars > 0:
                new_x += inclusive_bars_width
                path.points.append(Edge2(Point2(new_x, current_edge.y)))
                new_x += chord_width
                path.list_of_edges.append(Edge2(Point2(new_x, current_edge.y), Point2(), radius, True, False))
                number_of_inclusive_bars -= 1
        elif end_style in ('l', 'L', 'r', 'R'):
            chord_width = (end_x - current_edge.x) * 2
            if chord_height > chord_width:
                chord_height = chord_width
            radius = radius_of_chord(chord_width / 2, chord_height)
            if end_style in ('r', 'R'):
                chord_height = - chord_height
            end_y = current_edge.y + chord_height
            path.points.append(Edge2(Point2(end_x, end_y), Point2(), radius, True, False))
            path.make_continuous()