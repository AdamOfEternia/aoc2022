from day12.day12 import read_file, get_fewest_steps_to_destination, get_height_map, get_position, Position


def test_get_start_position():
    test_pos = Position(1, 1)
    data = read_file("day12/day12_test_data.dat")
    height_map = get_height_map(data)
    start_pos = get_position(height_map, "S")
    assert start_pos == test_pos


def test_get_destination_position():
    test_pos = Position(6, 3)
    data = read_file("day12/day12_test_data.dat")
    height_map = get_height_map(data)
    start_pos = get_position(height_map, "E")
    assert start_pos == test_pos


def test_get_fewest_steps_to_destination():
    data = read_file("day12/day12_test_data.dat")
    height_map = get_height_map(data)
    steps = get_fewest_steps_to_destination(height_map)
    assert steps == 31
