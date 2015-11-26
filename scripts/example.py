#!/usr/bin/python
# Put the description of your file here
# Author: Your Name <your_email@vt.edu>

# Import the Default ROS tools
import rospy
# Import the JointState message from sensor_msgs
from sensor_msgs.msg import JointState
# Import String as well
from std_msgs.msg import String

# Create variable so we can always see/use it, but set it to a value that indicates it's not yet valid
pub = None

#Function which is called every time a JointState is received, if the Subscriber is set up to use this function
def js_call(data):
  #print name of first joint in JointMessage. This will crash on an empty message
  print "Publishing", data.name[0]
  #Declare using the global pub
  global pub
  #Create the new message as an example output
  new_msg = String()
  new_msg.data = data.name[0]
  #Publish the new message for demonstration
  pub.publish(new_msg)

# If this is loaded as the main python file, execute the main details
if __name__ == '__main__':
  try:
    #Initialize node
    rospy.init_node('this_node')
    # Declare we are using the pub defined above, not a new local variable
    global pub
    #Create publisher, to send out a String with the first joint name of every received message as an example.
    pub = rospy.Publisher('names', String, queue_size=10)
    #Create subscriber, and tell it to call js_call() whenever a message is received
    sub = rospy.Subscriber('topic_name', JointState, js_call)

    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
