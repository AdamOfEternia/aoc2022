import names
from dataclasses import dataclass


@dataclass
class Elf:
    name: str
    section_start: int
    section_end: int

    def __init__(self, section_start, section_end):
        self.name = names.get_first_name()
        self.section_start = section_start
        self.section_end = section_end


@dataclass
class Team:
    elf1: Elf
    elf2: Elf

    def __init__(self, elf1, elf2):
        self.elf1 = elf1
        self.elf2 = elf2

    def do_elves_clash_fully(self):
        if self.elf1.section_start >= self.elf2.section_start and self.elf1.section_end <= self.elf2.section_end:
            return True
        elif self.elf2.section_start >= self.elf1.section_start and self.elf2.section_end <= self.elf1.section_end:
            return True
        return False

    def do_elves_clash_partially(self):
        if self.elf2.section_start <= self.elf1.section_start <= self.elf2.section_end:
            return True
        elif self.elf2.section_start <= self.elf1.section_end <= self.elf2.section_end:
            return True
        if self.elf1.section_start <= self.elf2.section_start <= self.elf1.section_end:
            return True
        elif self.elf1.section_start <= self.elf2.section_end <= self.elf1.section_end:
            return True
        return False


def read_file():
    with open("pairs.dat") as file:
        lines = [line.rstrip() for line in file]
    return lines


def main():
    teams = []
    lines = read_file()
    for line in lines:
        first, second = line.split(',', 1)
        start1, end1 = first.split('-', 1)
        start2, end2 = second.split('-', 1)
        teams.append(Team(elf1=Elf(int(start1), int(end1)), elf2=Elf(int(start2), int(end2))))

    full_clash_count = 0
    partial_clash_count = 0
    for team in teams:
        if team.do_elves_clash_fully():
            full_clash_count += 1
        if team.do_elves_clash_partially():
            partial_clash_count += 1
    print(f"Number of clashing teams is {full_clash_count}")
    print(f"Number of partial clashing teams is {partial_clash_count}")


if __name__ == "__main__":
    main()
