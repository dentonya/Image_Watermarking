import cv2
import numpy as np
import glob
import os

logo = cv2.imread("elite_logo.jpg")
img = cv2.imread("flowers\sunflower.jpg")
cv2.imshow("Img", img)
cv2.imshow("Logo", logo)
cv2.waitKey(0)
