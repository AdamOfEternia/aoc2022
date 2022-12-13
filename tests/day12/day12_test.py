from day12.day12 import read_file, get_fewest_steps_to_destination, get_height_map, get_position, Position, reset_marker, get_shortest_journey_to_destination


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
    end_pos = get_position(height_map, "E")
    assert end_pos == test_pos


def test_get_fewest_steps_to_destination():
    data = read_file("day12/day12_test_data.dat")
    height_map = get_height_map(data)
    start_pos = get_position(height_map, "S")
    reset_marker(height_map, "S", "a")
    end_pos = get_position(height_map, "E")
    reset_marker(height_map, "E", "z")
    steps = get_fewest_steps_to_destination(height_map, start_pos, end_pos)
    assert steps == 31


def test_get_shortest_journey_to_destination():
    data = read_file("day12/day12_test_data.dat")
    height_map = get_height_map(data)
    end_pos = get_position(height_map, "E")
    reset_marker(height_map, "S", "a")
    reset_marker(height_map, "E", "z")
    steps = get_shortest_journey_to_destination(height_map, "a", end_pos)
    assert steps == 29
