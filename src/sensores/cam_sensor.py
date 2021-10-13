#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/trab/bateria', String, queue_size=10)
rospy.init_node('sensor_cam')
r = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
   pub.publish("I'm Bat-ery")
   r.sleep()