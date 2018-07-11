import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage import io
from skimage.exposure import equalize_hist
import datetime
import random
import os.path

def convolution_gray(image, kernel):
	if image.ndim != 2:
		raise Exception('Invalid image rank!')
	if kernel.ndim != 2:
		raise Exception('Invalid kernel rank!')
	kernel_height, kernel_width = kernel.shape
	if kernel_height % 2 == 0 or kernel_width % 2 == 0:
		raise Exception('Invalid kernel dimensions!')
	image_height, image_width = image.shape
	if kernel_height > image_height or kernel_width > image_width:
		raise Exception('Kernel is too big to be applied at the given image!')
	print(kernel)
	kernel = np.flip(np.flip(kernel, 1), 0)
	print(kernel)

	result = np.zeros((image_height - kernel_height + 1, image_width - kernel_width + 1))
	for i in range(image_height - kernel_height):
		for j in range(image_width - kernel_width):
			for k in range(kernel_height):
				for l in range(kernel_width):
					result[i][j] += image[i + k][j + l] * kernel[k][l]
	return result

def normalize_image(image):
	if image.ndim != 2:
		raise Exception('Invalid image rank!')
	min_value, max_value = image.min(), image.max()
	difference = max_value - min_value
	if difference == 0:
		return np.zeros(image.shape)
	return (image - min_value) / difference

def add_noise_to_image(image, probability):
	result = np.zeros(image.shape)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			result[i][j] = random.random() if random.random() < probability else image[i][j]
	return result

kernels = {
	'id': np.ones((1, 1)),
	'simple_blur_3': np.ones((3, 3)),
	'simple_blur_5': np.ones((5, 5)),
	'simple_blur_7': np.ones((7, 7)),
	'simple_blur_9': np.ones((9, 9)),
	'simple_blur_11': np.ones((11, 11)),
	'simple_blur_13': np.ones((13, 13)),
	'simple_blur_21': np.ones((21, 21)),
	'gaussian_filter_3': np.array([
			[1, 2, 1],
			[2, 4, 2],
			[1, 2, 1]
		]),
	'gaussian_filter_5': np.array([
			[2, 7, 12, 7, 2],
			[7, 31, 52, 31, 7],
			[12, 52, 127, 52, 12],
			[7, 31, 52, 31, 7],
			[2, 7, 12, 7, 2]
		]),
	'h_edge_detection_3': np.array([
			[-1, -2, -1],
			[0, 0, 0],
			[1, 2, 1]
		]),
	'v_edge_detection_3': np.array([
			[-1, 0, 1],
			[-2, 0, 2],
			[-1, 0, 1]
		]),
	'custom_1': np.array([
			[4, 2, 1],
			[2, 1, 0],
			[1, 0, 0]
		]),
	'sharpen': np.array([
			[0, -1, 0],
			[-1, 5, -1],
			[0, -1, 0]
		])
}

if __name__ == "__main__":
	noise = 0
	filter_name = 'v_edge_detection_3'
	image_name = 'img.jpg'

	# READING AND ADDING NOISE + CHANGING TO GRAYSCALE
	img = color.rgb2gray(io.imread(image_name))
	if noise:
		img = add_noise_to_image(img, noise)

	# FILTERING
	new_img = normalize_image(convolution_gray(img, kernels[filter_name]))
	
	# SHOWING
	io.imshow(new_img)
	plt.show()

	# SAVING
	now = datetime.datetime.now()
	io.imsave('%s_result_%d-%d-%d_%d-%d-%d%s%s.jpg' % (
		os.path.splitext(image_name)[0],
		now.year,
		now.month,
		now.day,
		now.hour,
		now.minute,
		now.second,
		'_filter-' + filter_name if filter_name else '',
		'_noise-' + str(noise) if noise else ''), new_img)