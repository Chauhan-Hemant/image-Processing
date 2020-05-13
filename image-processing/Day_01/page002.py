import numpy as np
import cv2

# 3 dimensional array

image1 = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')
image2 = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg', cv2.IMREAD_GRAYSCALE)

# to show the image
cv2.imshow('messi-color', image1)
cv2.imshow('messi-gray', image2)

# wait for 5 seconds
# cv2.waitKey(5000)

# wait till user press a key
key = cv2.waitKey(0)

# destroy the window
cv2.destroyAllWindows()

# check if the key pressed  is 'q'
# if key == ord('q'):
