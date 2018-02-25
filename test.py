from neural_network import NeuralNetwork
from timeit import default_timer as timer

net = NeuralNetwork()
start = timer()
for i in range(50):
	print('Game',i)
	for _ in range(200):
		time_123 = timer()
		net.sess.run([net.prediction, net.output_layer], feed_dict={
			net.input_layer: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
		})

		net.sess.run(net.train, feed_dict={
			net.input_layer: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
			net.next_values: [[1, 1, 1, 1]]
		})
		print('Iteration time', timer() - time_123)
print(timer() - start)
