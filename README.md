# 3dof_planar_arm_ros2
### 3-DOF Arm RViz2
3dof planar robotic arm to test with ros2, rviz, moveit2.

Currently the implementation can be tested with Rviz2, we can use standard joint state publisher to drive robot in FK.
<img width="1203" height="870" alt="image" src="https://github.com/user-attachments/assets/3da21bb0-3d8f-48ff-9459-8f1da4b89de2" />

This project demonstrates a simple 3-DOF planar robotic arm in ROS2, visualized in RViz, with an interactive inverse kinematics (IK) slider GUI.

### Update
Robot model updated to SCARA type in 3dof configuration, in same file.
<img width="1195" height="783" alt="image" src="https://github.com/user-attachments/assets/1bd502b7-3dd9-44db-951f-eb2f1fabd1b1" />


## Components
- **URDF/Xacro**: Defines the arm links and joints.
- **robot_state_publisher**: Publishes transforms from the URDF.
- **joint_state_publisher_gui**: (optional) for manual joint sliders.
- **RViz**: Displays the robot model and updates with transforms.

## Usage

1. Build and source:
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select my_3dof_arm
   source install/setup.bash

