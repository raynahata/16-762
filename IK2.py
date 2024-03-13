Last login: Wed Mar  6 16:13:37 on ttys001
(base) raynahata@raynas-mbp ~ %  ssh -X  hello-robot@172.26.171.22 

hello-robot@172.26.171.22's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-173-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

Expanded Security Maintenance for Applications is not enabled.

43 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

Last login: Mon Feb 26 16:47:51 2024 from 172.26.71.37
hello-robot@stretch-re1-1076:~$ stretch_home.py
stretch_home.py: command not found
hello-robot@stretch-re1-1076:~$ stretch_robot_home.py
For use with S T R E T C H (R) RESEARCH EDITION from Hello Robot Inc.
---------------------------------------------------------------------

[ERROR] [head]: SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_pan]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_tilt]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
--------- Homing Head ----
--------- Homing Lift ----
Homing Lift...
Hardstop detected at motor position (rad) 109.52464294433594
Marking Lift position to 1.099175 (m)
Marking Lift position to 0.000000 (m)
[INFO] [robot_monitor]: Guarded contact lift
[INFO] [robot_monitor]: Base bump event
[INFO] [robot_monitor]: Base bump event
Lift homing successful
--------- Homing Arm ----
Homing Arm...
Hardstop detected at motor position (rad) 0.051312681287527084
Marking Arm position to 0.000000 (m)
[INFO] [robot_monitor]: Guarded contact arm
Arm homing successful
--------- Homing stretch_gripper ----
Moving to first hardstop...
First hardstop contact at position (ticks): -13
-----
Homing offset was 5484
Marking current position to zero ticks
Homing offset is now  5493 (ticks)
-----
Current position (ticks): 98
Moving to calibrated zero: (rad)
--------- Homing wrist_yaw ----
Moving to first hardstop...
First hardstop contact at position (ticks): -4
-----
Homing offset was -653
Marking current position to zero ticks
Homing offset is now  -680 (ticks)
-----
Current position (ticks): 97
Moving to calibrated zero: (rad)
hello-robot@stretch-re1-1076:~$ ls
catkin_ws  Downloads    mm2024    Public  stretch_install  Videos
Desktop    gpd          Music     repos   stretch_user
Documents  grocery_bot  Pictures  snap    Templates
hello-robot@stretch-re1-1076:~$ cd desktop 
-bash: cd: desktop: No such file or directory
hello-robot@stretch-re1-1076:~$ cd Desktop
hello-robot@stretch-re1-1076:~/Desktop$ ls
ShoppingCart
hello-robot@stretch-re1-1076:~/Desktop$ cd ShoppingCart
hello-robot@stretch-re1-1076:~/Desktop/ShoppingCart$ ls
pointcloud.py  rgb.py
hello-robot@stretch-re1-1076:~/Desktop/ShoppingCart$ cd
hello-robot@stretch-re1-1076:~$ cd repos
hello-robot@stretch-re1-1076:~/repos$ ls
hello-robot@stretch-re1-1076:~/repos$ cd grocery_bot.py
-bash: cd: grocery_bot.py: No such file or directory
hello-robot@stretch-re1-1076:~/repos$ cd
hello-robot@stretch-re1-1076:~$ cd grocery_bot.py
-bash: cd: grocery_bot.py: No such file or directory
hello-robot@stretch-re1-1076:~$ cd grocery_bot
hello-robot@stretch-re1-1076:~/grocery_bot$ ls
catkin_ws  IK.py  README.md
hello-robot@stretch-re1-1076:~/grocery_bot$ ll
total 28
drwxrwxr-x  4 hello-robot hello-robot 4096 Feb 28 16:37 ./
drwxr-xr-x 33 hello-robot hello-robot 4096 Mar 10 17:43 ../
drwxr-xr-x  5 hello-robot hello-robot 4096 Mar 10 17:50 catkin_ws/
drwxrwxr-x  8 hello-robot hello-robot 4096 Mar  6 17:35 .git/
-rw-rw-r--  1 hello-robot hello-robot 7767 Mar 10 17:28 IK.py
-rw-rw-r--  1 hello-robot hello-robot   20 Feb 28 16:38 README.md
hello-robot@stretch-re1-1076:~/grocery_bot$ git push 
Username for 'https://github.com': raynahata
Password for 'https://raynahata@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/raynahata/16-762.git/'
hello-robot@stretch-re1-1076:~/grocery_bot$ git push 
Username for 'https://github.com': raynahata
Password for 'https://raynahata@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/raynahata/16-762.git/'
hello-robot@stretch-re1-1076:~/grocery_bot$ git push 
Username for 'https://github.com': raynahata
Password for 'https://raynahata@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/raynahata/16-762.git/'
hello-robot@stretch-re1-1076:~/grocery_bot$ giut

