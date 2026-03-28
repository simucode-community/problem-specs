# 019. Topics - Custom Message

**Difficulty:** 🟡 Medium  
**Category:** Topics  
**Tags:** `topics`, `custom-message`, `publisher`, `subscriber`  
**Execution Type:** `ros2_node`  

**Seen at:** Clearpath Robotics  
**Frequency:** high  

## 💡 Why This Problem Matters

Defining semantic messages (e.g., `BatteryStatus`, `GripperCommand`) makes your code readable and typesafe. It's better than sending a float array and remembering `index 0 is voltage`.

## Problem Statement

## Problem Statement
Define a custom message type (`.msg`) for a specific application. Standard messages (`String`, `Int32`) are often insufficient.

### Requirements
- Define a message named `SensorReading`
- Fields:
  - `int32 id`
  - `float32 value`
  - `string label`
- Return the content string of the `.msg` file

### Input/Output Format
**Output:**
- String content of the file (e.g. "int32 id\n...")

### ⚠️ Common Pitfalls
- Using Python types (`int`, `str`) instead of ROS types (`int32`, `string`).

### 📚 Helpful Resources
- [Creating Custom Messages](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html)

## Test Cases

- **Custom message:** Complex message structure
- **Publisher/Subscriber:** Both created
- **Message fields:** All fields populated

## Learning Objective

Define and use a custom ROS 2 message interface

## Similar Problems

- Problem #20
- Problem #21

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
