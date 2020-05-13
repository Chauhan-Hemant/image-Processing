import numpy as np
import cv2


def function1():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/someshapes.jpg')

    # binaries the image
    edges_detected = cv2.Canny(image, 255, 255)
    contours, hierarchy = cv2.findContours(edges_detected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # print(contours)
    for c in contours:
        print(c)
    cv2.imshow('original', image)
    cv2.imshow('edges_detected', edges_detected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()

def function2():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/someshapes.jpg')

    edges_detected = cv2.Canny(image, 255, 255)
    contours, h = cv2.findContours(edges_detected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"found contours: {len(contours)}")
    # highlight all the contours
    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)
    # for c in contours:
    #     print(c)

    cv2.imshow('original', image)
    cv2.imshow('edges_detected', edges_detected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function2()

def function3():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/someshapes.jpg')
    edges_detected = cv2.Canny(image, 255, 255)
    contours, h = cv2.findContours(edges_detected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"found contours: {len(contours)}")

    # highlights all the contours
    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)

    cv2.imshow('original', image)
    cv2.imshow("edges_detected", edges_detected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function3()


def function4():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/someshapes.jpg')
    edges_detected = cv2.Canny(image, 255, 255)
    contours, h = cv2.findContours(edges_detected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    index = 1
    for contour in contours:
        # find the bounding rectangles
        (x, y, w, h) = cv2.boundingRect(contour)
        # print(f"x: {x}, y:{y}, w:{w}, h:{h}")

        # draw the bounding rectangles
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # crop the contour
        image_contour = image[y: y + h, x: x + w]
        cv2.imshow(f"contour_{index}", image_contour)

        # save the contour
        cv2.imwrite(f"/tmp/contour_{index}.jpg", image_contour)
        index += 1

        cv2.waitKey(0)
        cv2.destroyAllWindows()
# function4()

def function5():
    image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set2/numbers.jpg')

    # detect the edges
    image_edged = cv2.Canny(image, 255, 255)

    # find all the contours
    contours, h = cv2.findContours(image_edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
    # print(f"contours: {len(contours)}")

    for c in contours:
        # find the bounding rectangle
        (x, y, w, h) = cv2.boundingRect(c)

        # highlighting the rectangle
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255),  2)
        # highlight the corner
        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)


        cv2.imshow("original", image)
        cv2.imshow("edged", image_edged)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
function5()