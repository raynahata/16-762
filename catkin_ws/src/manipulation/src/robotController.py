import rospy
from geometry_msgs.msg import PoseStamped
import ikpy.urdf.utils
import urdfpy
import numpy as np
import ikpy.chain
import stretch_body.robot
import time

class RobotController:
    def __init__(self, pose_topic):
        self.latest_pose_stamped = PoseStamped()
        self.robot = stretch_body.robot.Robot()
        self.chain = None

        # Initialize ROS node
        rospy.init_node('robot_controller')

        # Create a subscriber for PoseStamped messages
        
        self.pose_subscriber = rospy.Subscriber(pose_topic, PoseStamped, self.pose_callback)

        # Setup the robot
        self.setup_robot()

    def pose_callback(self, msg):
        self.latest_pose_stamped = msg

    def setup_robot(self):
        if not self.robot.startup():
            print("Failed to open connection to the robot")
            return

        if not self.robot.is_calibrated():
            self.robot.home()

        # (Your URDF modification and chain setup code from the original script goes here)
        # Make sure to set self.chain after modifying the URDF and creating the chain

    def move_to_configuration(self, tool):
        x = self.latest_pose_stamped.pose.position.x
        y = self.latest_pose_stamped.pose.position.y
        z = self.latest_pose_stamped.pose.position.z
        # robot.base.translate_by(-0.38)#x

        self.robot.lift.move_to(z)#0.85) #z
        self.robot.push_command()


        time.sleep(5)
        self.robot.end_of_arm.move_to('stretch_gripper', 50)
        self.robot.push_command()
        self.robot.arm.move_to(y)#0.29)  #Y
        self.robot.push_command()
        
        self.robot.end_of_arm.move_to('wrist_yaw', 0)
        self.robot.push_command()
        self.robot.arm.wait_until_at_setpoint() 


        self.robot.end_of_arm.move_to('stretch_gripper', 0)
        self.robot.push_command()
        self.robot.arm.wait_until_at_setpoint() 
        time.sleep(5)

        self.robot.arm.move_to(0)
        self.robot.push_command()
        


    def run(self):
        # Main loop or other functionality to keep the robot operating
        try:
            rospy.spin()  # Keep the program running, listening for PoseStamped messages
        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    controller = RobotController('gripper_pose')
    controller.run()
