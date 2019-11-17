#!/usr/bin/env python

import numpy as np
import cv2

video_capture = cv2.VideoCapture('videos/squats.mp4')
#### To read a video from a camera connected to USB port or web cam
# video_capture = cv2.VideoCapture(0) 

while(True):
    ret, frame = video_capture.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## To cobvert video to Gray scale
    # frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) ## To resize it up to half frames
    # cv2.line(frame, (0,0),(511,511),(255,0,0),5) ##To draw a line in video
    cv2.imshow("Frame",frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()