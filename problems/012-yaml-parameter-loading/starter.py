import rclpy
from rclpy.node import Node

class YAMLConfigNode(Node):
    def __init__(self):
        super().__init__('yaml_config_node')
        # TODO: Declare parameters with defaults
        # Parameters: max_speed, robot_name, enable_debug
        
        # TODO: Get parameter values
        # TODO: Log all loaded parameters
        pass

def main(args=None):
    rclpy.init(args=args)
    node = YAMLConfigNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# Example YAML file content:
# /**:
#   ros__parameters:
#     max_speed: 1.5
#     robot_name: "my_robot"
#     enable_debug: true