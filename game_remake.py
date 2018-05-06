import numpy as np
import random

board_shape = [4, 4]

def initial_state():
	return np.zeros(board_shape)

def is_game_over(state):
	height, width = state.shape
	height -= 1
	width -= 1
	for i in range(height):
		for j in range(width):
			if not state[i][j] or state[i][j] == state[i + 1][j] or state[i][j] == state[i][j + 1]:
				return False
	return True

# Repeating code, but everything for speed
def move_left(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	for i in range(height):
		setter_index = -1
		last_found = 0
		for mover_index in range(width):
			if result[i][mover_index]:
				if last_found == result[i][mover_index]:
					result[i][setter_index] *= 2
					last_found = 0
				else:
					setter_index += 1
					result[i][setter_index] = result[i][mover_index]
					last_found = result[i][setter_index]

		setter_index += 1

		while setter_index < width:
			result[i][setter_index] = 0
			setter_index += 1
	return result

def move_right(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	for i in range(height):
		setter_index = width
		last_found = 0
		for mover_index in reversed(range(width)):
			if result[i][mover_index]:
				if last_found == result[i][mover_index]:
					result[i][setter_index] *= 2
					last_found = 0
				else:
					setter_index -= 1
					result[i][setter_index] = result[i][mover_index]
					last_found = result[i][setter_index]

		setter_index -= 1

		while setter_index >= 0:
			result[i][setter_index] = 0
			setter_index -= 1
	return result

def move_up(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	for j in range(width):
		setter_index = -1
		last_found = 0
		for mover_index in range(height):
			if result[mover_index][j]:
				if last_found == result[mover_index][j]:
					result[setter_index][j] *= 2
					last_found = 0
				else:
					setter_index += 1
					result[setter_index][j] = result[mover_index][j]
					last_found = result[setter_index][j]

		setter_index += 1

		while setter_index < height:
			result[setter_index][j] = 0
			setter_index += 1
	return result

def move_down(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	for j in range(width):
		setter_index = height
		last_found = 0
		for mover_index in reversed(range(height)):
			if result[mover_index][j]:
				if last_found == result[mover_index][j]:
					result[setter_index][j] *= 2
					last_found = 0
				else:
					setter_index -= 1
					result[setter_index][j] = result[mover_index][j]
					last_found = result[setter_index][j]

		setter_index -= 1

		while setter_index >= 0:
			result[setter_index][j] = 0
			setter_index -= 1
	return result

def count_free_tiles(state):
	return np.count_nonzero(state == 0)

def do_a_random_spawn(state):
	value = 2 if random.random() < 0.9 else 4
	tile_num = random.randrange(0, count_free_tiles(state))
	height, width = state.shape
	k = 0
	for i in range(height):
		for j in range(width):
			if not state[i][j]:
				if tile_num == k:
					state[i][j] = value
					return state
				else:
					k += 1
	return None

'''
	0 - up
	1 - right
	2 - down
	3 - left
'''
enumerated_action_list = [move_up, move_right, move_down, move_left]
def action(state, action_num, copy=False):
	return enumerated_action_list[action_num](state, copy)

#game = initial_state()
#game1 = game
game = np.array([
		[0,		2,		0,		2],
		[2,		2,		4,		8],
		[0,		16,		0,		4],
		[32,	128,	128,	4]
	])
print(action(game, 0))
