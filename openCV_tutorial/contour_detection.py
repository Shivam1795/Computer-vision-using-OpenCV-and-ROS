#!/usr/bin/env python

import numpy as np
import cv2


def read_rgb_image(img_name, show):
    rgb_img = cv2.imread(img_name)
    if show:
        cv2.imshow("RGB Image",rgb_img)
    return rgb_img

def rgb_to_gray(rgb_img, show):
    gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
    if show:
        cv2.imshow("Gray Image",gray_img)
    return gray_img

def gray_to_binary(gray_img, adaptive, show):
    if adaptive:
        th_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 10)
    else:
        _, th_img = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY_INV)

    if show:
        cv2.imshow("Binary Image", th_img)
    
    return th_img

def getContours(bin_img):
    _, contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


def draw_contours(img, contours, img_name):
    index = -1 ## Means draw all contours
    thickness = 2 ## Thickness of line
    color = (255, 0, 255) ## Colour of contour line
    cv2.drawContours(img, contours, index, color, thickness)
    cv2.imshow(img_name, img)


def main():
    image_name = "images/geom.jpg"
    rgb_img = read_rgb_image(image_name, True)
    gray_img = rgb_to_gray(rgb_img, True)
    binary_img = gray_to_binary(gray_img, False, True)
    contours = getContours(binary_img)
    draw_contours(rgb_img, contours, "RGB Contours")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
