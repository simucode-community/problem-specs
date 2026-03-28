import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor, SetParametersResult

class ParameterNode(Node):
    def __init__(self):
        super().__init__('parameter_node')
        
        # TODO: Declare parameters with descriptors
        self.declare_parameter(
            'my_parameter',
            'default_value',
            ParameterDescriptor(description='Description of parameter')
        )
        
        # TODO: Declare numeric parameter with constraints
        # self.declare_parameter(
        #     'speed',
        #     1.0,
        #     ParameterDescriptor(
        #         description='Robot speed',
        #         floating_point_range=[{
        #             'from_value': 0.0,
        #             'to_value': 10.0,
        #             'step': 0.1
        #         }]
        #     )
        # )
        
        # TODO: Add parameter callback for dynamic reconfiguration
        self.add_on_set_parameters_callback(self.parameter_callback)
        
        # Timer to demonstrate parameter usage
        self.timer = self.create_timer(1.0, self.timer_callback)
    
    def parameter_callback(self, params):
        """Handle parameter changes."""
        for param in params:
            self.get_logger().info(f'Parameter {param.name} changed to {param.value}')
            
            # TODO: Add validation logic
            # if param.name == 'speed' and param.value < 0:
            #     return SetParametersResult(successful=False, reason='Speed must be positive')
        
        return SetParametersResult(successful=True)
    
    def timer_callback(self):
        """Demonstrate reading parameters."""
        value = self.get_parameter('my_parameter').get_parameter_value().string_value
        self.get_logger().info(f'Current parameter value: {value}')

def main(args=None):
    rclpy.init(args=args)
    node = ParameterNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
