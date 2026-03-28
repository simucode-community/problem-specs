# 015. Python Launch - Basic Node Launch

**Difficulty:** 🟢 Easy  
**Category:** Python Launch  
**Tags:** `launch`, `python`, `parameters`, `configuration`  
**Execution Type:** `launch_file`  

**Seen at:** Open Robotics  
**Frequency:** very-high  

## 💡 Why This Problem Matters

Even a simple robot needs a launch file to start its driver with the correct USB port (parameter) and topic names (remappings) to integrate with the rest of the system.

## Problem Statement

## Problem Statement
Create a basic Launch file to start a single ROS2 node. This introduces the `LaunchDescription` and `Node` action.

### Requirements
- Create a function `generate_launch_description`
- Launch package: `demo_nodes_cpp`, executable: `talker`
- Set parameter: `param1` to `"value1"`
- Remap topic: `/chatter` to `/my_chatter`
- **Note:** The test uses mocks, so these packages don't need to physically exist.

### Input/Output Format
**Output:**
- Return a `LaunchDescription` object

### ⚠️ Common Pitfalls
- Forgetting to import `Node` from `launch_ros.actions`.
- Remappings are a list of tuples: `[('/old', '/new')]`.

### 📚 Helpful Resources
- [ROS2 Launch Tutorials](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html)

## Test Cases

- **LaunchDescription:** Launch description created
- **Node action:** Node configured
- **Parameters set:** Parameters included

## Learning Objective

Launch multiple ROS 2 nodes from a single Python launch file

## Similar Problems

- Problem #16
- Problem #17

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
