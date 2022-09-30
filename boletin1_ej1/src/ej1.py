#!/usr/bin/env python
import rospy 

rospy.init_node('prueba')
rate=rospy.Rate(1)

while not rospy.is_shutdown():
	print('funciona')
	rate.sleep()
