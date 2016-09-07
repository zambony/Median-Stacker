from PIL import Image
from os import listdir
import numpy

def stackImages(directory):
	"""Employ median stacking to combine images and remove noise

	Args:
		directory (str): The path to the folder containing your input images

	Returns:
		list: A list of tuples containing the image data
	"""
	images = []

	# For every file inside our working directory...
	for fileName in (listdir(directory + "\\")):
		# Open the image and create an array from it, then append that image array into our image list
		img = Image.open(directory + "\\" + fileName)
		images.append(numpy.array(img))

	# Use the built-in median function inside numpy to find the median image, and convert all values to uint8 (0 - 255)
	stacked = numpy.uint8(numpy.median(images, axis = 0))

	# Return the list of tuples so the user can do whatever he/she wants with it
	return stacked
