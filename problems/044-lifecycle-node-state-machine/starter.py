import rclpy
from rclpy.lifecycle import LifecycleNode
from lifecycle_msgs.msg import Transition

class ManagedRunner(LifecycleNode):
    def __init__(self):
        super().__init__('managed_runner')
        # TODO: Implement on_configure, on_activate, on_deactivate
        # TODO: Provide a service or topic to trigger the 'run' action
        pass

def main(args=None):
    rclpy.init(args=args)
    node = ManagedRunner()
    # TODO: Bring node through configure -> activate programmatically for test
    rclpy.shutdown()
