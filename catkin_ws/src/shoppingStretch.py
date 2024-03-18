import pointToPointNav
import rospy

'''
Driver file for shopping bot
'''
if __name__ == '__main__':

    #parser = argparse.ArgumentParser()
    #parser.add_argument('--pickup', '-p', type = int, default=None)
    #parser.add_argument('--dropoff', '-d', type=int, default=None) 
    #args = parser.parse_args()

    try:
        rospy.loginfo("Starting point to point")
        p2p = pointToPointNav.Move2Point()

        rospy.loginfo(f"Going to pickup location")
        pickupReached = p2p.moveToGoal("pickup") #go to pick up location
       
        if(pickupReached):
            rospy.loginfo(f"Reached pickup location")
            #grab itemon method
            rospy.sleep(3)
            rospy.loginfo(f"Grabbed item")

            rospy.loginfo(f"Going to dropoff location")
            dropoffReached = p2p.moveToGoal("dropoff") #go to drop off location

            if(dropoffReached):
                rospy.loginfo(f"Reached dropoff location")
                #drop off item method
                rospy.sleep(3)
            else:
                rospy.loginfo(f"Failed to reach dropoff location")

        else:
            rospy.loginfo(f"Failed to reach pickup location")

    except rospy.ROSInterruptException:
        rospy.loginfo("p2p node terminated.")
