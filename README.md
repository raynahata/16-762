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

   








