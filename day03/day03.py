import string
from dataclasses import dataclass

lowers = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)


@dataclass
class Rucksack:
    compartments: list

    def __init__(self, items):
        self.compartments = []
        self.compartments.append(items[:len(items) // 2])
        self.compartments.append(items[len(items) // 2:])

    def get_duplicate_item_in_compartments(self):
        for ch in lowers:
            if all(ch in compartment for compartment in self.compartments):
                return ch
        for ch in uppers:
            if all(ch in compartment for compartment in self.compartments):
                return ch
        return None


@dataclass()
class Group:
    rucksacks: list

    def __init__(self, rucksacks):
        self.rucksacks = rucksacks

    def get_group_badge(self):
        compartments = []
        for rucksack in self.rucksacks:
            compartments.append("".join([str(compartment) for compartment in rucksack.compartments]))
        for ch in lowers:
            if all(ch in compartment for compartment in compartments):
                return ch
        for ch in uppers:
            if all(ch in compartment for compartment in compartments):
                return ch
        return None


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

    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(Group(rucksacks[i:i+3]))
    print(groups)

    total_priority = 0
    for rucksack in rucksacks:
        duplicate_item = rucksack.get_duplicate_item_in_compartments()
        item_priority = get_priority_value(duplicate_item)
        total_priority += item_priority
        print(f"Duplicate packed item is {duplicate_item}, priority {item_priority}")
    print(f"Total priority value {total_priority}")

    total_badge_priority = 0
    for group in groups:
        badge = group.get_group_badge()
        badge_priority = get_priority_value(badge)
        total_badge_priority += badge_priority
        print(f"Badge is {badge}, priority {badge_priority}")
    print(f"Total badge priority value {total_badge_priority}")


if __name__ == "__main__":
    main()
