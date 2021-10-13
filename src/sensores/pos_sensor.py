#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Point32

pub = rospy.Publisher('/trab/posicao', Point32, queue_size=5)
rospy.init_node('sensor_pos')
atual = Point32()
atual.x=0
atual.y=0
atual.z=0

##!#######################################
## TODO: TRANSFORM THIS FILE INTO C++  ##
##!#######################################

r = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():

   axis = random.randint(1,6)

   if axis==1:
      atual.x +=1
   elif axis==2 :
      atual.y +=1

   pub.publish(atual)
   r.sleep()