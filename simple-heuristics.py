from game import *

scores = []
max_tiles = []
lengths = []

for i in range(20):
    state = initial_state()
    moved = True
    action_counter = 0
    score = 0
    length = 0

    while not is_game_over(state):
        if moved:
            state = do_a_random_spawn(state)
            action_counter = 0

        if not moved:
            action_counter += 1

        if action_counter >= 4:
            raise ValueError('Bug encountered')

        state, moved, score_increase = action(state, action_counter)
        if moved:
            length += 1
            score += score_increase

    max_tiles.append(state.max())
    scores.append(score)
    lengths.append(length)
    print('Game', (i + 1), ': max_tile', state.max(), ', score', score, ', length', length)
print(max(max_tiles))
print(max(scores))
print(max(lengths))
