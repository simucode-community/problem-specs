import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # We'll simulate multiply

class MultiplyService(Node):
    """
    TODO: Create a service that multiplies two floats.
    
    Note: Using AddTwoInts as base, but implement multiplication logic.
    In practice, create a custom service type for floats.
    """
    
    def __init__(self):
        super().__init__('multiply_service')
        
        self.srv = self.create_service(
            AddTwoInts,
            'multiply_two_floats',
            self.multiply_callback
        )
        
        self.get_logger().info('Multiply service ready')
    
    def multiply_callback(self, request, response):
        """Multiply two numbers."""
        # TODO: Implement multiplication
        result = request.a * request.b
        response.sum = int(result)  # Using 'sum' field for result
        
        self.get_logger().info(f'{request.a} * {request.b} = {result}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = MultiplyService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
