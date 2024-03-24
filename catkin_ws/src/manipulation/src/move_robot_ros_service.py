#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty, EmptyResponse  # Import Empty service message
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseStamped
import hello_helpers.hello_misc as hm
import numpy as np
from manipulation.srv import ExecuteCommand, ExecuteCommandResponse 
# to stow robot while the stretch_driver.launch is running run the following command:
# python3 move_robot_ros.py 


# rosrun /home/hello-robot/grocery_bot/catkin_ws/src/manipulation move_robot_ros_service.py 
# rosservice call /execute_multipoint_command "command: 'pick_up'"
# rosservice call /execute_multipoint_command "command: 'drop_off'"

class MultiPointCommand(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)
        self.gripper_open = 0.2
        self.gripper_close = -0.35
        self.arm_stow_height = 0.2
        self.latest_gripper_pose = None
        self.gripper_pose_subscriber = rospy.Subscriber('/gripper_pose', PoseStamped, self.gripper_pose_callback)
        # Initialize the service server
        self.service = rospy.Service('execute_multipoint_command', ExecuteCommand, self.handle_execute_command)

    def gripper_pose_callback(self, msg):
        self.latest_gripper_pose = msg

    def handle_execute_command(self, req):
        command = req.command  # Now you have "pick_up" or "drop_off"
        rospy.loginfo('Service call received with command: {}'.format(command))
        
        if command == "pick_up":
            z_offset = 0.1  # Example offset for pick_up
            y_offset = 0.1 # Example offset for pick_up
        elif command == "drop_off":
            z_offset = 0.35  # Example offset for drop_off
            y_offset = 0.1  # Example offset for drop_off
        else:
            rospy.logwarn("Unknown command received: {}".format(command))
            return ExecuteCommandResponse()  # Assuming you've defined a response part, even if it's empty

        self.move_camera()  # Move the camera
        self.issue_multipoint_command(y_offset, z_offset)  # Pass offsets to the method
        return ExecuteCommandResponse()


    def move_camera(self):
        # # Create and send trajectory goal for head pan and tilt
        # trajectory_goal = FollowJointTrajectoryGoal()
        # trajectory_goal.trajectory.joint_names = ['joint_head_pan', 'joint_head_tilt']
        # rospy.loginfo('Begin moving camera to position.')
        # # Initialize JointTrajectoryPoint with positions for both joints
        # # Adjust pan and tilt
        # # Since both movements are intended to start simultaneously, they are combined into a single JointTrajectoryPoint
        # joint_point = JointTrajectoryPoint()
        # joint_point.positions = [-1,-1]#[np.radians(-90), np.radians(-50)]  # Pan and Tilt positions respectively
        # joint_point.velocities = [0.5,0.5]
        
        # joint_point.time_from_start = rospy.Duration(4.0)  # Assuming both movements take 2 seconds

        # trajectory_goal.trajectory.points = [joint_point]
        # trajectory_goal.trajectory.header.stamp = rospy.Time.now()
        # trajectory_goal.trajectory.header.frame_id = 'base_link'


        # self.trajectory_client.send_goal(trajectory_goal)
        # rospy.loginfo('End moving camera to position.')
        # self.trajectory_client.wait_for_result()

        rospy.loginfo('Moving camera to position.')

        # Create the trajectory goal with specified joint names
        trajectory_goal = FollowJointTrajectoryGoal()
        trajectory_goal.trajectory.joint_names = ['joint_head_pan', 'joint_head_tilt']

        # Set up the joint trajectory point
        joint_point = JointTrajectoryPoint()
        joint_point.positions = [-1, -1]  # Target positions for pan and tilt
        joint_point.velocities = [0.5, 0.5]  # Target velocities
        joint_point.time_from_start = rospy.Duration(4.0)  # Time to reach the target positions

        # Add the joint trajectory point to the trajectory goal
        trajectory_goal.trajectory.points = [joint_point]
        trajectory_goal.trajectory.header.stamp = rospy.Time.now()
        trajectory_goal.trajectory.header.frame_id = 'base_link'

        # Send the trajectory goal
        self.trajectory_client.send_goal(trajectory_goal)
        rospy.loginfo('Camera movement command sent.')

        # Wait for the trajectory execution to complete
        self.trajectory_client.wait_for_result()
        rospy.loginfo('Camera movement complete.')


    def issue_multipoint_command(self, y_offset, z_offset):
        """
        Sends multiple joint trajectory goals to move the joint_lift, open the gripper,
        move the joint_lift again, and then extend the wrist.
        """
        if self.latest_gripper_pose is None:
            rospy.logwarn("No gripper pose received yet.")
            return
        

        z = self.latest_gripper_pose.pose.position.z + z_offset
        y = self.latest_gripper_pose.pose.position.y + y_offset

        # ROSINFO("current y,z",y,z)
        # Joint names
        joint_names = ['joint_lift', 'wrist_extension', 'joint_wrist_yaw', 'joint_gripper_finger_left']


        # close gripper (fully close position)
        close_gripper = JointTrajectoryPoint()

        close_gripper.positions = [self.arm_stow_height, 0.0, 0.0, self.gripper_close]  # Assuming 0.2 is the initial lift position
        close_gripper.time_from_start = rospy.Duration(2.0)

        # Move joint_lift to point 1
        move_lift_to_point_1 = JointTrajectoryPoint()
        move_lift_to_point_1.positions = [z, 0.0, 0.0, self.gripper_close]  # Keep gripper close
        move_lift_to_point_1.time_from_start = rospy.Duration(4.0)

        # Extend arm to point 2
        extend_arm_to_point_2 = JointTrajectoryPoint()
        extend_arm_to_point_2.positions = [z, y, 0.0, self.gripper_close]  # Extend wrist_extension to 0.2
        extend_arm_to_point_2.time_from_start = rospy.Duration(6.0)

        # open gripper
        open_gripper = JointTrajectoryPoint()
        open_gripper.positions = [z, y, 0.0, self.gripper_open]  # Open gripper
        open_gripper.time_from_start = rospy.Duration(6.0)


        # Create and send trajectory goal
        trajectory_goal = FollowJointTrajectoryGoal()
        trajectory_goal.trajectory.joint_names = joint_names
        trajectory_goal.trajectory.points = [close_gripper,move_lift_to_point_1,extend_arm_to_point_2,open_gripper]
        trajectory_goal.trajectory.header.stamp = rospy.Time.now()
        
        self.trajectory_client.send_goal(trajectory_goal)
        # rospy.loginfo('Sent list of goals = {0}'.format(trajectory_goal))
        rospy.loginfo('Executing trajectory with y: {:.3f}, z: {:.3f}'.format(y, z))
        self.trajectory_client.wait_for_result()

    def main(self):
        hm.HelloNode.main(self, 'multipoint_command', 'multipoint_command', wait_for_first_pointcloud=False)
        rospy.loginfo('MultiPointCommand service ready.')
        rospy.spin()  # Keep the node running to listen for service calls

if __name__ == '__main__':
    # rospy.init_node('multipoint_command_service')
    try:
        node = MultiPointCommand()
        node.main()
    except rospy.ROSInterruptException:
        rospy.loginfo('Interrupt received, so shutting down')
