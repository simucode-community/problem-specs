import rclpy
from rclpy.node import Node
import subprocess
import os
import signal

class BagRecorderNode(Node):
    def __init__(self):
        super().__init__('bag_recorder_node')
        
        # Target configuration
        self.bag_name = 'my_bag'
        self.topic_name = '/chatter'
        
        # TODO: Use subprocess.Popen to start 'ros2 bag record'
        # Hint: Use the '-o' flag to specify the bag name
        self.process = None 

        # TODO: Create a timer to stop recording after exactly 5.0 seconds
        self.timer = None

    def stop_recording(self):
        self.get_logger().info('Stopping recording...')
        
        # TODO: Safely terminate the bag recording process
        # Hint: Send signal.SIGINT to the process to allow it to save metadata
        
        # Exit the node
        raise SystemExit

def main(args=None):
    rclpy.init(args=args)
    node = BagRecorderNode()
    try:
        rclpy.spin(node)
    except SystemExit:
        pass 
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()