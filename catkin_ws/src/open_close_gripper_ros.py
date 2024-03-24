import rospy
import time
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
import hello_helpers.hello_misc as hm

class GripperController(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)

    def open_gripper(self):
        """
        Function that sends a joint trajectory goal to open the gripper.
        """
        self.send_gripper_command(-0.35)  # Fully open position

    def close_gripper(self):
        """
        Function that sends a joint trajectory goal to close the gripper.
        """
        self.send_gripper_command(0.165)  # Closed position

    def send_gripper_command(self, position):
        """
        Sends a joint trajectory goal to move the gripper to a specified position.
        :param position: The target position of the gripper.
        """
        trajectory_goal = FollowJointTrajectoryGoal()
        trajectory_goal.trajectory.joint_names = ['joint_gripper_finger_left']

        point = JointTrajectoryPoint()
        point.positions = [position]
        point.time_from_start = rospy.Duration(1.0)  # Move to the position in 1 second

        trajectory_goal.trajectory.points = [point]
        trajectory_goal.trajectory.header.stamp = rospy.Time.now() + rospy.Duration(0.1)
        self.trajectory_client.send_goal(trajectory_goal)
        rospy.loginfo('Sent gripper goal = {0}'.format(trajectory_goal))
        self.trajectory_client.wait_for_result()

    def main(self):
        """
        Function that initiates the gripper control commands.
        """
        hm.HelloNode.main(self, 'gripper_control', 'gripper_control', wait_for_first_pointcloud=False)
        rospy.loginfo('Issuing gripper commands...')
        self.open_gripper()
        time.sleep(2)  # Wait for 2 seconds
        self.close_gripper()
        time.sleep(2)  # Wait for 2 seconds

if __name__ == '__main__':
    try:
        node = GripperController()
        node.main()
    except KeyboardInterrupt:
        rospy.loginfo('Interrupt received, so shutting down')
