#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from std_msgs.msg import Float64

joint_20 = JointState()
joint_20.name =['aa2','mcp2','pip2','dip2','aa1','mcp1','pip1','dip1','aa3','mcp3','pip3','dip3','aa4','mcp4','pip4','dip4','act1','act2','act3','act4']
joint_20.position = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def callback(data) :
    pip_fe_joints =[0, 0, 0, 0]
    dip_fe_joints =[0, 0, 0, 0]
    act_joints =[0, 0, 0, 0]

    joint_8 = data.position      # 0-3 aa joints, 4-7 mcp fe joints 
    aa_joints =[joint_8[0],joint_8[1],joint_8[2],joint_8[3]]
    mcp_fe_joints = [joint_8[4],joint_8[5],joint_8[6],joint_8[7]]

    for i in range(4):    # joint coupling equations
        pip_fe_joints[i] = -0.1108*mcp_fe_joints[i]**4 + 0.3230*mcp_fe_joints[i]**3 -0.2964*mcp_fe_joints[i]**2 +1.2475*mcp_fe_joints[i]**1 + 0.0034
        dip_fe_joints[i] = 0.1005*mcp_fe_joints[i]**5 + 0.3467*mcp_fe_joints[i]**4 -0.4016*mcp_fe_joints[i]**3 +0.3414*mcp_fe_joints[i]**2 +0.6245*mcp_fe_joints[i]**1 -0.00087
        act_joints[i] = mcp_fe_joints[i]*0.8

    joint_20.position = [aa_joints[1], mcp_fe_joints[1],pip_fe_joints[1], dip_fe_joints[1],aa_joints[0], mcp_fe_joints[0],pip_fe_joints[0], dip_fe_joints[0],aa_joints[2], mcp_fe_joints[2],pip_fe_joints[2], dip_fe_joints[2],aa_joints[3], mcp_fe_joints[3],pip_fe_joints[3], dip_fe_joints[3],act_joints[0],act_joints[1],act_joints[2],act_joints[3]]




if __name__ == '__main__':
    pub = rospy.Publisher('/joint_states', JointState , queue_size = 1)
    sub = rospy.Subscriber('/hand_joint_command', JointState, callback, queue_size = 1)
    rospy.init_node('hand_joint_coupler', anonymous=True)
    rate = rospy.Rate(200)

    while not rospy.is_shutdown() :
        joint_20.header = Header()
        joint_20.header.stamp = rospy.Time.now()
        pub.publish(joint_20)
        rate.sleep()