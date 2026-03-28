import rclpy
from rclpy.node import Node
import os # UNUSED IMPORT
from std_msgs.msg import String
import sys # UNUSED IMPORT

class well_documented_node(Node): # WRONG NAMING (Should be PascalCase)
  def __init__(self):
    super().__init__('quality_node')
    self.MyCounter = 0 # WRONG NAMING (Should be snake_case)
    # TODO: Fix indentation, naming, and remove unused imports
    # TODO: Add Docstrings
    self.create_timer(1.0, self.TimerCallback)

  def TimerCallback(self): # WRONG NAMING
    msg = String()
    msg.data = 'Counting: ' + str(self.MyCounter)
    self.get_logger().info(msg.data)
    self.MyCounter += 1

def main(args=None):
    rclpy.init(args=args)
    node = well_documented_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()