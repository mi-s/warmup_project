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

__Code Explanation__<br/>

![person follower](./person_follower.gif)\

## Challenges

## Future Work

## Takeaways
