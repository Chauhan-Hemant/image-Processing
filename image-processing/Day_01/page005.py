import numpy as np
import cv2

# get the video capture
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture('/home/hemant/GIT_DATA/ML/images/set1/Megamind.avi')

# capture the first frame
# ret, frame1 = capture.read()
# ret, frame2 = capture.read()
# ret, frame3 = capture.read()
#
# cv2.imshow('frame1', frame1)
# cv2.imshow('frame2', frame2)
# cv2.imshow('frame3', frame3)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('live video - original', frame)
    cv2.imshow('live video - gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

capture.release()