Command 'giut' not found, did you mean:

  command 'git' from deb git (1:2.25.1-1ubuntu3.11)
  command 'gift' from deb gnuift (0.1.14+ds-1ubuntu1)
  command 'gout' from deb scotch (6.0.9-1)
  command 'gist' from deb yorick (2.2.04+dfsg1-10)

Try: sudo apt install <deb name>

hello-robot@stretch-re1-1076:~/grocery_bot$ git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local branch
   push              Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
hello-robot@stretch-re1-1076:~/grocery_bot$ git commit
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
  (commit or discard the untracked or modified content in submodules)
	modified:   IK.py
	modified:   catkin_ws/build/CMakeCache.txt
	modified:   catkin_ws/build/CMakeFiles/CMakeRuleHashes.txt
	modified:   catkin_ws/build/CMakeFiles/Makefile.cmake
	modified:   catkin_ws/build/CMakeFiles/Makefile2
	modified:   catkin_ws/build/CMakeFiles/TargetDirectories.txt
	modified:   catkin_ws/build/Makefile
	modified:   catkin_ws/build/atomic_configure/_setup_util.py
	modified:   catkin_ws/build/catkin_generated/generate_cached_setup.py
	modified:   catkin_ws/build/catkin_generated/installspace/_setup_util.py
	modified:   catkin_ws/build/catkin_generated/order_packages.cmake
	modified:   catkin_ws/build/catkin_generated/order_packages.py
	modified:   catkin_ws/build/catkin_generated/stamps/Project/_setup_util.py.stamp
	modified:   catkin_ws/build/catkin_make.cache
	modified:   catkin_ws/build/cmake_install.cmake
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/CMakeFiles/progress.marks
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera.dir/progress.make
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera_generate_messages_cpp.dir/progress.make
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera_generate_messages_eus.dir/progress.make
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera_generate_messages_lisp.dir/progress.make
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera_generate_messages_nodejs.dir/progress.make
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/CMakeFiles/realsense2_camera_generate_messages_py.dir/progress.make
	modified:   catkin_ws/build/realsense-ros/realsense2_camera/catkin_generated/installspace/realsense2_cameraConfig.cmake
	modified:   catkin_ws/build/realsense-ros/realsense2_description/catkin_generated/installspace/realsense2_descriptionConfig.cmake
	modified:   catkin_ws/build/realsense_gazebo_plugin/CMakeFiles/realsense_gazebo_plugin.dir/progress.make
	modified:   catkin_ws/build/realsense_gazebo_plugin/catkin_generated/installspace/realsense_gazebo_pluginConfig.cmake
	modified:   catkin_ws/build/respeaker_ros/CMakeFiles/progress.marks
	modified:   catkin_ws/build/respeaker_ros/CMakeFiles/respeaker_ros_gencfg.dir/progress.make
	modified:   catkin_ws/build/respeaker_ros/catkin_generated/installspace/respeaker_rosConfig.cmake
	modified:   catkin_ws/build/stretch_ros/hello_helpers/catkin_generated/installspace/hello_helpersConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_calibration/catkin_generated/installspace/stretch_calibrationConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_core/catkin_generated/installspace/stretch_coreConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_dashboard/catkin_generated/installspace/stretch_dashboardConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_deep_perception/catkin_generated/installspace/stretch_deep_perceptionConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_ArucoHeadScanAction.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_ArucoHeadScanActionFeedback.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_ArucoHeadScanActionGoal.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_ArucoHeadScanActionResult.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_VisualServoAction.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_VisualServoActionFeedback.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_VisualServoActionGoal.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/_stretch_demos_generate_messages_check_deps_VisualServoActionResult.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/progress.marks
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_cpp.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_cpp.dir/progress.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_eus.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_eus.dir/progress.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_lisp.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_lisp.dir/progress.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_nodejs.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_nodejs.dir/progress.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_py.dir/build.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/CMakeFiles/stretch_demos_generate_messages_py.dir/progress.make
	modified:   catkin_ws/build/stretch_ros/stretch_demos/catkin_generated/installspace/stretch_demosConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_demos/cmake/stretch_demos-genmsg.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_description/catkin_generated/installspace/stretch_descriptionConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_funmap/catkin_generated/installspace/stretch_funmapConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_gazebo/catkin_generated/installspace/stretch_gazeboConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_navigation/catkin_generated/installspace/stretch_navigationConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_octomap/catkin_generated/installspace/stretch_octomapConfig.cmake
	modified:   catkin_ws/build/stretch_ros/stretch_rtabmap/catkin_generated/installspace/stretch_rtabmapConfig.cmake
	modified:   catkin_ws/devel/_setup_util.py
	modified:   catkin_ws/devel/share/hello_helpers/cmake/hello_helpersConfig.cmake
	modified:   catkin_ws/devel/share/pointcloud_processor/cmake/pointcloud_processorConfig.cmake
	modified:   catkin_ws/devel/share/realsense2_camera/cmake/realsense2_cameraConfig.cmake
	modified:   catkin_ws/devel/share/realsense2_description/cmake/realsense2_descriptionConfig.cmake
	modified:   catkin_ws/devel/share/realsense_gazebo_plugin/cmake/realsense_gazebo_pluginConfig.cmake
	modified:   catkin_ws/devel/share/respeaker_ros/cmake/respeaker_rosConfig.cmake
	modified:   catkin_ws/devel/share/stretch_calibration/cmake/stretch_calibrationConfig.cmake
	modified:   catkin_ws/devel/share/stretch_core/cmake/stretch_coreConfig.cmake
	modified:   catkin_ws/devel/share/stretch_dashboard/cmake/stretch_dashboardConfig.cmake
	modified:   catkin_ws/devel/share/stretch_deep_perception/cmake/stretch_deep_perceptionConfig.cmake
	modified:   catkin_ws/devel/share/stretch_demos/cmake/stretch_demosConfig.cmake
	modified:   catkin_ws/devel/share/stretch_description/cmake/stretch_descriptionConfig.cmake
	modified:   catkin_ws/devel/share/stretch_funmap/cmake/stretch_funmapConfig.cmake
	modified:   catkin_ws/devel/share/stretch_gazebo/cmake/stretch_gazeboConfig.cmake
	modified:   catkin_ws/devel/share/stretch_navigation/cmake/stretch_navigationConfig.cmake
	modified:   catkin_ws/devel/share/stretch_octomap/cmake/stretch_octomapConfig.cmake
	modified:   catkin_ws/devel/share/stretch_rtabmap/cmake/stretch_rtabmapConfig.cmake
	deleted:    catkin_ws/src/pointcloud_processor/CMakeLists.txt
	deleted:    catkin_ws/src/pointcloud_processor/package.xml
	deleted:    catkin_ws/src/pointcloud_processor/src/point_cloud_processor.py
	modified:   catkin_ws/src/stretch_ros (modified content)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	catkin_ws/build/gpd_ros/
	catkin_ws/build/manipulation/
	catkin_ws/devel/include/gpd_ros/
	catkin_ws/devel/lib/gpd_ros/
	catkin_ws/devel/lib/libgpd_ros_grasp_messages.so
	catkin_ws/devel/lib/libgpd_ros_grasp_plotter.so
	catkin_ws/devel/lib/pkgconfig/gpd_ros.pc
	catkin_ws/devel/lib/python3/dist-packages/gpd_ros/
	catkin_ws/devel/share/common-lisp/ros/gpd_ros/
	catkin_ws/devel/share/gennodejs/ros/gpd_ros/
	catkin_ws/devel/share/gpd_ros/
	catkin_ws/devel/share/roseus/ros/gpd_ros/
	catkin_ws/src/gpd_ros/
	catkin_ws/src/manipulation/

