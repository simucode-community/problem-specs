import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class DeadlineDemo(Node):
    def __init__(self):
        super().__init__('deadline_demo')
        # TODO: Create QoS with deadline=0.1, lifespan=0.5
        # TODO: Publish slower than deadline and log missed deadlines
        pass

def main(args=None):
    rclpy.init(args=args)
    node = DeadlineDemo()
    rclpy.shutdown()