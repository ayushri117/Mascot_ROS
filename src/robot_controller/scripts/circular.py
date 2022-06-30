#!/usr/bin/env python3
import rospy
from gpiozero import Motor

if __name__=="__main__":
	rospy.init_node("circular")
	rospy.loginfo("The node has been started")
	motor1=Motor(17,27)
	motor2=Motor(18,23)
	while True:
		motor1.forward(speed=1)
