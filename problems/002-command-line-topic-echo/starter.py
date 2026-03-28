import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TopicEcho(Node):
    def __init__(self):
        super().__init__('topic_echo')
        # TODO: Create subscriber to /input
        
    def listener_callback(self, msg):
        # TODO: Log the received message
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TopicEcho()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()