import cv2
import numpy as np
import glob
import os

from numpy._distributor_init import filename

logo = cv2.imread("elite_logo.jpg")
h_logo, w_logo, _ = logo.shape
images_path = glob.glob("flowers/*.*")
print("Adding watermark")
for img_path in images_path:
    img = cv2.imread(img_path)
    h_img, w_img, _ = img.shape
    center_y = int(h_img / 2)
    center_x = int(w_img / 2)
    top_y = center_y - int(h_logo / 2)
    left_x = center_x - int(w_logo / 2)
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo
    # cv2.circle(img, (left_x, top_y), 10, (0, 255, 0), -1)
    # cv2.circle(img, (right_x, bottom_y), 10, (0, 255, 0), -1)
    # Extract ROI
    roi = img[top_y:bottom_y, left_x:right_x]

    result = cv2.addWeighted(roi, 1, logo, 0.3, 0)
    img[top_y:bottom_y, left_x:right_x] = result
    filename= os.path.basename(img_path)

    cv2.imwrite("watermarked_images/watermarked_" + filename, img)

print("Watermark added to all Images")
