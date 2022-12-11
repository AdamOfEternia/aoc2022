from day01.day01 import read_file, parse_data, get_elf_with_most_calories, get_elves_with_most_calories


def test_get_elf_with_most_calories():
    data = read_file("day01/day01_test_data.dat")
    elves = parse_data(data)
    top_elf = get_elf_with_most_calories(elves)
    assert top_elf.calories == 24000


def test_get_elves_with_most_calories():
    data = read_file("day01/day01_test_data.dat")
    elves = parse_data(data)
    top_elves = get_elves_with_most_calories(elves, 3)
    assert len(top_elves) == 3
    assert sum(e.calories for e in top_elves) == 45000
