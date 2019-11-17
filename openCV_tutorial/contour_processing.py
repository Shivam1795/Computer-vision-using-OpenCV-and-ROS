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
        th_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 4)
    else:
        _, th_img = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY_INV)

    if show:
        cv2.imshow("Binary Image", th_img)
    
    return th_img

def getContours(bin_img):
    _, contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours


def process_contours(bin_img, rgb_img, contours):
    black_img = np.zeros([bin_img.shape[0], bin_img.shape[1], 3], np.uint8)

    for c in contours:
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        cv2.drawContours(rgb_img, [c], -1, (150, 250, 150), 1)
        cv2.drawContours(black_img, [c], -1, (150, 250, 150), 1)

        cx, cy = get_contour_center(c)
        cv2.circle(rgb_img, (cx, cy), (int)(radius), (0,0,255), 1)
        cv2.circle(black_img, (cx, cy), (int)(radius), (0,0,255), 1)

        print ("Area: {}, Perimeter: {}".format(area, perimeter))
    print("No. of contours: {}".format(len(contours)))
    cv2.imshow("RGB Image Contours", rgb_img)
    cv2.imshow("Black Image Contours", black_img)

def get_contour_center(contour):
    M = cv2.moments(contour)
    cx = -1
    cy = -1
    if (M['m00'] != 0):
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    return cx, cy


def main():
    image_name = "images/geom.jpg"
    rgb_img = read_rgb_image(image_name, True)
    gray_img = rgb_to_gray(rgb_img, True)
    binary_img = gray_to_binary(gray_img, True, True)
    contours = getContours(binary_img)
    process_contours(binary_img, rgb_img, contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
