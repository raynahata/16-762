import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from aruco_msgs.msg import MarkerArray
import tf
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped

class RobotLocalizationFromMarker:
    def __init__(self):
        rospy.init_node('robot_localization_from_marker')

        #TODO: add in how to access the ARUCO markers 

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

        # Subscribe to ArUco marker detections and the robot's odometry
        rospy.Subscriber('/aruco_marker_publisher/markers', MarkerArray, self.marker_callback)

        # Publisher for the robot's updated pose
        self.pose_pub = rospy.Publisher('/updated_pose', PoseStamped, queue_size=10)

    def transform_to_map(self,req):
         try:
            transform_to_base = self.tf_buffer.lookup_transform("base_link", location_frame_id, rospy.Time(0), rospy.Duration(4.0))
            marker_pose_in_base = tf2_geometry_msgs.do_transform_pose(marker_pose, transform_to_base)

            transform_to_map = self.tf_buffer.lookup_transform("map", "base_link", rospy.Time(0), rospy.Duration(4.0))
            marker_pose_in_map = tf2_geometry_msgs.do_transform_pose(marker_pose_in_base, transform_to_map)

            marker_pose = self.calculate_desired_pose(marker_pose_in_map)
            print("Alignment pose")
            print(desired_pose)
           
       
            return marker_pose 
             #add this into the code below?
        
    def marker_callback(self, markers):
        for marker in markers.markers:
            marker_id = marker.id
            if marker_id in self.marker_map_locations:
                try:
                    
                    now = rospy.Time.now()
                    self.tf_listener.waitForTransform("map", marker.header.frame_id, now, rospy.Duration(1.0))
                    # Marker pose in the camera frame
                    marker_pose_camera = TransformStamped()
                    marker_pose_camera.header.frame_id = marker.header.frame_id
                    marker_pose_camera.child_frame_id = "aruco_marker_" + str(marker_id)
                    marker_pose_camera.transform.translation = marker.pose.pose.position
                    marker_pose_camera.transform.rotation = marker.pose.pose.orientation
                    
                    # Convert marker pose to map frame using TF
                    marker_pose_map = tf2_geometry_msgs.do_transform_pose(marker_pose_camera, self.tf_buffer.lookup_transform("map", marker.header.frame_id, now))
                    
                    # Known marker location
                    known_marker_location = self.marker_map_locations[marker_id]
                    
                    # Calculate the robot's new pose relative to the marker's known position
                    corrected_robot_pose = PoseStamped()
                    corrected_robot_pose.header.stamp = now
                    corrected_robot_pose.header.frame_id = "map"

                    corrected_robot_pose.pose.position.x = known_marker_location['x'] - (marker_pose_map.pose.position.x - marker_pose_camera.pose.position.x)
                    corrected_robot_pose.pose.position.y = known_marker_location['y'] - (marker_pose_map.pose.position.y - marker_pose_camera.pose.position.y)
                    corrected_robot_pose.pose.position.z = known_marker_location['z']
                    corrected_robot_pose.pose.orientation = marker_pose_map.pose.orientation

                    self.pose_pub.publish(corrected_robot_pose)

                except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException, tf2_ros.TransformException) as e:
                    rospy.logerr("TF error in marker callback: %s", e)

if __name__ == '__main__':
    try:
        RobotLocalizationFromMarker()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
