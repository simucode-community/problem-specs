# 102. ROS2 Parameter: Dynamic Speed Update

**Difficulty:** 🟢 Easy  
**Category:** Parameters  
**Tags:**   
**Execution Type:** `basic_python`  


## 💡 Why This Problem Matters

Tuning a controller (PID gains) or setting max velocity limits during operation requires dynamic parameters.

## Problem Statement

## Problem Statement
Use parameters to control a simulated robot's speed variable dynamically.

### Requirements
- Node `speed_controller`
- Parameter `target_speed` (float, default 0.0)
- Timer callback prints "Current Speed: [value]"
- Allow external tools (simulated test script) to change `target_speed`.

### Input/Output Format
**Output:**
- Console logs reflecting the parameter value updates.

### ⚠️ Common Pitfalls
- Caching the parameter value once in `__init__` and never reading it again.

### 📚 Helpful Resources
- [ROS2 Params](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Using-Parameters-In-A-Class-Python.html)

## Test Cases

- **ParameterDeclared:** speed
- **ParameterUpdates:** callback triggered

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
