from game import *
import random
import datetime

tiles = []
number_of_games = 1000
save_step = 100
out_file_name = 'random_data_' + str(number_of_games) + '-games_' + str(save_step) + '-save-step_' + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.txt'
for i in range(number_of_games):
    game_state = initial_state()
    moved = True
    score = 0
    steps = 0
    while not is_game_over(game_state):
        if moved:
            game_state = do_a_random_spawn(game_state)
            steps += 1
        step = random.randrange(4)
        game_state, moved, score_inc = action(game_state, step)
        score += score_inc
    tiles.append([steps, game_state.max(), score])
    print('Game',i,'tile',game_state.max())
    if (i + 1) % save_step == 0:
        data_file = open(out_file_name, 'a')
        print(i + 1, tiles, file=data_file)
        data_file.close()
print(tiles)
