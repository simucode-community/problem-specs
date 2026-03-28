import rclpy
from rclpy.node import Node
import json
import paho.mqtt.client as mqtt

class MqttBridgeNode(Node):
    """
    TODO: Design a minimal MQTT Bridge.
    
    Requirements:
    1. Connect to an MQTT broker (e.g. 'mqtt.eclipseprojects.io' or local)
    2. Subscribe to a ROS2 topic (e.g. '/sensor_data')
    3. Forward data to an MQTT topic (e.g. 'robot/sensors')
    4. Implement on_message callback for MQTT to publish back to ROS2
    """
    
    def __init__(self):
        super().__init__('mqtt_bridge_node')
        
        # TODO: Initialize MQTT Client
        # self.client = mqtt.Client()
        # self.client.connect(...)
        
        # TODO: Create ROS2 Subscription
        # self.subscription = self.create_subscription(...)
        
        # TODO: Create ROS2 Publisher (to bridge incoming MQTT messages)
        # self.publisher = self.create_publisher(...)
        
        pass

    def ros_callback(self, msg):
        """Receive ROS message and publish to MQTT."""
        # TODO: Serialize msg to JSON
        # payload = json.dumps(...)
        # TODO: Publish to MQTT
        # self.client.publish(...)
        pass
        
    def mqtt_on_message(self, client, userdata, msg):
        """Receive MQTT message and publish to ROS."""
        # TODO: Deserialize payload
        # TODO: Publish to ROS topic
        pass

def main(args=None):
    rclpy.init(args=args)
    node = MqttBridgeNode()
    
    # Optional: loop_start() for non-blocking MQTT
    # node.client.loop_start()
    
    rclpy.spin(node)
    
    # node.client.loop_stop()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
