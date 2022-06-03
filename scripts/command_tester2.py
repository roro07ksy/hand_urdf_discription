#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import JointState
from std_msgs.msg import Header



joint_8 = JointState()
joint_8.position = [0,0,0,0,0,0,0,0]  # input joint data order = [ aa1 aa2 aa3 aa4 fe1 fe2 fe3 fe4 ]
i=0
mcp_fe_max = 0.65


if __name__ == '__main__':
    pub = rospy.Publisher('/hand_joint_command', JointState , queue_size = 1)
    rospy.init_node('hand_command_tester', anonymous=True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown() :
        joint_8.header = Header()
        joint_8.header.stamp = rospy.Time.now()

        joint_8.position = [0.5*np.sin(3.14/200*i),0.5*np.sin(3.14/200*i),0.5*np.sin(3.14/200*i),0.5*np.sin(3.14/200*i),0,0,0,0]

        pub.publish(joint_8)

        i = i+1
        rate.sleep()