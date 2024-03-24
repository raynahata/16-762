# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "manipulation: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(manipulation_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



<<<<<<< HEAD
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv" NAME_WE)
add_custom_target(_manipulation_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "manipulation" "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv" ""
=======
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv" NAME_WE)
add_custom_target(_manipulation_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "manipulation" "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv" ""
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(manipulation
<<<<<<< HEAD
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv"
=======
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv"
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/manipulation
)

### Generating Module File
_generate_module_cpp(manipulation
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/manipulation
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(manipulation_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(manipulation_generate_messages manipulation_generate_messages_cpp)

# add dependencies to all check dependencies targets
<<<<<<< HEAD
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv" NAME_WE)
=======
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv" NAME_WE)
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
add_dependencies(manipulation_generate_messages_cpp _manipulation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(manipulation_gencpp)
add_dependencies(manipulation_gencpp manipulation_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS manipulation_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(manipulation
<<<<<<< HEAD
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv"
=======
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv"
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/manipulation
)

### Generating Module File
_generate_module_eus(manipulation
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/manipulation
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(manipulation_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(manipulation_generate_messages manipulation_generate_messages_eus)

# add dependencies to all check dependencies targets
<<<<<<< HEAD
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv" NAME_WE)
=======
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv" NAME_WE)
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
add_dependencies(manipulation_generate_messages_eus _manipulation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(manipulation_geneus)
add_dependencies(manipulation_geneus manipulation_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS manipulation_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(manipulation
<<<<<<< HEAD
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv"
=======
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv"
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/manipulation
)

### Generating Module File
_generate_module_lisp(manipulation
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/manipulation
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(manipulation_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(manipulation_generate_messages manipulation_generate_messages_lisp)

# add dependencies to all check dependencies targets
<<<<<<< HEAD
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv" NAME_WE)
=======
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv" NAME_WE)
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
add_dependencies(manipulation_generate_messages_lisp _manipulation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(manipulation_genlisp)
add_dependencies(manipulation_genlisp manipulation_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS manipulation_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(manipulation
<<<<<<< HEAD
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv"
=======
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv"
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/manipulation
)

### Generating Module File
_generate_module_nodejs(manipulation
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/manipulation
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(manipulation_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(manipulation_generate_messages manipulation_generate_messages_nodejs)

# add dependencies to all check dependencies targets
<<<<<<< HEAD
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv" NAME_WE)
=======
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv" NAME_WE)
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
add_dependencies(manipulation_generate_messages_nodejs _manipulation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(manipulation_gennodejs)
add_dependencies(manipulation_gennodejs manipulation_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS manipulation_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(manipulation
<<<<<<< HEAD
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv"
=======
  "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv"
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/manipulation
)

### Generating Module File
_generate_module_py(manipulation
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/manipulation
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(manipulation_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(manipulation_generate_messages manipulation_generate_messages_py)

# add dependencies to all check dependencies targets
<<<<<<< HEAD
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/AlignBase.srv" NAME_WE)
=======
get_filename_component(_filename "/home/hello-robot/grocery_bot/catkin_ws/src/manipulation/srv/ExecuteCommand.srv" NAME_WE)
>>>>>>> 0175771262e24e6499a87be41a07a53cb829079b
add_dependencies(manipulation_generate_messages_py _manipulation_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(manipulation_genpy)
add_dependencies(manipulation_genpy manipulation_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS manipulation_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/manipulation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/manipulation
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(manipulation_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/manipulation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/manipulation
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(manipulation_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/manipulation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/manipulation
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(manipulation_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/manipulation)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/manipulation
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(manipulation_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/manipulation)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/manipulation\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/manipulation
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(manipulation_generate_messages_py std_msgs_generate_messages_py)
endif()
