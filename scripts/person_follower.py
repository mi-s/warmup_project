#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class PersonFollower():
    def __init__(self):
        rospy.init_node('person_follower')
        self.vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.subscriber = rospy.Subscriber('/scan', LaserScan, self.scan_handler)
        self.vel_msg = Twist()

    # scan_handler: handles scan data to set robot velocity to follow person
    def scan_handler(self, scan):
        distance = max(scan.ranges)
        direction = 0

        for i, d in enumerate (scan.ranges):
            if d < distance:
                distance = d
                direction = i

        # person in front
        if direction <= 20 or direction >= 340:
            self.vel_msg.linear.x = .5
            self.vel_msg.angular.z = 0
        # person on left
        elif direction > 20 and direction <= 140:
            self.vel_msg.angular.z = .8
        # person on right
        elif direction < 340 and direction >= 220:
            self.vel_msg.angular.z = -.8
        # person behind on left
        elif direction > 140 and direction < 220:
            self.vel_msg.linear.x = 0
            self.vel_msg.angular.z = 1.6
        # person behind on right
        else:
            self.vel_msg.linear.x = 0
            self.vel_msg.angular.z = -1.6

        # stop robot when within distance of person
        if distance < 1:
            self.vel_msg.linear.x = 0

        self.vel_publisher.publish(self.vel_msg)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = PersonFollower()
    node.run()
