import game
import neural_network0
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# Statistics
losses = []

# Network initialization
net = neural_network0.NeuralNetwork()
net.start_session()

# Initialization of buffer for experience replay
replay_buffer = []
replay_buffer_size = 0
replay_buffer_limit = 10e6

# Q Learning hyperparameters
gamma = .9
epsilon = 0.15
epsilon_decay = 0.85

# Game parameters
number_of_actions = 4
game_iterations = 25

powers_of_two = { 2**i: i for i in range(17) }
powers_of_two[0] = 0
def transform_state_to_input(state):
    height, width = state.shape
    result = np.zeros([17, height, width], dtype=np.float32)
    for i in range(height):
        for j in range(width):
            result[powers_of_two[state[i][j]]][i][j] = 1
    return result

def Vchange(grid, v):
    g0 = grid
    g1 = g0[:,::-1,:]
    g2 = g0[:,:,::-1]
    g3 = g2[:,::-1,:]
    r0 = grid.swapaxes(1, 2)
    r1 = r0[:,::-1,:]
    r2 = r0[:,:,::-1]
    r3 = r2[:,::-1,:]
    xtrain = np.array([g0, g1, g2, g3, r0, r1, r2, r3], dtype=np.float32)
    ytrain = np.array([v] * 8, dtype=np.float32)
    net.train(xtrain, ytrain)

for game_counter in range(game_iterations):
    state = game.initial_state()
    moved = True
    print('Game', game_counter)
    game_len = 0
    game_score = 0
    last_grid = None
    keep_playing = False
    while True:
        state = game.do_a_random_spawn(state)
        board_list = []
        for m in range(4):
            result, moved, reward = game.action(state, m, copy=True)
            if moved:
                board_list.append( (state, m, reward) )
        if board_list:
            boards = np.array([transform_state_to_input(g) for g, m, s in board_list], dtype=np.float32)
            p = net.predict(boards)
            game_len += 1
            best_mpve = -1
            best_v = None
            for i, (g, m, s) in enumerate(board_list):
                v = s + p[i]
                if best_v is None or v > best_v:
                    best_v = v
                    best_move = m
                    best_score = s
                    best_grid = boards[i]
                game.action(state, best_move)
                game_score += best_score
        else:
            best_v = [0]
            best_grid = None
        if last_grid is not None:
            Vchange(last_grid, best_v)
        last_grid = best_grid
        if not board_list:
            break
    print('    Length',game_len,', max tile',state.max(),', score', game_score)
