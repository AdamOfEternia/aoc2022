from day15.day15 import parse_data, read_file, find_positions_where_beacon_cannot_be


def test_find_positions_where_beacon_cannot_be():
    positional_data = parse_data(read_file("day15/day15_test_data.dat"))

    # Part 1
    which_row = 10
    num_beacons_on_row = len([a for a in (set([b.closest_beacon for b in positional_data])) if a.y == which_row])
    num_empty_positions_on_row = len(find_positions_where_beacon_cannot_be(positional_data, which_row)) - num_beacons_on_row

    assert num_empty_positions_on_row == 26
