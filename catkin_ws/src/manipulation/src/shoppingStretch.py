#!/usr/bin/env python3

import pointToPointNav as pointToPointNav
import rospy
from manipulation.srv import AlignBase, AlignBaseRequest, ExecuteCommand


def call_align_base_service(location):
    rospy.wait_for_service('/align_base')
    try:
        align_base = rospy.ServiceProxy('/align_base', AlignBase)
        print("Found aligner service")
        response = align_base(location)
        return response.success
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)
        return False

def call_execute_multipoint_command(command):
    rospy.wait_for_service('/execute_multipoint_command')
    try:
        execute_command = rospy.ServiceProxy('/execute_multipoint_command', ExecuteCommand)
        response = execute_command(command)
        return response.success
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)
        return False

if __name__ == '__main__':
    try:
        rospy.init_node('shopping_bot_driver', anonymous=True)
        rospy.loginfo("Starting point to point")
        p2p = pointToPointNav.Move2Point()

        rospy.loginfo("Going to pickup location")
        # pickupReached = p2p.moveToGoal("pickup")  # go to pick up location

        if True:
            rospy.loginfo("Reached pickup location")
            if call_align_base_service("pick_up"):
                rospy.loginfo("Alignment at pickup successful")
                # Execute sequence of commands after aligning at pick-up
                # if call_execute_multipoint_command("pick_up"):
                #     rospy.loginfo("Pick up sequence executed successfully")
                # else:
                #     rospy.logerr("Failed to execute pick up sequence")
            else:
                rospy.logerr("Alignment at pickup failed")

            # rospy.loginfo("Going to dropoff location")
            # dropoffReached = p2p.moveToGoal("dropoff")  # go to drop off location

            # if dropoffReached:
            #     rospy.loginfo("Reached dropoff location")
            #     if call_align_base_service("drop_off"):
            #         rospy.loginfo("Alignment at dropoff successful")
            #         # Execute sequence of commands after aligning at drop-off
            #         if call_execute_multipoint_command("drop_off"):
            #             rospy.loginfo("Drop off sequence executed successfully")
            #         else:
            #             rospy.logerr("Failed to execute drop off sequence")
            #     else:
            #         rospy.logerr("Alignment at dropoff failed")
            # else:
            #     rospy.logerr("Failed to reach dropoff location")

    except rospy.ROSInterruptException:
        rospy.loginfo("Shopping bot driver node terminated.")



# if __name__ == '__main__':
#     try:
#         # Initialize the ROS node
#         rospy.init_node('shopping_bot_driver', anonymous=True)

#         rospy.wait_for_service('align_base')

#         rospy.loginfo("Starting point to point")
#         p2p = pointToPointNav.Move2Point()

#         rate = rospy.Rate(1) # 1 Hz, adjust as needed
#         while not rospy.is_shutdown():
#             rospy.loginfo("Going to pickup location")
#             pickupReached = p2p.moveToGoal("pickup") # go to pick up location

#             if(pickupReached):
#                 rospy.loginfo("Reached pickup location")
#                 # Grab item method
#                 rospy.sleep(3)

#                 rospy.loginfo("Starting alignment")

#                 rospy.loginfo("Finished Alignment")

#                 rospy.loginfo("Going to dropoff location")

#                 dropoffReached = p2p.moveToGoal("dropoff") # go to drop off location

#                 if(dropoffReached):
#                     rospy.loginfo("Reached dropoff location")
#                     # Drop off item method
#                     rospy.sleep(3)
#                 else:
#                     rospy.loginfo("Failed to reach dropoff location")
#                 break  # Break the loop once the task is completed or replace with appropriate task logic

#             else:
#                 rospy.loginfo("Failed to reach pickup location")
#                 break  # Assuming we want to stop the node if we fail to reach the pickup location

#         rate.sleep()  # Sleep to maintain the loop rate

#     except rospy.ROSInterruptException:
#         rospy.loginfo("Shopping bot driver node terminated.")
