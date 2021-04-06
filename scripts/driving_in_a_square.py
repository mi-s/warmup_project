#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class SquareDriver:
    def __init__(self):
        rospy.init_node('square_driver')
        self.publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
 
    ## function that drives robot forward in a straight line for 3 seconds
    def straight(self):
        rospy.sleep(.5) 
        vel_msg = Twist()
        vel_msg.linear.x = 0

        ## drive forward
        vel_msg.linear.x = .2 
        self.publisher.publish(vel_msg)
        rospy.sleep(4.85)

        ## stop robot
        vel_msg.linear.x = .1
        self.publisher.publish(vel_msg)
        rospy.sleep(.5)
        vel_msg.linear.x = 0
        self.publisher.publish(vel_msg)
        rospy.sleep(1)

   ## function that turns robot counter-clockwise 90 degrees in place
    def turn(self):
        vel_msg = Twist()
        
        # begin turn motion
        vel_msg.angular.z = .51 
        self.publisher.publish(vel_msg)
        rospy.sleep(3)

        # stop turn motion
        vel_msg.angular.z = 0
        self.publisher.publish(vel_msg)
        rospy.sleep(1)
       
    ## function that uses above functions to make the robot drive in a square
    def run(self):
        for x in range(4):
            self.straight()
            self.turn()

if __name__ == '__main__':
     node = SquareDriver()
     node.run()
