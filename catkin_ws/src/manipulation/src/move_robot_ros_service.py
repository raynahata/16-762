#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_srvs.srv import Empty, EmptyResponse  # Import Empty service message
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseStamped
import hello_helpers.hello_misc as hm
import numpy as np
from manipulation.srv import ExecuteCommand, ExecuteCommandResponse 
import tf2_ros
import tf2_geometry_msgs
from gpd_ros.msg import GraspConfigList
import pdb
# to stow robot while the stretch_driver.launch is running run the following command:
# python3 move_robot_ros.py 


# rosrun /home/hello-robot/grocery_bot/catkin_ws/src/manipulation move_robot_ros_service.py 
# rosservice call /execute_multipoint_command "location: 'pick_up' item: 'spray bottle'"

# rosservice call /execute_multipoint_command "location: 'drop_off' item: 'spray bottle'"

class MultiPointCommand(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)
        self.gripper_open = 0.165
        self.gripper_close = -0.35
        self.arm_stow_height = 0.2
        self.tf_buffer = tf2_ros.Buffer(rospy.Duration(100.0))  # tf buffer length
        # self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)
        self.latest_gripper_pose = None
        self.location = None
        self.service = rospy.Service('execute_multipoint_command', ExecuteCommand, self.handle_execute_command)

        self.gripper_pose_subscriber = rospy.Subscriber('/detect_grasps/clustered_grasps', GraspConfigList, self.gripper_pose_callback)
        self.grocery_item_publisher = rospy.Publisher('/grocery_item', String, queue_size=10)  # Publisher for grocery item     
        

    def gripper_pose_callback(self, msg):
        self.latest_gripper_pose = msg

    def handle_execute_command(self, req):
        self.move_camera()
        """Service callback to process pick_up or drop_off commands."""
        location = req.location  # "pick_up" or "drop_off"
        item =  "white cap"
        
        
        self.location = location
        if location == "pick_up":
            # Publish the item to grocery_item topic only on pick_up
            self.grocery_item_publisher.publish(item)
            rospy.loginfo(f'Service call received with location: {location} for item: {item}')
            
            # Example offsets for pick_up
            z_offset = 0.2
            y_offset = 0.1
            self.issue_multipoint_command(y_offset, z_offset)
        
        elif location == "drop_off":
            # Example offsets for drop_off
            z_offset = 0.35
            y_offset = 0.1
            self.issue_multipoint_command(y_offset, z_offset)
        
        else:
            rospy.logwarn(f"Unknown location received: {location}")
            return ExecuteCommandResponse(success=False)

        return ExecuteCommandResponse(success=True)

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
        joint_point.positions = [-1.57, -0.1]  # Target positions for pan and tilt
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


        # ROSINFO("current y,z",y,z)
        # Joint names
        z = -1
        y = -1
        joint_names = ['joint_lift', 'wrist_extension', "translate_mobile_base",'joint_wrist_yaw', 'joint_gripper_finger_left']     
        trajectory_goal = []
        if self.location == "pick_up":

            timeout = rospy.Duration(10)  
            start_time = rospy.Time.now()

            # Wait for the latest gripper pose to be received or until timeout
            while self.latest_gripper_pose is None and (rospy.Time.now() - start_time) < timeout:
                rospy.sleep(0.1)  # Sleep to prevent busy waiting
                rospy.loginfo("Waiting for latest gripper pose...")

            grasp_frame_id = self.latest_gripper_pose.header.frame_id
            grasp_pose = PoseStamped()        
            grasp_pose.header.frame_id = grasp_frame_id
            # pdb.set_trace()

            grasp_pose.pose.position.x = self.latest_gripper_pose.grasps[0].position.x
            grasp_pose.pose.position.y = self.latest_gripper_pose.grasps[0].position.y
            grasp_pose.pose.position.z = self.latest_gripper_pose.grasps[0].position.z
            transform_to_base = self.tf_buffer.lookup_transform("camera_color_optical_frame", grasp_frame_id, rospy.Time(0), rospy.Duration(4.0))
            grasps_pose_in_base = tf2_geometry_msgs.do_transform_pose(grasp_pose, transform_to_base)
            
            grasps_pose_in_base_x = grasps_pose_in_base.pose.position.x
            grasps_pose_in_base_y = grasps_pose_in_base.pose.position.y
            grasps_pose_in_base_z = grasps_pose_in_base.pose.position.z
            print("grasps_pose_in_base",grasps_pose_in_base)

            z = grasps_pose_in_base_z + z_offset
            y = grasps_pose_in_base_x + y_offset
            x = grasps_pose_in_base_y

            # open gripper (fully close position)
            open_gripper = JointTrajectoryPoint()
            open_gripper.positions = [self.arm_stow_height, 0.0,x, 0.0, self.gripper_open]  # Assuming 0.2 is the initial lift position
            open_gripper.time_from_start = rospy.Duration(2.0)

            # Move joint_lift to point 1
            move_lift_to_point_1 = JointTrajectoryPoint()
            move_lift_to_point_1.positions = [z, 0.0, 0.0,0.0, self.gripper_open]  # Keep gripper close
            move_lift_to_point_1.time_from_start = rospy.Duration(4.0)

            # Extend arm to point 2
            extend_arm_to_point_2 = JointTrajectoryPoint()
            extend_arm_to_point_2.positions = [z, y, 0.0,0.0, self.gripper_open]  # Extend wrist_extension to 0.2
            extend_arm_to_point_2.time_from_start = rospy.Duration(6.0)

            # close gripper
            close_gripper = JointTrajectoryPoint()
            close_gripper.positions = [z, y, 0.0,0.0, self.gripper_close]  # close gripper
            close_gripper.time_from_start = rospy.Duration(6.0)

            retract_arm = JointTrajectoryPoint()
            retract_arm.positions = [z, 0.0, 0.0, 0.0,self.gripper_close]  # Extend wrist_extension to 0.2
            retract_arm.time_from_start = rospy.Duration(6.0)


            # lower_arm = JointTrajectoryPoint()
            # lower_arm.positions = [self.arm_stow_height, 0.0, 0.0, self.gripper_close]  # Extend wrist_extension to 0.2
            # lower_arm.time_from_start = rospy.Duration(6.0)

            trajectory_goal = FollowJointTrajectoryGoal()
            trajectory_goal.trajectory.joint_names = joint_names
            trajectory_goal.trajectory.points = [open_gripper,move_lift_to_point_1,extend_arm_to_point_2,close_gripper, retract_arm]
            trajectory_goal.trajectory.header.stamp = rospy.Time.now()

        elif self.location == "drop_off":
            z_drop_off = 0.95
            y_drop_off = 0.4
            move_lift_to_point_1 = JointTrajectoryPoint()
            move_lift_to_point_1.positions = [z_drop_off, 0.0, 0.0,0.0, self.gripper_close]  
            move_lift_to_point_1.time_from_start = rospy.Duration(4.0)

            extend_arm_to_point_2 = JointTrajectoryPoint()
            extend_arm_to_point_2.positions = [z_drop_off, y_drop_off,0.0, 0.0, self.gripper_close] 
            extend_arm_to_point_2.time_from_start = rospy.Duration(6.0)

            open_gripper = JointTrajectoryPoint()
            open_gripper.positions = [z_drop_off, y_drop_off, 0.0,0.0, self.gripper_open] 
            open_gripper.time_from_start = rospy.Duration(8.0)

            retract_arm1 = JointTrajectoryPoint()
            retract_arm1.positions = [z_drop_off, 0.0,0.0, 0.0, self.gripper_open]  # Extend wrist_extension to 0.2
            retract_arm1.time_from_start = rospy.Duration(6.0)

            retract_arm2 = JointTrajectoryPoint()
            retract_arm2.positions = [self.arm_stow_height, 0.0,0.0, 0.0, self.gripper_open]  # Extend wrist_extension to 0.2
            retract_arm2.time_from_start = rospy.Duration(6.0)

            trajectory_goal = FollowJointTrajectoryGoal()
            trajectory_goal.trajectory.joint_names = joint_names
            trajectory_goal.trajectory.points = [move_lift_to_point_1,extend_arm_to_point_2,extend_arm_to_point_2,open_gripper,retract_arm1,retract_arm2]
            trajectory_goal.trajectory.header.stamp = rospy.Time.now()
            y = y_drop_off
            z = z_drop_off
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

