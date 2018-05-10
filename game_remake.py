import numpy as np
import random

board_shape = [4, 4]

def initial_state():
	return np.zeros(board_shape)

def is_game_over(state):
	height, width = state.shape
	for i in range(height):
		for j in range(width):
			if not state[i][j]:
				return False
			if i != width - 1 and state[i][j] == state[i + 1][j]:
				return False
			if j != height - 1 and state[i][j] == state[i][j + 1]:
				return False
	return True

# Repeating code, but everything for speed
def move_left(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	moved = False
	for i in range(height):
		setter_index = -1
		last_found = 0
		for mover_index in range(width):
			if result[i][mover_index]:
				if last_found == result[i][mover_index]:
					result[i][setter_index] *= 2
					last_found = 0
					moved = True
				else:
					setter_index += 1
					result[i][setter_index] = result[i][mover_index]
					last_found = result[i][setter_index]
					moved = moved or setter_index != mover_index

		setter_index += 1

		while setter_index < width:
			result[i][setter_index] = 0
			setter_index += 1
	return result, moved

def move_right(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	moved = False
	for i in range(height):
		setter_index = width
		last_found = 0
		for mover_index in reversed(range(width)):
			if result[i][mover_index]:
				if last_found == result[i][mover_index]:
					result[i][setter_index] *= 2
					last_found = 0
					moved = True
				else:
					setter_index -= 1
					result[i][setter_index] = result[i][mover_index]
					last_found = result[i][setter_index]
					moved = moved or setter_index != mover_index

		setter_index -= 1

		while setter_index >= 0:
			result[i][setter_index] = 0
			setter_index -= 1
	return result, moved

def move_up(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	moved = False
	for j in range(width):
		setter_index = -1
		last_found = 0
		for mover_index in range(height):
			if result[mover_index][j]:
				if last_found == result[mover_index][j]:
					result[setter_index][j] *= 2
					last_found = 0
					moved = True
				else:
					setter_index += 1
					result[setter_index][j] = result[mover_index][j]
					last_found = result[setter_index][j]
					moved = moved or setter_index != mover_index

		setter_index += 1

		while setter_index < height:
			result[setter_index][j] = 0
			setter_index += 1
	return result, moved

def move_down(state, copy=False):
	result = state.copy() if copy else state
	height, width = state.shape
	moved = False
	for j in range(width):
		setter_index = height
		last_found = 0
		for mover_index in reversed(range(height)):
			if result[mover_index][j]:
				if last_found == result[mover_index][j]:
					result[setter_index][j] *= 2
					last_found = 0
					moved = True
				else:
					setter_index -= 1
					result[setter_index][j] = result[mover_index][j]
					last_found = result[setter_index][j]
					moved = moved or setter_index != mover_index

		setter_index -= 1

		while setter_index >= 0:
			result[setter_index][j] = 0
			setter_index -= 1
	return result, moved

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


import time

state = initial_state()
moved = True
while not is_game_over(state):
	if moved:
		state = do_a_random_spawn(state)
	print(state)
	print(15*'\n')
	time.sleep(0.3)
	step = random.randrange(0, 4)
	state, moved = action(state, step)
print(state)
print(is_game_over(state))
