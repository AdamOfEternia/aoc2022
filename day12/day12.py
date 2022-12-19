from dataclasses import dataclass, field

from utils.utils import read_file


@dataclass
class Position:
    x: int
    y: int
    g: int = field(init=False, default=0)
    h: int = field(init=False, default=0)
    f: int = field(init=False, default=0)
    parent: any = field(init=False, default=None)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")


def get_height_map(data):
    height_map = [f"~{x}~" for x in data]
    height_map.insert(0, "~" * len(height_map[0]))
    height_map.append("~" * len(height_map[0]))
    return height_map


def get_position(height_map, marker):
    pos = Position(-1, -1)
    for r in range(0, len(height_map)):
        c = height_map[r].find(marker)
        if c > -1:
            pos.x = c
            pos.y = r
            break
    return pos


def get_options(height_map, curr_pos):
    curr_pos_val = ord(height_map[curr_pos.y][curr_pos.x])
    options = []
    if ord(height_map[curr_pos.y][curr_pos.x - 1]) - curr_pos_val <= 1:
        options.append(Position(curr_pos.x - 1, curr_pos.y))
    if ord(height_map[curr_pos.y][curr_pos.x + 1]) - curr_pos_val <= 1:
        options.append(Position(curr_pos.x + 1, curr_pos.y))
    if ord(height_map[curr_pos.y - 1][curr_pos.x]) - curr_pos_val <= 1:
        options.append(Position(curr_pos.x, curr_pos.y - 1))
    if ord(height_map[curr_pos.y + 1][curr_pos.x]) - curr_pos_val <= 1:
        options.append(Position(curr_pos.x, curr_pos.y + 1))
    return options


def get_next_position(options, positions_travelled, end_pos):
    o_val_x = 999
    o_val_y = 999
    next_pos = Position(-1, -1)
    for o in options:
        last_o_val_x = o_val_x
        last_o_val_y = o_val_y
        if o not in positions_travelled:
            o_val_x = end_pos.x - o.x
            o_val_y = end_pos.y - o.y
            if o_val_x < last_o_val_x or o_val_y < last_o_val_y:
                next_pos.x = o.x
                next_pos.y = o.y
    return next_pos


def get_good_path(pos, ordered=False):
    good_path = []
    c = pos
    while c is not None:
        good_path.append((c.x, c.y))
        c = c.parent
    if ordered:
        good_path.reverse()
    return  good_path


def reset_marker(height_map, current_marker, correct_marker):
    for r in range(0, len(height_map)):
        height_map[r] = height_map[r].replace(current_marker, correct_marker)


def get_astar_path(height_map, start_pos, end_pos):
    # traverse the route
    open_list = [start_pos]
    closed_list = []

    path_found = False
    while len(open_list) > 0:
        current_pos = sorted(open_list, key=lambda n: n.f)[0]
        open_list.remove(current_pos)
        closed_list.append(current_pos)

        if current_pos == end_pos:
            path_found = True
            break

        options = get_options(height_map, current_pos)
        for child in options:
            if child in closed_list:
                continue

            if child not in open_list:
                open_list.append(child)
                child.parent = current_pos
                child.g = current_pos.g + 1
                child.h = abs(child.x - end_pos.x) + abs(child.y - end_pos.y)
                child.f = child.g + child.h

            for o in open_list:
                if child == o and child.g > o.g:
                    continue

    good_path = []
    if path_found:
        good_path = get_good_path(current_pos, True)
    return good_path


def get_fewest_steps_to_destination(height_map, start_pos, end_pos):
    path = get_astar_path(height_map, start_pos, end_pos)
    return len(path) - 1


def get_all_matching_positions(height_map, marker):
    matching_positions = []
    for r in range(0, len(height_map)):
        for c in range(0, len(height_map[r])):
            if height_map[r][c] == marker:
                matching_positions.append(Position(c, r))
    return matching_positions


def get_shortest_journey_to_destination(height_map, starting_marker, end_pos):
    starting_positions = get_all_matching_positions(height_map, starting_marker)
    shortest_lowest_journey_steps = 9999999999
    for pos in starting_positions:
        journey_steps = get_fewest_steps_to_destination(height_map, pos, end_pos)
        if 0 < journey_steps < shortest_lowest_journey_steps:
            shortest_lowest_journey_steps = journey_steps
    return shortest_lowest_journey_steps


def main():
    data = read_file("day12_data.dat")
    height_map = get_height_map(data)

    end_pos = get_position(height_map, "E")
    reset_marker(height_map, "E", "z")

    # Part 1
    start_pos = get_position(height_map, "S")
    reset_marker(height_map, "S", "a")
    fewest_steps = get_fewest_steps_to_destination(height_map, start_pos, end_pos)
    print(f"Fewest steps to destination={fewest_steps}")

    # Part 2
    starting_marker = "a"
    shortest_lowest_journey_steps = get_shortest_journey_to_destination(height_map, starting_marker, end_pos)
    print(f"Shortest journey from {starting_marker} to destination={shortest_lowest_journey_steps}")


if __name__ == "__main__":
    main()
