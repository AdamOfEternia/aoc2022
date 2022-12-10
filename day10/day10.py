def read_file():
    with (open("data.dat")) as file:
        data = [line.rstrip() for line in file]
    return data


def main():
    data = read_file()

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

    signal_strength = 0
    for cycle in range(19, len(cycles), 40):
        signal_strength += (cycle + 1) * cycles[cycle][1]
    print(f"Signal strength={signal_strength}")


if __name__ == "__main__":
    main()
