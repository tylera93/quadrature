#!/usr/bin/python
# Put the description of your file here
# Author: Tyler Atzingen <tylera93@vt.edu>

# Import the Default ROS tools
import rospy
# Need to import the Range 
from sensor_msgs.msg import Range
# Need to import ADC in order to get the raw voltage reading from pin P9_39
import Adafruit_BBIO.ADC as ADC
#Function will be called by the rate defined in the function which will be 5 Hz, or 5 times in a second
def IR_call():
  #Sets up the ADC pins which we will need to read the raw voltage of the IR sensor
  ADC.setup()
  pub = rospy.Publisher('/range', Range, queue_size=10)
  rospy.init_node('Range_Finder')
  r = rospy.Rate(5) #Sets the code to be executed 5 times per second
  IR.header.frame.id = "inertial_link"
  # Radiation value is set to 1 because the SHARP sensor is an infared sensor
  IR.radiation_type = 1
  # the field of view was set to 20 degrees but the value ha to be provided in 
  IR.field_of_view = 3.14/9.0
  # Minimum distance is set to 15 cm in order to avoid confusion where voltage could have two corresponding distances
  IR.min_range = 0.15
  # Maximum distance is 150 cm as sepcified by the spec sheet
  IR.Max_range = 1.50
  #Initalize IR sensor to have no value 
  IR.range = None
  while not rospy.is_shutdown():
    # We are going to use pin P9_39 because it worked and was used in the last assignment
    # Want to store the data as a float so it can be used to find the distance
    value = float(ADC.read_raw("P9_39")) 
    # Converts the voltage to distance by using an equation derived from the IR spec sheet
    # Distance to voltage was best modeled as a 4th degree polynomial
    distance = (20.065 * (value ** 4) - 155.71 * (value ** 3) + 443.24 * (value ** 2) - 570.96 * value + 324.71) * 100
    # Stores the distance conversion as the range
    IR.range = distance 
    rospy.loginfo(IR)
    # Publishes the data of the IR sensor
    pub.publish(IR)
    r.sleep()
 

# If this is loaded as the main python file, execute the main details
if __name__ == '__main__':
  try:
    # Calls the function that we just created above
    IR_call()
    #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass



