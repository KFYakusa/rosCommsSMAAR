#include <ros/ros.h>

#include "/* header */"

int main(int argc, char * argv[])
{
    ros::init(argc, argv, "/* node_name */");
    auto /* node_name */ = /* namespace_name::ClassName */();
    ros::spin();
    ros::shutdown();
    return 0;
}
