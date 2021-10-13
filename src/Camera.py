#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage

VERBOSE=rospy.get_param('~verbose',False)

class Camera():

    def __init__(self):
        self.img = None
        self.cvb = CvBridge()
        self.publisher = rospy.Publisher('camera/image/compressed', CompressedImage, queue_size=10)
        if VERBOSE:
            rospy.logdebug('Published initialized at topic: /camera/image/compressed')
            print("Published initialized at topic: /camera/image/compressed")

        #### READ IMAGE FROM PATH ####
        self.img = cv2.imread("/home/daniel/Imagens/test2.jpeg")
        rate = rospy.Rate(10) # 10hz
        #### CREATE COMPRESSEDIMAGE HERE ####
        while not rospy.is_shutdown():
            
            if self.img is not None:
                self.publisher.publish(self.cvb.cv2_to_compressed_imgmsg(self.img))
            rate.sleep()




def main(args=None):
    rospy.init_node('camera')
    camera = Camera()

    ##rospy.spin()


if __name__ == '__main__':
    main()
