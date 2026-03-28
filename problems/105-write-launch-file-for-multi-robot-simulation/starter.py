from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """
    TODO: Create a LaunchDescription that starts two nodes.
    
    Requirements:
    1. Start a 'turtlesim_node' (package: turtlesim, executable: turtlesim_node)
    2. Namespace it as '/robot1'
    3. Start another 'turtlesim_node'
    4. Namespace it as '/robot2'
    """
    
    return LaunchDescription([
        # TODO: Define Node 1
        # Node(
        #     package='turtlesim',
        #     executable='turtlesim_node',
        #     namespace='/robot1',
        #     name='sim'
        # ),
        
        # TODO: Define Node 2
        
    ])
