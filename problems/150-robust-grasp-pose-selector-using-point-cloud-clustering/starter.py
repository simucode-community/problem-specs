import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        
        # TODO: Create publishers
        self.publisher = self.create_publisher(String, '/output_topic', 10)
        
        # TODO: Create subscribers
        self.subscription = self.create_subscription(
            String,
            '/input_topic',
            self.listener_callback,
            10
        )
        
        # TODO: Create timer
        self.timer = self.create_timer(1.0, self.timer_callback)
        
        self.get_logger().info('Node initialized')
    
    def listener_callback(self, msg):
        """Handle incoming messages."""
        self.get_logger().info(f'Received: {msg.data}')
        
        # TODO: Process message
    
    def timer_callback(self):
        """Periodic callback."""
        msg = String()
        msg.data = 'Hello from timer!'
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
