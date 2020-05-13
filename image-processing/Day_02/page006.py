import numpy as np
import cv2

def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/someshapes.jpg')

    # binarise the image
    edges_detected = cv2.Canny(image, 255, 255)
    contours, hierarchy = cv2.findContours(edges_detected, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    shape_count = {
        'circle': 0,
        'triangle': 0,
        'rectangle': 0,
        'star': 0
    }

    index = 1
    for c in contours:
        # highlighting
        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)

        # find the contours centroid
        m = cv2.moments(c)

        # center of the contour
        cx = int(m['m10'] / m['m00'])
        cy = int(m['m01'] / m['m00'])

        # draw the circle
        # cv2.circle(image, (cx, cy), 30, (0, 255, 255), 2)
        # cv2.putText(image, f"{index}", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # detect the shape
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
        print(f"index: {index}, edges: {len(approx)}")

        shape = ''
        edges = len(approx)
        if edges == 3:
            shape = 'triangle'
            shape_count['triangle'] += 1
        elif edges == 4:
            shape = 'rectangle'
            shape_count['rectangle'] += 1
        elif edges == 10:
            shape = 'star'
            shape_count['star'] += 1
        elif edges > 10:
            shape = 'circle'
            shape_count['circle'] += 1

        cv2.putText(image, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        index += 1

        cv2.putText(image, f"Star: {shape_count['star']}, Rectangle: {shape_count['rectangle']}, Circle: {shape_count['circle']}, Tringle: {shape_count['triangle']}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        cv2.imshow('original', image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

function1()