#!/usr/bin/env python3

# import ROS for developing the node
import rospy
# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

from turtlesim.msg import Pose

from robotics_lab1.msg import Turtlecontrol

import math


pos_msg = Pose()
cntrl_msg = Turtlecontrol()


def pose_callback(data):
	global pos_msg
	# convert x and y to cm
	pos_msg.x = data.x

	
def control_from_user(data):
	global cntrl_msg
	# convert x and y to cm
	cntrl_msg.xd = data.xd
	cntrl_msg.kp = data.kp
	

if __name__ == '__main__':
	
	# initialize the node
	rospy.init_node('vel_publisher_node', anonymous = True)
	
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, control_from_user)
	
	# declare a publisher to publish in the velocity command topic
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	# run this control loop regularly
	
	while not rospy.is_shutdown():
		# publish the message
		cntrl_msg.xd = 8
		cntrl_msg.kp = 1
		
		
		vel_cmd.linear.x = cntrl_msg.kp * (cntrl_msg.xd - pos_msg.x)
		
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	
	
	
	

