import rclpy
from rclpy.node import Node
from typing import Optional

class TypedNode(Node):
    def __init__(self) -> None:
        super().__init__('typed_node')
        # TODO: Demonstrate all logging levels
        # TODO: Use type hints for variables
        self.message_count: int = 0
        
    def process_data(self, data: str) -> Optional[str]:
        # TODO: Add type-safe data processing
        # TODO: Use appropriate logging
        pass

def main(args=None) -> None:
    rclpy.init(args=args)
    node = TypedNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()