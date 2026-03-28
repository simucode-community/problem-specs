# 017. Conditional Launch

**Difficulty:** 🟡 Medium  
**Category:** Advanced Launch  
**Tags:** `launch`, `conditional`, `if-condition`, `logic`  
**Execution Type:** `launch_file`  

**Frequency:** medium  

## 💡 Why This Problem Matters

This is used extensively to switch between Simulation (Gazebo) and Real Robot hardware. `launch_sim.py` might be called with `headless:=true` to save resources on a server.

## Problem Statement

## Problem Statement
Launch files often need logic: "Only launch the camera driver if the camera is connected" or "Launch simulation if `sim:=true`". Use `IfCondition` to implement this.

### Requirements
- Declare argument `use_gui` (default: 'true')
- Launch `rviz2` ONLY if `use_gui` is true
- Launch `robot_state_publisher` always

### Input/Output Format
**Output:**
- `LaunchDescription` containing conditional logic.

### ⚠️ Common Pitfalls
- Forgetting that `IfCondition` expects a string 'true'/'false' or integer 1/0 from the configuration.

### 📚 Helpful Resources
- [Launch Conditions](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Using-ROS2-Launch-For-Large-Projects.html)

## Test Cases

- **Conditional nodes:** IfCondition/UnlessCondition used
- **Multiple conditions:** 2 conditional nodes
- **Default values:** Arguments have defaults

## Similar Problems

- Problem #16
- Problem #18

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
