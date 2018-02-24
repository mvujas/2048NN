from neural_network import NeuralNetwork
from game import Game
from cmd_gui import show
import random
import time

class QAgent:
    def __init__(self):
        self.game = Game()
        self.net = NeuralNetwork()

    def train(self, games, learning_rate=0.8):
        for i in range(games):
            print('Game', i)
            self.game.reset()
            epsilon = 1/(i/50 + 10)
            moved = True
            action = None
            initial_q_values = None
            reward = None
            while not self.game.is_game_over():
                if moved:
                    self.game.random_spawn()
                initial_state = self.game.state()

                if random.random() < epsilon:
                    initial_q_values = self.net.sess.run(self.net.output_layer, feed_dict={
                        self.net.input_layer: initial_state
                    })
                    action = random.randint(0, 3)
                else:
                    action, initial_q_values = self.net.sess.run([self.net.prediction[0], self.net.output_layer], feed_dict={
                        self.net.input_layer: initial_state
                    })
                moved, score_increase = self.game.step(action)
                done = self.game.is_game_over()
                if done:
                    reward = -500
                elif not moved:
                    reward = -10
                else:
                    new_state = self.game.state()
                    new_q_max = self.net.sess.run(self.net.output_layer, feed_dict={
                        self.net.input_layer: new_state
                    }).max()
                    reward = score_increase + new_q_max
                reward *= learning_rate

                initial_q_values[0][action] = reward

                self.net.sess.run(self.net.train, feed_dict={
                    self.net.input_layer: initial_state,
                    self.net.next_values: initial_q_values
                })



    def play_a_game(self, graphics=True):
        self.game.reset()
        moved = True
        while not self.game.is_game_over():
            if moved:
                self.game.random_spawn()
            if graphics:
                show(self.game)
                print('Score:', self.game.score)
                print(moved)
            action = None
            if moved:
                action = self.net.sess.run(self.net.prediction, feed_dict={
                    self.net.input_layer: self.game.state()
                })[0]
            else:
                action = random.randint(0, 3)
            moved, _ = self.game.step(action)
            time.sleep(0.1)

q = QAgent()
q.play_a_game(False)
first_score = q.game.score
q.train(5)
q.play_a_game(False)
second_score = q.game.score
print('Score 1:', first_score)
print('Score 2:', second_score)
