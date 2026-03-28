from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # TODO: Declare namespace argument
    
    # TODO: Find package share directory
    # pkg_share = FindPackageShare('other_package')
    
    # TODO: Create path to included launch file
    # launch_file = PathJoinSubstitution([pkg_share, 'launch', 'other.launch.py'])
    
    # TODO: Include launch with parameters
    
    # TODO: Use GroupAction for namespacing
    
    return LaunchDescription([
        # TODO: Add components
    ])