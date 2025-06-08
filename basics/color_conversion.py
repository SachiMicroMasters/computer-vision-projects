# Import OpenCV and OS modules
import cv2
import os

# Set the input image path and output folder
input_path = "inputs/logo.png"
output_dir = "outputs"

# Create the output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the original image from the input path
image = cv2.imread(input_path)

# Validate if the image was loaded correctly
if image is None:
    print("Error! Image doesn't exist")
    exit()

# Convert the original BGR image to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the original BGR image to HSV color space
HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display all three images in separate windows
cv2.imshow("Original BGR Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("HSV Image", HSV_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the converted images to the output folder
cv2.imwrite(os.path.join(output_dir, "gray_image.png"), gray_image)
cv2.imwrite(os.path.join(output_dir, "HSV_image.png"), HSV_image)




