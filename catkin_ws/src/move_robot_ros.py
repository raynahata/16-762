import rospy
import time
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseStamped  # Import PoseStamped
import hello_helpers.hello_misc as hm
import numpy as np


class MultiPointCommand(hm.HelloNode):
    """
    A class that sends multiple joint trajectory goals to the stretch robot.
    """
    def __init__(self):
        hm.HelloNode.__init__(self)
        self.gripper_open = 0.165
        self.gripper_close = -0.35
        self.arm_stow_height = 0.2
        self.latest_gripper_pose = None  # Attribute to store the latest gripper pose
        # Subscribe to the gripper_pose topic
        self.gripper_pose_subscriber = rospy.Subscriber('/gripper_pose', PoseStamped, self.gripper_pose_callback)

    def gripper_pose_callback(self, msg):
        """
        Callback function for the gripper_pose subscriber.
        """
        self.latest_gripper_pose = msg


    def issue_multipoint_command(self):
        """
        Sends multiple joint trajectory goals to move the joint_lift, open the gripper,
        move the joint_lift again, and then extend the wrist.
        """
        # if self.latest_gripper_pose is None:
        #     rospy.logwarn("No gripper pose received yet.")
        #     return
        
        # # Extract z and y from the latest gripper pose
        # z = self.latest_gripper_pose.pose.position.z
        # y = self.latest_gripper_pose.pose.position.y

        # Joint names
        joint_names = ['joint_lift', 'wrist_extension', 'joint_wrist_yaw', 'joint_gripper_finger_left']


        # close gripper (fully close position)
        close_gripper = JointTrajectoryPoint()

        close_gripper.positions = [self.arm_stow_height, 0.0, 0.0, self.gripper_close]  # Assuming 0.2 is the initial lift position
        close_gripper.time_from_start = rospy.Duration(2.0)

        # # Move joint_lift to point 1
        # move_lift_to_point_1 = JointTrajectoryPoint()
        # move_lift_to_point_1.positions = [z, 0.0, 0.0, self.gripper_close]  # Keep gripper close
        # move_lift_to_point_1.time_from_start = rospy.Duration(4.0)

        # # Extend arm to point 2
        # extend_arm_to_point_2 = JointTrajectoryPoint()
        # extend_arm_to_point_2.positions = [z, y, 0.0, self.gripper_close]  # Extend wrist_extension to 0.2
        # extend_arm_to_point_2.time_from_start = rospy.Duration(6.0)

        # # open gripper
        # open_gripper = JointTrajectoryPoint()
        # open_gripper.positions = [z, y, 0.0, self.gripper_open]  # Open gripper
        # open_gripper.time_from_start = rospy.Duration(6.0)


        # Create and send trajectory goal
        trajectory_goal = FollowJointTrajectoryGoal()
        trajectory_goal.trajectory.joint_names = joint_names
        trajectory_goal.trajectory.points = [close_gripper]
        trajectory_goal.trajectory.header.stamp = rospy.Time.now()
        
        self.trajectory_client.send_goal(trajectory_goal)
        rospy.loginfo('Sent list of goals = {0}'.format(trajectory_goal))
        self.trajectory_client.wait_for_result()

    def move_camera(self):
        # Create and send trajectory goal for head pan and tilt
        trajectory_goal = FollowJointTrajectoryGoal()
        trajectory_goal.trajectory.joint_names = ['joint_head_pan', 'joint_head_tilt']

        # Initialize JointTrajectoryPoint with positions for both joints
        # Adjust pan and tilt
        # Since both movements are intended to start simultaneously, they are combined into a single JointTrajectoryPoint
        joint_point = JointTrajectoryPoint()
        joint_point.positions = [np.radians(-90), np.radians(-30)]  # Pan and Tilt positions respectively
        joint_point.time_from_start = rospy.Duration(2.0)  # Assuming both movements take 2 seconds

        trajectory_goal.trajectory.points = [joint_point]
        trajectory_goal.trajectory.header.stamp = rospy.Time.now()

        self.trajectory_client.send_goal(trajectory_goal)
        rospy.loginfo('Moving camera to position.')
        self.trajectory_client.wait_for_result()
    def main(self):
        """
        Function that initiates the multipoint_command function.
        """
        hm.HelloNode.main(self, 'multipoint_command', 'multipoint_command', wait_for_first_pointcloud=False)
        rospy.loginfo('Waiting for gripper pose...')
        self.move_camera()
        self.issue_multipoint_command()
        # rospy.wait_for_message('/gripper_pose', PoseStamped)  # Wait for at least one message to be received
        rospy.loginfo('Issuing multipoint command...')
        # self.move_camera()
        time.sleep(2)

if __name__ == '__main__':
    try:
        node = MultiPointCommand()
        node.main()
    except KeyboardInterrupt:
        rospy.loginfo('Interrupt received, so shutting down')
