execute_process(COMMAND "/home/hello-robot/grocery_bot/catkin_ws/build/stretch_ros/hello_helpers/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/hello-robot/grocery_bot/catkin_ws/build/stretch_ros/hello_helpers/catkin_generated/python_distutils_install.sh) returned error code ")
endif()