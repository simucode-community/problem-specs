import rclpy
from rclpy.node import Node
import xml.etree.ElementTree as ET

class URDFLoaderNode(Node):
    def __init__(self):
        super().__init__('urdf_loader_node')
        
        # TODO: Define your URDF XML string here
        self.urdf_xml = """
<robot name="simple_arm">
  <!-- TODO: Add base_link, arm_link, and shoulder_joint -->
</robot>
"""
        
        # TODO: Declare and get 'robot_description' parameter
        
        try:
            # TODO: Parse the URDF using ET.fromstring()
            # root = ET.fromstring(...)
            
            # TODO: Validate links are found
            # links = root.findall('link')
            
            # Requirement: Success log (MUST MATCH THIS EXACT STRING)
            self.get_logger().info('URDF parsed successfully')
            
        except Exception as e:
            self.get_logger().error(f'Failed to parse URDF: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = URDFLoaderNode()
    
    # Spin once to process logs
    rclpy.spin_once(node, timeout_sec=0.1)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()