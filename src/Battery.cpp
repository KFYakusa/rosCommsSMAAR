
#include <ros/ros.h>
#include "work_smaart/BatCalc.h"

bool battery( work_smaart::BatCalc::Request & request, work_smaart::BatCalc::Response & response){
    ROS_INFO("Received request");
    /* calculo aqui para descer a bateria */
    response.isWeak = true;
    return true;
}

int main(int argc, char * argv[])
{
    ros::init(argc, argv, "battery");
    ros::NodeHandle n;
    ros::ServiceServer batteryService = n.advertiseService("battery_calc", battery);
    ros::spin();
    ros::shutdown();
    return 0;
}