no changes added to commit (use "git add" and/or "git commit -a")
hello-robot@stretch-re1-1076:~/grocery_bot$ git push 
Username for 'https://github.com': raynahata 
Password for 'https://raynahata@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/raynahata/16-762.git/'
hello-robot@stretch-re1-1076:~/grocery_bot$ ls
catkin_ws  IK.py  README.md
hello-robot@stretch-re1-1076:~/grocery_bot$ vim IK>py
Vim: Warning: Output is not to a terminal
hello-robot@stretch-re1-1076:~/grocery_bot$ vim IK.py
hello-robot@stretch-re1-1076:~/grocery_bot$ python3 IK.py
[ERROR] [head]: SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_pan]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_tilt]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
Failed to open connection to the robot
[WARNING] [robot]: is_calibrated() has been replaced by is_homed()
/home/hello-robot/grocery_bot/catkin_ws/src/stretch_ros/stretch_description/urdf/exported_urdf/stretch.urdf
Run: 'roslaunch stretch_description display.launch' to see where the base_link coordinate frame is.
/home/hello-robot/.local/lib/python3.8/site-packages/urdfpy/urdf.py:2169: RuntimeWarning: invalid value encountered in divide
  value = value / np.linalg.norm(value)
name: stretch_description
num links: 11
num joints: 10
name: stretch_description
num links: 12
num joints: 11
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_mast is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_arm_l4 is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_gripper is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_grasp_center is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link Base link (index: 0) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_mast (index: 2) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_arm_l4 (index: 4) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_gripper (index: 10) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_grasp_center (index: 11) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
--------- Stowing Arm ----
--------- Stowing Wrist Yaw ----
--------- Stowing Gripper ----
--------- Stowing Wrist Yaw ----
--------- Stowing Gripper ----
--------- Stowing Lift ----
Solution: [ 0.00000000e+00 -1.77842478e-01 -5.44374664e+03  7.85724996e-01
  1.30408661e+02  6.17700325e-02  6.17700325e-02  6.17700326e-02
  6.17700325e-02  1.55645013e+00  0.00000000e+00  0.00000000e+00]
