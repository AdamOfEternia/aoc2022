from day03.day03 import get_rucksacks, get_total_duplicate_item_in_rucksacks_priority, get_groups, get_total_badge_priority
from utils.utils import read_file


def test_get_rucksacks():
    data = read_file("day03/day03_test_data.dat")
    rucksacks = get_rucksacks(data)
    assert rucksacks[0].compartments[0] == "vJrwpWtwJgWr"
    assert rucksacks[0].compartments[1] == "hcsFMMfFFhFp"


def test_get_total_duplicate_item_in_rucksacks_priority():
    data = read_file("day03/day03_test_data.dat")
    rucksacks = get_rucksacks(data)
    total_priority = get_total_duplicate_item_in_rucksacks_priority(rucksacks)
    assert total_priority == 157


def test_get_groups():
    data = read_file("day03/day03_test_data.dat")
    rucksacks = get_rucksacks(data)
    groups = get_groups(rucksacks)
    assert len(groups[0].rucksacks) == 3


def test_get_total_badge_priority():
    data = read_file("day03/day03_test_data.dat")
    rucksacks = get_rucksacks(data)
    groups = get_groups(rucksacks)
    total_priority = get_total_badge_priority(groups)
    assert total_priority == 70
