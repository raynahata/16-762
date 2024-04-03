import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from aruco_msgs.msg import MarkerArray
import tf
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped

class ArucoLocalizationAdjust:
    def __init__(self):
        rospy.init_node('aruco_localization_adjust')

        #TODO: Add known marker locations

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)
        self.tf_broadcaster = tf2_ros.TransformBroadcaster()

        # Subscribe to ArUco markers and odometry
        rospy.Subscriber('/aruco_marker_publisher/markers', MarkerArray, self.marker_callback)
        rospy.Subscriber('/odom', Odometry, self.odom_callback)

        # Publisher for updated pose
        self.pose_pub = rospy.Publisher('/updated_pose', PoseStamped, queue_size=10)

        self.current_odom = None

    def odom_callback(self, msg):
        self.current_odom = msg

    def marker_callback(self, markers):
        if not self.current_odom:
            return

        for marker in markers.markers:
            marker_id = marker.id
            if marker_id in self.marker_map_locations:
                # Known marker pose in map frame
                known_pose = self.marker_map_locations[marker_id]

                try:
                    # Get transformation from camera to marker
                    trans_marker = self.tf_buffer.lookup_transform('camera_link', marker.header.frame_id, rospy.Time(0), rospy.Duration(1.0))
                    
                    # Known marker pose as a TransformStamped
                    known_marker_transform = TransformStamped()
                    known_marker_transform.header.stamp = rospy.Time.now()
                    known_marker_transform.header.frame_id = "map"
                    known_marker_transform.child_frame_id = "known_marker_" + str(marker_id)
                    known_marker_transform.transform.translation.x = known_pose['x']
                    known_marker_transform.transform.translation.y = known_pose['y']
                    known_marker_transform.transform.translation.z = known_pose['z']
                    known_marker_transform.transform.rotation.x = known_pose['qx']
                    known_marker_transform.transform.rotation.y = known_pose['qy']
                    known_marker_transform.transform.rotation.z = known_pose['qz']
                    known_marker_transform.transform.rotation.w = known_pose['qw']
                    
                    # Broadcast the known marker pose
                    self.tf_broadcaster.sendTransform(known_marker_transform)
                    
                    # Wait for transform to stabilize
                    rospy.sleep(0.1)

                    # Calculate robot's pose based on the observed marker pose and its known pose
                    trans_robot = self.tf_buffer.lookup_transform('map', 'camera_link', rospy.Time(0), rospy.Duration(1.0))
                    
                    # Publish robot's updated pose
                    updated_pose = PoseStamped()
                    updated_pose.header = trans_robot.header
                    updated_pose.pose.position = trans_robot.transform.translation
                    updated_pose.pose.orientation = trans_robot.transform.rotation
                    
                    self.pose_pub.publish(updated_pose)

                except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
                    rospy.logerr("TF2 error when processing marker: %s", e)
                    continue

if __name__ == '__main__':
    try:
        ArucoLocalizationAdjust()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
