#!/usr/bin/env python
import rospy
from std_msgs.msg import Int8


enable = 1

def talker_listener():

    pub = rospy.Publisher('barrera_solicitud', Int8)
#    sub = rospy.Subscriber("barrera_solicitud", Int8, callback)
    rospy.init_node('barrera_solicitud')
    while not rospy.is_shutdown():

	global enable
	enable = ipnut("1 = abrir | 2 = cerrar : ")
        rospy.loginfo(enable)
	pub.publish(Int8(enable))
        rospy.sleep(2.0)
	enable = enable + 1
	if enable > 2:
	  enable = 1


if __name__ == '__main__':
    try:
        talker_listener()
	#rospy.spin()
    except rospy.ROSInterruptException:
        pass
