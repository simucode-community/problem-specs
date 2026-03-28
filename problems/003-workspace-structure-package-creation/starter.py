import rclpy
from rclpy.node import Node

class MyPackageNode(Node):
    def __init__(self):
        super().__init__('my_package_node')
        # TODO: Add node initialization
        # TODO: Log package name and node name
        
def main(args=None):
    rclpy.init(args=args)
    # TODO: Create node instance
    # TODO: Spin the node
    # TODO: Cleanup
    pass

if __name__ == '__main__':
    main()