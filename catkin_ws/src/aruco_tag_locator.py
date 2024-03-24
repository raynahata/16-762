#! /usr/bin/env python3

import rospy
import time
import tf2_ros
import numpy as np
from math import pi

import hello_helpers.hello_misc as hm
from sensor_msgs.msg import JointState
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import TransformStamped

class LocateArUcoTag(hm.HelloNode):
    """
    A class that actuates the RealSense camera to find the docking station's
    ArUco tag and returns a Transform between the `base_link` and the requested tag.
    """
    def __init__(self):
        """
        A function that initializes the subscriber and other needed variables.
        :param self: The self reference.
        """
        hm.HelloNode.__init__(self)

        self.joint_states_sub = rospy.Subscriber('/stretch/joint_states', JointState, self.joint_states_callback)
        self.transform_pub = rospy.Publisher('ArUco_transform', TransformStamped, queue_size=10)

        self.joint_state = None

        self.min_pan_position = -4.10
        self.max_pan_position =  1.50
        self.pan_num_steps = 10
        self.pan_step_size = abs(self.min_pan_position - self.max_pan_position)/self.pan_num_steps

        self.min_tilt_position = -0.75
        self.tilt_num_steps = 3
        self.tilt_step_size = pi/16

        self.rot_vel = 0.5 # radians per sec

    def joint_states_callback(self, msg):
        """
        A callback function that stores Stretch's joint states.
        :param self: The self reference.
        :param msg: The JointState message type.
        """
        self.joint_state = msg

    def send_command(self, command):
        '''
        Handles single joint control commands by constructing a FollowJointTrajectoryGoal
        message and sending it to the trajectory_client created in hello_misc.
        :param self: The self reference.
        :param command: A dictionary message type.
        '''
        if (self.joint_state is not None) and (command is not None):
            joint_name = command['joint']
            trajectory_goal = FollowJointTrajectoryGoal()
            trajectory_goal.trajectory.joint_names = [joint_name]
            point = JointTrajectoryPoint()

            if 'delta' in command:
                joint_index = self.joint_state.name.index(joint_name)
                joint_value = self.joint_state.position[joint_index]
                delta = command['delta']
                new_value = joint_value + delta
                point.positions = [new_value]

            elif 'position' in command:
                point.positions = [command['position']]

            point.velocities = [self.rot_vel]
            trajectory_goal.trajectory.points = [point]
            trajectory_goal.trajectory.header.stamp = rospy.Time(0.0)
            trajectory_goal.trajectory.header.frame_id = 'base_link'
            self.trajectory_client.send_goal(trajectory_goal)
            self.trajectory_client.wait_for_result()

    def find_tag(self, tag_name='drop_off'):
        """
        A function that actuates the camera to search for a defined ArUco tag
        marker. Then the function returns the pose
        :param self: The self reference.
        :param tag_name: A string value of the ArUco marker name.

        :returns transform: The docking station's TransformStamped message.
        """
        pan_command = {'joint': 'joint_head_pan', 'position': self.min_pan_position}
        self.send_command(pan_command)
        tilt_command = {'joint': 'joint_head_tilt', 'position': self.min_tilt_position}
        self.send_command(tilt_command)

        for i in range(self.tilt_num_steps):
            for j in range(self.pan_num_steps):
                pan_command = {'joint': 'joint_head_pan', 'delta': self.pan_step_size}
                self.send_command(pan_command)
                rospy.sleep(0.2)

                try:
                    transform = self.tf_buffer.lookup_transform('base_link',
                                                                tag_name,
                                                                rospy.Time())
                    rospy.loginfo("Found Requested Tag: \n%s", transform)
                    self.transform_pub.publish(transform)
                    return transform
                except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                    continue

            pan_command = {'joint': 'joint_head_pan', 'position': self.min_pan_position}
            self.send_command(pan_command)
            tilt_command = {'joint': 'joint_head_tilt', 'delta': self.tilt_step_size}
            self.send_command(tilt_command)
            rospy.sleep(.25)

        rospy.loginfo("The requested tag '%s' was not found", tag_name)

    def main(self):
        """
        Function that initiates the issue_command function.
        :param self: The self reference.
        """
        hm.HelloNode.main(self, 'aruco_tag_locator', 'aruco_tag_locator', wait_for_first_pointcloud=False)
        self.static_broadcaster = tf2_ros.StaticTransformBroadcaster()
        self.tf_buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tf_buffer)
        rospy.sleep(1.0)
        rospy.loginfo('Searching for docking ArUco tag.')
        pose = self.find_tag("docking_station")

if __name__ == '__main__':
    try:
        node = LocateArUcoTag()
        node.main()
    except KeyboardInterrupt:
        rospy.loginfo('interrupt received, so shutting down')