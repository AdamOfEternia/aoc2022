from dataclasses import dataclass


@dataclass()
class Stack:
    num: int
    items: list

    def __init__(self, num):
        self.num = num
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        item = self.items[-1]
        self.items.pop()
        return item

    def get_top_item(self):
        return self.items[-1]

    def remove_items(self, count):
        items = self.items[-count:]
        for c in range(0, count):
            self.items.pop()
        return items

    def add_items(self, items):
        self.items.extend(items)


@dataclass
class Move:
    num_moves: int
    from_stack: int
    to_stack: int

    def __init__(self, num_moves, from_stack, to_stack):
        self.num_moves = num_moves
        self.from_stack = from_stack
        self.to_stack = to_stack


def remove_items_one_by_one(stacks, moves):
    """Day05 - Part1"""
    for move in moves:
        for m in range(0, move.num_moves):
            item = stacks[move.from_stack - 1].remove_item()
            stacks[move.to_stack - 1].add_item(item)
    return stacks


def remove_items_by_chunks(stacks, moves):
    """Day05 - Part2"""
    for move in moves:
        items = stacks[move.from_stack - 1].remove_items(move.num_moves)
        stacks[move.to_stack - 1].add_items(items)
    return stacks


def main():
    with (open("crates.dat")) as file:
        lines = [line.rstrip() for line in file]

    crates = []
    for line in lines:
        if line == "":
            break
        crates.append(line)
    crates = list(reversed(crates))
    print(crates)

    stack_indexes = crates[0].strip().split()
    stacks = []
    for stack in stack_indexes:
        stacks.append(Stack(int(stack)))
    print(stacks)

    stack_index = 0
    for r in crates[1:]:
        r2 = r
        crate_row = []
        while r2:
            crate_row.append(r2[:4].rstrip())
            r2 = r2[4:]
        for crate in crate_row:
            if crate != "":
                stacks[stack_index].add_item(crate)
            stack_index += 1
        stack_index = 0
    print(stacks)

    moves = []
    for line in lines:
        if line.startswith("move "):
            parts = line.split(sep=' ')
            moves.append(Move(int(parts[1]), int(parts[3]), int(parts[5])))
    print(moves)

    stacks = remove_items_by_chunks(stacks, moves)

    for stack in stacks:
        top_item = str(stack.get_top_item()).strip("[]")
        print(top_item, end='')


if __name__ == "__main__":
    main()