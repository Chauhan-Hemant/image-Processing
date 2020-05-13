import numpy as np
import cv2


def translation():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')
    (h, w, d) = image.shape

    image_copy = image.copy()

    # create the translation matrix
    t = np.float32([[1, 0, 20], [0, 1, 20]])

    new_image = cv2.warpAffine(image_copy, t, (w, h))
    cv2.imshow('messi', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# translation()

def rotation():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')
    (h, w, d) = image.shape

    center = (w // 2, h // 2)

    # rotation matrix
    t = cv2.getRotationMatrix2D(center, -45, 1)
    new_image = cv2.warpAffine(image, t, (w, h))
    cv2.imshow('messi', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# rotation()

def resize():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')
    (h, w, d) = image.shape
    new_image = cv2.resize(image, (w * 2, h * 2))
    cv2.imshow('messi', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('/tmp/messi_resized.jpg', new_image)

# resize()

def pyramid():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

    larger = cv2.pyrUp(image)

    smaller = cv2.pyrDown(image)

    smallest = cv2.pyrDown(smaller)

    cv2.imshow('original', image)
    cv2.imshow('larger', larger)
    cv2.imshow('smaller', smaller)
    cv2.imshow('smallest', smallest)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

pyramid()
