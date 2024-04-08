execute_process(COMMAND "/home/hello-robot/16-762/catkin_ws/build/stretch_ros/stretch_funmap/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/hello-robot/16-762/catkin_ws/build/stretch_ros/stretch_funmap/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
