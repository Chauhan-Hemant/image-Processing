import numpy as np
import cv2

def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/scan.jpg')

    points_A = np.float32([[320, 15], [700, 215], [85, 610], [530, 780]])
    points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

    M = cv2.getPerspectiveTransform(points_A, points_B)
    warped = cv2.warpPerspective(image, M, (420, 594))

    cv2.imshow('original', image)
    cv2.imshow('warped', warped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
# function1()

def function2():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/sudoku.png')

    points_A = np.float32([[74, 85], [489, 70], [35, 513], [519, 518]])
    points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

    M = cv2.getPerspectiveTransform(points_A, points_B)

    warped = cv2.warpPerspective(image, M, (420, 594))

    cv2.imshow('original', image)
    cv2.imshow('warped', warped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
# function2()

def function3():

    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/wrong_perspective.png')

    points_A = np.float32([[35, 254], [345, 150], [290, 740], [620, 520]])
    points_B = np.float32([[0, 0], [420, 0], [0, 594], [420, 594]])

    M = cv2.getPerspectiveTransform(points_A, points_B)

    warped = cv2.warpPerspective(image, M, (420, 594))
    cv2.imshow('original', image)
    cv2.imshow('warped', warped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
function3()