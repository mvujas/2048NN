import tensorflow as tf
import numpy as np

class NeuralNetwork:
    def __init__(self, activation_function=tf.sigmoid, hidden_layers_config=np.array([100, 500, 250, 300]), learning_rate=0.01):
        self.input_layer = tf.placeholder(tf.float32, shape=[1, 16])

        last_layer = self.input_layer
        last_layer_size = 16
        self.activation_function = activation_function

        self.weights = []
        self.biases = []
        self.hidden_layers = []

        for i in range(hidden_layers_config.size):
            print(hidden_layers_config[i])
            self.weights.append(tf.Variable(tf.random_uniform([last_layer_size, hidden_layers_config[i]], -1, 1)))
            self.biases.append(tf.Variable(tf.zeros([hidden_layers_config[i]])))
            self.hidden_layers.append(activation_function(tf.matmul(last_layer, self.weights[i]) + self.biases[i]))
            last_layer = self.hidden_layers[i]
            last_layer_size = hidden_layers_config[i]

        self.weights.append(tf.Variable(tf.random_uniform([last_layer_size, 4], -1, 1)))
        self.biases.append(tf.Variable(tf.zeros([4])))
        self.output_layer = activation_function(tf.matmul(last_layer, self.weights[hidden_layers_config.size]) + self.biases[hidden_layers_config.size])

        self.prediction = tf.argmax(self.output_layer, 1)

        self.next_values = tf.placeholder(tf.float32, shape=[1, 4])

        self.loss = tf.reduce_sum(tf.square(self.next_values - self.output_layer))

        self.train = tf.train.AdamOptimizer(learning_rate).minimize(self.loss)

'''
def neural_network_model():
    input_layer = tf.placeholder(tf.float32, shape=[1, 8])

    last_layer = input_layer
    last_layer_size = 8
    activation_function = tf.sigmoid


    hidden_layers = np.array([100, 500, 250, 300])

    weights = []
    biases = []
    layers = []

    for i in range(hidden_layers.size):
        print(hidden_layers[i])
        weights.append(tf.Variable(tf.random_uniform([last_layer_size, hidden_layers[i]], -1, 1)))
        biases.append(tf.Variable(tf.zeros([hidden_layers[i]])))
        layers.append(activation_function(tf.matmul(last_layer, weights[i]) + biases[i]))
        last_layer = layers[i]
        last_layer_size = hidden_layers[i]

    weights.append(tf.Variable(tf.random_uniform([last_layer_size, 4], -1, 1)))
    biases.append(tf.Variable(tf.zeros([4])))
    output_layer = activation_function(tf.matmul(last_layer, weights[hidden_layers.size]) + biases[hidden_layers.size])

    return input_layer, output_layer
'''

net = NeuralNetwork()

sess = tf.Session()
sess.run(tf.global_variables_initializer())

print(sess.run([net.output_layer, net.prediction], feed_dict={
    net.input_layer: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
}))
