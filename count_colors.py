from PIL import Image

# Open the image file
im = Image.open("test.png")

# Convert the image to RGB colors
rgb_im = im.convert("RGB")

# Initialize a dictionary to store the colors and their counts
colors = {}

# Get the width and height of the image
width, height = im.size

# Loop over the pixels in the image
for x in range(width):
  for y in range(height):
    # Get the RGB values for the current pixel
    r, g, b = rgb_im.getpixel((x, y))
    # Store the color in the dictionary, or increment its count if it's already there
    if (r, g, b) in colors:
      colors[(r, g, b)] += 1
    else:
      colors[(r, g, b)] = 1

# Calculate the total number of pixels in the image
total_pixels = width * height

# Loop over the colors in the dictionary
for color in colors:
  # Calculate the proportion of pixels that are this color
  proportion = colors[color] / total_pixels
  # Print the proportion of this color
  print(f"Color: {color}, Proportion: {proportion}")
