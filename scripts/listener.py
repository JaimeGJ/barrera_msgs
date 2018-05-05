#!/usr/bin/env python
import rospy
from std_msgs.msg import Int8


def callback(data):
    rospy.loginfo(rospy.get_name() + ": He leído %d" % data.data)


def listener():
    rospy.init_node('barrera_lector', anonymous=True)
#    rospy.Subscriber("chatter", String, callback)
    rospy.Subscriber("barrera_solicitud", Int8, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
