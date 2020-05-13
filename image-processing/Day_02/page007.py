import numpy as np
import cv2

def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/Hillary.jpg')

    # create the classifier
    classifier = cv2.CascadeClassifier('/home/hemant/GIT_DATA/ML/haarcascades/haarcascade_frontalface_default.xml')

    # find the face
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# function1()

def function2():
    capture = cv2.VideoCapture(0)
    classifier_face = cv2.CascadeClassifier('/home/hemant/GIT_DATA/ML/haarcascades/haarcascade_frontalface_default.xml')
    classifier_eye = cv2.CascadeClassifier('/home/hemant/GIT_DATA/ML/haarcascades/haarcascade_eye.xml')

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # find the highlight the faces
        faces = classifier_face.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # find the highlight the eyes
        eyes = classifier_eye.detectMultiScale(gray)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y+ h), (0, 0, 255), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
function2()