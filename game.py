import numpy as np
import random

board_size = (4, 4)
initial_value = 2

class Game:
    def __init__(self):
        self.board = None
        self.height = None
        self.width = None
        self.score = 0
        self.steps = [
            self.move_up,
            self.move_right,
            self.move_down,
            self.move_left
        ]
        self.reset()

    # Counts how many empty tiles are there
    def count_empty_fields(self):
        return np.count_nonzero(self.board == 0)

    # Picks one of empty tiles
    def random_spawn(self):
        empty_tiles = self.count_empty_fields()
        if empty_tiles == 0:
            return False
        return self.spawn_random_tile(random.randint(1, empty_tiles))

    # Sets choosen tile to have value of initial_value
    def spawn_random_tile(self, n_th):
        k = 0
        vertical, horizontal = range(self.height), range(self.width)
        for i in vertical:
            for j in horizontal:
                if self.board[i][j] == 0:
                    k += 1
                    if k == n_th:
                        self.board[i][j] = initial_value
                        return True
        return False

    # reset score adn board to initial state
    def reset(self):
        self.board = np.zeros(board_size, dtype=int)
        self.score = 0
        self.height, self.width = self.board.shape

    # tempalte for making moves easier
    def move_template(self, static_dim, dynamic_dim, starting, increment):
        moved = False
        score_increase = 0
        for i in static_dim:
            free = starting
            last_val = self.board[i][free]
            for j in dynamic_dim:
                if self.board[i][j] != 0:
                    if self.board[i][j] == last_val or last_val == 0:
                        moved = True
                        self.board[i][free] += self.board[i][j]
                        self.board[i][j] = 0
                        if last_val != 0:
                            score_increase += self.board[i][free]
                            free += increment
                    else:
                        free += increment
                        if j != free:
                            moved = True
                            self.board[i][free] = self.board[i][j]
                            self.board[i][j] = 0
                    last_val = self.board[i][free]
        self.score += score_increase
        return moved, score_increase

    def move_left(self):
        return self.move_template(range(self.height), range(1, self.width), 0, 1)

    def move_right(self):
        return self.move_template(range(self.height), range(self.width - 2, -1, -1), self.width - 1, -1)

    def move_up(self):
        self.board = self.board.T
        tmp = self.move_left()
        self.board = self.board.T
        return tmp

    def move_down(self):
        self.board = self.board.T
        tmp = self.move_right()
        self.board = self.board.T
        return tmp

    def step(self, action):
        return self.steps[action]()

    def state(self):
        return [self.board.copy().ravel()]

    def is_game_over(self):
        vertical, horizontal = range(self.height), range(self.width)
        for i in vertical:
            for j in horizontal:
                tile = self.board[i][j]
                if tile == 0:
                    return False
                if i != 0 and tile == self.board[i - 1][j]:
                    return False
                if j != 0 and tile == self.board[i][j - 1]:
                    return False
        return True
