# 105. Write Launch File for Multi-Robot Simulation

**Difficulty:** 🟡 Medium  
**Category:** Launch  
**Tags:**   
**Execution Type:** `launch_file`  


## 💡 Why This Problem Matters

Swarm robotics (warehouse picking) involves hundreds of identical robots. Namespacing is the only way to send "Move Left" to Robot #42 without Robot #43 moving too.

## Problem Statement

## Problem Statement
Simulate a multi-robot fleet. Write a launch file that spawns two identical robots in different namespaces, preventing topic collision.

### Requirements
- Create `multi_bot.launch.py`
- Launch two instances of `my_bot_node`
- Namespace 1: `/robot1`
- Namespace 2: `/robot2`
- Remap `/cmd_vel` to `/robotX/cmd_vel` if needed (namespaces usually handle this automatically)

### Input/Output Format
**Output:**
- `LaunchDescription` starting 2 tagged nodes.

### ⚠️ Common Pitfalls
- Forgetting that namespaces affect ALL topics, services, and parameters of that node.

### 📚 Helpful Resources
- [ROS2 Namespaces](https://docs.ros.org/en/humble/How-To-Guides/Using-ros2-param.html#namespace)

## Test Cases

- **TwoRobotsStarted:** 2 nodes
- **DifferentNamespaces:** robot1 and robot2

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
