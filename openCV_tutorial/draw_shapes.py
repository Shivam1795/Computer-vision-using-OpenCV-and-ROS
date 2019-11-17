#!/usr/bin/env python

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

#Draw circle
cv2.circle(img, (img.shape[0]/2, img.shape[1]/2), 100, (255,255,255),5)

#Draw line
cv2.line(img, (0,0), (511,511), (255,0,0),5)

#Draw Rectangle
cv2.rectangle(img, (200,200), (312,312), (0,0,255), 2)

#Draw Ellipse
cv2.ellipse(img, (300,300),(100,50),0, 0, 360, (0,0,255), 1)

#Draw Polygon
pts = np.array([[100,50],[200,300],[500,200],[100,500]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts], True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tutorial', (10,500), font, 2, (255,255,255),2,cv2.LINE_AA)

cv2.imshow("Draw_Shapes", img)

cv2.waitKey(0)
cv2.destroyAllWindows()