#!/usr/bin/env python3

import open3d
import numpy as np
from ctypes import *

import open3d.visualization # convert float to uint32

import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import matplotlib.pyplot as plt
import pdb
from std_msgs.msg import Float64MultiArray, MultiArrayDimension

class PointCloudFilter:
    def __init__(self):
        self.subscriber = rospy.Subscriber('/camera/depth/color/points', PointCloud2, self.point_cloud_callback)
        self.publisher = rospy.Publisher('/filtered_point_cloud', PointCloud2, queue_size=10)
        self.bounding_box_subscriber = rospy.Subscriber('/bounding_boxes', Float64MultiArray,self.bounding_box_callback)

        # The data structure of each point in ros PointCloud2: 16 bits = x + y + z + rgb
        self.FIELDS_XYZ = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
        ]
        self.FIELDS_XYZRGB = self.FIELDS_XYZ + \
            [PointField(name='rgb', offset=12, datatype=PointField.FLOAT32, count=1)]
        self.bounding_box = None
        # Bit operations
        self.BIT_MOVE_16 = 2**16
        self.BIT_MOVE_8 = 2**8
        self.convert_rgbUint32_to_tuple = lambda rgb_uint32: (
    (rgb_uint32 & 0x00ff0000)>>16, (rgb_uint32 & 0x0000ff00)>>8, (rgb_uint32 & 0x000000ff))
        self.convert_rgbFloat_to_tuple = lambda rgb_float: self.convert_rgbUint32_to_tuple(
    int(cast(pointer(c_float(rgb_float)), POINTER(c_uint32)).contents.value))

    def bounding_box_callback(self,bounding_box):
        
        self.bounding_box = bounding_box


    def point_cloud_callback(self, ros_cloud):
        if self.bounding_box is not None:
            print("here")
            # open_3d_point_cloud = self.convertCloudFromRosToOpen3d(ros_point_cloud)

            # # Convert Open3D point cloud to NumPy array for depth filtering
            # np_points = np.asarray(open_3d_point_cloud.points)

            # # Depth filtering: adjust min_depth and max_depth as needed
            # min_depth = 0.05  # Minimum depth
            # max_depth = 0.5  # Maximum depth
            # depth_filter_indices = np.where((np_points[:, 2] > min_depth) & (np_points[:, 2] < max_depth))[0]
            # depth_filtered_pcd = open_3d_point_cloud.select_by_index(depth_filter_indices)

            # # Continue with your existing processing on depth_filtered_pcd
            # down_sampled = depth_filtered_pcd.voxel_down_sample(voxel_size=0.01)
            # plane_model, inliers = down_sampled.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)
            # pcd_objects_only = down_sampled.select_by_index(inliers, invert=True)
            
            # labels = np.array(pcd_objects_only.cluster_dbscan(eps=0.05, min_points=20, print_progress=True))
            # max_label = labels.max()
            
            # # Generate a unique color for each cluster
            # colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
            # colors[labels < 0] = 0  # Set noise to black
            # pcd_objects_only.colors = open3d.utility.Vector3dVector(colors[:, :3])
            
            # # Convert the modified point cloud back to ROS message and publish
            # ros_cloud = self.convertCloudFromOpen3dToRos(open_3d_point_cloud)
            xmin, ymin, xmax, ymax = self.bounding_box.data #198, 134, 257, 171 #fliped x and y #self.bounding_box.data 
              
            field_names = [field.name for field in ros_cloud.fields]
            uvs = [(u, v) for v in range(int(ymin), int(ymax)) for u in range(int(xmin), int(xmax))]
            cloud_data = list(pc2.read_points(ros_cloud, skip_nans=True, field_names=field_names, uvs=uvs))
            header = Header()
            header.stamp = rospy.Time.now()
            header.frame_id = ros_cloud.header.frame_id
            fields=self.FIELDS_XYZRGB
            pc2_cloud = pc2.create_cloud(header, fields, cloud_data)
            self.publisher.publish(pc2_cloud)
        else:
            print("Waiting for bounding box")

    # def convertCloudFromRosToOpen3d(self, ros_cloud):
    
    #     # Get cloud data from ros_cloud
    #     field_names = [field.name for field in ros_cloud.fields]
    #     print(field_names)

    #     # Example bounding box coordinates from the OWLViT model
    #     # print(self.bounding_box)
    #     xmin, ymin, xmax, ymax = self.bounding_box.data #198, 134, 257, 171 #fliped x and y #self.bounding_box.data 
    #     # bbox = [249, 323,151,  180,-float('inf'),float('inf')] #[151, 101, 180, 175]
    #     # bbox = [-2, 2,-10,  10,0,1] 
    #     # print("xmin, ymin, xmax, ymax",xmin, ymin, xmax, ymax)  
        
    #     print("ros_cloud.width, height,row_step",ros_cloud.width,ros_cloud.height,ros_cloud.row_step)

    #     # pdb.set_trace()
    #     # Generate a list of UV coordinates within the bounding box

    #     uvs = [(u, v) for v in range(int(ymin), int(ymax)) for u in range(int(xmin), int(xmax))]
    #     uvs2 = [(10,10)]
    #     # print(uvs)
    #     min_bound = [0,0,-float('inf')]
    #     max_bound = [10,10,float('inf')]


    #     # Use read_points() with the uvs parameter to get points from the bounding box area
    #     cloud_data = list(pc2.read_points(ros_cloud, skip_nans=True, field_names=field_names, uvs=uvs))
    #     header = Header()
    #     header.stamp = rospy.Time.now()
    #     header.frame_id = "odom"
    #     fields=self.FIELDS_XYZRGB
    #     return pc2.create_cloud(header, fields, cloud_data)
    #     # print(cloud_data)
        # Check empty
        # open3d_cloud = open3d.geometry.PointCloud()
        # if len(cloud_data)==0:
        #     print("Converting an empty cloud")
        #     return None

        # # Set open3d_cloud
        # if "rgb" in field_names:
        #     IDX_RGB_IN_FIELD=3 # x, y, z, rgb
            
        #     # Get xyz
        #     xyz = [(x,y,z) for x,y,z,rgb in cloud_data ] # (why cannot put this line below rgb?)

        #     # Get rgb
        #     # Check whether int or float
        #     if type(cloud_data[0][IDX_RGB_IN_FIELD])==float: # if float (from pcl::toROSMsg)
        #         rgb = [self.convert_rgbFloat_to_tuple(rgb) for x,y,z,rgb in cloud_data ]
        #     else:
        #         rgb = [self.convert_rgbUint32_to_tuple(rgb) for x,y,z,rgb in cloud_data ]

        #     # combine
        #     open3d_cloud.points = open3d.utility.Vector3dVector(np.array(xyz))
        #     open3d_cloud.colors = open3d.utility.Vector3dVector(np.array(rgb)/255)
        # else:
        #     xyz = [(x,y,z) for x,y,z in cloud_data ] # get xyz
        #     open3d_cloud.points = open3d.utility.Vector3dVector(np.array(xyz))

        # cropped_point_cloud = open3d.geometry.crop_point_cloud(open3d_cloud,min_bound,max_bound)
        # open3d.visualization.draw_geometries([cropped_point_cloud])
        # mesh_frame = open3d.geometry.TriangleMesh.create_coordinate_frame(size=0.6, origin=[0,0,0])
        # open3d.visualization.draw_geometries([open3d_cloud])
        # open3d_cloud = np.asarray(open3d_cloud.points)
        # mask = (open3d_cloud[:, 0] >= bbox[0]) & (open3d_cloud[:, 0] <= bbox[1]) & \
        # (open3d_cloud[:, 1] >= bbox[2]) & (open3d_cloud[:, 1] <= bbox[3]) & \
        # (open3d_cloud[:, 2] >= bbox[4]) & (open3d_cloud[:, 2] <= bbox[5]) 
        # cropped_points = open3d_cloud[mask]
        # cropped_pcd = open3d.geometry.PointCloud()
        # cropped_pcd.points = open3d.utility.Vector3dVector(cropped_points)
        
        # open3d.visualization.draw_geometries([cropped_pcd,mesh_frame])

        # return cloud_data

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
