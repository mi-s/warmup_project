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

__Code Explanation__<br/>

## Person Follower
__High Level Description__<br/>

__Code Explanation__<br/>

![wall follower](./wall_follower.gif)\

## Challenges

## Future Work

## Takeaways
