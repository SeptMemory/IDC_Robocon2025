cmake_minimum_required(VERSION 3.8)

project(Building_Robot)

# Find necessary ROS2 packages
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED) # If you have messages/services
find_package(robot_state_publisher REQUIRED)
find_package(joint_state_publisher_gui REQUIRED)
find_package(rviz2 REQUIRED)

# Add custom message/service/action generators if needed
# rosidl_generate_interfaces(Building_Robot
#   "msg/MyMessage.msg"
# )

# Ament package registration
ament_package()

# Installation rules for resource files
install(DIRECTORY
  config
  launch
  meshes
  urdf
  DESTINATION share/${PROJECT_NAME}
)