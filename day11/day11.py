import math
from dataclasses import dataclass, field


@dataclass
class Monkey:
    name: str
    items: list
    operation: list
    div_test: int
    true_action: int
    false_action: int
    inspection_count: int = field(init=False)

    def __post_init__(self):
        self.inspection_count = 0

    def add_item(self, item):
        self.items.append(item)

    def remove_item_from_end(self):
        self.items.pop()

    def remove_item_from_start(self):
        self.items.pop(0)


def parse_data_into_monkeys(data):
    monkeys = []
    for i in range(0, len(data), 6):
        rows = data[i:i+6]
        name = rows[0]
        items = [int(x) for x in rows[1].split(":")[1].strip().split(",")]
        op = rows[2].split(":")[1].strip().split(" ")[-2:]
        test_div = int(rows[3].split(":")[-1].strip().split(" ")[-1])
        t_action = int(rows[4].split(":")[-1].strip().split(" ")[-1])
        f_action = int(rows[5].split(":")[-1].strip().split(" ")[-1])
        monkeys.append(Monkey(name, items, op, test_div, t_action, f_action))
    return monkeys


def read_file():
    with (open("data.dat")) as file:
        data = [l for l in (line.strip() for line in file) if l]
    return data


def get_target_monkey(worry_level, monkey):
    if worry_level % monkey.div_test == 0:
        return monkey.true_action
    return monkey.false_action


def get_worry_level(item, operation):
    worry_level = item
    v = worry_level
    if operation[1] != "old":
        v = int(operation[1])
    worry_level = eval(f"{worry_level} {operation[0]} {v}")
    return math.floor(worry_level / 3)


def main():
    data = read_file()
    monkeys = parse_data_into_monkeys(data)

    num_rnds = 20
    for rnd in range(0, num_rnds):
        for monkey in monkeys:
            tmp_list = [x for x in monkey.items]
            for item in tmp_list:
                monkey.inspection_count += 1
                worry_level = get_worry_level(item, monkey.operation)
                monkey.remove_item_from_start()
                target_monkey = get_target_monkey(worry_level, monkey)
                monkeys[target_monkey].add_item(worry_level)

    inspections = sorted([x.inspection_count for x in monkeys], reverse=True)
    product_of_top_two_inspections = math.prod(inspections[:2])
    print(f"Product of top two inspection counts={product_of_top_two_inspections}")


if __name__ == "__main__":
    main()
