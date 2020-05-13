import numpy as np
import cv2

def function1():
    image1 = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')
    image2 = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/opencv-logo-white.png')

    # resize both the images
    image1_resized = cv2.resize(image1, (512, 512))
    image2_resized = cv2.resize(image2, (512, 512))

    # image blending
    # new_image = cv2.add(image1_resized, image2_resized)
    new_image = cv2.addWeighted(image1_resized, 0.8, image2_resized, 0.2, 0.5)
    cv2.imshow('new image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function1()

def fucntion2():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')
    m = np.ones(image.shape, dtype='uint8') * 100

    new_image_add = cv2.add(image, m)
    new_image_subtract = cv2.subtract(image, m)

    cv2.imshow('new image - add', new_image_add)
    cv2.imshow('new image - subtract', new_image_subtract)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

fucntion2()
