#!/usr/bin/python
# Put the description of your file here
# Author: Tyler Atzingen <tylera93@vt.edu>

# Import the Default ROS tools
import rospy
# Import the JointState message from sensor_msgs
from sensor_msgs.msg import JointState
# Import String as well
from std_msgs.msg import String
# Need to import qaudrature 
from khan_msgs.msg import Quadrature
# Need to import the quadrature class from the code used for assignment 2.
from quadratureNew import QuadratureEstimator
# Need to import PWM and GPIO from adafruit
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

# Stores the PWM pins for each as variables
PWMpinm1 = "P9_14" 
PWMpinm2 = "P9_16"
PWMpinm3 = "P8_13"
PWMpinm4 = "P8_10"
# This chunck of code sets up all the GPIO pins for the motors
GPIO.setup("P9_11", GPIO.OUT)
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_15", GPIO.OUT)
GPIO.setup("P9_16", GPIO.OUT)
GPIO.setup("P8_08", GPIO.OUT)
GPIO.setup("P8_19", GPIO.OUT)
GPIO.setup("P8_11", GPIO.OUT)
GPIO.setup("P8_19", GPIO.OUT)
# Sets up the GPIO pins for the encoders
GPIO.setup("P9_24", GPIO.OUT)
GPIO.setup("P9_23", GPIO.OUT)
GPIO.setup("P8_17", GPIO.OUT)
GPIO.setup("P8_26", GPIO.OUT)
# Imports the quadrature code from the quadrature estimator file and stores in a variable called "code"
code = QuadratureEstimator(1000.0/3)
# Detects for events in the GPIO pins of one of the encoders
GPIO.add_event_detect("P9_24", GPIO.FALLING)
GPIO.add_event_detect("P9_23", GPIO.RISING)
# Names the first encoder as encoder left and makes it a JoinState data type
EncoderLeft = joinState()
# Gets the position for the encoder in rad by calling the quadrature code
EncoderLeft.position = code.positon 
# Gets the valocity for the encoder in rad/s by calling the quadrature code
EncoderLeft.velocity = code.velocity
# Detects for events in the GPIO pins of one of the encoders
GPIO.add_event_detect("P9_24", GPIO.FALLING)
GPIO.add_event_detect("P9_23", GPIO.RISING)
# Names the first encoder as encoder left and makes it a JoinState data type
EncoderRight = joinState()
# Gets the position for the encoder in rad by calling the quadrature code
EncoderRight.position = code.positon 
# Gets the valocity for the encoder in rad/s by calling the quadrature code
EncoderRight.velocity = code.velocity


# Function which is called every time a JointState is received for the front left wheel
def Callback_Motor_1(data):
  # Initiates if one one of the GPIO pins for the first motor is low and the other one is high
  if (GPIO.output("P9_11", GPIO.HIGH) and (GPIO.output("P9_12", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.1679 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P9_14", value) 
  # Initiates if one one of the GPIO pins if the pins have reverse high and low values than the first case  
  if (GPIO.input("P9_12", GPIO.HIGH) and (GPIO.input("P9_11", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.1679 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P9_14", value)
# Function which is called every time a JointState is received for the front right wheel
def Callback_Motor_2(data):
  if (GPIO.output("P9_13", GPIO.HIGH) and (GPIO.output("P9_15", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.1679 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P9_16", value)
  if (GPIO.input("P9_15", GPIO.HIGH) and (GPIO.input("P9_13", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.179 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P9_16", value)
# Function which is called every time a JointState is received for the rear left wheel
def Callback_Motor_3(data):
  if (GPIO.output("P8_09", GPIO.HIGH) and (GPIO.output("P8_08", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.1679 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P9_16", value)
  if (GPIO.input("P8_08", GPIO.HIGH) and (GPIO.input("P8_09", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.1679 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P8_13", value)
# Function which is called every time a JointState is received for the rear right wheel
def Callback_Motor_4(data):
  if (GPIO.output("P8_10", GPIO.HIGH) and (GPIO.output("P8_11", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.1679 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P8_19", value)
  if (GPIO.input("P8_11", GPIO.HIGH) and (GPIO.input("P8_10", GPIO.LOW)
    # Uses the function I plotted in excel to convert velocity in rad/s into a PWM signal
    int(value) = (7.1679 * data.velocity[0]) + 4.2376
    # Takes the PWM signal found from the conversion function at sets the duty cycle with that value
    PWM.set_duty_cycle("P8_19", value)

# If this is loaded as the main python file, execute the main details
if __name__ == '__main__':
  try:
    #Initializes the node. Note that the node name must be the same as the file name.
    rospy.init_node('Motor_Control')
    #Create the publishers. We need four publishers, one for each motor, that publish messages of type JointState
    pub_front_left_wheel = rospy.Publisher('/py_controller/front_left_wheel/encoder', JointState, queue_size=10)
    pub_front_right_wheel = rospy.Publisher('/py_controller/front_right_wheel/encoder', JointState, queue_size=10)
    pub_rear_left_wheel = rospy.Publisher('/py_controller/front_left_wheel/encoder', JointState, queue_size=10)
    pub_rear_right_wheel = rospy.Publisher('/py_controller/front_right_wheel/encoder', JointState, queue_size=10)
    

    #Creates the subscribers, since we have four motors we need four subscribers, one for each motor.
    sub_front_left_wheel = rospy.Subscriber('/py_controller/front_left_wheel/cmd', JointState, Callback_Motor_1)
    sub_front_right_wheel = rospy.Subscriber('/py_controller/front_right_wheel/cmd', JointState, Callback_Motor_2 )
    sub_rear_left_wheel = rospy.Subscriber('/py_controller/rear_left_wheel/cmd', JointState, Callback_Motor_3)
    sub_rear_right_wheel = rospy.Subscriber('/py_controller/rear_right_wheel/cmd', JointState, Callback_Motor_4)
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
