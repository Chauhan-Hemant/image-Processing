import numpy as np
import cv2

def function1():
    image = cv2.imread("/home/hemant/GIT_DATA/ML/images/set1/gradient.png")

    # threshold the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, image2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    ret, image3 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow('original', image)
    cv2.imshow('threshold 1', image2)
    cv2.imshow('threshold 2', image3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function1()

def function2():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/Origin_of_Species.jpg')
    
    # gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold
    ret, image_threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('original', image)
    cv2.imshow('threshold', image_threshold)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
function2()