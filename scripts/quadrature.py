#!/usr/bin/python
# Object for decoding/estimating Quadrature decodings.
# Framework by: Jason Ziglar <jpz@vt.edu>
# Edited by Tyler Atzingen <tylera93@vt.edu>

import rospy

class QuadratureEstimator:
  def __init__(self, ticks_per_revolution):
    self.ticks_per_revolution = ticks_per_revolution
    self._position = 0
    self._velocity = 0
    self.a_old = None
    self.b_old = None
    self.time_old = 0
    self.offset_old = 0
    self.offset = 0

  def update(self, a_state, b_state, time):

    print "Current a state",a_state
    print "Current b state",b_state
   
    if self.a_old is None or self.b_old is None:
       self.a_old = a_state
       self.b_old = b_state
       self.time_old = rospy.get_time()
       return

    self.offset_old = self.offset

    if (a_state == 1 and self.b_old == 0) or (a_state == 0 and self.b_old == 1):
      self.offset -= 1

    if (a_state == 0 and self.b_old == 0) or (a_state == 1 and self.b_old == 1):
      self.offset += 1

    # Calculates the position and velocity
    self._position = float(self.offset)
    num = float(self.offset - self.offset_old)
    seconds = rospy.get_time()
    den = (seconds - self.time_old)
    self._velocity = num / den

    # Need the old states and the old time for position and velocity calculations
    self.time_old = seconds
    self.a_old = a_state
    self.b_old = b_state
    
    
  @property
  def position(self):
      return self._position
  @property
  def velocity(self):
      return self._velocity


