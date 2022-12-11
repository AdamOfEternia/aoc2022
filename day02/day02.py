from dataclasses import dataclass


@dataclass
class Move:
    name: str
    value: int
    keys: list


moves = [
    Move(name="Rock", value=1, keys=['A', 'X']),
    Move(name="Paper", value=2, keys=['B', 'Y']),
    Move(name="Scissors", value=3, keys=['C', 'Z'])
]


def get_score(me, cpu):
    score = me.value

    if me.value == cpu.value:
        score += 3
    elif me.value == 1 and cpu.value == 3:
        score += 6
    elif me.value == 2 and cpu.value == 1:
        score += 6
    elif me.value == 3 and cpu.value == 2:
        score += 6

    return score


def get_my_total_score_pt2(games):
    my_total_score = 0
    for game in games:
        cpu = next((x for x in moves if game[0] in x.keys), None)
        if game[2] == 'X':
            me_idx = moves.index(cpu) - 1
            if me_idx < 0:
                me_idx = len(moves) - 1
            me = moves[me_idx]
        elif game[2] == 'Y':
            me = next((x for x in moves if game[0] in x.keys), None)
        elif game[2] == 'Z':
            me_idx = moves.index(cpu) + 1
            if me_idx == len(moves):
                me_idx = 0
            me = moves[me_idx]
        my_total_score += get_score(me, cpu)
    return my_total_score


def get_my_total_score(games):
    my_total_score = 0
    for game in games:
        my_game_score = 0

        cpu = next((x for x in moves if game[0] in x.keys), None)
        me = next((x for x in moves if game[2] in x.keys), None)

        my_game_score += me.value
        if me.value == cpu.value:
            my_game_score += 3
        elif me.value == 1 and cpu.value == 3:
            my_game_score += 6
        elif me.value == 2 and cpu.value == 1:
            my_game_score += 6
        elif me.value == 3 and cpu.value == 2:
            my_game_score += 6
        my_total_score += my_game_score
    return my_total_score


def read_file(file_name):
    with open(file_name) as file:
        data = [line.rstrip() for line in file]
    return data


def main():
    games = read_file("day02_data.dat")
    print(f"My total score (Pt1) is {get_my_total_score(games)}")
    print(f"My total score (Pt2) is {get_my_total_score_pt2(games)}")


if __name__ == "__main__":
    main()
