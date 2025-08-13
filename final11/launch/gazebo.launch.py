import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    # Define the path to the robot's URDF file 
    urdf_path = os.path.join(
        get_package_share_directory('Building_Robot'),
        'urdf',
        'Building_Robot.urdf')

    # Read the URDF file content for the spawner
    with open(urdf_path, 'r') as file:
        robot_description_content = file.read()

    # Include the Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch'),
            '/gazebo.launch.py' # Replaces empty_world.launch
        ]),
        launch_arguments={'pause': 'true'}.items() # Start Gazebo paused
    )

    # Robot State Publisher node (required for the spawner)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content}]
    )

    # Gazebo Spawner node
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py', # Replaces the 'spawn_model' script 
        arguments=['-topic', 'robot_description', '-entity', 'Building_Robot'],
        output='screen'
    )

    # Static Transform Publisher node
    static_tf_pub = Node(
        package='tf2_ros', # The 'tf' package is now 'tf2_ros'
        executable='static_transform_publisher',
        name='static_transform_publisher',
        output='screen',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'] # Note: interval is now a parameter
    )

    # A command to publish a topic message
    fake_joint_calibrator = ExecuteProcess(
        cmd=['ros2', 'topic', 'pub', '-1', '/calibrated', 'std_msgs/msg/Bool', '"{data: true}"'],
        shell=True
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher_node,
        spawn_entity,
        static_tf_pub,
        fake_joint_calibrator
    ])