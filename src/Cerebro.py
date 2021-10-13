#!/usr/bin/env python3


import rospy
import cv2
from geometry_msgs.msg import Point
from sensor_msgs.msg import CompressedImage
import numpy as np
from work_smaart.srv import *
from cv_bridge import CvBridge

VERBOSE=rospy.get_param('~verbose',False)

class Cerebro():

    def __init__(self):
        self.img = None
        self.cvb = CvBridge()
        self.subImages = rospy.Subscriber('camera/image/compressed', CompressedImage, self.imgCallback, queue_size=10)
        if VERBOSE :
            print("subscribed to camera/image/compressed")
    
    def imgCallback(self, response_images):
        if VERBOSE : 
            rospy.logdebug('received image of type: "%s"'%response_images.format )
        
        self.img = cv2.imread("/home/daniel/Imagens/Base.jpeg")
        image_numpy = self.cvb.compressed_imgmsg_to_cv2(response_images)

        self.histogramComparator(image_numpy)
        cv2.imshow('fromCamera: ',image_numpy)
        cv2.waitKey(2)

    def batteryClient(self):
        rospy.wait_for_service('battery_calc')
        try:
            calculoBateria = rospy.ServiceProxy('battery_calc',BatCalc)
            
            # distancia total percorrida
            resposta = calculoBateria(20)
            return  resposta.isWeak
        except rospy.ServiceException as e:
            print("service call failed:  %s" %e)
            
    def histogramComparator(self,imgTest):
        imgBase = self.img
        if imgBase is None or imgTest is None:
            print("could not read the images")
            return
        
        hsv_base = cv2.cvtColor(imgBase, cv2.COLOR_BGR2HSV)
        hsv_test = cv2.cvtColor(imgTest, cv2.COLOR_BGR2HSV)
        
        hsv_half_down = hsv_base[hsv_base.shape[0]//2:,:]
        
        hue_bins=50
        saturation_bins=60
        histSize = [hue_bins, saturation_bins]
        
        #hue varia entre 0~179, saturação entre 0~255
        h_ranges = [0,180]
        s_ranges=[0,256]
        ranges=h_ranges + s_ranges # concatenando as lista
        
        #usar os canais 0 e 1
        channels= [0,1]
        

        hist_base = cv2.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
        cv2.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        hist_half_down = cv2.calcHist([hsv_half_down], channels, None, histSize, ranges, accumulate=False)
        cv2.normalize(hist_half_down, hist_half_down, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        hist_test = cv2.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
        cv2.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        for compare_method in range(3):
            base_base = cv2.compareHist(hist_base, hist_base, compare_method)
            base_half = cv2.compareHist(hist_base, hist_half_down, compare_method)
            base_test1 = cv2.compareHist(hist_base, hist_test, compare_method)
            print('Method:', compare_method, 'Perfect, Base-Half, Base-Test(1) :', base_base, '/', base_half, '/', base_test1 )
        print("success")
        return 







def main(args=None):
    rospy.init_node('cerebro')
    
    cerebro = Cerebro()
    try:
        
        retorno = cerebro.batteryClient()
        if retorno is True: 
            rospy.loginfo(f"tá consumindo o serviço certo: {retorno}")
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down Cerebro module")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

