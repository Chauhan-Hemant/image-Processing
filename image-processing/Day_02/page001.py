import numpy as np
import cv2

def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

    # extract the kernel matrix
    # please normalize the values
    kernel = np.ones((10, 10), dtype='float32') / 100

    # extract the face
    # face = image[60:150, 200:275]

    # perform the blurred operation
    blurred = cv2.filter2D(image, -1, kernel)

    cv2.imshow('original', image)
    cv2.imshow('blurred', blurred)

    cv2.imwrite('/tmp/messi_blurred.jpg', blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function1()

def function2():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

    # blurred the image
    # blurred = cv2.blur(image, (5, 5))
    blurred = cv2.GaussianBlur(image, (9, 9), 0)

    cv2.imshow('original', image)
    cv2.imshow('blurred1', blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
# function2()

def function3():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

    # kernel for sharpening the image
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

    # get the sharpened image
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # sharpened = cv2.filter2D(gray, -1, kernel)
    sharpened = cv2.filter2D(image, -1, kernel)

    cv2.imshow('original', image)
    cv2.imshow('sharpned', sharpened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
function3()