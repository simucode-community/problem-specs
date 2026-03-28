# 011. Xacro - Parameterized Robot

**Difficulty:** 🟡 Medium  
**Category:** Xacro  
**Tags:** `xacro`, `urdf`, `parameters`, `generation`  
**Execution Type:** `ros2_node`  

**Frequency:** medium  

## 💡 Why This Problem Matters

Real robots have repeated parts (4 wheels, 6 legs). Writing URDF for a hexapod robot manually is tedious and error-prone. Xacro allows you to write `create_leg` once and use it 6 times with different transforms.

## Problem Statement

## Problem Statement
Understand how to use Xacro (XML Macros) to create reusable and parameterized URDF files. Xacro allows you to define constants, math, and macros to reduce code duplication.

### Requirements
- Create a Xacro file that generates a valid URDF
- Define a property `wheel_radius` with value `0.1`
- Use this property in a `<cylinder>` geometry for a link named `wheel_link`
- Define a macro `create_wheel` that takes a `name` parameter

### Input/Output Format
**Output:**
- Valid URDF XML string with substituted values (radius="0.1")

### ⚠️ Common Pitfalls
- Forgetting the xacro namespace in the robot tag: `xmlns:xacro="http://www.ros.org/wiki/xacro"`
- Missing `${}` around math expressions or property usage.

### 📚 Helpful Resources
- [ROS2 Xacro Tutorials](https://github.com/ros/xacro/wiki)

## Test Cases

- **Xacro loaded:** Xacro file processed
- **Parameters applied:** Xacro parameters substituted
- **URDF generated:** Valid URDF output

## Similar Problems

- Problem #10
- Problem #12

## Contributing

Found an issue with this problem's description, or have a better hint?  
[Open a PR](../../CONTRIBUTING.md) or [report it in Discussions](https://github.com/simucode-community/problem-specs/discussions).

**Note:** TestScripts and reference solutions are maintained by the SimuCode team  
and are not part of this open spec. This ensures grading integrity on [simucode.online](https://simucode.online).
