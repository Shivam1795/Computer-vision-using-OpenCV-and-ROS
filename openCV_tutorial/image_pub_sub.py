#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = CvBridge()

def img_callback(ros_image):
    
    print 'Got image from ROS Topic'
    global bridge

    #Convert ros_image into an OpenCV compatible image
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as err:
        print (err)
    
    #From nowOn we can use all OpenCV functions
    (rows, cols, ch) = cv_image.shape
    if cols > 200 and rows > 200:
        cv2.circle(cv_image, (100,100), 90, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(cv_image, 'Webcam Video with ROS & OpenCV...!!', (5,300), font, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow("Image Window", cv_image)
    cv2.waitKey(3)

def main(args):

    rospy.init_node('image_converter', anonymous=True)

    image_sub = rospy.Subscriber("/usb_cam/image_raw",Image, img_callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)




