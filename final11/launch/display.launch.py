'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-08-14 03:55:03
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-08-14 04:47:56
FilePath: \final11\launch\display.launch.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Define the path to the URDF file
    urdf_path = os.path.join(
        get_package_share_directory('Building_Robot'),
        'urdf',
        'Building_Robot.urdf')

    # Define the path to the RViz configuration file
    rviz_config_path = os.path.join(
        get_package_share_directory('Building_Robot'),
        'urdf.rviz') # Assuming the file is named urdf.rviz

    # Read the URDF file content
    with open(urdf_path, 'r') as file:
        robot_description_content = file.read()

    return LaunchDescription([
        # robot_state_publisher node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_content}]
        ),

        # joint_state_publisher_gui node
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),

        # RViz node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]
        )
    ])