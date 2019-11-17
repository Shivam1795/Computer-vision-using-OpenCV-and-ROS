#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys


def main(args):

    bridge = CvBridge()

    video_capture = cv2.VideoCapture("videos/Tennis_balls.mp4")

    rospy.init_node('image_converter', anonymous=True)

    image_pub = rospy.Publisher("/video_stream",Image)

    while(True):

        ref, rgb_frame = video_capture.read()

        # try:
        image_pub.publish(bridge.cv2_to_imgmsg(rgb_frame, "bgr8"))
        # except CvBridgeError as e:
            # print(e)

        cv2.waitKey(3)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)




