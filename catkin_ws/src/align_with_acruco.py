#!/usr/bin/env python3

import rospy
import actionlib
import tf
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class NavigateToMarker:
    def __init__(self):
        rospy.init_node('navigate_to_marker')

        # Transform listener to convert poses between frames
        self.listener = tf.TransformListener()

        # Action client for move_base
        self.move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.move_base_client.wait_for_server()

        # Subscribe to MarkerArray topic where marker poses are published
        # Adjust '/marker_array_topic' to your actual topic name
        self.marker_array_subscriber = rospy.Subscriber('/aruco/marker_array', MarkerArray, self.marker_array_callback)
        self.goal_sent = False

    def marker_array_callback(self, marker_array):
        for marker in marker_array.markers:
            marker_pose = PoseStamped()
            marker_pose.header = marker.header
            marker_pose.pose = marker.pose

            self.listener.waitForTransform("map", marker_pose.header.frame_id, rospy.Time.now(), rospy.Duration(4.0))
            marker_pose_in_map = self.listener.transformPose("map", marker_pose)

            # Calculate desired robot pose in map frame
            desired_pose = self.calculate_desired_pose(marker_pose_in_map)

            self.send_goal_to_move_base(desired_pose)
            rospy.sleep(5.0)

            
    def calculate_desired_pose(self, marker_pose_in_map):
        desired_pose = PoseStamped()
        # Placeholder for actual calculation based on marker_pose_in_map
        offset_x = -0.03  # Example offset
        offset_y = -0.7  # Example offset
        
        desired_pose.header = marker_pose_in_map.header
        desired_pose.pose.position.x = marker_pose_in_map.pose.position.x - offset_x
        desired_pose.pose.position.y = marker_pose_in_map.pose.position.y + offset_y
        desired_pose.pose.orientation.x = 0
        desired_pose.pose.orientation.y = 0.0
        desired_pose.pose.orientation.z = 1
        desired_pose.pose.orientation.w = 0.0

        return desired_pose
    
    def send_goal_to_move_base(self, desired_pose):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = desired_pose.pose

        print(desired_pose.pose)
        self.move_base_client.send_goal(goal)
        rospy.loginfo("Goal sent to move_base.")

if __name__ == '__main__':
    try:
        navigator = NavigateToMarker()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
