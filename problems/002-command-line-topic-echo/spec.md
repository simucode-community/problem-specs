# 002. Command Line - Topic Echo

**Difficulty:** 🟢 Easy  
**Category:** CLI Tools  
**Tags:** `python`, `subscriber`, `cli`, `logging`  
**Execution Type:** `ros2_node`  

**Seen at:** Waymo  
**Frequency:** high  

## 💡 Why This Problem Matters

Subscribers allow robots to react to sensor data. A robot's navigation stack subscribes to Lidar scans to avoid obstacles, and its arm controller subscribes to joint states to know its position.

## Problem Statement

## Problem Statement
Create a ROS2 Python node that listens to messages from a topic and processes them. This completes the communication loop started by the publisher.

### Requirements
- Create a node named `simple_subscriber`
- Subscribe to topic `/chatter`
- Message type: `std_msgs/String`
- Log the received message to the console using `self.get_logger().info()`
- Format: "I heard: [message data]"

### Input/Output Format
**Input:**
- `/chatter` (std_msgs/String) - Receives string messages

**Output:**
- Console Logs - Prints "I heard: Hello ROS2!" (or whatever is published)

### ⚠️ Common Pitfalls
- Forgetting to add `self` to the callback method definition.
- Mismatched message types between publisher and subscriber.

### 📚 Helpful Resources
- [ROS2 Subscriber Documentation](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

## Test Cases

- **Subscriber exists:** Listening on /input
- **Callback triggered:** Callback executed
- **Logger used:** Messages logged

## Learning Objective

Use the ROS 2 CLI tools to inspect nodes, topics, and messages

## Similar Problems

- Problem #1
- Problem #3

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
