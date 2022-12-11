from day02.day02 import read_file, get_my_total_score, get_my_total_score_pt2


def test_get_total_score():
    game_data = read_file("day02/day02_test_data.dat")
    total_score = get_my_total_score(game_data)
    assert total_score == 15


def test_get_total_score_pt2():
    game_data = read_file("day02/day02_test_data.dat")
    total_score = get_my_total_score_pt2(game_data)
    assert total_score == 12
