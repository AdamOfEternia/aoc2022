from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x}-{self.y}")


@dataclass
class Move:
    dir: str
    steps: int


def get_moves(data):
    moves = []
    for row in data:
        parts = row.split()
        moves.append(Move(str(parts[0]), int(parts[1])))
    return moves


def read_file():
    with (open("data.dat")) as file:
        data = [line.rstrip() for line in file]
    return data


def main():
    data = read_file()
    moves = get_moves(data)

    num_knots = 2
    knots = []
    for i in range(0, num_knots):
        knots.append([Position(0, 0)])

    for move in moves:
        hx = knots[0][-1].x
        hy = knots[0][-1].y
        steps = move.steps
        for step in range(0, steps):
            # move head
            match move.dir:
                case "U":
                    hy -= 1
                case "D":
                    hy += 1
                case "L":
                    hx -= 1
                case "R":
                    hx += 1
            knots[0].append(Position(hx, hy))

            kx = knots[1][-1].x
            ky = knots[1][-1].y

            if abs(hx - kx) == 2 and hy - ky == 0:
                match move.dir:
                    case "L":
                        kx -= 1
                    case "R":
                        kx += 1
                knots[1].append(Position(kx, ky))
            elif abs(hy - ky) == 2 and hx - kx == 0:
                match move.dir:
                    case "U":
                        ky -= 1
                    case "D":
                        ky += 1
                knots[1].append(Position(kx, ky))
            elif abs(hx - kx) == 2 or abs(hy - ky) == 2:
                kx = knots[0][-2].x
                ky = knots[0][-2].y
                knots[1].append(Position(kx, ky))

    print(f"Head positions={len(knots[0])}")

    unique_tail_positions = set(knots[-1])
    print(f"Unique tail positions={len(unique_tail_positions)}")


if __name__ == "__main__":
    main()
