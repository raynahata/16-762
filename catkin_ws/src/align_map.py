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

    def transform_to_map(self):
         try:
            transform_to_base = self.tf_buffer.lookup_transform("base_link", location_frame_id, rospy.Time(0), rospy.Duration(4.0))
            marker_pose_in_base = tf2_geometry_msgs.do_transform_pose(marker_pose, transform_to_base)

            transform_to_map = self.tf_buffer.lookup_transform("map", "base_link", rospy.Time(0), rospy.Duration(4.0))
            marker_pose_in_map = tf2_geometry_msgs.do_transform_pose(marker_pose_in_base, transform_to_map)

            marker_pose = self.calculate_desired_pose(marker_pose_in_map)
            print("Alignment pose")
            print(desired_pose)

        `#transform_to_map = self.tf_buffer.lookup_transform("base_link","map", rospy.Time(0), rospy.Duration(4.0))

       
            return marker_pose 
             #add this into the code below?
        
    def marker_callback(self, markers):
        for marker in markers.markers:
            marker_id = marker.id
            if marker_id in self.marker_map_locations:
                try:
                    # Marker pose according to the camera frame (observed pose)
                    observed_marker_pose = TransformStamped()
                    observed_marker_pose.header = marker.header
                    observed_marker_pose.child_frame_id = f"aruco_marker_{marker_id}"
                    observed_marker_pose.transform.translation = marker.pose.pose.position
                    observed_marker_pose.transform.rotation = marker.pose.pose.orientation
    
                    # Lookup the transformation from the camera to the map frame
                    #camera_to_map_transform = self.tf_buffer.lookup_transform("map", marker.header.frame_id, rospy.Time(0), rospy.Duration(1.0))
                   
                    transform_to_map = self.tf_buffer.lookup_transform("base_link","map", rospy.Time(0), rospy.Duration(4.0))

                    
    

                    
                    
                    # Transform the observed marker pose to the map frame
                    observed_marker_pose_in_map = tf2_geometry_msgs.do_transform_pose(observed_marker_pose, camera_to_map_transform)
    
                    # Known marker position in the map frame 
                    known_marker_pose = self.marker_map_locations[marker_id]
    
                    # Calculate the difference in position and orientation between the observed and known marker poses
                    
                    
                    
                    position_difference = [
                        known_marker_pose['x'] - observed_marker_pose_in_map.pose.position.x,
                        known_marker_pose['y'] - observed_marker_pose_in_map.pose.position.y,
                        known_marker_pose['z'] - observed_marker_pose_in_map.pose.position.z,
                    ]
    
                    # Apply the position difference to calculate the corrected robot pose in the map
                    corrected_robot_pose = PoseStamped()
                    corrected_robot_pose.header.stamp = rospy.Time.now()
                    corrected_robot_pose.header.frame_id = "map"
                    corrected_robot_pose.pose.position.x = camera_to_map_transform.transform.translation.x + position_difference[0]
                    corrected_robot_pose.pose.position.y = camera_to_map_transform.transform.translation.y + position_difference[1]
                    corrected_robot_pose.pose.position.z = camera_to_map_transform.transform.translation.z + position_difference[2]
                    corrected_robot_pose.pose.orientation = camera_to_map_transform.transform.rotation  
    
                    self.pose_pub.publish(corrected_robot_pose)
    
                except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException, tf2_ros.TransformException) as e:
                    rospy.logerr("TF error in marker callback: %s", e)

if __name__ == '__main__':
    try:
        RobotLocalizationFromMarker()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
