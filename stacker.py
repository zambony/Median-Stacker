from PIL import Image;
from os import listdir;
import numpy;

def main():
	# Create an array to hold all of our images
	images = [];

	# For every file inside our working directory...
	for fileName in (listdir("images\\")):
		# Open the image and create an array from it, then append that image array into our image list
		images.append(numpy.array(Image.open("images\\" + fileName)));

	# Use the built-in median function inside numpy to find the median image, and convert all values to uint8 (0 - 255)
	stacked = numpy.uint8(numpy.median(images, 0));

	# Use Pillow to create an image from an array of data
	output = Image.fromarray(stacked);

	# Save it as a PNG for max quality
	output.save("stacked.png", "PNG");

main();