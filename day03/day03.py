from dataclasses import dataclass


@dataclass
class Rucksack:
    compartments: list

    def __init__(self, items):
        self.compartments = []
        self.compartments.append(items[:len(items) // 2])
        self.compartments.append(items[len(items) // 2:])

    def get_duplicate_item_in_compartments(self):
        for search_item in self.compartments[0]:
            for item in self.compartments[1]:
                if search_item == item:
                    return search_item


def get_priority_value(ch: str):
    if ch.islower():
        return ord(ch) - 96
    elif ch.isupper():
        return ord(ch) - 38


def read_file():
    with open("packed.dat") as file:
        bags = [line.rstrip() for line in file]
    return bags


def main():
    bags = read_file()
    rucksacks = []
    for bag in bags:
        rucksacks.append(Rucksack(bag))

    for rucksack in rucksacks:
        duplicate_item = rucksack.get_duplicate_item_in_compartments()
        item_priroty = get_priority_value(duplicate_item)
        print(f"Duplicate packed item is {duplicate_item}, priority {item_priroty}")


if __name__ == "__main__":
    main()
