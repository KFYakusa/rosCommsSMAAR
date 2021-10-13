#!/usr/bin/env python

## controlar árvore de caminho
## controlar histograma

import sys
import rospy
from work_smaart.srv import *

def isWeakBattery(x):
    rospy.wait_for_service('BatCalc')
    try:
        batCalc = rospy.ServiceProxy('BatCalc', BatCalc )
        resp1 = batCalc(x)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

# def isGoalAlready():
    
if __name__ == "__main__":

    dist = 6
    print("Requesting %s" %( dist ) )

    finished = isGoalAlready()
    retBatteryService = isWeakBattery(dist)
    if retBatteryService :
        print("voltar base") 
        # voltar pra base 
    else:
        print("continuar andando")
        #continuar caminho
    
##    print("%s , %s"%(dist, isWeakBattery(dist)))


