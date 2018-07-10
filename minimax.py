from game import *
import random
import datetime

minimum_depth = 4

def minimax(state, max_player, depth):
    if depth == 0:
        return 0
    depth -= 1
    if max_player:
        # Maximizing player
        possible_states = list(enumerate(filter(lambda x: x[1], get_possible_states(state))))
        if not possible_states:
            return -1000 # terminal state
        return max([data[2] + minimax(data[0], False, depth) for index, data in possible_states])
    else:
        # Minimizing player
        possible_spawns = get_possible_spawns(state)
        if not possible_spawns:
            return -1000 # terminal state
        return min([minimax(spawn_state, True, depth) for spawn_state in possible_spawns])

def choose_best_step(state, moved):
    if not moved:
        print('Random!')
        return random.randrange(0, 4)

    possible_states = enumerate(get_possible_states(state))
    depth = minimum_depth - 1
    best_score = -10000000
    best_action = -1
    for index, data in possible_states:
        if data[1]:
            score = data[2] + minimax(data[0], False, depth)
            if score > best_score:
                best_score = score
                best_action = index
    return best_action

tiles = []
number_of_games = 1000
save_step = 100
out_file_name = 'minimax_data_' + str(number_of_games) + '-games_' + str(save_step) + '-save-step_' + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.txt'
for i in range(number_of_games):
    game_state = initial_state()
    moved = True
    score = 0
    steps = 0
    while not is_game_over(game_state):
        if moved:
            game_state = do_a_random_spawn(game_state)
            steps += 1
        step = choose_best_step(game_state, moved)
        game_state, moved, score_inc = action(game_state, step)
        score += score_inc
    tiles.append([steps, game_state.max(), score])
    print('Game',i,'tile',game_state.max())
    if (i + 1) % save_step == 0:
        data_file = open(out_file_name, 'a')
        print(i + 1, tiles, file=data_file)
        data_file.close()
print(tiles)
