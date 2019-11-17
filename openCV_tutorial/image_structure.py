#!/usr/bin/env python

import numpy as np
import cv2

#image read
image_name = "wall_e"
img = cv2.imread("images/"+image_name+".jpg")

print 'image as numpy array'
print img

print 'Type of the image'
print type(img)

print 'image size'
print img.size

print 'image shape'
print img.shape

print 'Length of image'
leng = img.shape[0]
print leng, 'or using <len(img)> = ', len(img)

print 'Width of the image'
wid = img.shape[1]
print wid

print 'Channels of image'
ch = img.shape[2]
print ch

print 'Length, Width and Chnnels at once'
l, w, c = img.shape
print l,' ', w,' ', c

print 'Data type of image'
print img.dtype

print 'Access [10,5] pixel of image => O/p is three values from each channels'
print img[10][5]

print 'Shape of one Row of pixels'
print img[10].shape

print 'Access 1st channel'
print img[:,:,0]

print 'Access 2nd Channel'
print img[:,:,1]

print 'Access 3rd Channel'
print img[:,:,2]





