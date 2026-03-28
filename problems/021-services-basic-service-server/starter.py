import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
# TODO: Import appropriate service type if different

class MyServiceServer(Node):
    def __init__(self):
        super().__init__('my_service_server')
        
        # TODO: Create service server
        # self.srv = self.create_service(
        #     ServiceType,
        #     'service_name',
        #     self.service_callback
        # )
        
        self.get_logger().info('Service server ready')
    
    def service_callback(self, request, response):
        """Handle incoming service requests."""
        # TODO: Implement service logic
        # Process request and populate response
        
        self.get_logger().info(f'Received request: {request}')
        
        # TODO: Set response fields
        # response.result = ...
        
        return response

def main(args=None):
    rclpy.init(args=args)
    node = MyServiceServer()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
