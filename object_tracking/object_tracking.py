#!/usr/bin/env python

import numpy as np
import cv2


def extrectMask(rgb_frame, lower_limit, upper_limit):
        ## Convert frames from RGB to HSV
        hsv_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_BGR2HSV)

        ##Define a MASK
        mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)

        return mask

def getContours(bin_frame):
    _, contours, hierarchy = cv2.findContours(bin_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def process_contours(bin_frame, rgb_frame, contours):
    # black_frame = np.zeros([bin_frame.shape[0], bin_frame.shape[1], 3], np.uint8)
    for c in contours:
        cv2.drawContours(rgb_frame, [c], -1, (0,0,255), 2)
        # cv2.drawContours(black_frame, [c], -1, (0,0,255), 2)
        cv2.imshow("Tracking tennis ball", rgb_frame)
        # cv2.imshow("Black Image Contours", black_frame)


def main():

    video_capture = cv2.VideoCapture("videos/Tennis_balls.mp4")

    yellow_low = (30, 50, 100)
    yellow_up = (60, 255, 255)

    while (True):

        ref, rgb_frame = video_capture.read()

        if not ref:
            print ('Unable to read frames')
            break

        ## Get binary image/Mask
        bin_frame = extrectMask(rgb_frame, yellow_low, yellow_up)

        ## Obtain Contours
        contours = getContours(bin_frame)

        ## Processing of contours
        process_contours(bin_frame, rgb_frame, contours)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    main()