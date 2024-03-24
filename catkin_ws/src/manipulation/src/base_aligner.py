#!/usr/bin/env python3

import rospy
import actionlib
import tf2_ros
import tf2_geometry_msgs
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from manipulation.srv import AlignBase, AlignBaseResponse

class BaseAligner:
    def __init__(self):
        rospy.init_node('base_aligner')

        # Transform listener to convert poses between frames
        self.tf_buffer = tf2_ros.Buffer(rospy.Duration(100.0))  # tf buffer length
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

        # Action client for move_base
        self.move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.move_base_client.wait_for_server()

        # Subscribe to MarkerArray topic where marker poses are published
        # Adjust '/marker_array_topic' to your actual topic name
        self.marker_array_subscriber = rospy.Subscriber('/aruco/marker_array', MarkerArray, self.marker_array_callback)
        self.gripper_pose = rospy.Publisher('/gripper_pose',PoseStamped,queue_size=10)
        self.align_base_service = rospy.Service('/align_base', AlignBase, self.handle_align_base)
    
    def handle_align_base(self, req):
        location_frame_id = req.location  # "pick_up" or "dropoff"
        
        # Assuming marker pose is somehow available (e.g., last seen marker, a fixed marker, etc.)
        # You might need to adjust how you obtain/use the marker pose here.
        marker_pose = PoseStamped()
        marker_pose.header.frame_id = location_frame_id  # Adjust as necessary
        # Fill marker_pose with actual pose data as required

        # Transform marker_pose to the map frame
        try:
            transform_to_map = self.tf_buffer.lookup_transform("map", location_frame_id, rospy.Time(0), rospy.Duration(4.0))
            marker_pose_in_map = tf2_geometry_msgs.do_transform_pose(marker_pose, transform_to_map)

            desired_pose = self.calculate_desired_pose(marker_pose_in_map)
            self.send_goal_to_move_base(desired_pose)

            return AlignBaseResponse(True)
        
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            rospy.logerr('Error transforming marker pose: %s' % str(e))
            return AlignBaseResponse(False)

    def marker_array_callback(self, marker_array):
        for marker in marker_array.markers:
            marker_pose = PoseStamped()
            marker_pose.header = marker.header
            marker_pose.pose = marker.pose
            
            transform_to_base = self.tf_buffer.lookup_transform("base_link",
                                       # source frame:
                                       "object",
                                       # get the tf at the time the pose was valid
                                       rospy.Time(0),
                                       # wait for at most 1 second for transform, otherwise throw
                                       rospy.Duration(4.0))

            marker_pose_in_base = tf2_geometry_msgs.do_transform_pose(marker_pose, transform_to_base)
            self.gripper_pose.publish(marker_pose_in_base)

    def calculate_desired_pose(self, marker_pose_in_map):
        desired_pose = PoseStamped()
        # Placeholder for actual calculation based on marker_pose_in_map
        offset_x = -0.1  # Example offset
        offset_y = 0.0  # Example offset
        
        desired_pose.header = marker_pose_in_map.header
        desired_pose.pose.position.x = marker_pose_in_map.pose.position.x + offset_x
        desired_pose.pose.position.y = marker_pose_in_map.pose.position.y + offset_y
        desired_pose.pose.orientation.x = 0.0
        desired_pose.pose.orientation.y = 0.0
        desired_pose.pose.orientation.z = 1.0
        desired_pose.pose.orientation.w = 1.0

        return desired_pose
    
    def send_goal_to_move_base(self, desired_pose):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = desired_pose.pose

        self.move_base_client.send_goal(goal)
        rospy.loginfo("Goal sent to move_base.")

if __name__ == '__main__':
    try:
        aligner = BaseAligner()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
