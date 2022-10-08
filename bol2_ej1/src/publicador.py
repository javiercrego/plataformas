#!/usr/bin/env python
import rospy
from bol2_ej1.msg import msg_ex
import random 

rospy.init_node('publicadorbol2ej1')
pub=rospy.Publisher('consigna',msg_ex,queue_size=5)
dato=msg_ex()
l=['iniciar','continuar','interrumpir']
rate=rospy.Rate(1)

while not rospy.is_shutdown():

	dato.comando=l[random.randint(0,2)]
	dato.tiempo=random.randint(30,100)

	dato.posi.position.x=random.randint(0,150)
	dato.posi.position.y=random.randint(0,150)
	dato.posi.position.z=random.randint(0,150)

	dato.posi.orientation.x=random.randint(0,150)
	dato.posi.orientation.y=random.randint(0,150)
	dato.posi.orientation.z=random.randint(0,150)
	dato.posi.orientation.w=random.randint(0,150)

	pub.publish(dato)
	rate.sleep()

