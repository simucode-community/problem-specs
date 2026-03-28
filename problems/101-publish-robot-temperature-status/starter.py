import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        
        # TODO: Create publisher for temperature topic
        # self.publisher = self.create_publisher(Float32, 'temperature', 10)
        
        # TODO: Initialize temperature value
        # self.temperature = 20.0  # Starting temperature in Celsius
        
        # TODO: Create timer to publish every 1 second
        # self.timer = self.create_timer(1.0, self.publish_temperature)
        
        pass
    
    def publish_temperature(self):
        """Publish current temperature and increment it"""
        # TODO: Create Float32 message
        # msg = Float32()
        
        # TODO: Set temperature value
        # msg.data = self.temperature
        
        # TODO: Publish the message
        # self.publisher.publish(msg)
        
        # TODO: Log the published temperature
        # self.get_logger().info(f'Publishing temperature: {self.temperature}°C')
        
        # TODO: Increment temperature by 0.5 degrees
        # self.temperature += 0.5
        
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
