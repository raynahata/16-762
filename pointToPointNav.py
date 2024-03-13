import rospy
import math

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

'''
This class moves robot to a goal location. 
Based on Food Basket Delivery with the Stretch RE1 by J. Sun & P. Varshney - https://zackory.com/rc2023/media/16_887_Team_1_Project_Report.pdf
'''

POINTS = json.load(open('points.json', 'r'))
# PATH_COORDS = []

class Move2Point():
    def __init__(self, pickup, dropoff): #path_points are list of path locations

        rospy.init_node('p2p_nav')

        # self.path_coords = []

        # self.get_path_coords(path_points) #get position and orientation of each point in path
        # pickup_coords = POINTS[pickup]
        # dropoff_coords = POINTS[dropoff]

        # self.pickupReached = self.moveToGoal(pickup_coords)
        # if(self.pickupReached):
        #     rospy.loginfo(f"Reached pickup location at {pickup}")
        #     rospy.o
        # else:
        #     rospy.loginfo(f"Failed to reach pickup location at {pickup}")


    

    def moveToGoal(self, goal):
        goal_coords = POINTS[goal]
        goal_pos = goal_coords['position']
        goal_orientation = goal_coords['orientation']
        xGoal, yGoal = goal_pos['x'], goal_pos['y']

        ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

        while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
            rospy.loginfo("Waiting for move_base action server")

        goal = MoveBaseGoal()

        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position = Point(xGoal, yGoal, 0)
        goal.target_pose.pose.orientation.x = goal_orientation['x']
        goal.target_pose.pose.orientation.y = goal_orientation['y']
        goal.target_pose.pose.orientation.z = goal_orientation['z']
        goal.target_pose.pose.orientation.w = goal_orientation['w']

        rospy.loginfo("Sending goal location...")
        ac.send_goal(goal)
        start_time = time.perf_counter()

        ac.wait_for_result(rospy.Duration(60))

        if(ac.get_state() == GoalStatus.SUCCEEDED):
            return True
        else:
            return False

