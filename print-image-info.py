import cv2 as cv
import sys

path = sys.argv[1]
img = cv.imread(path)

print(path, img.shape[0], img.shape[1], img.shape[2])
