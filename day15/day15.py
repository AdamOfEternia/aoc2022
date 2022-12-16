from dataclasses import dataclass, field


@dataclass
class Grid:
    rows: list = field(init=False, default_factory=list)
    left: int
    top: int
    width: int
    height: int


@dataclass
class Positional:
    sensor_x: int
    sensor_y: int
    beacon_x: int
    beacon_y: int


def display_grid(grid):
    for row in grid.rows:
        print(row)


def calc_md(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def update_sensor_grid_row(grid, row, start, end):
    if grid.top <= row < grid.height:
        gr = grid.rows[row]
        r = gr[:start] + ("#" * (end - start)) + gr[end:grid.width]
        grid.rows[row] = r


def scan_sensor_grid(grid, positions):
    for pos in positions:
        md = calc_md(pos.sensor_x, pos.beacon_x, pos.sensor_y, pos.beacon_y)
        factor = md
        for idx in range(0, md + 1):
            l_pos = max(0, pos.sensor_x - grid.left - factor)
            r_pos = min(pos.sensor_x - grid.left + factor + 1, grid.width)
            update_sensor_grid_row(grid, pos.sensor_y - idx, l_pos, r_pos)
            update_sensor_grid_row(grid, pos.sensor_y + idx, l_pos, r_pos)
            factor -= 1


def populate_sensors_and_beacons(grid, positions):
    for pos in positions:
        x = pos.sensor_x - grid.left
        y = pos.sensor_y - grid.top
        gr = str(grid.rows[y])
        r = gr[:x] + "S" + gr[x+1:]
        grid.rows[y] = r

        x = pos.beacon_x - grid.left
        y = pos.beacon_y - grid.top
        gr = str(grid.rows[y])
        r = gr[:x] + "B" + gr[x+1:]
        grid.rows[y] = r


def create_grid(data):
    ssx = sorted([p.sensor_x for p in data])
    ssy = sorted([p.sensor_y for p in data])
    sbx = sorted([p.beacon_x for p in data])
    sby = sorted([p.beacon_y for p in data])
    width = max(ssx[-1], sbx[-1]) - min(ssx[0], sbx[0]) + 1
    height = max(ssy[-1], sby[-1]) - min(ssy[0], sby[0]) + 1
    grid = Grid(left=min(ssx[0], sbx[0]), top=min(ssy[0], sby[0]), width=width, height=height)
    for y in range(grid.top, grid.height):
        grid.rows.append("." * grid.width)
    return grid


def parse_data(data):
    parsed_data = []
    for row in data:
        parts = row.split(":")
        sx = int(parts[0][parts[0].find("x=") + 2:parts[0].find(",")])
        sy = int(parts[0][parts[0].rfind("y=") + 2:])
        bx = int(parts[1][parts[1].find("x=") + 2:parts[1].find(",")])
        by = int(parts[1][parts[1].rfind("y=") + 2:])
        parsed_data.append(Positional(sx, sy, bx, by))
    return parsed_data


def read_file(file_name):
    with open(file_name) as file:
        data = [line.rstrip() for line in file]
    return data


def main():
    positional_data = parse_data(read_file("day15_data.dat"))

    positional_grid = create_grid(positional_data)
    populate_sensors_and_beacons(positional_grid, positional_data)
    display_grid(positional_grid)

    print()
    sensor_grid = create_grid(positional_data)
    scan_sensor_grid(sensor_grid, positional_data)
    display_grid(sensor_grid)

    print()
    num_row = 10
    beacons_in_row = str(positional_grid.rows[num_row]).count("B")
    num_positions = str(sensor_grid.rows[num_row]).count("#") - beacons_in_row
    print(f"{num_positions} cannot contain a beacon on row {num_row}")


if __name__ == "__main__":
    main()
