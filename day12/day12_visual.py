from dataclasses import dataclass, field
import turtle as t

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


def get_astar_path(height_map):
    # get start and end positions
    start_pos = get_position(height_map, "S")
    end_pos = get_position(height_map, "E")

    # set height map values for actual start and end positions
    height_map[start_pos.y] = height_map[start_pos.y].replace("S", "a")
    height_map[end_pos.y] = height_map[end_pos.y].replace("E", "z")

    # traverse the route
    open_list = [start_pos]
    closed_list = []

    t.color(200, 25, 25)

    path_found = False
    while len(open_list) > 0:
        current_pos = sorted(open_list, key=lambda n: n.f)[0]
        open_list.remove(current_pos)
        closed_list.append(current_pos)

        t.setposition((current_pos.x * 15) - (1200 / 2), (current_pos.y * 15) - (1200 / 2))
        t.write(height_map[current_pos.y][current_pos.x])

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


def get_fewest_steps_to_destination(height_map):
    path = get_astar_path(height_map)
    return len(path) - 1


def main():
    data = read_file("day12_data.dat")
    height_map = get_height_map(data)

    t.screensize(1200, 1200)
    t.colormode(255)
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.color(100, 100, 100)
    for r in range(0, len(height_map)):
        for c in range(0, len(height_map[r])):
            t.setposition((c * 15) - (1200 / 2), (r * 15) - (1200 / 2))
            t.write(height_map[r][c])

    fewest_steps = get_fewest_steps_to_destination(height_map)
    print(f"Fewest steps to destination={fewest_steps}")

    t.exitonclick()


if __name__ == "__main__":
    main()
