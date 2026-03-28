from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    """
    Create a conditional launch file.
    
    Requirements:
    1. Declare 'use_rviz' argument (default: 'true')
    2. Declare 'use_gazebo' argument (default: 'false')
    3. Create RViz node (package='rviz2', executable='rviz2') with IfCondition(use_rviz)
    4. Create Gazebo node (package='gazebo_ros', executable='gazebo') with IfCondition(use_gazebo)
    5. Create main node (package='my_package', executable='my_node')
    
    Note: Don't worry about package availability - the test environment uses mocks.
    """
    
    # TODO: Declare 'use_rviz' argument (default: 'true')
    
    # TODO: Declare 'use_gazebo' argument (default: 'false')
    
    # TODO: Get LaunchConfiguration values
    
    # TODO: Create RViz node with IfCondition
    # Node(package='rviz2', executable='rviz2', condition=IfCondition(...))
    
    # TODO: Create Gazebo node with IfCondition
    # Node(package='gazebo_ros', executable='gazebo', condition=IfCondition(...))
    
    # TODO: Create main node (always runs)
    # Node(package='my_package', executable='my_node')
    
    return LaunchDescription([
        # TODO: Add all arguments and nodes
    ])
