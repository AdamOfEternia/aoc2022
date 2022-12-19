from dataclasses import dataclass, field

from utils.utils import read_file


@dataclass
class Beacon:
    icon: str = field(init=False, default="B")
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")


@dataclass
class Sensor:
    icon: str = field(init=False, default="S")
    x: int
    y: int
    closest_beacon: Beacon

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")


def find_positions_where_beacon_cannot_be(positional_data, row):
    empty_pos = set()
    for s in positional_data:
        y_dist = abs(s.y - row)
        x_dist = calc_md(s.x, s.y, s.closest_beacon.x, s.closest_beacon.y) - y_dist
        for x in range(s.x - x_dist, s.x + x_dist + 1):
            empty_pos.add(x)
    return empty_pos


def calc_md(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def parse_data(data):
    parsed_data = []
    for row in data:
        parts = row.split(":")
        sx = int(parts[0][parts[0].find("x=") + 2:parts[0].find(",")])
        sy = int(parts[0][parts[0].rfind("y=") + 2:])
        bx = int(parts[1][parts[1].find("x=") + 2:parts[1].find(",")])
        by = int(parts[1][parts[1].rfind("y=") + 2:])
        b = Beacon(bx, by)
        s = Sensor(sx, sy, b)
        parsed_data.append(s)
    return parsed_data


def main():
    positional_data = parse_data(read_file("day15_data.dat"))

    # Part 1
    which_row = 2_000_000
    num_beacons_on_row = len([a for a in (set([b.closest_beacon for b in positional_data])) if a.y == which_row])
    num_positions_beacon_cannot_be = len(find_positions_where_beacon_cannot_be(positional_data, which_row)) - num_beacons_on_row
    print(f"How many positions on row {which_row} cannot contain a beacon?  {num_positions_beacon_cannot_be}")


if __name__ == "__main__":
    main()
