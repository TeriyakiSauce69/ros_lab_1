#!/usr/bin/env python3

# import ROS for developing the node
import rospy
# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

from turtlesim.msg import Pose

from robotics_lab1.Turtlecontrol

import math

def pose_callback(data):
	global pos_msg
	# convert x and y to cm
	pos_msg.x = data.x * 100

	
def control_from_user(data):
	global pos_msg
	# convert x and y to cm
	pos_msg.xd = data.x * 100
	pos_msg.kp = data.y * 100
	

if __name__ == '__main__':
	# declare a publisher to publish in the velocity command topic
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# initialize the node
	rospy.init_node('vel_publisher_node', anonymous = True)
	
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, control_from_user)
	
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	# run this control loop regularly
	
	
	while not rospy.is_shutdown():
		# set the linear (forward/backward) velocity command
		vel_cmd.linear.x = 0.5
		# set the angular (heading) velocity command
		vel_cmd.angular.z = 0.5
		# publish the command to the defined topic
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
