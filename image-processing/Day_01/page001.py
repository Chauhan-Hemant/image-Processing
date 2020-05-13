import numpy as np
import cv2

# read the file into 3 dimensional array
image = cv2.imread('/home/hemant/GIT_DATA/ML/images/set1/messi5.jpg')

# print(image)
# print(type(image))
# print(image.shape)

# print(f"Height: {image.shape[0]}, Width: {image.shape[1]}, channels: {image.shape[2]}")

# (h, w, d) = image.shape
# print(f"Height: {h}, Width: {w}, Channels: {d}")

print(image[0, 0])
# print(image[316, 371])