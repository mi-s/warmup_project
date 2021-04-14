# warmup_project

## Driving in a Square
__High Level Description__<br/>
My objective with this behavior is self-explanatory: make the robot drive in a square.  My approach was to create two functions which give the robot the ability to turn left and drive straight in separate motions.  Then, I used these functions to create a loop that causes the robot to drive in a square.<br/>

__Code Explanation__<br/>
*straight*<br/>
This function causes the robot to drive in a straight line for a fixed distance before stopping.  In the context of the problem, it represents one side of a square.<br/><br/>
*turn*<br/>
This function causes the robot to turn left 90 degrees.  In the context of the problem, this function runs when the robot has finished one side of the square and must turn before beginning the next side<br/><br/>
*run*<br/>
This function loops through the *straight* and *turn* functions 4 times, creating a square.
<br/><br/>

![Driving in a Square](./driving_in_a_square.gif)\

## Wall Follower
__High Level Description__<br/>
My original objective was to make the robot recognize when it was approaching walls before turning right until it is parallel with the wall.  However, due to difficulties I simplified my implementation.  My robot recognizes walls within a 30 degree arc ahead once they are within a certain distance.  Then, it turns right until the wall is no longer within that distance within the 30 degree arc.

__Code Explanation__<br/>
*scan_handler*<br/>
This function reads the scan data provided by the robot.  It first calculates the distance of the closest wall within a 30 degree arc in front of the robot.  When faced with no walls, it drives the robot forward.  If the robot is approaching a wall but not close enough yet, it slows the robot down.  If the robot is within a certain distance of the wall, it stops and turns right in place until it is no longer facing the wall anymore.  This function is repeatedly run on the robot's scan data to make the robot perform the behavior.

![wall follower](./wall_follower.gif)\

## Person Follower
__High Level Description__<br/>
The objective of this behavior is to make the robot follow the person.  My approach was to use the 360 degree LIDAR data given by the robot to identify the direction and distance to the person before instructing the robot to turn and move towards the person.  Once the person is within a certain distance, the robot will stop and use the LIDAR data to face the person until the person leaves the robot's distance.

__Code Explanation__<br/>
*scan_handler*<br/>
This function reads the scan data provided by the robot to determine the robot's velocity.  It first finds the direction in which it is closest to the person.  Should the person be ahead of the robot, the robot will simply drive forward.  If the person is to the side of the robot but not behind it, the robot will turn towards the person while moving forward.  If the person is behind the robot, the robot will stop and turn in place to face the person.  Once the robot is within a certain distance of the person, it will only move to turn towards the person.

![person follower](./person_follower.gif)\

## Challenges

## Future Work

## Takeaways
