#!/usr/bin/env python3

import rospy
from  geometry_msgs.msg import Twist
from curses import wrapper

def main(stdscr):
	rospy.init_node("keyboard")
	pub=rospy.Publisher("/cmd_vel",Twist,queue_size=10)
	while not rospy.is_shutdown():
		msg=Twist()
		key=stdscr.getkey()
		if key=="KEY_UP":
			msg.linear.x=1
		if key=="KEY_DOWN":
			msg.linear.x=-1
		if key=="KEY_LEFT":
			msg.angular.z=1
		if key=="KEY_RIGHT":
			msg.angular.z=-1
		pub.publish(msg)
wrapper(main)
