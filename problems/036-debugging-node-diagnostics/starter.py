import rclpy
from rclpy.node import Node
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue

class DiagnosticNode(Node):
    def __init__(self):
        super().__init__('diagnostic_node')
        
        # TODO: Create publisher for /diagnostics
        self.diag_pub = self.create_publisher(DiagnosticArray, '/diagnostics', 10)
        
        # TODO: Create timer for diagnostics update
        self.timer = self.create_timer(1.0, self.publish_diagnostics)
        
        self.message_count = 0
        
    def publish_diagnostics(self):
        # TODO: Create DiagnosticArray
        # TODO: Create DiagnosticStatus
        # TODO: Set level (OK, WARN, ERROR)
        # TODO: Add key-value pairs
        # TODO: Publish diagnostics
        
        self.message_count += 1
        pass

def main(args=None):
    rclpy.init(args=args)
    node = DiagnosticNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()