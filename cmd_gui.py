from game import Game
import os
import random
import time

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
    action = None
    if inpt == '\x1b':
        return CODE_EXIT
    elif inpt == '\x1b[D':
        action = 3
    elif inpt == '\x1b[C':
        action = 1
    elif inpt == '\x1b[A':
        action = 0
    elif inpt == '\x1b[B':
        action = 2
    else:
        return CODE_INVALID_INPUT
    successfulness, score_increase = game.step(action)
    print(score_increase)
    return CODE_OK if successfulness else CODE_UNAVALIABLE_MOVEMENT

if __name__ == "__main__":
    game = Game()
    code = CODE_OK

    while not game.is_game_over() and code != CODE_EXIT:
        if code == CODE_OK:
            game.random_spawn()

        show(game)
        print(game.is_game_over())
        print('Score: %d' % game.score)
        '''
        if code == CODE_INVALID_INPUT:
            print('Nevalidan potez!')
        if code == CODE_UNAVALIABLE_MOVEMENT:
            print('Nijedno polje se ne moze pomeriti!')

        print("Unesi sledeci pravac: ")
        code = play_turn(game, input())
        '''
        game.step(random.randint(0, 3))
        time.sleep(0.1)

    print('Izazak iz igre...')
