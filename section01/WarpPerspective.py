import cv2
import numpy as np

# Load the original image
image = cv2.imread("../images/cards.jpg")

# Define the output image size
width, height = 500, 500

# Define the four corner points of the region you want to transform in the original image
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 448]])

# Define the destination points for the transformed image
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Compute the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation to warp the image
imgOutput = cv2.warpPerspective(image, matrix, (width, height))

# Display the original and transformed images
cv2.imshow("Original Image", image)
cv2.imshow("Output Image", imgOutput)

# Wait for a key press to close the images
cv2.waitKey(0)
cv2.destroyAllWindows()
