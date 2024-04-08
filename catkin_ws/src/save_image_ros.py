#!/usr/bin/env python

#save_image_ros.py
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageSaver:
    def __init__(self):
        # Initialize the node with rospy
        rospy.init_node('image_saver', anonymous=True)

        # Create a CvBridge to convert ROS image messages to OpenCV images
        self.bridge = CvBridge()

        # Subscribe to the image topic you want to save images from
        self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)

    def image_callback(self, data):
        try:
            # Convert the ROS image message to an OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        # Save the OpenCV image to a file
        cv2.imwrite('captured_image.jpg', cv_image)
        rospy.loginfo("Image saved.")

        # Optionally, display the image
        cv2.imshow("Image Window", cv_image)
        cv2.waitKey(3)

def main():
    image_saver = ImageSaver()
    rospy.spin()

if __name__ == '__main__':
    main()