[[-0.26896735 -0.96297999  0.01805827 -0.08310949]
 [ 0.96306741 -0.26914169 -0.00799513  0.05176118]
 [ 0.01255938  0.01524091  0.99980497  0.24255199]
 [ 0.          0.          0.          1.        ]]
^CCaught signal 2
Exception ignored in: <module 'threading' from '/usr/lib/python3.8/threading.py'>
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 1388, in _shutdown
    lock.acquire()
  File "/home/hello-robot/.local/lib/python3.8/site-packages/stretch_body/hello_utils.py", line 294, in thread_service_shutdown
    raise ThreadServiceExit
stretch_body.hello_utils.ThreadServiceExit: 
Exception in thread NonDXLStatusThread:
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    self.run()
  File "/home/hello-robot/.local/lib/python3.8/site-packages/stretch_body/robot.py", line 115, in run
hello-robot@stretch-re1-1076:~/grocery_bot$ vim IK.py
hello-robot@stretch-re1-1076:~/grocery_bot$ python3 IK.py
[ERROR] [head]: SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_pan]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_tilt]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
Failed to open connection to the robot
[WARNING] [robot]: is_calibrated() has been replaced by is_homed()
/home/hello-robot/grocery_bot/catkin_ws/src/stretch_ros/stretch_description/urdf/exported_urdf/stretch.urdf
Run: 'roslaunch stretch_description display.launch' to see where the base_link coordinate frame is.
/home/hello-robot/.local/lib/python3.8/site-packages/urdfpy/urdf.py:2169: RuntimeWarning: invalid value encountered in divide
  value = value / np.linalg.norm(value)
name: stretch_description
num links: 11
num joints: 10
name: stretch_description
num links: 12
num joints: 11
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_mast is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_arm_l4 is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_gripper is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_grasp_center is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link Base link (index: 0) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_mast (index: 2) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_arm_l4 (index: 4) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_gripper (index: 10) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_grasp_center (index: 11) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
--------- Stowing Arm ----
--------- Stowing Wrist Yaw ----
--------- Stowing Gripper ----
--------- Stowing Wrist Yaw ----
--------- Stowing Gripper ----
--------- Stowing Lift ----
Solution: [ 0.00000000e+00 -1.74047822e-01  2.12685137e+02  7.77038801e-01
  5.97755681e+02  3.72255364e-24  5.33611602e-25  7.23896881e-31
  5.07600357e-24  1.61202870e+00  0.00000000e+00  0.00000000e+00]
IKPy did not find a valid solution
[[-0.26896735 -0.96297999  0.01805827 -0.08310843]
 [ 0.96306741 -0.26914169 -0.00799513  0.05174735]
 [ 0.01255938  0.01524091  0.99980497  0.24240853]
 [ 0.          0.          0.          1.        ]]
