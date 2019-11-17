#!/usr/bin/env python

import numpy as np
import cv2

print 'Read image from file'
img = cv2.imread("images/wall_e.jpg",cv2.IMREAD_COLOR)

print 'Display image in native colour'
cv2.imshow("Original image", img)
cv2.moveWindow("Original image", 0, 0)
print(img.shape)

hight, width, channels = img.shape

print 'Split images into three channels'
blue, green, red = cv2.split(img)

cv2.imshow("Blue channel", blue)
cv2.moveWindow("Blue channel", 0, hight)

cv2.imshow("Green channel", green)
cv2.moveWindow("Green channel", 0, 2*hight)

cv2.imshow("Red channel", red)
cv2.moveWindow("Red channel", 0, 3*hight)

print '......Convert RGB image to HSV format and split into HSV Channels......'

#Convert in HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Split images into different channels
h, s, v = cv2.split(hsv_img)

#Concinate all the images to show them into one window.
hsv_image = np.concatenate((h,s,v), axis=1)

cv2.imshow("HSV images",hsv_image)


print 'Convert images to grayScale image'

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", gray_img)

print gray_img




cv2.waitKey(0)
cv2.destroyAllWindows()