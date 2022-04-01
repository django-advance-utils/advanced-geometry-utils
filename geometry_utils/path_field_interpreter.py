import copy

from geometry_utils.three_d.point3 import is_point3
from geometry_utils.two_d.path2 import Path2
from geometry_utils.three_d.path3 import is_path3
from geometry_utils.two_d.edge2 import Edge2
from geometry_utils.two_d.point2 import Point2, is_point2


class PathFieldInterpreter(Path2, object):
    # Symbols used in the PathField
    NEW_PATH_CHAR = '|'
    LAYER_CHAR = '&'
    NAME_CHAR = '@'
    POINT_SEPARATOR = ';'
    POINT_ELEMENT_SEPARATOR = ':'
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
        self.write_buffer = ''
        self.read_buffer = ''
        self.variables = {}

    def clear_path(self):
        self.write_buffer = ''
        self.read_buffer = ''
        self.list_of_edges = []

    def add_path(self, path):
        """
        Add a Path2() to the PathField and return the PathField string.
        The paths accumulate in the buffer, so multiple calls to this function will
        build up a PathField string containing multiple paths.
        @param path: Path2() instance
        @return: PathField string
        """
        def format_num(num):
            """
            Formats a number to PathField spec:
             - Rounded to 2dp.
             - Any trailing 0's and .'s removed.
             - eg: 12.00003535 -> 12
             - eg: 12.300 -> 12.3
             - eg: 12.000000 -> 12
            @param num: float or integer.
            @return: formatted number as string
            """
            try:
                str_num = "%.2f" % float(num)
            except ValueError:
                return "%s" % num
            if str_num == '0.00':
                return '0'
            return str_num.rstrip('0').rstrip('.')

        def format_point(point):
            if is_point2(point):
                point_string = [format_num(point.x), format_num(point.y)]
                return point_string
            elif is_point3(point):
                point_string = [format_num(point.x), format_num(point.y), format_num(point.z)]
                return point_string
            else:
                raise TypeError('Argument must be a type of Point2 or Point3')

        def get_curve_indicator(_edge):
            """
            Retrieves the correct curve indicator given large and clockwise parameters
            for a curve.
            @param _edge:
            @return:
            """
            if _edge.large and _edge.clockwise:
                return self.CURVE_LARGE_CLOCK
            elif _edge.large and not _edge.clockwise:
                return self.CURVE_LARGE_ANTICLOCK
            elif not _edge.large and _edge.clockwise:
                return self.CURVE_SMALL_CLOCK
            elif not _edge.large and not _edge.clockwise:
                return self.CURVE_SMALL_ANTICLOCK

        def add_point(_index, point, _last):
            delimiter_buffer = ''
            point_string = format_point(point)
            if point_string[0] != _last[0]:
                self.write_buffer += point_string[0]
                _last[0] = point_string[0]
            elif _index == 0 and self.path_length == 1:
                self.write_buffer += _last[0]
            delimiter_buffer += self.POINT_ELEMENT_SEPARATOR

            if point_string[1] != _last[1]:
                self.write_buffer += delimiter_buffer + point_string[1]
                _last[1] = point_string[1]
                delimiter_buffer = self.POINT_ELEMENT_SEPARATOR
            elif _index == 0 and self.path_length == 1:
                self.write_buffer += delimiter_buffer + _last[1]
                delimiter_buffer = self.POINT_ELEMENT_SEPARATOR
            else:
                delimiter_buffer += self.POINT_ELEMENT_SEPARATOR

            if is_point3(point):
                if point_string[2] != _last[2]:
                    self.write_buffer += delimiter_buffer + point_string[2]
                    _last[2] = format_num(point.z)
            return _last

        # If there is already a path in the buffer, append the path separator first
        if self.write_buffer != '':
            self.write_buffer += self.NEW_PATH_CHAR

        # Write out layer names if given
        if path.layers:
            first = True
            for layer in path.layers:
                if not first:
                    self.write_buffer += ','
                self.write_buffer += layer
                first = False
            self.write_buffer += self.LAYER_CHAR

        # Write out path name if given
        if path.name != '':
            self.write_buffer += path.name + self.NAME_CHAR

        # State variables, initialised to 0 so if first point is 0, 0, 0 the values wont be written
        # as required by the spec
        last = ['0', '0', '0']
        last_r = '0'

        indicator_buffer = ''
        path_length = path.path_length
        last_index = path_length - 1

        # Loop through the points and write them out
        for index, edge in enumerate(path.list_of_edges):
            # If this is the last point in a closed path, output the closed path indicator, rather than the xyz pos
            if path.is_closed and index == last_index:
                self.write_buffer += self.CLOSED_PATH_INDICATOR
            else:
                if index == 0 or edge.p1 != path.list_of_edges[index - 1].p2:
                    last = add_point(index, edge.p1, last)
                    if index != last_index:
                        self.write_buffer += self.POINT_SEPARATOR
                last = add_point(index, edge.p2, last)

            # Only a valid curve if all three curve parameters are present
            if edge.is_arc():
                self.write_buffer += get_curve_indicator(edge)
                if format_num(edge.radius) != last_r:
                    self.write_buffer += format_num(edge.radius)
                    last_r = format_num(edge.radius)
            indicator_buffer = ''

            # Add point name if given
            # Skip the point name if its the last point in a closed path, as path name is invalid
            # and extra comma not needed
            if not (index == last_index and path.is_closed):
                indicator_buffer += ','
                if edge.p1.name:
                    self.write_buffer += indicator_buffer + edge.p1.name
                elif edge.p2.name:
                    self.write_buffer += indicator_buffer + edge.p2.name
                indicator_buffer = ''

            # Add edge name if given
            indicator_buffer += ','
            if edge.name:
                self.write_buffer += indicator_buffer + edge.name
                indicator_buffer = ''

            # Add edge style if given
            if edge.style:
                self.write_buffer += indicator_buffer + self.LINE_STYLE_INDICATOR + edge.style
                indicator_buffer = ''

            if index != last_index:
                self.write_buffer += self.POINT_SEPARATOR

        if path.fill != '':
            if indicator_buffer != '':
                if path.list_of_edges[-1].is_arc():
                    self.write_buffer += indicator_buffer + self.FILL_INDICATOR
                self.write_buffer += path.fill
            else:
                self.write_buffer += self.FILL_INDICATOR + path.fill

        outbuf = self.write_buffer.replace(';;', ';')

        return outbuf

    def parse_curve_def(self, curve_def, edit_mode):
        """
        Turns arc definition into clockwise, large and radius attributes.
        @param curve_def: arc definition eg: '(10'
        @param edit_mode:
        @return: clockwise (bool), large (bool), radius (num) (if radius is not given, returns -1)
        """
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
        """
        Reads a PathField string and outputs a list of Path2s
        @param path_field: string
        @param edit_mode: boolean used for the shape editor
        @param override_data:
        @param return_single:
        @return: [Path2]
        @param point_name_prefix:

        @param round_value: int required number of decimal places
        @param enlarge_offset: enlarge_offset only works for pre-defined shapes ie rect / diamond etc
        """
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

            # Check if layers are specified
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

            points = path_str.split(self.POINT_SEPARATOR)

            # State variables
            last_edge = Edge2()
            last_r = 0.0

            is_closed = False
            is_mirrored = False
            mirrored_point = -1
            if self.CLOSED_PATH_INDICATOR in points[len(points) - 1]:  # Check if path is closed
                is_closed = True
            if self.MIRRORED_PATH_INDICATOR in points[len(points) - 1]:  # Check if path is mirrored
                is_mirrored = True

            for index, point in enumerate(points):
                default_point_name = "%s%d" % (point_name_prefix, index)
                edge_d = Edge2(Point2(), Point2(), 0, False, False)

                # if the path is closed, process the last point differently as the format could be quite different,
                # especially if there is a fill colour specified

                if point.startswith(self.INCLUDE_START):
                    if self.process_include_tag(point, path, last_edge, edit_mode):
                        continue

                elif point.startswith(self.FUNCTION_CHAR):
                    path_field_functions = PathFieldFunctions()
                    path_field_functions.process(point, path)

                elif is_closed and point is points[len(points) - 1]:  # last point of a closed path
                    self.process_closed_point(point, path, last_edge, last_r, edit_mode)
                    break

                elif is_mirrored:  # mirrored point
                    if point is points[len(points) - 1]:
                        self.process_mirrored_points(point, edge_d, path,
                                                     last_edge, last_r, mirrored_point, edit_mode, default_point_name,
                                                     round_value=round_value)
                        break

                    else:
                        if len(point) > 0 and point[0] == self.MIRRORED_PATH_POINT_INDICATOR:
                            mirrored_point = path.path_length - 1
                            point = point[1:]
                            # if edit_mode:
                            # path.points[-1]['mirror'] = self.MIRRORED_PATH_POINT_INDICATOR
                        self.process_normal_point(point, edge_d, path, last_edge, last_r,
                                                  edit_mode, default_point_name,
                                                  round_value=round_value)
                else:  # Normal point
                    self.process_normal_point(point, edge_d, path, last_edge, last_r,
                                              edit_mode, default_point_name,
                                              round_value=round_value)
                if last_edge.is_arc():
                    last_r = last_edge.radius
                last_edge = path.list_of_edges[-1]

            if not is_closed and path.path_length > 1:
                del path.list_of_edges[-1]

            if path.is_incomplete_circle():
                path.complete_circle()

            if return_single is not None and path.name == return_single:
                return path
            out_paths.append(path)

        if return_single is None:
            return out_paths
        else:
            return None

    def process_include_tag(self, tag, path, last_edge, edit_mode):
        function_data = tag.lstrip(self.INCLUDE_START)
        edge_type = 'pp'

        offset_vector = last_edge.p1.to_vector2()
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
            edge_type = include_data[1]
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
            edge.type = edge_type
            path.list_of_edges.append(edge)
            return False

        if valid:
            path_string = self.variables.get(variable_name, ';')
            new_path2 = self.load_path(path_string, point_name_prefix=variable_name + '_')[0]
            result = new_path2.offset(offset_vector)
            path += result
            return True
        else:
            path.list_of_edges.append(Edge2(Point2(offset_vector.x, offset_vector.y), Point2()))
            return True

    def process_mirrored_points(self, point, edge_d, path, last_edge, last_r, mirrored_point, edit_mode, default_point_name,
                                round_value):
        self.process_normal_point(point[:-1], edge_d, path, last_edge, last_r, edit_mode, default_point_name, round_value)
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
                end_point = path.list_of_edges[-1].p1
                for local_path_edge in reversed(local_path_edges[:mirrored_point]):
                    mirrored_point -= 1
                    if (not mirror_x and offset - local_path_edge.p1.y == end_point.y and
                            local_path_edge.p1.x == end_point.x):
                        break
                    elif (mirror_x and local_path_edge.p1.y == end_point.y and
                          offset - local_path_edge.p1.x == end_point.x):
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
                        held_arc = None

                    if local_path_edge.radius:
                        held_arc = local_path_edge

                    path.list_of_edges.append(edge_d)
            else:
                return

    def process_closed_point(self, point, path, last_edge, last_r, edit_mode):
        """
        Closed path, last point xyz is same as first point
        @param point:
        @param path:
        @param last_edge:
        @param edit_mode:
        """
        path.list_of_edges[-1].p2 = copy.deepcopy(path.list_of_edges[0].p1)

        if len(point) == 1:
            return

        point = point[1:]  # Strip off the closed path indicator, now we've processed the position

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
                edge_d.radius = last_r

            else:
                edge_d.radius = radius

            if len(point) == 0:
                #path.list_of_edges.append(edge_d)
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
            path.list_of_edges = path_left + path_right[1:]
            paths.append(path)
        return paths

    def process_normal_point(self, point, edge_d, path, last_edge, last_r, edit_mode, default_point_name, round_value):
        idx1 = point.find(self.CURVE_SMALL_CLOCK)
        if idx1 == -1:
            idx1 = point.find(self.CURVE_SMALL_ANTICLOCK)
            if idx1 == -1:
                idx1 = point.find(self.CURVE_LARGE_CLOCK)
                if idx1 == -1:
                    idx1 = point.find(self.CURVE_LARGE_ANTICLOCK)

        if idx1 == -1:
            idx1 = point.find(',')

        # extract the position part of the point.
        if idx1 != -1:
            position = point[:idx1]
            point = point[idx1:]
        else:
            position = point
            point = ''

        xyz = position.split(self.POINT_ELEMENT_SEPARATOR)
        while len(xyz) < 3:
            xyz.append('')

        edge_d.p1.x = self.get_value(xyz[0], last_edge.p1.x, round_value)
        edge_d.p1.y = self.get_value(xyz[1], last_edge.p1.y, round_value)
        # if is_path3(path):
            # edge_d.p1.z = self.get_value(xyz[2], last_edge.p1.z, round_value)

        # Now process the curve definition if there is one
        if len(point) == 0:
            edge_d.p1.name = default_point_name
            path.list_of_edges.append(edge_d)
            path.make_continuous()
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
                edge_d.radius = last_r
            else:
                edge_d.radius = radius

        point = point[1:]

        if len(point) == 0:
            path.list_of_edges.append(edge_d)
            edge_d.p1.name = default_point_name
            path.make_continuous()
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
        path.make_continuous()

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
                path.list_of_edges.append(Edge2(Point2(new_x, current_edge.y)))
                new_x += chord_width
                path.list_of_edges.append(Edge2(Point2(new_x, current_edge.y), Point2(), radius, True, False))
                number_of_inclusive_bars -= 1

        elif end_style in ('l', 'L', 'r', 'R'):
            chord_width = (end_x - current_edge.p1.x) * 2
            if chord_height > chord_width:
                chord_height = chord_width
            radius = radius_of_chord(chord_width / 2, chord_height)
            if end_style in ('r', 'R'):
                chord_height = - chord_height
            end_y = current_edge.p1.y + chord_height
            path.points.append(Edge2(Point2(end_x, end_y), Point2(), radius, True, False))
