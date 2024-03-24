#!/usr/bin/env python3

import pointToPointNav as pointToPointNav
import rospy


if __name__ == '__main__':
    try:
        # Initialize the ROS node
        rospy.init_node('shopping_bot_driver', anonymous=True)

        rospy.loginfo("Starting point to point")
        p2p = pointToPointNav.Move2Point()

        rate = rospy.Rate(1) # 1 Hz, adjust as needed
        while not rospy.is_shutdown():
            rospy.loginfo("Going to pickup location")
            pickupReached = p2p.moveToGoal("pickup") # go to pick up location

            if(pickupReached):
                rospy.loginfo("Reached pickup location")
                # Grab item method
                rospy.sleep(3)

                rospy.loginfo("Starting alignment")

                rospy.loginfo("Finished Alignment")

                rospy.loginfo("Going to dropoff location")

                dropoffReached = p2p.moveToGoal("dropoff") # go to drop off location

                if(dropoffReached):
                    rospy.loginfo("Reached dropoff location")
                    # Drop off item method
                    rospy.sleep(3)
                else:
                    rospy.loginfo("Failed to reach dropoff location")
                break  # Break the loop once the task is completed or replace with appropriate task logic

            else:
                rospy.loginfo("Failed to reach pickup location")
                break  # Assuming we want to stop the node if we fail to reach the pickup location

        rate.sleep()  # Sleep to maintain the loop rate

    except rospy.ROSInterruptException:
        rospy.loginfo("Shopping bot driver node terminated.")
