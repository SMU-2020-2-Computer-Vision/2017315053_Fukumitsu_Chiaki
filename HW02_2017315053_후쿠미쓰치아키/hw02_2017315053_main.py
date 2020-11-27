import os
import cv2
from hw02_2017315053_template_matching import template_matching

# Set the working directory to be the current one
cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

# Load a reference image
img_refrence = cv2.imread("img/test_background.png")

# Load a template image as grayscale
img_template = cv2.imread('img/fish.png', 0)

#call function
template_matching(img_template, img_refrence)

cv2.waitKey(0)
cv2.destroyAllWindows()