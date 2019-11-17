#!/usr/bin/env python

import numpy as np
import cv2

def read_image(image_name, as_gray):
    if as_gray:
        image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(image_name, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Read Image", image)

    return image

def basic_thresholding(gray_image, th_value):
    ret, th_basic = cv2.threshold(gray_image, th_value, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Binary image by simple thresholding", th_basic)

def adaptive_thresholding(gray_image, th_value):
    adap_th_img = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, th_value, 2) ##cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    cv2.imshow("Adaptive Thresholding Image", adap_th_img)

def main():

    image_name = "images/wall_e.jpg"
    as_gray = True
    th_value = 115
    gray_image = read_image(image_name, as_gray)

    basic_thresholding(gray_image, th_value)
    adaptive_thresholding(gray_image, th_value)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()