import numpy as np
import cv2

def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

    image_copy = image.copy()

    cv2.rectangle(image_copy, (200, 60), (275, 150), (0, 0, 255), 2)
    cv2.rectangle(image_copy, (330, 285), (400, 340), (0, 255, 255), 2)

    cv2.imshow('messi', image_copy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function1()

def function2():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')
    image_copy = image.copy()

    cv2.circle(image_copy, (235, 100), 50, (0, 255, 255), 2)
    cv2.circle(image_copy, (365, 315), 27, (0, 0, 255), 2)

    cv2.putText(image_copy, "Messi and his football", (30, 30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow('messi', image_copy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('/tmp/messi01.jpg', image_copy)

# function2()

def function3():
    image = np.zeros((512, 512, 3), dtype='uint8')

    center = (256, 256)
    cv2.circle(image, center, 100, (0, 255, 255), 3)
    cv2.putText(image, "Smiley Face", (20, 30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow('new image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('/tmp/smiley_face.jpg', image)

function3()