import numpy as np
import cv2

image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

# split the image into 3 channels
(b, g, r) = cv2.split(image)

# print(b)
# print(g)
# print(r)

# merge the channels to create new image
image1 = cv2.merge([b, g, r])
image_r = cv2.merge([b, g, r + 100])
image_g = cv2.merge([b, g + 100, r])
image_b = cv2.merge([b + 100, g, r])

cv2.imshow('original image', image1)
cv2.imshow('red image', image_r)
cv2.imshow('blue image', image_b)
cv2.imshow('green image', image_g)

cv2.waitKey(0)
cv2.destroyAllWindows()