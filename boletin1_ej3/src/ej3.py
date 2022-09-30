#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import random

rospy.init_node('mensaje')
pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)
mensaje=Twist()
rate=rospy.Rate(0.5)

while not rospy.is_shutdown():
	mensaje.linear.x=random.randint(0,100)	
	mensaje.linear.y=random.randint(0,100)
	mensaje.linear.z=random.randint(0,100)

	mensaje.angular.x=random.randint(0,100)
	mensaje.angular.y=random.randint(0,100)
	mensaje.angular.z=random.randint(0,100)
	pub.publish(mensaje)
	rate.sleep()
