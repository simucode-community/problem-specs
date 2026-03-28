import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
import time

class LatencyMeasurer(Node):
    """
    TODO: Implement a tool that measures round-trip latency.
    
    Requirements:
    1. Publish messages with current timestamp to '/ping'
    2. Listen for echoed messages on '/echo' (assume another node echoes them)
    3. Calculate and log the round-trip latency
    """
    
    def __init__(self):
        super().__init__('latency_measurer')
        
        # TODO: Create publisher and subscription
        # self.pub = self.create_publisher(...)
        # self.sub = self.create_subscription(...)
        
        # TODO: Create timer to send pings periodically
        pass
    
    def send_ping(self):
        """Send a message with current timestamp."""
        # TODO: Construct message with header stamp = self.get_clock().now()
        # TODO: Publish
        pass
        
    def echo_callback(self, msg):
        """Receive echo and calculate latency."""
        # TODO: Get current time
        # TODO: Calculate difference from msg.stamp
        # TODO: Log latency (ms or us)
        pass

def main(args=None):
    rclpy.init(args=args)
    node = LatencyMeasurer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
