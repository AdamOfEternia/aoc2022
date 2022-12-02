import names


class Elf:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"Elf {self.name} is carrying {self.calories} calories"

    def __repr__(self):
        return str(self)

    def get_calories(self):
        return self.calories


def main():
    with open("input.dat") as file:
        data = [line.rstrip() for line in file]

    elves = []
    elf_calories = 0
    for calories in data:
        if calories != "":
            elf_calories += int(calories)
        else:
            elves.append(Elf(names.get_first_name(), calories=elf_calories))
            elf_calories = 0
    if elf_calories > 0:
        elves.append(Elf(names.get_first_name(), calories=elf_calories))

    print(max(elves, key=lambda x: x.calories))
    top3_elves = sorted(elves, key=lambda x: x.calories, reverse=True)[:3]
    print(*top3_elves, sep=", ")
    print(f"Total calories of top 3 Elves is {sum(e.calories for e in top3_elves)} calories")


if __name__ == "__main__":
    main()
