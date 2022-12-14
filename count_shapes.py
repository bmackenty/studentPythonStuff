import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply the Canny edge detection algorithm to find the edges
edges = cv2.Canny(blurred, 50, 150)

# Use the Hough transform to detect circles in the image
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Print the number of circles detected
print('Number of circles:', len(circles))

# Use the Hough transform to detect lines in the image
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Print the number of lines detected
print('Number of lines:', len(lines))

# Use the Hough transform to detect rectangles in the image
rectangles = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
