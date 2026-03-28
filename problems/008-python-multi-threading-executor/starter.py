import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import time

class NodeA(Node):
    def __init__(self):
        super().__init__('node_a')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('node_a is running')

class NodeB(Node):
    def __init__(self):
        super().__init__('node_b')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('node_b is running')

def main(args=None):
    rclpy.init(args=args)
    
    # TODO: Instantiate both NodeA and NodeB
    # TODO: Create a MultiThreadedExecutor
    # TODO: Add both nodes to the executor
    # TODO: Spin the executor
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()