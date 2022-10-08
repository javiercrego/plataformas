#!/usr/bin/env python
import rospy
from bol2_ej1.msg import msg_ex

def callback(msg):
	print(msg)

rospy.init_node('subscriptor')
sub=rospy.Subscriber('consigna',msg_ex,callback)
rospy.spin()
