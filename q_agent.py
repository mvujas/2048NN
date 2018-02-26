from neural_network import NeuralNetwork
from game import Game
from cmd_gui import show
from timeit import default_timer as timer
import random
import time
import numpy as np
import tensorflow as tf
import datetime
import os
import matplotlib.pyplot as plt

class QAgent:
    def __init__(self):
        self.game = Game()
        self.net = NeuralNetwork()

    def train(self, games, discount_factor=0.8, saving_step=100, plot_scores=False):
        max_tiles = []
        scores = []
        start_date = datetime.datetime.now()
        saver = tf.train.Saver()
        if games >= saving_step:
            saving_folder = 'models/model-%d.%d.%d.-%d:%d:%d' % (start_date.day, start_date.month, start_date.year, start_date.hour, start_date.minute, start_date.second)
            os.system('mkdir %s' % saving_folder)
        for i in range(games):
            print('Game', i)
            self.game.reset()
            epsilon = 0.2#1/(i/50 + 10)
            moved = True
            action = None
            initial_q_values = None
            reward = None
            iteration = 1
            while not self.game.is_game_over():

                if moved:
                    self.game.random_spawn()
                initial_state = self.game.state()

                #start_time = timer()
                #show(self.game)
                if random.random() < epsilon:
                    initial_q_values = self.net.sess.run(self.net.output_layer, feed_dict={
                        self.net.input_layer: initial_state
                    })
                    action = random.randint(0, 3)
                else:
                    action, initial_q_values = self.net.sess.run([self.net.prediction, self.net.output_layer], feed_dict={
                        self.net.input_layer: initial_state
                    })
                    action = action[0]

                #iter_time = timer() - start_time
                #print('Iteration',iteration,', iteration time', iter_time)
                #iteration += 1

                moved, score_increase = self.game.step(action)
                done = self.game.is_game_over()
                if done:
                    reward = -100
                elif not moved:
                    reward = -50
                else:
                    new_state = self.game.state()
                    new_q_max = self.net.sess.run(self.net.output_layer, feed_dict={
                        self.net.input_layer: new_state
                    }).max()
                    reward = score_increase + discount_factor * new_q_max - initial_q_values[0][action]

                initial_q_values[0][action] = reward

                self.net.sess.run(self.net.train, feed_dict={
                    self.net.input_layer: initial_state,
                    self.net.next_values: initial_q_values
                })
            max_tiles.append(self.game.board.max())
            scores.append(self.game.score)
            if i and i % saving_step == 0:
                saver.save(q.net.sess, './%s/model' % saving_folder, global_step=i)
        print("256:",len(list(filter(lambda x: x == 256, max_tiles))))
        print("512:",len(list(filter(lambda x: x == 512, max_tiles))))
        print("1024:",len(list(filter(lambda x: x == 1024, max_tiles))))
        print("2048:",len(list(filter(lambda x: x == 2048, max_tiles))))
        print("4096:",len(list(filter(lambda x: x == 4096, max_tiles))))
        print(max_tiles)
        if plot_scores:
            plt.plot(scores)
            plt.show()

    def play_a_game(self, graphics=True):
        self.game.reset()
        moved = True

        invalid = 0
        while not self.game.is_game_over():
            if moved:
                self.game.random_spawn()
            else:
                invalid += 1
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
        print(invalid)

if __name__ == "__main__":
    start_time = timer()
    q = QAgent()
    q.play_a_game(False)
    time_passed = timer() - start_time
    print('Time required:', time_passed)
    first_score = q.game.score
    q.train(5)
    q.play_a_game(True)
    second_score = q.game.score
    print('Score 1:', first_score)
    print('Score 2:', second_score)
    saver = tf.train.Saver()
