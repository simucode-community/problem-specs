import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from action_tutorials_interfaces.action import Fibonacci
# TODO: Import appropriate action type

class MyActionServer(Node):
    def __init__(self):
        super().__init__('my_action_server')
        
        # TODO: Create action server
        self._action_server = ActionServer(
            self,
            Fibonacci,  # TODO: Replace with your action type
            'fibonacci',  # TODO: Replace with your action name
            self.execute_callback
        )
        
        self.get_logger().info('Action server ready')
    
    def execute_callback(self, goal_handle):
        """Execute the action goal."""
        self.get_logger().info('Executing goal...')
        
        # TODO: Get goal request
        # goal = goal_handle.request
        
        # TODO: Create feedback message
        feedback_msg = Fibonacci.Feedback()
        
        # TODO: Implement action logic with feedback
        # for i in range(goal.order):
        #     feedback_msg.partial_sequence.append(...)
        #     goal_handle.publish_feedback(feedback_msg)
        
        # TODO: Mark goal as succeeded
        goal_handle.succeed()
        
        # TODO: Return result
        result = Fibonacci.Result()
        # result.sequence = ...
        
        return result

def main(args=None):
    rclpy.init(args=args)
    node = MyActionServer()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
