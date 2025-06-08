"""
Lesson 1: Read, Display & Save Image
S.No: 01
Date: 2025-06-08
Author: Sadan Asampally.
e-mail: sachimicromasters@gmail.com

Description:
- Read an image from disk
- Display the image in a window
- Save the image to output folder
"""




#import OpenCV library
import cv2

# Read the image from the 'basics' folder using relative path
image = cv2.imread("inputs/logo.png")

# Check if the image was loaded successfully
if image is None:
      print("Error: The image is not found")
else:
      # Display the original image in a window named 'Original Image'
      cv2.imshow("Original Image", image)
      # Wait indefinitely for a key press
      cv2.waitKey(0)
      # Save the displayed image to 'basics/OutputImage.png'
      cv2.imwrite("outputs/OutputImage.png", image)
      # Close all OpenCV windows
      cv2.destroyAllWindows()
