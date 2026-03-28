import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity
from geometry_msgs.msg import Pose

class GazeboSpawner(Node):
    def __init__(self):
        super().__init__('gazebo_spawner')

        # 1. Create a service client for /spawn_entity
        # TODO: Create client using self.create_client(SpawnEntity, '/spawn_entity')
        self.client = None  # Replace with service client

        # 2. Wait for the service to become available
        # TODO: Use self.client.wait_for_service(timeout_sec=1.0) in a loop

        # 3. Call the spawn function
        self.spawn_robot()

    def spawn_robot(self):
        request = SpawnEntity.Request()

        # 4. Set the entity name
        # TODO: Set request.name to 'my_robot'
        request.name = ''

        # 5. Set a simple URDF as the robot XML
        request.xml = '''<?xml version="1.0"?>
<robot name="my_robot">
  <link name="base_link">
    <visual>
      <geometry><box size="0.5 0.5 0.5"/></geometry>
    </visual>
  </link>
</robot>'''

        # 6. Set initial pose (x=0, y=0, z=1)
        pose = Pose()
        # TODO: Set pose.position.z = 1.0
        request.initial_pose = pose

        # 7. Call the service asynchronously
        # TODO: Use self.client.call_async(request) and add_done_callback
        

    def spawn_done_callback(self, future):
        response = future.result()
        if response.success:
            self.get_logger().info('Robot spawned successfully!')
        else:
            self.get_logger().error(f'Spawn failed: {response.status_message}')

def main(args=None):
    rclpy.init(args=args)
    node = GazeboSpawner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
