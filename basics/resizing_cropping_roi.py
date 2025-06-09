"""
Lesson 3: Image Resizing, Cropping & ROI
S.No: 01
Date: 2025-06-09
Author: Sadan Asampally
e-mail: sachimicromasters@gmail.com

Description:
- Read image from inputs/
- Resize to different dimensions (half and double)
- Crop a central square region (ROI)
- Display and save all results
"""

import cv2
import os

# Define input image path and output directory
input_path = "inputs/logo.png"
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)  # Create outputs folder if it doesn't exist

# Read the image
image = cv2.imread(input_path)
if image is None:
    print("Error: Image does not exist at the specified path!")
    exit()

# Get original dimensions of the image
h, w = image.shape[:2]

# Resize image to half its size
half_image = cv2.resize(image, (w // 2, h // 2))

# Resize image to double its size
doubled_image = cv2.resize(image, (w * 2, h * 2))

# Define central square Region of Interest (ROI)
cx, cy = w // 2, h // 2  # Center coordinates
roi_size = min(w, h) // 4  # Size of the ROI region
roi = image[cy - roi_size:cy + roi_size, cx - roi_size:cx + roi_size]

# Display all images in different windows
cv2.imshow("Original Image", image)
cv2.imshow("Half Size Image", half_image)
cv2.imshow("Double Size Image", doubled_image)
cv2.imshow("Central ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output images
cv2.imwrite(os.path.join(output_dir, "resized_half.png"), half_image)
cv2.imwrite(os.path.join(output_dir, "resized_double.png"), doubled_image)
cv2.imwrite(os.path.join(output_dir, "central_roi.png"), roi)

