import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PatrolNode(Node):
    def __init__(self):
        super().__init__('patrol_node')
        
        # TODO: Create a publisher for '/goal_pose' (Type: PoseStamped)
        
        # TODO: Define a list of at least 3 waypoints as (x, y) tuples
        self.waypoints = [] 
        self.current_index = 0
        
        # TODO: Create a timer to call 'timer_callback' every 5.0 seconds
    
    def timer_callback(self):
        # TODO: Check if we have reached the end of the waypoint list
        
        # TODO: Create a PoseStamped message
        msg = PoseStamped()
        
        # TODO: Set the header (stamp and frame_id must be 'map')
        
        # TODO: Set the position (x, y) from the current waypoint
        # Note: Set orientation.w to 1.0 to ensure a valid quaternion
        
        # TODO: Publish the message and increment the index
        self.get_logger().info(f'Publishing waypoint {self.current_index}')

def main(args=None):
    rclpy.init(args=args)
    node = PatrolNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()