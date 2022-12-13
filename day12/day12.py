from dataclasses import dataclass, field


@dataclass
class Position:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")


def get_height_map(data):
    height_map = [f"~{x}~" for x in data]
    height_map.insert(0, "~" * len(height_map[0]))
    height_map.append("~" * len(height_map[0]))
    return height_map


def read_file(file_name):
    with open(file_name) as file:
        data = [line.rstrip() for line in file]
    return data


def get_position(height_map, marker):
    pos = Position(-1, -1)
    for r in range(0, len(height_map)):
        c = height_map[r].find(marker)
        if c > -1:
            pos.x = c
            pos.y = r
            break
    return pos


def get_options(height_map, curr_pos, curr_pos_val):
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


def get_fewest_steps_to_destination(height_map):
    # get start and end positions
    start_pos = get_position(height_map, "S")
    end_pos = get_position(height_map, "E")

    # set height map values for actual start and end positions
    height_map[start_pos.y] = height_map[start_pos.y].replace("S", "a")
    height_map[end_pos.y] = height_map[end_pos.y].replace("E", "z")

    # traverse the route
    curr_pos = Position(start_pos.x, start_pos.y)
    positions_travelled = [curr_pos]
    good_route = [curr_pos]
    arrived = curr_pos == end_pos
    while not arrived:
        curr_pos_val = ord(height_map[curr_pos.y][curr_pos.x])
        options = get_options(height_map, curr_pos, curr_pos_val)
        next_pos = get_next_position(options, positions_travelled, end_pos)
        if next_pos.x == -1 and next_pos.y == -1:
            good_route.pop()
        if next_pos.x != -1 and next_pos.y != -1:
            positions_travelled.append(next_pos)
            good_route.append(next_pos)
            arrived = next_pos == end_pos
        curr_pos = good_route[-1]

    steps_taken = len(set(positions_travelled)) - 1
    return steps_taken


def main():
    data = read_file("day12_data.dat")
    height_map = get_height_map(data)

    fewest_steps = get_fewest_steps_to_destination(height_map)
    print(f"Fewest steps to destination={fewest_steps}")


if __name__ == "__main__":
    main()
