import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class DynamicFramePublisher(Node):
    def __init__(self):
        super().__init__('dynamic_broadcaster')

        # 1. Create a TransformBroadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

        # 2. Initialize angle for circular path
        self.angle = 0.0

        # 3. Create a timer that calls broadcast_transform at 10 Hz
        # TODO: Create timer with period 0.1 second calling self.broadcast_transform
        

    def broadcast_transform(self):
        t = TransformStamped()

        # 4. Set header - use current time and 'odom' as frame_id
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        # 5. Calculate x, y position on a circular path (radius = 2.0 m)
        # TODO: Calculate x using cos(self.angle) and y using sin(self.angle)
        t.transform.translation.x = 0.0  # Replace with circular path calculation
        t.transform.translation.y = 0.0  # Replace with circular path calculation
        t.transform.translation.z = 0.0

        # 6. Set rotation (identity quaternion - no rotation)
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        # 7. Send the transform
        # TODO: Call self.tf_broadcaster.sendTransform(t)

        # 8. Update angle for next iteration (increment by 0.1 radians)
        # TODO: Update self.angle

def main(args=None):
    rclpy.init(args=args)
    node = DynamicFramePublisher()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