^CCaught signal 2
Exception ignored in: <module 'threading' from '/usr/lib/python3.8/threading.py'>
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 1388, in _shutdown
    lock.acquire()
  File "/home/hello-robot/.local/lib/python3.8/site-packages/stretch_body/hello_utils.py", line 294, in thread_service_shutdown
    raise ThreadServiceExit
stretch_body.hello_utils.ThreadServiceExit: 
Exception in thread NonDXLStatusThread:
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
hello-robot@stretch-re1-1076:~/grocery_bot$ stretch_robot_home.py
For use with S T R E T C H (R) RESEARCH EDITION from Hello Robot Inc.
---------------------------------------------------------------------

[ERROR] [head]: SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_pan]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_tilt]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
--------- Homing Head ----
--------- Homing Lift ----
Homing Lift...
Hardstop detected at motor position (rad) 115.35771942138672
Marking Lift position to 1.099175 (m)
Marking Lift position to 0.000000 (m)
[INFO] [robot_monitor]: Guarded contact lift
[INFO] [robot_monitor]: Base bump event
[INFO] [robot_monitor]: Base bump event
Lift homing successful
--------- Homing Arm ----
Homing Arm...
Hardstop detected at motor position (rad) 0.028972463682293892
Marking Arm position to 0.000000 (m)
[INFO] [robot_monitor]: Guarded contact arm
Arm homing successful
--------- Homing stretch_gripper ----
Moving to first hardstop...
First hardstop contact at position (ticks): 9
-----
Homing offset was 5493
Marking current position to zero ticks
Homing offset is now  5478 (ticks)
-----
Current position (ticks): 72
Moving to calibrated zero: (rad)
--------- Homing wrist_yaw ----
Moving to first hardstop...
First hardstop contact at position (ticks): -34
-----
Homing offset was -680
Marking current position to zero ticks
Homing offset is now  -675 (ticks)
-----
Current position (ticks): 96
Moving to calibrated zero: (rad)
hello-robot@stretch-re1-1076:~/grocery_bot$ python3 IK.py
[ERROR] [head]: SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_pan]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
[ERROR] [head_tilt]: Dynamixel SerialException(2): could not open port /dev/hello-dynamixel-head: [Errno 2] No such file or directory: '/dev/hello-dynamixel-head'
Failed to open connection to the robot
[WARNING] [robot]: is_calibrated() has been replaced by is_homed()
/home/hello-robot/grocery_bot/catkin_ws/src/stretch_ros/stretch_description/urdf/exported_urdf/stretch.urdf
Run: 'roslaunch stretch_description display.launch' to see where the base_link coordinate frame is.
/home/hello-robot/.local/lib/python3.8/site-packages/urdfpy/urdf.py:2169: RuntimeWarning: invalid value encountered in divide
  value = value / np.linalg.norm(value)
name: stretch_description
num links: 11
num joints: 10
name: stretch_description
num links: 12
num joints: 11
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_mast is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_arm_l4 is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_gripper is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/urdf/URDF.py:261: UserWarning: Joint joint_grasp_center is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored
  warnings.warn("Joint {} is of type: fixed, but has an 'axis' attribute defined. This is not in the URDF spec and thus this axis is ignored".format(joint.attrib["name"]))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link Base link (index: 0) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_mast (index: 2) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_arm_l4 (index: 4) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_gripper (index: 10) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
/home/hello-robot/.local/lib/python3.8/site-packages/ikpy/chain.py:60: UserWarning: Link joint_grasp_center (index: 11) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive
  warnings.warn("Link {} (index: {}) is of type 'fixed' but set as active in the active_links_mask. In practice, this fixed link doesn't provide any transformation so is as it were inactive".format(link.name, link_index))
--------- Stowing Arm ----
[INFO] [robot_monitor]: Wrist single tap: 3
--------- Stowing Wrist Yaw ----
--------- Stowing Gripper ----
--------- Stowing Wrist Yaw ----
--------- Stowing Gripper ----
--------- Stowing Lift ----
Solution: [ 0.00000000e+00 -1.74047822e-01  6.77398237e+01  7.77038801e-01
  3.27619068e+02  2.02567116e-27  7.10802447e-24  5.22168017e-24
  5.47989203e-24  1.61202870e+00  0.00000000e+00  0.00000000e+00]
IKPy did not find a valid solution
[[-0.26896735 -0.96297999  0.01805827 -0.08310947]
 [ 0.96306741 -0.26914169 -0.00799513  0.05176122]
 [ 0.01255938  0.01524091  0.99980497  0.24254866]
 [ 0.          0.          0.          1.        ]]
