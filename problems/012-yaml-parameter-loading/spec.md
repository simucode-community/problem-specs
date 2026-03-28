# 012. YAML - Parameter Loading

**Difficulty:** 🟢 Easy  
**Category:** YAML Configuration  
**Tags:** `yaml`, `parameters`, `config`, `loading`  
**Execution Type:** `ros2_node`  

**Frequency:** very-high  

## 💡 Why This Problem Matters

A robot might need different PID gains for 'indoor' vs 'outdoor' operation. Instead of changing code, you just load `indoor_params.yaml` or `outdoor_params.yaml` at runtime.

## Problem Statement

## Problem Statement
Learn how to load parameters from a YAML file into a ROS2 node. This is the standard way to configure robots without recompiling code.

### Requirements
- Create a node `yaml_loader`
- Load parameters from a file `config/params.yaml` (simulated)
- The YAML contains: `scan_topic: /scan`, `max_speed: 2.5`
- Read these parameters and log them.

### Input/Output Format
**Output:**
- Console Logs showing the loaded values: "Topic: /scan", "Speed: 2.5"

### ⚠️ Common Pitfalls
- YAML indentation errors (tabs vs spaces).
- Not declaring parameters before reading them (unless `allow_undeclared_parameters` is true).

### 📚 Helpful Resources
- [ROS2 Parameters Tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python.html)

## Test Cases

- **Parameters declared:** 3 parameters declared
- **Values loaded:** YAML values retrieved
- **Type checking:** Correct parameter types

## Learning Objective

Load configuration from YAML files using the ROS 2 parameter server

## Similar Problems

- Problem #10
- Problem #13

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
