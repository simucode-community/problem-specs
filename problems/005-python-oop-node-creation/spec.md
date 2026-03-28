# 005. Python - OOP Node Creation

**Difficulty:** 🟢 Easy  
**Category:** Python for ROS2  
**Tags:** `python`, `oop`, `class`, `inheritance`  
**Execution Type:** `ros2_node`  

**Seen at:** iRobot, ABB  
**Frequency:** very-high  

## 💡 Why This Problem Matters

Starting 20 different nodes manually in 20 terminals is impossible. Launch files automate the startup process for complex robot systems, handling dependencies (`robot_state_publisher` before `nav2`) and configurations.

## Problem Statement

## Problem Statement
Learn how to structure a ROS 2 node using Python's Object-Oriented Programming (OOP) principles. You'll create a class that inherits from `Node` and implements the standard ROS 2 node lifecycle.

### Requirements
- Import `rclpy` and `from rclpy.node import Node`
- Define a class that **inherits from `Node`**
- Call `super().__init__("node_name")` in `__init__` with a string node name
- Create at least one publisher, subscriber, or timer inside `__init__`
- Call `rclpy.init()` and `rclpy.spin(node)` in `main()`

### Input/Output Format
**Output:**
- A running ROS 2 node that stays alive via `rclpy.spin()`

### ⚠️ Common Pitfalls
- Forgetting to call `super().__init__("name")` — the node name must be a string.
- Not calling `rclpy.spin(node)` — without it the node exits immediately.
- Defining `__init__` without `self` as the first parameter.

### 📚 Helpful Resources
- [ROS2 Node Tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)
- [rclpy Node API](https://docs.ros2.org/latest/api/rclpy/api/node.html)

## Test Cases

- **Class inheritance:** Inherits from Node
- **Publisher created:** Publisher exists
- **Counter increments:** Counter working

## Learning Objective

Structure a ROS 2 node using Python OOP best practices

## Similar Problems

- Problem #1
- Problem #6

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
