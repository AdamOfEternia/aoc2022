import string
from dataclasses import dataclass

from utils.utils import read_file

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


@dataclass
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


def get_total_badge_priority(groups):
    total_badge_priority = 0
    for group in groups:
        badge = group.get_group_badge()
        badge_priority = get_priority_value(badge)
        total_badge_priority += badge_priority
    return total_badge_priority


def get_total_duplicate_item_in_rucksacks_priority(rucksacks):
    total_priority = 0
    for rucksack in rucksacks:
        duplicate_item = rucksack.get_duplicate_item_in_compartments()
        item_priority = get_priority_value(duplicate_item)
        total_priority += item_priority
    return total_priority


def get_groups(rucksacks):
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(Group(rucksacks[i:i+3]))
    return groups


def get_rucksacks(data):
    return [Rucksack(x) for x in data]


def main():
    data = read_file("day03_data.dat")
    rucksacks = get_rucksacks(data)
    groups = get_groups(rucksacks)

    total_priority = get_total_duplicate_item_in_rucksacks_priority(rucksacks)
    print(f"Total duplicate item in rucksacks priority={total_priority}")

    total_badge_priority = get_total_badge_priority(groups)
    print(f"Total badge priority={total_badge_priority}")


if __name__ == "__main__":
    main()
