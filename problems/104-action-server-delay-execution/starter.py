import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from action_tutorials_interfaces.action import Fibonacci
import time

class DelayActionServer(Node):
    """
    TODO: Create an action server that executes with delay.
    
    Requirements:
    - Accept a goal with duration
    - Provide periodic feedback
    - Complete after specified delay
    """
    
    def __init__(self):
        super().__init__('delay_action_server')
        
        self._action_server = ActionServer(
            self,
            Fibonacci,  # Using Fibonacci, but implementing delay logic
            'delay_action',
            self.execute_callback
        )
        
        self.get_logger().info('Delay action server ready')
    
    def execute_callback(self, goal_handle):
        """Execute delayed action with feedback."""
        self.get_logger().info('Executing delay action...')
        
        # Get delay duration from goal (using 'order' as seconds)
        delay_seconds = goal_handle.request.order
        
        feedback_msg = Fibonacci.Feedback()
        
        # Execute with periodic feedback
        for i in range(delay_seconds):
            # Check for cancellation
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return Fibonacci.Result()
            
            # Send feedback
            feedback_msg.partial_sequence = [i + 1]
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'Progress: {i + 1}/{delay_seconds} seconds')
            
            time.sleep(1.0)
        
        # Complete goal
        goal_handle.succeed()
        
        result = Fibonacci.Result()
        result.sequence = [delay_seconds]
        
        self.get_logger().info(f'Delay complete: {delay_seconds} seconds')
        return result

def main(args=None):
    rclpy.init(args=args)
    node = DelayActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
