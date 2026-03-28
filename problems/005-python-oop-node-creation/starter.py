import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class OOPNode(Node):
    def __init__(self, node_name='oop_node'):
        # TODO: Initialize parent class
        # TODO: Create publisher
        # TODO: Create timer
        self.counter = 0
        
    def publish_message(self):
        # TODO: Increment counter
        # TODO: Create and publish message
        pass

def main(args=None):
    rclpy.init(args=args)
    node = OOPNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()