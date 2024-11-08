from PIL import Image
import random

# Set image dimensions
width, height = 4, 4

# Create a new image with RGB mode
image = Image.new('RGB', (width, height))

my_array = []
# Generate random colors for each pixel
for x in range(width):
    for y in range(height):
        # Randomly assign a color to each pixel
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        my_array.append(color)
        image.putpixel((x, y), color)

# Display the image
image.show()
print(my_array)
