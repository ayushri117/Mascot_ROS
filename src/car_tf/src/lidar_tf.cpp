#include "ros/ros.h"
#include "tf/transform_broadcaster.h"
 
 int main(int argc, char** argv){
   ros::init(argc, argv, "lidar_tf");
   ros::NodeHandle n;
 
   ros::Rate r(100);
 
     tf::TransformBroadcaster broadcaster;
   
     while(n.ok()){
       broadcaster.sendTransform(
         tf::StampedTransform(
           tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.070, 0.000, 0.130)),
           ros::Time::now(),"base_link", "lidar_1"));
       r.sleep();
     }
   }