^CCaught signal 2
Exception ignored in: <module 'threading' from '/usr/lib/python3.8/threading.py'>
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 1388, in _shutdown
    lock.acquire()
  File "/home/hello-robot/.local/lib/python3.8/site-packages/stretch_body/hello_utils.py", line 294, in thread_service_shutdown
    raise ThreadServiceExit
stretch_body.hello_utils.ThreadServiceExit: 
Exception in thread NonDXLStatusThread:
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
hello-robot@stretch-re1-1076:~/grocery_bot$ vim IK.py

#copy of Inverse Kinematics 

import ikpy.urdf.utils
import pathlib
import stretch_body.hello_utils as hu
import urdfpy
import numpy as np
import ikpy.chain
import stretch_body.robot

# NOTE before running: `python3 -m pip install ikpy graphviz urdfpy`

target_point = [0.0, 0.4, 0.8]
target_orientation = ikpy.utils.geometry.rpy_matrix(0.0, 0.0, 0.0) # [roll, pitch, yaw]
pretarget_orientation = ikpy.utils.geometry.rpy_matrix(0.0, 0.0, np.pi/2)


# Setup the Python API
robot = stretch_body.robot.Robot()
if not robot.startup():
    print("Failed to open connection to the robot")

# Ensure robot is homed
if not robot.is_calibrated():
    robot.home()

urdf_path = "/home/hello-robot/grocery_bot/catkin_ws/src/stretch_ros/stretch_description/urdf/exported_urdf/stretch.urdf"
print(urdf_path)
tree = ikpy.urdf.utils.get_urdf_tree(urdf_path, "base_link")[0]
# display.display_png(tree)
# print(f"Your robot is equipped with the '{robot.end_of_arm.name}' end-effector")

print('Run: \'roslaunch stretch_description display.launch\' to see where the base_link coordinate frame is.')

# Remove unnecessary links/joints
original_urdf = urdfpy.URDF.load(urdf_path)
modified_urdf = original_urdf
names_of_links_to_remove = ['link_right_wheel', 'link_left_wheel', 'caster_link', 'link_gripper_finger_left', 'link_gripper_fingertip_left', 'link_gripper_finger_right', 'link_gripper_fingertip_right', 'link_head', 'link_head_pan', 'link_head_tilt', 'link_aruco_right_base', 'link_aruco_left_base', 'link_aruco_shoulder', 'link_aruco_top_wrist', 'link_aruco_inner_wrist', 'camera_bottom_screw_frame', 'camera_link', 'camera_depth_frame', 'camera_depth_optical_frame', 'camera_infra1_frame', 'camera_infra1_optical_frame', 'camera_infra2_frame', 'camera_infra2_optical_frame', 'camera_color_frame', 'camera_color_optical_frame', 'camera_accel_frame', 'camera_accel_optical_frame', 'camera_gyro_frame', 'camera_gyro_optical_frame', 'laser', 'respeaker_base', 'base_imu']
links_to_remove = [l for l in modified_urdf._links if l.name in names_of_links_to_remove]
for lr in links_to_remove:
    modified_urdf._links.remove(lr)
names_of_joints_to_remove = ['joint_right_wheel', 'joint_left_wheel', 'caster_joint', 'joint_gripper_finger_left', 'joint_gripper_fingertip_left', 'joint_gripper_finger_right', 'joint_gripper_fingertip_right', 'joint_head', 'joint_head_pan', 'joint_head_tilt', 'joint_aruco_right_base', 'joint_aruco_left_base', 'joint_aruco_shoulder', 'joint_aruco_top_wrist', 'joint_aruco_inner_wrist', 'camera_joint', 'camera_link_joint', 'camera_depth_joint', 'camera_depth_optical_joint', 'camera_infra1_joint', 'camera_infra1_optical_joint', 'camera_infra2_joint', 'camera_infra2_optical_joint', 'camera_color_joint', 'camera_color_optical_joint', 'camera_accel_joint', 'camera_accel_optical_joint', 'camera_gyro_joint', 'camera_gyro_optical_joint', 'joint_laser', 'joint_respeaker', 'joint_base_imu']
joints_to_remove = [l for l in modified_urdf._joints if l.name in names_of_joints_to_remove]
for jr in joints_to_remove:
                                                                                                                                       1,21          Top
