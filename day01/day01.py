class Elf:
    def __init__(self, index, calories):
        self.index = index
        self.calories = calories

    def __str__(self):
        return f"Elf {self.index} is carrying {self.calories} calories"

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
        if calories == "":
            elves.append(Elf(index=len(elves) + 1, calories=elf_calories))
            elf_calories = 0
    if elf_calories > 0:
        elves.append(Elf(index=len(elves) + 1, calories=elf_calories))

    print(max(elves, key=lambda x: x.calories))


if __name__ == "__main__":
    main()
