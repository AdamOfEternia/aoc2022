from dataclasses import dataclass

import names


@dataclass
class Elf:
    name: str
    calories: int

    def __init__(self, calories):
        self.name = names.get_first_name()
        self.calories = calories


def get_elf_with_most_calories(elves):
    return max(elves, key=lambda x: x.calories)


def get_elves_with_most_calories(elves, num_elves):
    return sorted(elves, key=lambda x: x.calories, reverse=True)[:num_elves]


def parse_data(data):
    elves = []
    elf_calories = 0
    for calories in data:
        if calories != "":
            elf_calories += int(calories)
        else:
            elves.append(Elf(calories=elf_calories))
            elf_calories = 0
    return elves


def read_file(file_name):
    with open(file_name) as file:
        data = [line.rstrip() for line in file]
    # add empty line to end of data if none exists
    if data[-1] != "":
        data.append("")
    return data


def main():
    data = read_file("day01_data.dat")
    elves = parse_data(data)

    top_elf = get_elf_with_most_calories(elves)
    print(f"Elf carrying the highest total calories is {top_elf.name}, carrying {top_elf.calories} calories")

    top3_elves = get_elves_with_most_calories(elves, 3)
    print(f"Total calories of top 3 Elves ({str([x.name for x in top3_elves])[1:-1]}) is {sum(e.calories for e in top3_elves)} calories")


if __name__ == "__main__":
    main()
