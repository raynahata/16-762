#!/usr/bin/env python3

import open3d
import numpy as np
from ctypes import * # convert float to uint32

import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import matplotlib.pyplot as plt

class PointCloudFilter:
    def __init__(self):
        self.subscriber = rospy.Subscriber('/camera/depth/color/points', PointCloud2, self.point_cloud_callback)
        self.publisher = rospy.Publisher('/filtered_point_cloud', PointCloud2, queue_size=10)

        # The data structure of each point in ros PointCloud2: 16 bits = x + y + z + rgb
        self.FIELDS_XYZ = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
        ]
        self.FIELDS_XYZRGB = self.FIELDS_XYZ + \
            [PointField(name='rgb', offset=12, datatype=PointField.FLOAT32, count=1)]

        # Bit operations
        self.BIT_MOVE_16 = 2**16
        self.BIT_MOVE_8 = 2**8
        self.convert_rgbUint32_to_tuple = lambda rgb_uint32: (
    (rgb_uint32 & 0x00ff0000)>>16, (rgb_uint32 & 0x0000ff00)>>8, (rgb_uint32 & 0x000000ff))
        self.convert_rgbFloat_to_tuple = lambda rgb_float: self.convert_rgbUint32_to_tuple(
    int(cast(pointer(c_float(rgb_float)), POINTER(c_uint32)).contents.value))


    def point_cloud_callback(self, ros_point_cloud):
        open_3d_point_cloud = self.convertCloudFromRosToOpen3d(ros_point_cloud)

        # Convert Open3D point cloud to NumPy array for depth filtering
        np_points = np.asarray(open_3d_point_cloud.points)

        # Depth filtering: adjust min_depth and max_depth as needed
        min_depth = 0.2  # Minimum depth
        max_depth = 1.0  # Maximum depth
        depth_filter_indices = np.where((np_points[:, 2] > min_depth) & (np_points[:, 2] < max_depth))[0]
        depth_filtered_pcd = open_3d_point_cloud.select_by_index(depth_filter_indices)

        # Continue with your existing processing on depth_filtered_pcd
        down_sampled = depth_filtered_pcd.voxel_down_sample(voxel_size=0.01)
        plane_model, inliers = down_sampled.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)
        pcd_objects_only = down_sampled.select_by_index(inliers, invert=True)
        
        labels = np.array(pcd_objects_only.cluster_dbscan(eps=0.05, min_points=50, print_progress=True))
        max_label = labels.max()
        
        # Generate a unique color for each cluster
        colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
        colors[labels < 0] = 0  # Set noise to black
        pcd_objects_only.colors = open3d.utility.Vector3dVector(colors[:, :3])
        
        # Convert the modified point cloud back to ROS message and publish
        ros_cloud = self.convertCloudFromOpen3dToRos(pcd_objects_only)
        self.publisher.publish(ros_cloud)

    def convertCloudFromRosToOpen3d(self, ros_cloud):
    
        # Get cloud data from ros_cloud
        field_names=[field.name for field in ros_cloud.fields]
        cloud_data = list(pc2.read_points(ros_cloud, skip_nans=True, field_names = field_names))

        # Check empty
        open3d_cloud = open3d.geometry.PointCloud()
        if len(cloud_data)==0:
            print("Converting an empty cloud")
            return None

        # Set open3d_cloud
        if "rgb" in field_names:
            IDX_RGB_IN_FIELD=3 # x, y, z, rgb
            
            # Get xyz
            xyz = [(x,y,z) for x,y,z,rgb in cloud_data ] # (why cannot put this line below rgb?)

            # Get rgb
            # Check whether int or float
            if type(cloud_data[0][IDX_RGB_IN_FIELD])==float: # if float (from pcl::toROSMsg)
                rgb = [self.convert_rgbFloat_to_tuple(rgb) for x,y,z,rgb in cloud_data ]
            else:
                rgb = [self.convert_rgbUint32_to_tuple(rgb) for x,y,z,rgb in cloud_data ]

            # combine
            open3d_cloud.points = open3d.utility.Vector3dVector(np.array(xyz))
            open3d_cloud.colors = open3d.utility.Vector3dVector(np.array(rgb)/255)
        else:
            xyz = [(x,y,z) for x,y,z in cloud_data ] # get xyz
            open3d_cloud.points = open3d.utility.Vector3dVector(np.array(xyz))

        return open3d_cloud

    def convertCloudFromOpen3dToRos(self, open3d_cloud, frame_id="odom"):
        # Set "header"
        header = Header()
        header.stamp = rospy.Time.now()
        header.frame_id = frame_id

        # Set "fields" and "cloud_data"
        points=np.asarray(open3d_cloud.points)
        if not open3d_cloud.colors: # XYZ only
            fields=self.FIELDS_XYZ
            cloud_data=points
        else: # XYZ + RGB
            fields=self.FIELDS_XYZRGB
            # -- Change rgb color from "three float" to "one 24-byte int"
            # 0x00FFFFFF is white, 0x00000000 is black.
            colors = np.floor(np.asarray(open3d_cloud.colors)*255) # nx3 matrix
            colors = colors[:,0] * self.BIT_MOVE_16 +colors[:,1] * self.BIT_MOVE_8 + colors[:,2]  
            cloud_data=np.c_[points, colors]
        
        # create ros_cloud
        return pc2.create_cloud(header, fields, cloud_data)

if __name__ == '__main__':
    rospy.init_node('point_cloud_filter', anonymous=True)
    pcf = PointCloudFilter()
    rospy.spin()
