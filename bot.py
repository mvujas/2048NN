import game
import neural_network
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import datetime

# Statistics
losses = []

# Network initialization
net = neural_network.NeuralNetwork()
net.start_session()

# Initialization of buffer for experience replay
replay_buffer = []
replay_buffer_size = 0
replay_buffer_limit = 10e6

# Q Learning hyperparameters
gamma = .9
epsilon = 1

# Game parameters
number_of_actions = 4
game_iterations = 25

start_time = time.time()
models_dir = os.path.join(os.getcwd(), 'models')
target_dir = os.path.join(models_dir, 'model_' + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
log_counter = 20

def log_result(game_counter):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    time_passed = time.time() - start_time
    hours_passed_str = '%.2f' % (time_passed / 3600)
    batch_name = '%d_games-%s_hours_batch' % (game_counter, hours_passed_str)
    batch_dir = os.path.join(target_dir, batch_name)
    if os.path.exists(batch_dir):
        return
    os.makedirs(batch_dir)
    if losses:
        plt.plot(losses)
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.savefig(os.path.join(batch_dir, 'losses.pdf'))
        plt.savefig(os.path.join(batch_dir, 'losses.png'))
        plt.clf()
        losses[:] = []
    net.save_model(os.path.join(batch_dir, 'net_model'))
    print('Logged successfully after %d games and %s hours' % (game_counter, hours_passed_str))

powers_of_two = { 2**i: i for i in range(17) }
powers_of_two[0] = 0
def transform_state_to_input(state):
    height, width = state.shape
    result = np.zeros([1, height, width, 17], dtype=np.float32)
    for i in range(height):
        for j in range(width):
            result[0][i][j][powers_of_two[state[i][j]]] = 1
    return result

state = game.initial_state()
moved = True
while not game.is_game_over(state):
    if moved:
        game.do_a_random_spawn(state)
    if not moved:
        action = random.randrange(number_of_actions)
    else:
        _, action = net.predict(transform_state_to_input(state))
        action = action[0]
    state, moved, _ = game.action(state, action)
print(state)

for game_counter in range(game_iterations):
    state = game.initial_state()
    moved = True
    print('Game', game_counter)
    steps = 0
    # Repeat until game reaches terminal state
    while not game.is_game_over(state):

        # Spawn new tile
        if moved:
            game.do_a_random_spawn(state)
            steps += 1
        action = None

        # Choose action according to epsilon greedy policy
        if not moved or random.random() < epsilon:
            action = random.randrange(number_of_actions)
        else:
            _, action = net.predict(transform_state_to_input(state))
            action = action[0]

        tmp_state = None
        tmp_moved = None

        for action_num in range(number_of_actions):
            # Do an action and get new state and reward
            new_state, moved, reward = game.action(state, action_num, copy=True)

            # Save state info into buffer
            if moved:
                experience = [transform_state_to_input(state), action, reward, transform_state_to_input(new_state)]
                if replay_buffer_size != replay_buffer_limit:
                    replay_buffer.append(experience)
                    replay_buffer_size += 1
                else:
                    replay_buffer[random.randrange(replay_buffer_limit)] = experience

            if action_num == action:
                tmp_state = new_state.copy()
                tmp_moved = moved

        state = tmp_state
        moved = tmp_moved

        # If replay_buffer isn't empty get random batch and train the network on it, we also need to gather enough data to efficiently train the network
        if replay_buffer_size:
            for _ in range(2):
                state1, action, reward, state2 = replay_buffer[random.randrange(replay_buffer_size)]
                initial_Q, _ = net.predict(state1)

                new_state_Q, _ = net.predict(state2)

                initial_Q[0][action] = 2 * reward + gamma * max(new_state_Q[0])

                loss, _ = net.train(state1, initial_Q)
                losses.append(loss)
    print('     Steps:', steps)
    epsilon = max(0.1, 1 - game_counter / 5)
    if game_counter > 0 and  game_counter % log_counter == 0:
        log_result(game_counter + 1)

for test_game_counter in range(10):
    state = game.initial_state()
    moved = True
    while not game.is_game_over(state):
        if moved:
            game.do_a_random_spawn(state)
        if not moved:
            action = random.randrange(number_of_actions)
        else:
            _, action = net.predict(transform_state_to_input(state))
            action = action[0]
        state, moved, _ = game.action(state, action)
    print('Test game', test_game_counter)
    print(state)
for _ in range(10):
    print(net.predict(replay_buffer[random.randrange(replay_buffer_size)][0]))
