import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from std_msgs.msg import String

class QoSNode(Node):
    def __init__(self):
        super().__init__('qos_node')
        
        # TODO: Create QoS profile with RELIABLE reliability
        reliable_qos = QoSProfile(
            # TODO: Set reliability to RELIABLE
            # TODO: Set history to KEEP_LAST with depth 10
            # TODO: Set durability to VOLATILE
        )
        
        # TODO: Create QoS profile with BEST_EFFORT reliability
        best_effort_qos = QoSProfile(
            # TODO: Set reliability to BEST_EFFORT
        )
        
        # TODO: Create publishers with different QoS
        # TODO: Create subscribers with matching QoS
        
def main(args=None):
    rclpy.init(args=args)
    node = QoSNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()