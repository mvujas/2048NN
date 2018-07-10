from experience_replay import ExperienceBuffer
import neural_network as dnn
import numpy as np
import game
import random

# Buffer for experience replay
exp_buffer = ExperienceBuffer()

# Hyperparameters
discount_factor = 0.9
learning_rate = 0.0005
epsilon = 1
turns_until_min_epsilon = 50000

# Network
net = dnn.NeuralNetwork(learning_rate=learning_rate)
net.start_session()

# Information about training
number_of_games = 10
batch_size = 3
turn_count = 0

for game_count in range(number_of_games):
    print('Game', game_count + 1)
    state = game.initial_state()
    moved = True
    while not game.is_game_over(state):
        action = None
        if moved:
            turn_count = min(turn_count + 1, turns_until_min_epsilon)
            epsilon = 0#1 - 0.95 * turn_count / turns_until_min_epsilon
            state = game.do_a_random_spawn(state)
            if random.random() < epsilon:
                action = random.randrange(game.number_of_actions)
            else:
                action = net.predict([dnn.prepare_input(state)])[1][0]
        else:
            action = random.randrange(game.number_of_actions)

        new_state, moved, reward = game.action(state, action, copy=True)
        if moved:
            exp_buffer.add([dnn.prepare_input(state), action, reward, dnn.prepare_input(new_state)])
            state = new_state
        if not exp_buffer.is_empty():
            batch = exp_buffer.get_batch(batch_size)
            old_states = [i[0] for i in batch]
            new_states = [i[3] for i in batch]
            rewards = [i[2] for i in batch]
            actions = [i[1] for i in batch]
            Q_values, initial_predictions = net.predict(old_states)
            target_Q_values = net.max_Q(new_states) * discount_factor + rewards
            for i in range(batch_size):
                Q_values[i][actions[i]] = target_Q_values[i]
            loss, _ = net.train(old_states, Q_values)
            print('Game', game_count + 1, loss)
    print('Max tile after game', game_count + 1, 'is', state.max())
