from game import Game
import os

def show(game):
    os.system("clear")
    print(" -----| 2048 |-----")
    for i in range(game.height):
        for j in range(game.width):
            if game.board[i][j]:
                print("%4d " % game.board[i][j], end='')
            else:
                print("   - ", end='')
        print()
    print(" ------------------")

CODE_INVALID_INPUT = 0
CODE_EXIT = 1
CODE_OK = 2
CODE_UNAVALIABLE_MOVEMENT = 3

def play_turn(game, inpt):
    code = CODE_INVALID_INPUT
    if inpt == '\x1b':
        code = CODE_EXIT
    elif inpt == '\x1b[D':
        code = CODE_OK if game.move_left() else CODE_UNAVALIABLE_MOVEMENT
    elif inpt == '\x1b[C':
        code = CODE_OK if game.move_right() else CODE_UNAVALIABLE_MOVEMENT
    elif inpt == '\x1b[A':
        code = CODE_OK if game.move_up() else CODE_UNAVALIABLE_MOVEMENT
    elif inpt == '\x1b[B':
        code = CODE_OK if game.move_down() else CODE_UNAVALIABLE_MOVEMENT
    return code


game = Game()
code = CODE_OK

while True and code != CODE_EXIT:
    if code == CODE_OK:
        game.random_spawn()

    show(game)

    if code == CODE_INVALID_INPUT:
        print('Nevalidan potez!')
    if code == CODE_UNAVALIABLE_MOVEMENT:
        print('Nijedno polje se ne moze pomeriti!')

    print("Unesi sledeci pravac: ")
    code = play_turn(game, input())

print('Izazak iz igre...')
