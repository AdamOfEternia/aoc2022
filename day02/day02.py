class Move:

    def __init__(self, name, value, keys):
        self.name = name
        self.value = value
        self.keys = keys

    def __str__(self):
        return f"{self.name} ({self.value})"


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


def main():
    moves = [
        Move(name="Rock", value=1, keys=['A']),
        Move(name="Paper", value=2, keys=['B']),
        Move(name="Scissors", value=3, keys=['C'])
    ]

    with open("game.dat") as file:
        games = [line.rstrip() for line in file]

    my_score = 0
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

        my_score += get_score(me, cpu)

    print(f"My final score is {my_score}")


if __name__ == "__main__":
    main()
