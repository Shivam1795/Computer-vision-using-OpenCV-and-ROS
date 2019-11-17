#!/usr/bin/env python

import numpy as np
import cv2

image_name = "wall_e"

print 'Reading an image from file'
img = cv2.imread("images/"+image_name+".jpg")

print 'Create a window holder for image'
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)#cv2.WINDOW_AUTOSIZE

print 'Display the image'
cv2.imshow("Image",img)

print 'Press a key inside image to make a copy of image'
cv2.waitKey(0)

print 'Image copyed to images/copy/'
cv2.imwrite("images/copy/"+image_name+"_copy.jpg",img)
