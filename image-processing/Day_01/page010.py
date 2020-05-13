import numpy as np
import cv2

def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/smarties.png')
    edge = cv2.Canny(image, 255, 255)
    cv2.imshow('original', image)
    cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# function1()

def function2():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        edge = cv2.Canny(frame, 255, 255)
        cv2.imshow('video', edge)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
function2()