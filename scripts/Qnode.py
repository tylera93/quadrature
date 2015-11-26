#!/usr/bin/env python

import rospy
from quadrature import QuadratureEstimator
# Imports Quadrature.msg that was provided for the assignment
from khan_msgs.msg import Quadrature
# Stores the class from quadrature.py in a variable
code = QuadratureEstimator(200)

def data(msg):
    code.update(msg.state_a.data, msg.state_b.data, msg.header.stamp)
    print "Position : ",code.position   # Reports the current position
    print "Velocity : ",code.velocity   # Reports the current velocity

def listener():
    rospy.init_node('Qnode', anonymous=True)
    rospy.Subscriber("/ticks", Quadrature, data)
    # Keeps your node from exiting until the node has been shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()





