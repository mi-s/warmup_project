#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

class WallFollower():
    def __init__(self):
        rospy.init_node('wall_follower')
        self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.subscriber = rospy.Subscriber('/scan', LaserScan, self.scan_handler)
        self.vel_msg = Twist()

    ## scan_handler: adjusts robot velocity using scan data
    def scan_handler(self, scan):
        ## distance to closest wall in 30 degree arc in front of robot
        distance = min(scan.ranges[0:15] + scan.ranges[345:360])

        ## robot drives forward, slowing down as it approachs a wall
        ## upon approach wall, turns right until no longer facing the wall
        if distance < .7:
            self.vel_msg.linear.x = 0
            self.vel_msg.angular.z = -.4
        elif distance < .9:
            self.vel_msg.linear.x = .15
            self.vel_msg.angular.z = 0
        else:
            self.vel_msg.linear.x = .3
            self.vel_msg.angular.z = 0
            
        self.vel_publisher.publish(self.vel_msg)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = WallFollower()
    node.run() 
