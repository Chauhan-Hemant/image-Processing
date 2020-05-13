import numpy as np
import cv2

image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

# convert the colorful image to gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('messi', image)
cv2.imshow('grey', gray)

# save the file
cv2.imwrite('/tmp/messi.jpg', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()