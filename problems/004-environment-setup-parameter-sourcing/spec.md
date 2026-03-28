# 004. Environment Setup - Parameter Sourcing

**Difficulty:** 🟡 Medium  
**Category:** ROS2 Basics  
**Tags:** `python`, `environment`, `setup`, `parameters`  
**Execution Type:** `ros2_python_node`  

**Frequency:** medium  

## 💡 Why This Problem Matters

Hardcoding values (like PID gains, robot dimensions, or topic names) is bad practice. Parameters allow you to deploy the same code on different robots with different configurations (e.g., Robot A has max_speed=1.0, Robot B has max_speed=2.0).

## Problem Statement

## Problem Statement
Parameters allow you to configure nodes at runtime without changing code. Create a node that reads a parameter and uses it.

### Requirements
- Create a node named `param_reader`
- Declare a parameter named `my_param` with default value "default_value"
- Log the parameter value immediately on startup
- Log format: "Parameter value: [value]"

### Input/Output Format
**Input:**
- Parameter: `my_param` (string)

**Output:**
- Console Log: "Parameter value: default_value" (or the overriding value)

### ⚠️ Common Pitfalls
- Trying to get a parameter before declaring it.
- Forgetting to extract the value using `.value` or `.string_value` (the API returns a Parameter object).

### 📚 Helpful Resources
- [Understanding ROS2 Parameters](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python.html)

## Test Cases

- **Environment check:** ROS_DISTRO found
- **Distribution logged:** ROS2 distro displayed
- **Node initialized:** Node running

## Similar Problems

- Problem #3

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
