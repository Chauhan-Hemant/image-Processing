import numpy as np
import cv2

def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/opencv_inv.png')

    # kernel to decide the number of pixels added on the boundaries
    kernel = np.ones((5, 5), dtype='uint8')

    # dilate the image
    image_dilated = cv2.dilate(image, kernel)
    image_erosed = cv2.erode(image, kernel)

    cv2.imshow('original', image)
    cv2.imshow('dilated', image_dilated)
    cv2.imshow('erosed', image_erosed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
# function1()

def function2():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/opencv.png')

    # kernel to decide the number of pixels added on the boundaries
    kernel = np.ones((5, 5), dtype='uint8')

    # dilate the image
    image_dilate = cv2.dilate(image, kernel)
    image_erosed = cv2.erode(image, kernel)

    cv2.imshow('original', image)
    cv2.imshow('dilated', image_dilate)
    cv2.imshow('erosed', image_erosed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
# function2()

def function3():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/Origin_of_Species.jpg')

    # gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # dilate the image
    kernel = np.ones((2, 2), dtype='uint8')
    dilated = cv2.dilate(thresh, kernel)
    
    cv2.imshow('original', image)
    cv2.imshow('thresh', thresh)
    cv2.imshow('dilated', dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
function3()