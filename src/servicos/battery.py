#!/usr/bin/env python

from __future__ import print_function

NAME = 'calc_battery_server'

from work_smaart.srv import BatCalc, BatCalcResponse
import rospy
from geometry_msgs.msg import Point32
from work_smaart.srv import BatCalc
class BatteryServer():
    battery = 100
    posAnterior:Point32 = None

    def __init__(self):
        rospy.init_node(NAME)
        rospy.Subscriber('/trab/posicao',Point32, self.callbackSubscriber)
        rospy.Service('BatCalc', BatCalc, self.handleCalcBatery)
        rospy.spin()

    def callbackSubscriber(self,data):
        if self.posAnterior==None:
            self.posAnterior = data
        elif self.posAnterior != data:
            self.battery -= 1
            self.posAnterior = data
        print("battery"+ str(self.battery))

    def handleCalcBatery(self,req):
        if req.dist > self.battery+2: return BatCalcResponse(True)
        else: return BatCalcResponse(False)

def main():
    servidor = BatteryServer()

if __name__ == "__main__":
    main()
