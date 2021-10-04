# please name this file data_rep_images.py
from PIL import Image
import numpy
import sys

# we need to change the way numpy prints, even though we are only working with one row at a time
numpy.set_printoptions(threshold=numpy.inf)

# we open the file here. beware of path problems, make sure the image is in the same folder that your python program is in
# we assign the variable im the image value
im = Image.open("image1.png")
im = im.convert('L')

# we print out some information about this image:
print('image format is: ', im.format)
print('image size is: ', im.size)
print('image mode is: ', im.mode)

# here we assign the variable "image_as_array" to a numpy array that is the image
image_as_array = numpy.array(im)


# how many pixels on row 50?
print(len(image_as_array[50]))

# now we are going to print the pixels from row 50 from the image
print(image_as_array[50])

# now we are going to change ONE pixel. It should be in the upper-left corner of our circle. 
image_as_array[50][100] = 255

# Now we are going to turn our array back into an image:
altered_image = Image.fromarray(image_as_array)

# finally, we show the image
altered_image.show()
