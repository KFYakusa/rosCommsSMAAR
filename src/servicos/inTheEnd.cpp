#include <ros/ros.h>
#include "work_smaart/isGoal.h"
#include <geometry_msgs/Point32.h>

using namespace geometry_msgs;
using namespace ros;

bool isInTheEnd(work_smaart::isGoal::Request  &req, work_smaart::isGoal::Response &res){    
  if(req.pos.x==19 && req.pos.y ==19) res.isGoal = true;
  else res.isGoal=false;
  return res.isGoal;
}

int main(int argc, char **argv){
  init(argc, argv, "inTheEnd");
  NodeHandle n;
  ServiceServer service = n.advertiseService("isGoal", isInTheEnd);
  spin();
  return 0;
}