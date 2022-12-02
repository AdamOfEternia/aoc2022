from enum import Enum


class Move:

    def __init__(self, name, value, keys):
        self.name = name
        self.value = value
        self.keys = keys

    def __str__(self):
        return f"{self.name} ({self.value})"


def main():
    moves = [
        Move(name="Rock", value=1, keys=['A', 'Y']),
        Move(name="Paper", value=2, keys=['B', 'Y']),
        Move(name="Scissors", value=3, keys=['C', 'Z'])
    ]

    with open("game.dat") as file:
        games = [line.rstrip() for line in file]

    my_score = 0
    for game in games:
        cpu = next((x for x in moves if game[0] in x.keys), None)
        me = next((x for x in moves if game[2] in x.keys), None)

        print(f"{cpu} vs {me}... ", end='')

        my_score += me.value
        if me.value == cpu.value:
            my_score += 3
            print("Draw")
        elif me.value == 1 and cpu.value == 3:
            my_score += 6
            print("Win")
        elif me.value == 2 and cpu.value == 1:
            my_score += 6
            print("Win")
        elif me.value == 3 and cpu.value == 2:
            print("Win")
            my_score += 6
        else:
            print("Lose")

    print(f"My final score is {my_score}")


if __name__ == "__main__":
    main()
