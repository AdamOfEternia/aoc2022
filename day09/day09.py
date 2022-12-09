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

    head_positions = [Position(0, 0)]
    tail_positions = [Position(0, 0)]

    for move in moves:
        hx = head_positions[-1].x
        hy = head_positions[-1].y
        steps = move.steps
        for step in range(0, steps):
            px = head_positions[-1].x
            py = head_positions[-1].y
            match move.dir:
                case "U":
                    hy -= 1
                case "D":
                    hy += 1
                case "L":
                    hx -= 1
                case "R":
                    hx += 1
            head_positions.append(Position(hx, hy))
            tx = tail_positions[-1].x
            ty = tail_positions[-1].y
            if abs(hx - tx) == 2 or abs(hy - ty) == 2:
                tail_positions.append(Position(px, py))

    print(f"Head positions={len(head_positions)}")

    unique_tail_positions = set(tail_positions)
    print(f"Unique tail positions={len(unique_tail_positions)}")


if __name__ == "__main__":
    main()
