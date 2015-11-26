#!/usr/bin/env python

import rospy
from quadrature import QuadratureEstimator
from khan_msgs.msg import Quadrature
code = QuadratureEstimator(200)

def data(msg):
    code.update(msg.state_a, msg.state_b, msg.time)
    print "position : "  % code._position    # Reports the current position
    print "velocity : "  % code._velocity   # Reports the current velocity

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/ticks", Quadrature, data)
    rospy.spin()

if __name__ == '__main__':
    listener()

