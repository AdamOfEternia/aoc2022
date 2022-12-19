from utils.utils import read_file


def main():
    data = read_file("data.dat")

    reg_x = 1
    cycle = 1
    cycles = []
    for row in data:
        match row.split():
            case ["noop"]:
                cycles.append((cycle, reg_x))
                cycle += 1
            case ["addx", *rest]:
                cycles.append((cycle, reg_x))
                cycle += 1
                cycles.append((cycle, reg_x))
                cycle += 1
                reg_x += int(rest[0])

    # pt1
    signal_strength = 0
    for cycle in range(19, len(cycles), 40):
        signal_strength += (cycle + 1) * cycles[cycle][1]
    print(f"Signal strength={signal_strength}")

    # pt2
    col = 0
    for cycle in cycles:
        sprite_pos = cycle[1]
        if (sprite_pos-1) <= col <= (sprite_pos+1):
            print("#", end='')
        else:
            print(".", end='')
        col += 1
        if col > 39:
            print()
            col = 0


if __name__ == "__main__":
    main()
