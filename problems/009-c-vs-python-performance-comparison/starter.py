import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
import time

class HighFrequencyPublisher(Node):
    def __init__(self):
        super().__init__('high_frequency_publisher')
        # TODO: Create publisher for 'counter_topic'
        # TODO: Create timer at 100 Hz (0.01 seconds)
        self.counter = 0
        self.last_time = time.time()
        
    def timer_callback(self):
        # TODO: Increment self.counter
        # TODO: Publish counter message
        
        # TODO: Log performance every 100 messages
        # Note: Use self.get_logger().info() or print(..., flush=True)
        # Example: 
        # if self.counter % 100 == 0:
        #     now = time.time()
        #     self.get_logger().info(f"Avg Frequency: {100 / (now - self.last_time):.2f} Hz")
        #     self.last_time = now
        pass

def main(args=None):
    rclpy.init(args=args)
    node = HighFrequencyPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()