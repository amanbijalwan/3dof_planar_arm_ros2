cmake_minimum_required(VERSION 3.5)
project(my_3dof_arm)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

# Install URDF/Xacro files
install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}/
)

install(PROGRAMS
  scripts/arm_fk_pub.py
  DESTINATION lib/${PROJECT_NAME}
)


ament_package()
