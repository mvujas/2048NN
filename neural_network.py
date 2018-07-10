import tensorflow as tf
import numpy as np

MAX_EXP = 18

class NeuralNetwork:
    def __init__(
            self,
            activation_function=tf.nn.relu,
            learning_rate=0.0005,
            padding='same'
        ):
        self.input = tf.placeholder(tf.float32, shape=(None, 4, 4, MAX_EXP), name='input')

        conv_1 = tf.layers.conv2d(
            inputs=self.input,
            filters=1000,
            kernel_size=[4, 1],
            padding=padding,
            activation=activation_function
        )

        conv_2 = tf.layers.conv2d(
            inputs=conv_1,
            filters=1000,
            kernel_size=[1, 4],
            padding=padding,
            activation=activation_function
        )

        conv_3 = tf.layers.conv2d(
            inputs=conv_2,
            filters=1000,
            kernel_size=[4, 1],
            padding=padding,
            activation=activation_function
        )

        conv_4 = tf.layers.conv2d(
            inputs=conv_3,
            filters=1000,
            kernel_size=[1, 4],
            padding=padding,
            activation=activation_function
        )

        conv_4_flat = tf.layers.flatten(conv_4)

        fc_1 = tf.layers.dense(conv_4_flat, units=512, activation=activation_function)
        self.output = tf.layers.dense(fc_1, units=4)

        self.max = tf.reduce_max(self.output, axis=1)

        self.prediction = tf.argmax(self.output, 1)

        self.nextQ = tf.placeholder(tf.float32, shape=(None, 4))

        self.loss = tf.reduce_sum(tf.square(self.output - self.nextQ))

        optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
        self.train_layer = optimizer.minimize(self.loss)
        self.sess = None

        self.config = tf.ConfigProto(
            device_count = {'GPU': 0}
        )
        self.sess = None

    def start_session(self):
        self.sess = tf.Session(config=self.config)
        init = tf.global_variables_initializer()
        self.sess.run(init)

    def predict(self, state):
        if not self.sess:
            raise Exception('Session is not initalized!')
        return self.sess.run([self.output, self.prediction], feed_dict={
                    self.input: state
                })

    def max_Q(self, state):
        if not self.sess:
            raise Exception('Session is not initalized!')
        return self.sess.run(self.max, feed_dict={
                    self.input: state
                })

    def train(self, state, nextQ):
        if not self.sess:
            raise Exception('Session is not initalized!')
        return self.sess.run([self.loss, self.train_layer], feed_dict={
            self.input: state,
            self.nextQ: nextQ
        })

log_array = {(2 ** i if i else 0): i for i in range(MAX_EXP)}
def prepare_input(input_state):
    height, width = input_state.shape
    result = np.zeros((height, width, MAX_EXP))
    for i in range(height):
        for j in range(width):
            result[i][j][log_array[input_state[i][j]]] = 1
    return result
