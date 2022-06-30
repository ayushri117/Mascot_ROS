#!/usr/bin/env python3

import rospy
from gpiozero import Motor
from geometry_msgs.msg import Twist
def motor_callback(msg):
	rospy.loginfo(f"linear: {msg.linear.x} {msg.linear.y} {msg.linear.z}")
	rospy.loginfo(f"angular: {msg.angular.x} {msg.angular.y} {msg.angular.z}")
	spee=msg.linear.x
	turn=msg.angular.z
	if turn==0 and spee>0:
		motor1.backward(speed=spee)
		motor2.backward(speed=spee)
	elif turn==0 and spee<0:
		motor1.forward(speed=-1*spee)
		motor2.forward(speed=-1*spee)
	elif turn>0:
		motor1.backward(speed=turn)
	elif turn<0:
		motor2.backward(speed=-1*turn)

if __name__=="__main__":
	rospy.init_node("motor")
	sub=rospy.Subscriber("/turtle1/cmd_vel",Twist,callback=motor_callback)
	motor1=Motor(17,27)
	motor2=Motor(18,23)
	rospy.loginfo("The node 'Motor' has been started")
	rospy.spin()
