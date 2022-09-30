#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(msg):
	print(msg)


rospy.init_node('subscriptor_ej5')
pub=rospy.Subscriber('cmd_vel',Twist,callback)
rospy.spin()
