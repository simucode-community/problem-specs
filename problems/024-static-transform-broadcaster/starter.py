import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped

class StaticFramePublisher(Node):
    def __init__(self):
        super().__init__('static_transform_broadcaster')

        # TODO: Create a StaticTransformBroadcaster
        # self.tf_static_broadcaster = ...

        # TODO: Call your publish method here
        # self.publish_static_transform()

    def publish_static_transform(self):
        """Publish a static transform from 'world' to 'robot_base'."""
        t = TransformStamped()

        # TODO: Set the header timestamp using self.get_clock().now().to_msg()

        # TODO: Set the parent frame (frame_id) and child frame (child_frame_id)

        # TODO: Set translation values (x=1.0, y=2.0, z=0.5)

        # TODO: Set rotation using a quaternion (x, y, z, w)
        # Hint: for no rotation, use w=1.0 and x=y=z=0.0

        # TODO: Send the transform using self.tf_static_broadcaster.sendTransform(t)
        pass

def main(args=None):
    rclpy.init(args=args)
    node = StaticFramePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
