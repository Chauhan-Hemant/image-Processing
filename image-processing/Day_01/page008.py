import numpy as np
import cv2

image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

# cropping the face
# (200, 60), (275, 150)
face = image[60:150, 200:275]

# cropping the football
# (330, 285), (400, 340)
football = image[285:340, 330:400]

no_football = image[280:335, 140:210].copy()

# pasting the football to some other location
# (160, 275), (230, 330)
image[280:335, 140:210] = football


image[285:340, 330:400] = no_football

# cv2.imshow('face', face)
# cv2.imshow('football', football)
cv2.imshow('messi', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('/tmp/mess_2_footballs.jpg', image)