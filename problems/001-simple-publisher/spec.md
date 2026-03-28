# 001. Simple Publisher

**Difficulty:** 🟢 Easy  
**Category:** ROS2 Basics  
**Tags:** `python`, `publisher`, `beginner`, `topics`  
**Execution Type:** `ros2_publisher`  

**Seen at:** Boston Dynamics, Tesla  
**Frequency:** very-high  

## 💡 Why This Problem Matters

Publishers are the backbone of ROS2 systems. Sensors (Lidar, Cameras, IMUs) use publishers to stream data to the rest of the robot. Mastering this is essential for any robotics application.

## Problem Statement

## Problem Statement
Create a ROS2 Python node that continually publishes a string message to a topic. This is the "Hello World" of ROS2, establishing the fundamental communication pattern.

### Requirements
- Create a node named `simple_publisher`
- Publish to topic `/chatter`
- Message type: `std_msgs/String`
- Publish rate: **1 Hz** (once per second)
- Message content: "Hello ROS2!"

### Input/Output Format
**Output:**
- `/chatter` (std_msgs/String) - Publishes "Hello ROS2!" continuously

### ⚠️ Common Pitfalls
- Forgetting to call `rclpy.init()` before creating the node.
- Not spinning the node with `rclpy.spin()`.
- Publishing at the wrong rate (check your timer period).

### 📚 Helpful Resources
- [ROS2 Publisher/Subscriber Tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

## Test Cases

- **Publisher created:** Publisher on /chatter topic
- **Correct message:** Message: 'Hello ROS2!'
- **Publish rate:** Rate: 1 Hz

## Learning Objective

Write your first ROS 2 publisher node and understand the topic model

## Similar Problems

- Problem #2
- Problem #3

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
