#!/usr/bin/env python

import numpy as np
import cv2

img = cv2.imread("images/ball5.jpg")
cv2.imshow("Original", img)

##Convert to HSV from BGR
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", hsv_img)

##Upper & Lower bounds of RED Colour
red_low = (0, 100, 50)
red_up = (30, 255,255)

## Define a MASK
mask = cv2.inRange(hsv_img, red_low, red_up)

cv2.imshow("Mask", mask)


cv2.waitKey(0)
cv2.distroyAllWindows()