# 16-762 Mobile Manipulation Spring 2024

## Aruco Tags


### Detect Aruco Tags 
1. roslaunch stretch_core stretch_driver.launch
2. roslaunch stretch_core d435i_low_resolution.launch
3. roslaunch stretch_core stretch_aruco.launch
4. rosrun rviz rviz -d /home/hello-robot/catkin_ws/src/stretch_tutorials/rviz/aruco_detector_example.rviz

### Navstack 
roslaunch stretch_navigation navigation.launch map_yaml:=/home/hello-robot/16-762/maps/team_1_map3.yaml

### Base Alignment 
rosservice call /align_base "location: 'drop_off'"


## Running just navigation 
1. roslaunch stretch_navigation navigation.launch map_yaml:=/home/hello-robot/16-762/maps/team_1_map3.yaml
2. roslaunch stretch_core d435i_low_resolution.launch
3. python3 base_aligner.py

## Running with the object pickup 
1. roslaunch stretch_navigation navigation.launch map_yaml:=/home/hello-robot/16-762/maps/team_1_map3.yaml
2. roslaunch stretch_core d435i_low_resolution.launch
3. process_pcl.py (in manipulation folder)
4. owlnode.py (in manipulation folder)
5. Roslaunch ur5.launch (in gpd_ros folder)
6. rosrun move_robot_ros_service.py (in manipulation folder)
7. rosservice call /execute_multipoint_command "location: 'pick_up' item: 'spray bottle'"






   








